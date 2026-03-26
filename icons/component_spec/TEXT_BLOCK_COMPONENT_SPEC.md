# 文本块 TextBlock · 组件设计规范

纯文本内容的排版区域，涵盖标题、正文、摘要、提示等层级，支持居左与居中两种对齐方式，用于构建页面的信息层次与阅读节奏。

---

## 1. 组件概述

文本块组件包含 **13 种子组件变体**，分为 **A.居左**（7 种）和 **B.居中**（6 种）两大类：

| 编号 | 名称 | 对齐方式 | 文字类型 | 容器高度 |
|------|------|----------|----------|----------|
| A1 | 大标题 | 居左 | title | 50px |
| A2 | 一级标题 | 居左 | subtitle | 44px |
| A3 | 二级标题 | 居左 | aux-title | 42px |
| A4 | 正文段落 | 居左 | body | 56px |
| A5 | 前缀正文 | 居左 | body | 56px |
| A6 | 摘要文本 | 居左 | summary | 48px |
| A7 | 提示文本 | 居左 | hint | 42px |
| B1 | 大标题 | 居中 | title | 50px |
| B2 | 一级标题 | 居中 | subtitle | 44px |
| B3 | 二级标题 | 居中 | aux-title | 42px |
| B4 | 正文段落 | 居中 | body | 56px |
| B5 | 摘要文本 | 居中 | summary | 48px |
| B6 | 提示文本 | 居中 | hint | 42px |

> **A 类与 B 类的区别**：文字属性（字号、字重、行高、颜色）完全相同，仅 `text-align` 不同（`left` vs `center`）。居中类（B）不包含"前缀正文"变体，因为前缀标识在居中排版中无意义。

---

## 2. Markdown 渲染规范

本章节定义了 Markdown 语法与文本块子组件的对应关系，用于 AI 生成内容、富文本渲染等场景。

### 2.1 Markdown 语法触发映射

| Markdown 语法 | 触发的子组件 | 说明 |
|---------------|-------------|------|
| `# 一级标题` | **A1 大标题** | 页面/模块顶级标题 |
| `## 二级标题` | **A2 一级标题** | 内容区段标题 |
| `### 三级标题` | **A3 二级标题** | 二级分类标题 |
| `#### 四级标题` | **A3 二级标题** | 同二级标题，四级及以下统一使用 A3 |
| 普通段落文本 | **A4 正文段落** | 无特殊标记的正文内容 |
| `1. 有序列表` / `- 无序列表` | **A5 前缀正文** | 带序号/标记的列表项 |
| `> 引用文本` | **A6 摘要文本** | 引用块、摘要信息 |
| `*斜体*` / `**粗体**` 段落 | **A4 正文段落** | 内联样式，不改变段落类型 |
| `<small>提示</small>` / 脚注 | **A7 提示文本** | 次要辅助信息、脚注 |
| `[链接文本](url)` | **内联 Textlink** | 链接色文字，可在正文/摘要/提示中使用 |

### 2.1.1 Textlink 链接色规范

在 **A4 正文段落**、**A5 前缀正文**、**A6 摘要文本**、**A7 提示文本** 中，部分文字可设置为 Textlink 链接色，用于标识可点击的超链接或强调性操作入口。

#### 触发条件

| 触发方式 | 语法示例 | 说明 |
|----------|----------|------|
| Markdown 链接 | `[点击查看](https://...)` | 标准超链接语法 |
| 行内 HTML | `<a href="...">链接文字</a>` | HTML 锚点标签 |
| 自定义标记 | `<textlink>文字链接</textlink>` | 纯展示型链接样式（无实际跳转） |

#### Textlink 样式属性

| 属性 | 值 | CSS 变量 |
|------|------|----------|
| 颜色 | `#214CA5` | `var(--text-link)` |
| 字号 | 继承父容器 | — |
| 字重 | 继承父容器（400） | — |
| 下划线 | 无 | `text-decoration: none` |
| 光标 | 手型 | `cursor: pointer` |

#### 适用的文本类型

