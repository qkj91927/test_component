#!/usr/bin/env python3
"""
Token system switcher for plus-v1.0 and basic-v1.0.

Capabilities:
- List available token systems from othertokens/
- Apply selected token system to json/index.json and css/QQ_color_tokens.css
- Validate results after switching
- Generate multi-dimensional comparison report
"""

from __future__ import annotations

import argparse
import json
import re
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

TOKEN_FILE_PATTERN = "*.tokens.json"

# 源 token 层级 -> 目标 token 层级（目标层级不含末尾 $value）
INDEX_COLOR_MAPPING: Dict[str, str] = {
    "tokens.color.text_primary": "Color.文本色.text_primary",
    "tokens.color.text_secondary": "Color.文本色.text_secondary",
    "tokens.color.text_tertiary": "Color.文本色.text_tertiary",
    "tokens.color.text_quaternary": "Color.文本色.text_quaternary",
    "tokens.color.text_link": "Color.文本色.text_link",
    "tokens.color.text_allwhite": "Color.文本色.text_allwhite",
    "tokens.color.brand_standard": "Color.品牌色.brand_standard",
    "tokens.color.brand_pressed": "Color.品牌色.brand_standard",
    "tokens.color.feedback_error": "Color.反馈色.feedback_error",
    "tokens.color.separator": "Color.分割色.Separators",
    "tokens.color.border_standard": "Color.分割色.Separators",
    "tokens.color.bg_page": "Color.分组背景色.Primary",
    "tokens.color.bg_item": "Color.背景色.Primary",
    "tokens.color.bg_secondary": "Color.背景色.Secondary",
    "tokens.color.overlay_dark": "Color.叠加色.active",
    "tokens.color.overlay_dialog": "Color.叠加色.active",
    "tokens.color.btn_bg": "Color.透明填充色.Quaternary",
    "tokens.color.fill_tertiary": "Color.透明填充色.Tertiary",
    "tokens.color.fill_standard_primary": "Color.透明填充色.Quaternary",
    "tokens.color.fill_pressed": "Color.叠加色.active",
    "tokens.color.fill_standard_brand": "Color.透明填充色.Secondary",
    "tokens.color.icon_secondary": "Color.图标色.icon_secondary",
    "tokens.color.icon_primary": "Color.图标色.icon_primary",
    "tokens.color.bg_bottom_light": "Color.背景色.Primary",
    "tokens.color.bg_bottom_standard": "Color.分组背景色.Primary",
    "tokens.color.bg_bottom_brand": "Color.品牌色.brand_light",
}

# CSS 变量 -> index color key
CSS_VAR_TO_INDEX_KEY: Dict[str, str] = {
    "--color-brand-standard": "brand_standard",
    "--color-brand-pressed": "brand_pressed",
    "--color-text-primary": "text_primary",
    "--color-text-secondary": "text_secondary",
    "--color-text-tertiary": "text_tertiary",
    "--color-text-quaternary": "text_quaternary",
    "--color-text-link": "text_link",
    "--color-icon-primary": "icon_primary",
    "--color-icon-secondary": "icon_secondary",
    "--color-feedback-error": "feedback_error",
    "--color-border-standard": "border_standard",
    "--color-separator": "separator",
    "--color-overlay-dark": "overlay_dark",
    "--color-fill-pressed": "fill_pressed",
    "--color-bg-item": "bg_item",
    "--color-fill-standard-primary": "fill_standard_primary",
    "--color-fill-standard-brand": "fill_standard_brand",
    "--color-bg-bottom-light": "bg_bottom_light",
    "--color-bg-page": "bg_page",
    "--color-bg-bottom-brand": "bg_bottom_brand",
    "--color-bg-secondary": "bg_secondary",
    "--color-bg-bottom-standard": "bg_bottom_standard",
    "--color-overlay-dialog": "overlay_dialog",
    "--color-btn-bg": "btn_bg",
    "--color-fill-tertiary": "fill_tertiary",
}


