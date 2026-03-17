# 文本块 TextBlock · 组件设计规范

纯文本内容的排版区域，涵盖标题、正文、辅助说明等层级，用于构建页面的信息层次与阅读节奏。

---

## 1. 组件概述

文本块组件包含 **8 种子组件变体**，按文本层级分为以下类型：

| 编号 | 名称 | 文字类型 | 容器高度 |
|------|------|----------|----------|
| A1 | 大标题·单行 | title | 50px |
| A2 | 大标题·双行 | title | 84px |
| A3 | 一级标题 | subtitle | 44px |
| A4 | 二级标题 | aux-title | 42px |
| A5 | 正文段落 | body | 80px |
| A6 | 前缀正文 | body | 80px |
| A7 | 链接文本 | link | 32px |
| A8 | 辅助说明 | caption | 28px |

---

## 2. 通用布局规格

| 属性 | 值 |
|------|------|
| 容器宽度 | 428px |
| 背景色 | `white` |
| `position` | `relative` |
| 文字区域宽度 | 388px（容器 428 - 左右各 20px 内边距） |
| 文字区域 `left` | 20px |
| 文字区域 `position` | `absolute` |

---

## 3. 文字属性详解

### 3.1 大标题（A1-A2）

| 属性 | 值 |
|------|------|
| CSS class | `.text-block-title .left` |
| 字体 | PingFang SC |
| 字号 | 26px |
| 字重 | 600（Semibold） |
| 行高 | 34px |
| 颜色 | `rgba(0, 0, 0, 0.90)` |
| 对齐 | `text-align: left` |
| 文字顶部偏移 | 8px |
| 示例文案 | A1: "大标题 Semibold 26/34"；A2: "双行大标题\<br\>Semibold 26/34" |

### 3.2 一级标题（A3）

| 属性 | 值 |
|------|------|
| CSS class | `.text-block-subtitle` |
| 字体 | PingFang SC |
| 字号 | 22px |
| 字重 | 500（Medium） |
| 行高 | 28px |
| 颜色 | `rgba(0, 0, 0, 0.90)` |
| 文字顶部偏移 | 8px |
| 示例文案 | "一级标题 Medium 22/28" |

### 3.3 二级标题（A4）

| 属性 | 值 |
|------|------|
| CSS class | `.text-block-aux-title` |
| 字体 | PingFang SC |
| 字号 | 18px |
| 字重 | 500（Medium） |
| 行高 | 26px |
| 颜色 | `rgba(0, 0, 0, 0.90)` |
| 文字顶部偏移 | 8px |
| 示例文案 | "二级标题 Medium 18/26" |

### 3.4 正文段落 / 前缀正文（A5-A6）

| 属性 | 值 |
|------|------|
| CSS class | `.text-block-body` |
| 字体 | PingFang SC |
| 字号 | 17px |
| 字重 | 400（Regular） |
| 行高 | 24px |
| 颜色 | `rgba(0, 0, 0, 0.90)` |
| `display` | `inline-block` |
| `vertical-align` | `middle` |
| 文字顶部偏移 | 4px |
| 示例文案 | A5: "这是正文文本，Regular 17/24。这里收录了空友们喜爱的说说……"；A6: "这是前缀正文，Regular 17/24。这里收录了空友们喜爱的说说……" |

> **A5 与 A6 的区别**：A6"前缀正文"用于需要在正文前附加前缀标识（如序号、标记）的场景，CSS 样式与 A5 相同，仅语义和使用场景不同。

### 3.5 链接文本（A7）

| 属性 | 值 |
|------|------|
| CSS class | `.text-block-link` |
| 字体 | PingFang SC |
| 字号 | 17px |
| 字重 | 400（Regular） |
| 行高 | 24px |
| 颜色 | `#214CA5`（text_link） |
| `display` | `inline-block` |
| `vertical-align` | `middle` |
| 文字顶部偏移 | 4px |
| 示例文案 | "链接文本 Regular 17/24" |

### 3.6 辅助说明（A8）

| 属性 | 值 |
|------|------|
| CSS class | `.text-block-caption` |
| 字体 | PingFang SC |
| 字号 | 14px |
| 字重 | 400（Regular） |
| 行高 | 20px |
| 颜色 | `rgba(60, 60, 67, 0.76)`（text_primary_light） |
| `display` | `inline-block` |
| `vertical-align` | `middle` |
| 文字顶部偏移 | 4px |
| 示例文案 | "这是辅助说明文本，Regular 14/20，建议不超过两行。" |

---

## 4. 容器高度推导

| 变体 | textTop | 内容行数 × 行高 | 容器高度 |
|------|---------|----------------|----------|
| A1 大标题·单行 | 8px | 1 × 34 = 34px | 8 + 34 + 8 = **50px** |
| A2 大标题·双行 | 8px | 2 × 34 = 68px | 8 + 68 + 8 = **84px** |
| A3 一级标题 | 8px | 1 × 28 = 28px | 8 + 28 + 8 = **44px** |
| A4 二级标题 | 8px | 1 × 26 = 26px | 8 + 26 + 8 = **42px** |
| A5 正文段落 | 4px | ~3 × 24 = 72px | 4 + 72 + 4 = **80px** |
| A6 前缀正文 | 4px | ~3 × 24 = 72px | 4 + 72 + 4 = **80px** |
| A7 链接文本 | 4px | 1 × 24 = 24px | 4 + 24 + 4 = **32px** |
| A8 辅助说明 | 4px | 1 × 20 = 20px | 4 + 20 + 4 = **28px** |

---

## 5. 交互行为

### 5.1 文本可编辑（仅组件构建器）

- 在 `component-builder.html` 的画布拼装模式中，所有文本元素添加 `.editable-text` class
- 涵盖 CSS class：`.text-block-title`、`.text-block-subtitle`、`.text-block-aux-title`、`.text-block-body`、`.text-block-link`、`.text-block-caption`
- 用户可直接点击文本进行内联编辑

### 5.2 链接文本样式

- A7 链接文本使用蓝色 `#214CA5`，暗示可点击
- 实际点击交互由业务层实现，组件本身不处理跳转逻辑

### 5.3 `word-wrap`

- 所有文本类型均设置 `word-wrap: break-word`，确保长文本自动换行不溢出

---

## 6. 设计 Token

| Token 名称 | CSS 变量 | 值 | 使用变体 |
|-----------|---------|------|---------|
| 主文字色 | `--文本色-text_primary` | `rgba(0, 0, 0, 0.90)` | A1-A6 |
| 链接色 | `--文本色-text_link` | `#214CA5` | A7 |
| 次文字色 | `--文本色-text_primary_light` | `rgba(60, 60, 67, 0.76)` | A8 |
| 背景色 | `--通用背景色-bg_bottom_light` | `white` | 所有 |

---

## 7. 使用场景

| 场景 | 推荐变体 |
|------|---------|
| 页面/模块大标题 | A1（单行）、A2（双行） |
| 内容区段标题 | A3（一级标题） |
| 二级分类标题 | A4（二级标题） |
| 说明文案/详情描述 | A5（正文段落） |
| 带序号/标记的段落 | A6（前缀正文） |
| 可点击的文字链 | A7（链接文本） |
| 底部辅助提示 | A8（辅助说明） |