| 文本类型 | 是否支持 Textlink | 说明 |
|----------|------------------|------|
| A1 大标题 | ❌ 不支持 | 标题不应包含链接 |
| A2 一级标题 | ❌ 不支持 | 标题不应包含链接 |
| A3 二级标题 | ❌ 不支持 | 标题不应包含链接 |
| A4 正文段落 | ✅ 支持 | 正文中嵌入链接 |
| A5 前缀正文 | ✅ 支持 | 列表项中嵌入链接 |
| A6 摘要文本 | ✅ 支持 | 引用/摘要中嵌入链接 |
| A7 提示文本 | ✅ 支持 | 辅助说明中嵌入链接（如"了解更多"） |

#### 使用示例

**正文段落 (A4) 中的 Textlink：**
```
这是正文文本，点击[了解详情](https://...)可查看更多信息。
```
渲染效果：`这是正文文本，点击` <span style="color:#214CA5">了解详情</span> `可查看更多信息。`

**提示文本 (A7) 中的 Textlink：**
```
如有疑问，请[联系客服](https://...)或查看[帮助中心](https://...)。
```
渲染效果：`如有疑问，请` <span style="color:#214CA5">联系客服</span> `或查看` <span style="color:#214CA5">帮助中心</span> `。`

#### 注意事项

1. **链接密度**：单段文本中 Textlink 不宜过多，建议不超过 2 个
2. **链接长度**：Textlink 文字应简洁，通常 2-6 个字为宜
3. **位置建议**：Textlink 常位于句末或作为独立短语
4. **无下划线**：设计规范中 Textlink 不带下划线，仅通过颜色区分

### 2.2 文字块间距规范

文本块之间的垂直间距根据相邻元素类型决定，遵循"层级跨度越大，间距越大"原则：

#### 2.2.1 标题后间距

| 上方元素 | 下方元素 | 间距值 | 说明 |
|----------|----------|--------|------|
| A1 大标题 | A2 一级标题 | **16px** | 大标题后接一级标题 |
| A1 大标题 | A4 正文段落 | **16px** | 大标题后接正文 |
| A2 一级标题 | A3 二级标题 | **12px** | 一级标题后接二级标题 |
| A2 一级标题 | A4 正文段落 | **12px** | 一级标题后接正文 |
| A3 二级标题 | A4 正文段落 | **8px** | 二级标题后接正文 |
| A3 二级标题 | A5 前缀正文 | **8px** | 二级标题后接列表 |

#### 2.2.2 正文/列表间距

| 上方元素 | 下方元素 | 间距值 | 说明 |
|----------|----------|--------|------|
| A4 正文段落 | A4 正文段落 | **8px** | 段落之间 |
| A4 正文段落 | A5 前缀正文 | **8px** | 正文后接列表 |
| A5 前缀正文 | A5 前缀正文 | **4px** | 列表项之间 |
| A5 前缀正文 | A4 正文段落 | **8px** | 列表后接正文 |

#### 2.2.3 辅助文本间距

| 上方元素 | 下方元素 | 间距值 | 说明 |
|----------|----------|--------|------|
| A4 正文段落 | A6 摘要文本 | **12px** | 正文后接摘要 |
| A4 正文段落 | A7 提示文本 | **16px** | 正文后接提示 |
| A6 摘要文本 | A7 提示文本 | **8px** | 摘要后接提示 |
| A7 提示文本 | A2 一级标题 | **24px** | 提示后接新章节 |

#### 2.2.4 章节分隔间距

| 场景 | 间距值 | 说明 |
|------|--------|------|
| 章节结束 → 新章节开始 | **24px** | 一级标题前的分隔 |
| 内容区块结束 → 新区块开始 | **16px** | 二级标题前的分隔 |

### 2.3 组合顺序规范

文本块的堆叠应遵循以下层级顺序，从上到下递进：