@dataclass
class ValidationResult:
    json_valid: bool
    css_vars_found: int
    css_vars_total: int
    missing_css_vars: List[str]


def _read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path: Path, data: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def _list_token_systems(othertokens_dir: Path) -> List[Path]:
    return sorted(othertokens_dir.glob(TOKEN_FILE_PATTERN))


def _flatten_dict(data: Any, prefix: str = "") -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    if isinstance(data, dict):
        for k, v in data.items():
            key = f"{prefix}.{k}" if prefix else k
            out.update(_flatten_dict(v, key))
    else:
        out[prefix] = data
    return out


def _get_nested(data: Dict[str, Any], path: str) -> Any:
    cur: Any = data
    for key in path.split("."):
        if not isinstance(cur, dict) or key not in cur:
            raise KeyError(path)
        cur = cur[key]
    return cur


def _set_nested(data: Dict[str, Any], path: str, value: Any) -> None:
    parts = path.split(".")
    cur = data
    for key in parts[:-1]:
        cur = cur[key]
    cur[parts[-1]] = value


def _resolve_alias(token_data: Dict[str, Any], value: Any) -> Any:
    if isinstance(value, str):
        m = re.fullmatch(r"\{([^{}]+)\}", value.strip())
        if m:
            ref_path = m.group(1)
            ref_obj = _get_nested(token_data, ref_path)
            if isinstance(ref_obj, dict) and "$value" in ref_obj:
                return _resolve_alias(token_data, ref_obj["$value"])
            return ref_obj
    return value


def _to_css_value(value: Any, token_data: Dict[str, Any]) -> str:
    resolved = _resolve_alias(token_data, value)
    if isinstance(resolved, dict) and "hex" in resolved:
        hex_value = resolved["hex"]
        alpha = resolved.get("alpha", 1)
        if alpha is None:
            alpha = 1
        try:
            alpha_num = float(alpha)
        except Exception:
            alpha_num = 1
        if alpha_num >= 0.999:
            return hex_value.lower()
        hex_clean = hex_value.lstrip("#")
        if len(hex_clean) == 6:
            r = int(hex_clean[0:2], 16)
            g = int(hex_clean[2:4], 16)
            b = int(hex_clean[4:6], 16)
            return f"rgba({r}, {g}, {b}, {alpha_num:.3f})"
        return hex_value.lower()
    if isinstance(resolved, str):
        return resolved
    return json.dumps(resolved, ensure_ascii=False)


def _extract_target_value(target_data: Dict[str, Any], mapped_path: str) -> Any:
    node = _get_nested(target_data, mapped_path)
    if isinstance(node, dict) and "$value" in node:
        return _resolve_alias(target_data, node["$value"])
    return _resolve_alias(target_data, node)


def _collect_color_changes(before: Dict[str, Any], after: Dict[str, Any]) -> List[Tuple[str, Any, Any]]:
    changes: List[Tuple[str, Any, Any]] = []
    for p in sorted(INDEX_COLOR_MAPPING.keys()):
        b = _get_nested(before, p)
        a = _get_nested(after, p)
        if b != a:
            changes.append((p, b, a))
    return changes


def _replace_css_var(css_text: str, var_name: str, new_value: str) -> Tuple[str, int]:
    pattern = re.compile(rf"({re.escape(var_name)}\s*:\s*)([^;]+)(;)")
    new_css, count = pattern.subn(rf"\1{new_value}\3", css_text)
    return new_css, count


def _apply_index_colors(index_data: Dict[str, Any], target_data: Dict[str, Any]) -> Dict[str, Any]:
    updated = deepcopy(index_data)
    for src_path, target_path in INDEX_COLOR_MAPPING.items():
        target_value = _extract_target_value(target_data, target_path)
        # index.json 中 color token 使用 string（hex/rgba）格式
        if isinstance(target_value, dict) and "hex" in target_value:
            css_value = _to_css_value(target_value, target_data)
            _set_nested(updated, src_path, css_value)
        else:
            _set_nested(updated, src_path, target_value)
    return updated


