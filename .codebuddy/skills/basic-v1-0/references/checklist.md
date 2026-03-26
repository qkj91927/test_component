# 生成检查清单（执行版）

## 生成前

- [ ] 已读取 `README.md`
- [ ] 已读取 `json/index.json`
- [ ] 已读取 `css/tokens.css`
- [ ] 已读取 `css/QQ_color_tokens.css`
- [ ] 已读取目标组件对应 `md/*_SPEC.md`
- [ ] 已读取目标组件对应 `json/components/*.json`

## 组合合法性

- [ ] List 组合满足 `LIST_COMPONENT_SPEC.md` 约束
- [ ] Grouped List 组合满足 `GROUPED_LIST_COMPONENT_SPEC.md` 约束
- [ ] NavBar 满足 `NAVBAR_COMPONENT_SPEC.md` 约束
- [ ] 模态组件未嵌套

## 视觉与Token

- [ ] `<html>` 已设置 `data-theme`
- [ ] 颜色全部使用 Token（无自定义色值）
- [ ] 间距均为 4px 整数倍
- [ ] 页面背景色符合强约束与优先级

## 状态栏与图标

- [ ] 页面顶部包含 428×54 StatusBar
- [ ] StatusBar 时间固定 `9:41`
- [ ] StatusBar 图标路径正确（network/wifi/battery）
- [ ] `empty_icon.svg` 已全部替换为真实图标

## 输出后审查

- [ ] 缺失组件：已说明
- [ ] 缺失变体：已说明
- [ ] 不合理之处：已说明
- [ ] 主流设计系统对比建议：已说明
