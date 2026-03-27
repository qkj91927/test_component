# Token 切换对比分析报告

- 目标 Token 系统：`iOS.tokens`
- 生成时间：`2026-03-27 14:07:23`

## 一、切换摘要

- 映射总数：**26**
- 实际变化：**26**
- 变化覆盖率：**100.0%**
- CSS 命中变量：**25/25**

## 二、层级映射说明

- 映射遵循：`json/index.json -> tokens.color.*` 对应 `othertokens/*.tokens.json -> Color.*`
- 依据原 token 层级逐项切换，不做随机替换

## 三、关键变化（前后对比）

- `tokens.color.bg_bottom_brand`: `#EFF4FF` → `rgba(0, 136, 255, 0.200)`
- `tokens.color.bg_bottom_light`: `#FFFFFF` → `#ffffff`
- `tokens.color.bg_bottom_standard`: `#F0F0F2` → `#f2f2f7`
- `tokens.color.bg_item`: `#FFFFFF` → `#ffffff`
- `tokens.color.bg_page`: `#F0F0F2` → `#f2f2f7`
- `tokens.color.bg_secondary`: `#F3F3F7` → `#f3f3f7`
- `tokens.color.border_standard`: `rgba(0, 0, 0, 0.10)` → `rgba(60, 60, 67, 0.250)`
- `tokens.color.brand_pressed`: `#008AE5` → `#0088ff`
- `tokens.color.brand_standard`: `#0099FF` → `#0088ff`
- `tokens.color.btn_bg`: `rgba(116, 116, 128, 0.08)` → `rgba(116, 116, 128, 0.080)`
- `tokens.color.feedback_error`: `#F74C30` → `#ff383c`
- `tokens.color.fill_pressed`: `rgba(0, 0, 0, 0.04)` → `rgba(118, 118, 128, 0.120)`
- `tokens.color.fill_standard_brand`: `rgba(13, 16, 49, 0.04)` → `rgba(120, 120, 128, 0.160)`
- `tokens.color.fill_standard_primary`: `rgba(13, 16, 49, 0.04)` → `rgba(116, 116, 128, 0.080)`
- `tokens.color.fill_tertiary`: `rgba(118, 118, 128, 0.12)` → `rgba(118, 118, 128, 0.120)`
- `tokens.color.icon_primary`: `#1A1A1A` → `#000000`
- `tokens.color.icon_secondary`: `#929296` → `rgba(60, 60, 67, 0.600)`
- `tokens.color.overlay_dark`: `rgba(0, 0, 0, 0.50)` → `rgba(118, 118, 128, 0.120)`
- `tokens.color.overlay_dialog`: `rgba(0, 0, 0, 0.40)` → `rgba(118, 118, 128, 0.120)`
- `tokens.color.separator`: `rgba(0, 0, 0, 0.08)` → `rgba(60, 60, 67, 0.250)`
- `tokens.color.text_allwhite`: `#FFFFFF` → `#ffffff`
- `tokens.color.text_link`: `#214CA5` → `#0088ff`
- `tokens.color.text_primary`: `rgba(0, 0, 0, 0.90)` → `#000000`
- `tokens.color.text_quaternary`: `rgba(60, 60, 67, 0.26)` → `rgba(60, 60, 67, 0.180)`
- `tokens.color.text_secondary`: `rgba(60, 60, 67, 0.76)` → `rgba(60, 60, 67, 0.600)`
- `tokens.color.text_tertiary`: `rgba(60, 60, 67, 0.56)` → `rgba(60, 60, 67, 0.300)`

## 四、自动校验结果

- JSON 结构校验：✅ 通过
- CSS 变量校验：**25/25** ✅
- 缺失变量：无

## 五、多维度结论

- **语义一致性**：映射基于层级路径，保证语义对齐。
- **视觉风格变化**：以文本色、品牌色、背景/分割色为主变化维度。
- **工程影响范围**：仅更新 `json/index.json` 与 `css/QQ_color_tokens.css` 的映射项。
- **风险评估**：若 CSS 中存在非映射私有变量，保留原值，不阻断切换。