def _apply_css_colors(css_text: str, updated_index: Dict[str, Any], target_data: Dict[str, Any]) -> Tuple[str, Dict[str, int]]:
    result = css_text
    hit_counter: Dict[str, int] = {}
    for css_var, index_key in CSS_VAR_TO_INDEX_KEY.items():
        src_path = f"tokens.color.{index_key}"
        value = _get_nested(updated_index, src_path)
        css_value = _to_css_value(value, target_data)
        result, count = _replace_css_var(result, css_var, css_value)
        hit_counter[css_var] = count
    return result, hit_counter


def _validate(index_path: Path, css_path: Path) -> ValidationResult:
    json_valid = True
    try:
        _read_json(index_path)
    except Exception:
        json_valid = False

    css_text = _read_text(css_path)
    missing: List[str] = []
    found = 0
    for var in CSS_VAR_TO_INDEX_KEY:
        if re.search(rf"{re.escape(var)}\s*:", css_text):
            found += 1
        else:
            missing.append(var)

    return ValidationResult(
        json_valid=json_valid,
        css_vars_found=found,
        css_vars_total=len(CSS_VAR_TO_INDEX_KEY),
        missing_css_vars=missing,
    )


def _make_report(
    report_path: Path,
    target_name: str,
    color_changes: List[Tuple[str, Any, Any]],
    css_hit_counter: Dict[str, int],
    validation: ValidationResult,
) -> None:
    changed_paths = [p for p, _, _ in color_changes]
    total_mapped = len(INDEX_COLOR_MAPPING)
    changed_count = len(changed_paths)
    coverage = (changed_count / total_mapped * 100) if total_mapped else 0

    css_replaced_vars = sum(1 for _, c in css_hit_counter.items() if c > 0)

    lines: List[str] = []
    lines.append("# Token 切换对比分析报告")
    lines.append("")
    lines.append(f"- 目标 Token 系统：`{target_name}`")
    lines.append(f"- 生成时间：`{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`")
    lines.append("")
    lines.append("## 一、切换摘要")
    lines.append("")
    lines.append(f"- 映射总数：**{total_mapped}**")
    lines.append(f"- 实际变化：**{changed_count}**")
    lines.append(f"- 变化覆盖率：**{coverage:.1f}%**")
    lines.append(f"- CSS 命中变量：**{css_replaced_vars}/{len(CSS_VAR_TO_INDEX_KEY)}**")
    lines.append("")
    lines.append("## 二、层级映射说明")
    lines.append("")
    lines.append("- 映射遵循：`json/index.json -> tokens.color.*` 对应 `othertokens/*.tokens.json -> Color.*`")
    lines.append("- 依据原 token 层级逐项切换，不做随机替换")
    lines.append("")
    lines.append("## 三、关键变化（前后对比）")
    lines.append("")
    if not color_changes:
        lines.append("- 无变化（目标系统与当前系统一致或映射值相同）")
    else:
        for path, before, after in color_changes[:30]:
            lines.append(f"- `{path}`: `{before}` → `{after}`")
        if len(color_changes) > 30:
            lines.append(f"- ... 其余 {len(color_changes) - 30} 项变化略")

    lines.append("")
    lines.append("## 四、自动校验结果")
    lines.append("")
    lines.append(f"- JSON 结构校验：{'✅ 通过' if validation.json_valid else '❌ 失败'}")
    lines.append(
        f"- CSS 变量校验：**{validation.css_vars_found}/{validation.css_vars_total}**"
        + (" ✅" if validation.css_vars_found == validation.css_vars_total else " ⚠️")
    )
    if validation.missing_css_vars:
        lines.append("- 缺失变量：")
        for v in validation.missing_css_vars:
            lines.append(f"  - `{v}`")
    else:
        lines.append("- 缺失变量：无")

    lines.append("")
    lines.append("## 五、多维度结论")
    lines.append("")
    lines.append("- **语义一致性**：映射基于层级路径，保证语义对齐。")
    lines.append("- **视觉风格变化**：以文本色、品牌色、背景/分割色为主变化维度。")
    lines.append("- **工程影响范围**：仅更新 `json/index.json` 与 `css/QQ_color_tokens.css` 的映射项。")
    lines.append("- **风险评估**：若 CSS 中存在非映射私有变量，保留原值，不阻断切换。")

    _write_text(report_path, "\n".join(lines) + "\n")