```
┌─────────────────────────────────────────────────────┐
│  A1 大标题（页面/模块标题，可选）                      │
├─────────────────────────────────────────────────────┤
│  A2 一级标题（章节标题）                              │ ← 16px
├─────────────────────────────────────────────────────┤
│  A3 二级标题（子章节标题，可选）                       │ ← 12px
├─────────────────────────────────────────────────────┤
│  A4 正文段落 / A5 前缀正文（内容主体）                 │ ← 8px
│  A4 正文段落 / A5 前缀正文                           │ ← 8px/4px
│  ...                                                │
├─────────────────────────────────────────────────────┤
│  A6 摘要文本（引用/摘要，可选）                        │ ← 12px
├─────────────────────────────────────────────────────┤
│  A7 提示文本（辅助说明/脚注，可选）                    │ ← 8px
└─────────────────────────────────────────────────────┘
```

#### 2.3.1 层级递进规则

1. **标题层级递减**：大标题(A1) → 一级标题(A2) → 二级标题(A3)，不可跨级（如 A1 直接到 A3）
2. **内容主体居中**：正文段落(A4)和前缀正文(A5)构成内容核心
3. **辅助信息置尾**：摘要文本(A6)和提示文本(A7)放在内容区块末尾
4. **前缀正文限定**：A5 仅用于带编号/标记的内容，普通文本使用 A4

#### 2.3.2 禁止的组合

| 禁止模式 | 原因 |
|----------|------|
| A7 提示文本 → A4 正文段落 | 提示文本应为区块末尾，后面应是新章节 |
| A6 摘要文本 → A3 二级标题 | 引用后不应直接接子标题 |
| A1 大标题 → A1 大标题 | 同级大标题不可连续 |
| A5 前缀正文 → A1/A2 标题 | 列表项后应有间隔段落或章节分隔 |

#### 2.3.3 推荐的内容模板

**模板 A：标准文章结构**
```
A1 大标题
  └─ A4 正文段落（导语）
  
A2 一级标题（第一章）
  └─ A4 正文段落
  └─ A4 正文段落
  └─ A6 摘要文本
  
A2 一级标题（第二章）
  └─ A3 二级标题
    └─ A4 正文段落
    └─ A5 前缀正文（列表）
  └─ A3 二级标题
    └─ A4 正文段落
  └─ A7 提示文本
```

**模板 B：说明/帮助页面**
```
A2 一级标题（主题）
  └─ A4 正文段落（简介）

A3 二级标题（步骤/要点）
  └─ A5 前缀正文（1. 第一步）
  └─ A5 前缀正文（2. 第二步）
  └─ A5 前缀正文（3. 第三步）

A6 摘要文本（注意事项）
A7 提示文本（更多帮助链接）
```

**模板 C：卡片内简介**
```
A3 二级标题（卡片标题）
  └─ A4 正文段落（简短描述）
  └─ A7 提示文本（时间/来源）
```

---

## 3. 通用布局规格

| 属性 | 值 |
|------|------|
| 容器宽度 | 428px |
| 背景色 | `white`（`var(--bg-item)`） |
| `position` | `relative` |
| 文字区域宽度 | 388px（容器 428 - 左右各 20px 内边距） |
| 文字区域 `left` | 20px |
| 文字区域 `position` | `absolute` |

---

## 4. 文字属性详解

### 4.1 大标题（A1 / B1）

| 属性 | 值 |
|------|------|
| CSS class | `.text-block-title .left` / `.text-block-title .center` |
| 字体 | PingFang SC |
| 字号 | 26px |
| 字重 | 600（Semibold） |
| 行高 | 34px |
| 颜色 | `rgba(0, 0, 0, 0.90)`（`var(--text-primary)`） |
| 文字顶部偏移 | 8px |
| 示例文案 | "大标题 Semibold 26/34" |

### 4.2 一级标题（A2 / B2）

| 属性 | 值 |
|------|------|
| CSS class | `.text-block-subtitle .left` / `.text-block-subtitle .center` |
| 字体 | PingFang SC |
| 字号 | 22px |
| 字重 | 500（Medium） |
| 行高 | 28px |
| 颜色 | `rgba(0, 0, 0, 0.90)`（`var(--text-primary)`） |
| 文字顶部偏移 | 8px |
| 示例文案 | "一级标题 Medium 22/28" |

### 4.3 二级标题（A3 / B3）