def run(project_root: Path, target: str, apply: bool, report_out: Path) -> int:
    othertokens_dir = project_root / "othertokens"
    index_path = project_root / "json" / "index.json"
    css_path = project_root / "css" / "QQ_color_tokens.css"

    if not othertokens_dir.exists():
        raise FileNotFoundError(f"未找到目录: {othertokens_dir}")
    if not index_path.exists():
        raise FileNotFoundError(f"未找到文件: {index_path}")
    if not css_path.exists():
        raise FileNotFoundError(f"未找到文件: {css_path}")

    systems = _list_token_systems(othertokens_dir)
    if not systems:
        raise FileNotFoundError("othertokens 目录下未发现 *.tokens.json")

    target_file: Path | None = None
    normalized_target = target.lower().replace(".tokens", "")
    for p in systems:
        stem_normalized = p.stem.lower().replace(".tokens", "")
        if (
            stem_normalized == normalized_target
            or p.stem.lower() == target.lower()
            or p.name.lower() == target.lower()
        ):
            target_file = p
            break
    if target_file is None:
        maybe = othertokens_dir / target
        if maybe.exists():
            target_file = maybe

    if target_file is None:
        available = ", ".join([p.stem for p in systems])
        raise ValueError(f"未找到目标系统 `{target}`。可选：{available}")

    index_before = _read_json(index_path)
    css_before = _read_text(css_path)
    target_data = _read_json(target_file)

    index_after = _apply_index_colors(index_before, target_data)
    css_after, css_hit_counter = _apply_css_colors(css_before, index_after, target_data)

    color_changes = _collect_color_changes(index_before, index_after)

    if apply:
        _write_json(index_path, index_after)
        _write_text(css_path, css_after)

    validation = _validate(index_path if apply else index_path, css_path if apply else css_path)

    report_path = report_out if report_out.is_absolute() else (project_root / report_out)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    _make_report(report_path, target_file.stem, color_changes, css_hit_counter, validation)

    mode = "APPLY" if apply else "DRY-RUN"
    print(f"[{mode}] target={target_file.name}")
    print(f"变更项: {len(color_changes)}/{len(INDEX_COLOR_MAPPING)}")
    print(f"报告: {report_path}")
    if not apply:
        print("未写入文件（dry-run）。如需应用，请增加 --apply")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Switch token system for plus-v1.0/basic-v1.0 (project-agnostic)")
    parser.add_argument("--project-root", default=".", help="项目根目录")
    parser.add_argument("--target", help="目标 token 系统名（如 iOS / Material / Microsoft / One+UI）")
    parser.add_argument("--list", action="store_true", help="列出可用 token 系统")
    parser.add_argument("--apply", action="store_true", help="真正写入文件；默认 dry-run")
    parser.add_argument("--report", default="md/TOKEN_SWITCH_REPORT.md", help="报告输出路径")

    args = parser.parse_args()
    root = Path(args.project_root).resolve()

    othertokens_dir = root / "othertokens"
    if args.list:
        systems = _list_token_systems(othertokens_dir)
        if not systems:
            print("未发现可用 token 系统")
            return 1
        print("可用 token 系统:")
        for p in systems:
            print(f"- {p.stem}")
        return 0

    if not args.target:
        raise ValueError("请通过 --target 指定目标 token 系统，或使用 --list 查看可选项")

    return run(
        project_root=root,
        target=args.target,
        apply=args.apply,
        report_out=Path(args.report),
    )


if __name__ == "__main__":
    raise SystemExit(main())