| 属性 | 值 |
|------|------|
| CSS class | `.text-block-aux-title .left` / `.text-block-aux-title .center` |
| 字体 | PingFang SC |
| 字号 | 18px |
| 字重 | 500（Medium） |
| 行高 | 26px |
| 颜色 | `rgba(0, 0, 0, 0.90)`（`var(--text-primary)`） |
| 文字顶部偏移 | 8px |
| 示例文案 | "二级标题 Medium 18/26" |

### 4.4 正文段落 / 前缀正文（A4-A5 / B4）

| 属性 | 值 |
|------|------|
| CSS class | `.text-block-body .left` / `.text-block-body .center` |
| 字体 | PingFang SC |
| 字号 | 17px |
| 字重 | 400（Regular） |
| 行高 | 24px |
| 颜色 | `rgba(0, 0, 0, 0.90)`（`var(--text-primary)`） |
| `display` | `inline-block` |
| `vertical-align` | `middle` |
| 文字顶部偏移 | 4px |
| 示例文案 | A4/B4: "这是正文文本，Regular 17/24。……"；A5: "这是前缀正文，Regular 17/24。……" |

> **A4 与 A5 的区别**：A5"前缀正文"用于需要在正文前附加前缀标识（如序号、标记）的场景，CSS 样式与 A4 相同，仅语义和使用场景不同。

### 4.5 摘要文本（A6 / B5）

| 属性 | 值 |
|------|------|
| CSS class | `.text-block-summary .left` / `.text-block-summary .center` |
| 字体 | PingFang SC |
| 字号 | 14px |
| 字重 | 400（Regular） |
| 行高 | 20px |
| 颜色 | `rgba(0, 0, 0, 0.90)`（`var(--text-primary)`） |
| `display` | `inline-block` |
| `vertical-align` | `middle` |
| 文字顶部偏移 | 4px |
| 示例文案 | "这是摘要文本，Regular 14/20，这是摘要文本，Regular 14/20，这是摘要文本，Regular 14/20。" |

### 4.6 提示文本（A7 / B6）

| 属性 | 值 |
|------|------|
| CSS class | `.text-block-hint .left` / `.text-block-hint .center` |
| 字体 | PingFang SC |
| 字号 | 12px |
| 字重 | 400（Regular） |
| 行高 | 20px |
| 颜色 | `rgba(0, 0, 0, 0.90)`（`var(--text-primary)`） |
| `display` | `inline-block` |
| `vertical-align` | `middle` |
| 文字顶部偏移 | 4px |
| 示例文案 | "这是提示文本，Regular 12/20，这是提示文本，Regular 12/20，这是提示文本，Regular 12/20，这是提示文本，Regular 12/20。" |

---

## 5. 容器高度推导

| 变体 | textTop | 内容行数 × 行高 | 容器高度 |
|------|---------|----------------|----------|
| A1/B1 大标题 | 8px | 1 × 34 = 34px | 8 + 34 + 8 = **50px** |
| A2/B2 一级标题 | 8px | 1 × 28 = 28px | 8 + 28 + 8 = **44px** |
| A3/B3 二级标题 | 8px | 1 × 26 = 26px | 8 + 26 + 8 = **42px** |
| A4/A5/B4 正文段落 | 4px | 2 × 24 = 48px | 4 + 48 + 4 = **56px** |
| A6/B5 摘要文本 | 4px | 2 × 20 = 40px | 4 + 40 + 4 = **48px** |
| A7/B6 提示文本 | 4px | ~1.7 × 20 ≈ 34px | 4 + 34 + 4 ≈ **42px** |

---

## 6. 交互行为

### 6.1 文本可编辑（仅组件构建器）

- 在 `component-builder.html` 的画布拼装模式中，所有文本元素添加 `.editable-text` class
- 涵盖 CSS class：`.text-block-title`、`.text-block-subtitle`、`.text-block-aux-title`、`.text-block-body`、`.text-block-summary`、`.text-block-hint`
- 用户可直接点击文本进行内联编辑

### 6.2 `word-wrap`

- 所有文本类型均设置 `word-wrap: break-word`，确保长文本自动换行不溢出

---

## 7. 设计 Token

| Token 名称 | CSS 变量 | 值 | 使用变体 |
|-----------|---------|------|---------| 
| 主文字色 | `--text-primary` | `rgba(0, 0, 0, 0.90)` | 全部（A1-A7、B1-B6） |
| 链接色 | `--text-link` | `#214CA5` | A4/A5/A6/A7/B4/B5/B6 内联 Textlink |
| 背景色 | `--bg-item` / `bg_bottom_light` | `white` | 全部 |

---

## 8. 使用场景

| 场景 | 推荐变体 |
|------|---------| 
| 页面/模块大标题 | A1（居左）、B1（居中） |
| 内容区段标题 | A2（居左）、B2（居中） |
| 二级分类标题 | A3（居左）、B3（居中） |
| 说明文案/详情描述 | A4（居左）、B4（居中） |
| 带序号/标记的段落 | A5（居左前缀正文） |
| 次要摘要信息 | A6（居左）、B5（居中） |
| 底部提示/辅助文字 | A7（居左）、B6（居中） |

---

## 9. CSS 实现代码块

### 9.1 文本块容器

```css
.text-block-container {
    width: 428px;
    background: var(--bg-item);
    position: relative;
}
```

### 9.2 标题体系

```css
/* 大标题 26px */
.text-block-container .text-block-title {
    font-family: 'PingFang SC', sans-serif;
    font-size: 26px;
    font-weight: 600;
    color: var(--text-primary);
    line-height: 34px;
    word-wrap: break-word;
}
.text-block-container .text-block-title.center { text-align: center; }
.text-block-container .text-block-title.left { text-align: left; }

/* 一级标题 22px */
.text-block-container .text-block-subtitle {
    font-family: 'PingFang SC', sans-serif;
    font-size: 22px;
    font-weight: 500;
    color: var(--text-primary);
    line-height: 28px;
    word-wrap: break-word;
}
.text-block-container .text-block-subtitle.center { text-align: center; }
.text-block-container .text-block-subtitle.left { text-align: left; }

/* 二级标题 18px */
.text-block-container .text-block-aux-title {
    font-family: 'PingFang SC', sans-serif;
    font-size: 18px;
    font-weight: 500;
    color: var(--text-primary);
    line-height: 26px;
    word-wrap: break-word;
}
.text-block-container .text-block-aux-title.center { text-align: center; }
.text-block-container .text-block-aux-title.left { text-align: left; }
```

### 9.3 正文、摘要与提示

```css
/* 正文段落 17px */
.text-block-container .text-block-body {
    font-family: 'PingFang SC', sans-serif;
    font-size: 17px;
    font-weight: 400;
    color: var(--text-primary);
    line-height: 24px;
    word-wrap: break-word;
}
.text-block-container .text-block-body.center { text-align: center; }
.text-block-container .text-block-body.left { text-align: left; }

/* 摘要文本 14px */
.text-block-container .text-block-summary {
    font-family: 'PingFang SC', sans-serif;
    font-size: 14px;
    font-weight: 400;
    color: var(--text-primary);
    line-height: 20px;
    word-wrap: break-word;
}
.text-block-container .text-block-summary.center { text-align: center; }
.text-block-container .text-block-summary.left { text-align: left; }

/* 提示文本 12px */
.text-block-container .text-block-hint {
    font-family: 'PingFang SC', sans-serif;
    font-size: 12px;
    font-weight: 400;
    color: var(--text-primary);
    line-height: 20px;
    word-wrap: break-word;
}
.text-block-container .text-block-hint.center { text-align: center; }
.text-block-container .text-block-hint.left { text-align: left; }
```

### 9.4 Textlink 链接样式

```css
/* Textlink 内联链接色 - 适用于正文、摘要、提示文本 */
.text-block-container .text-link,
.text-block-container a {
    color: var(--text-link);
    text-decoration: none;
    cursor: pointer;
}

/* 字号继承父容器 */
.text-block-body .text-link { font-size: 17px; }
.text-block-summary .text-link { font-size: 14px; }
.text-block-hint .text-link { font-size: 12px; }
```
