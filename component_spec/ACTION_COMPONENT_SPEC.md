# 操作组合 ActionCombo 组件设计规范 (ActionCombo Component Spec)

本文件定义了移动端操作组合组件的系统化构建逻辑、属性约束及 UI 规范。操作组合用于页面底部或表单尾部的操作区域，分为 **操作组合 (A)** 和 **辅助操作组合 (B)** 两大类。

---

## 1. 组件概述 (Overview)

操作行是半屏浮层、弹窗、表单等场景底部的核心交互区域。它由两类子组件构成：

- **A. 操作行 (Action Bar)**：以 **Button 按钮** 为主的操作区域，承载主要交互行为（确认、取消、提交等）。
- **B. 辅助操作行 (Auxiliary Action Bar)**：以 **Action 文字链** 为主的辅助操作区域，承载次要交互（协议勾选、文字链跳转等）。

**核心区别：**
- **Button (按钮)**：圆角胶囊型实体按钮，具有明确的视觉层级（一级/二级），适用于主操作。
- **Action (文字链)**：纯文字链接，无背景色，颜色为 `text_link`，适用于辅助操作。

---

## 2. 属性定义 (Properties)

### 2.1 A. 操作行 (Action Bar) — 7 种变体

| 标识 | 名称 | 构成 | 高度 | 来源 Frame |
| :--- | :--- | :--- | :--- | :--- |
| A1 | 双按钮（二级+一级） | 1 个二级按钮 + 1 个一级按钮，等宽排列 | 84px | 1_9731 |
| A2 | 三按钮（二级+二级+一级） | 2 个二级按钮 + 1 个一级按钮，等宽排列 | 84px | 1_9731 |
| A3 | 单按钮（一级满宽） | 1 个一级按钮，满宽 | 84px | 1_9731 |
| A4 | 单按钮（二级满宽） | 1 个二级按钮，满宽 | 84px | 1_9731 |
| A5 | 图标按钮组+一级按钮 | 3 个圆形图标按钮 + 1 个一级按钮 | 84px | 1_9731 |
| A6 | 四宫格操作 | 4 个图标+文字操作项，等宽排列 | 72px | 1_9731 |
| A7 | 操作+勾选+按钮 | 文字操作 + 2 个勾选项 + 小一级按钮 | 72px | 1_9731 |

### 2.2 B. 辅助操作行 (Auxiliary Action Bar) — 5 种变体

| 标识 | 名称 | 构成 | 高度 | 来源 Frame |
| :--- | :--- | :--- | :--- | :--- |
| B1 | 勾选+文案+文字链 | Checkbox + 辅助文案 + 文字链 | 36px | 1_9746 |
| B2 | 辅助文案+文字链 | 辅助说明文案 + 文字链 | 36px | 1_9746 |
| B3 | 单 Action | 1 个居中 Action 文字链 | 36px | 1_9746 |
| B4 | 双 Action | 2 个 Action 文字链 + 分隔线 | 36px | 1_9746 |
| B5 | 三 Action | 3 个 Action 文字链 + 分隔线 | 36px | 1_9746 |

---

## 3. 按钮属性详解 (Button Properties)

### 3.1 一级按钮 (Primary Button)
| 属性 | 值 |
| :--- | :--- |
| 背景色 | `var(--品牌色-brand_standard, #0099FF)` |
| 文字色 | `var(--文本色-text_allwhite, white)` |
| 字号 | 17px (大) / 14px (小) |
| 字重 | 600 (大) / 500 (小) |
| 高度 | 52px (大) / 36px (小) |
| 圆角 | 999px / 9999px |
| Figma 属性 | `data-图标="false" data-尺寸="大/小" data-状态="默认" data-类型="一级"` |

### 3.2 二级按钮 (Secondary Button)
| 属性 | 值 |
| :--- | :--- |
| 背景色 | `var(--透明填充色-Tertiary, rgba(118, 118, 128, 0.12))` |
| 文字色 | `var(--文本色-text_primary, rgba(0, 0, 0, 0.90))` |
| 字号 | 17px |
| 字重 | 600 |
| 高度 | 52px |
| 圆角 | 999px |
| Figma 属性 | `data-图标="false" data-尺寸="大" data-状态="默认" data-类型="二级"` |

### 3.3 图标按钮 (Icon Button)
| 属性 | 值 |
| :--- | :--- |
| 背景色 | `var(--透明填充色-Tertiary, rgba(118, 118, 128, 0.12))` |
| 尺寸 | 52×52px |
| 图标尺寸 | 24×24px |
| 圆角 | 999px |
| Figma 属性 | `data-图标="true" data-尺寸="大" data-状态="默认" data-类型="二级"` |

---

## 4. Action 文字链属性详解 (Action Text Link Properties)

| 属性 | 值 |
| :--- | :--- |
| 字号 | 14px |
| 字重 | 500 |
| 颜色 | `var(--文本色-text_link, #214CA5)` |
| 分隔线 | 1×14px, `rgba(0, 0, 0, 0.08)`, 水平间距 8px |

### 辅助文案
| 属性 | 值 |
| :--- | :--- |
| 字号 | 14px |
| 字重 | 400 |
| 颜色 | `var(--文本色-text_secondary, rgba(60, 60, 67, 0.76))` |

### 勾选框 (Checkbox)
| 属性 | 值 |
| :--- | :--- |
| 尺寸 | 16×16px (B1) / 20×20px (A7) |
| 间距 | 右侧 4px |
| Figma 属性 | `data-尺寸="大" data-状态="未选中" data-类型="普通型"` |

---

## 5. 布局规格 (Layout Specs)

### A. 操作行布局
| 属性 | 值 |
| :--- | :--- |
| 容器宽度 | 428px (适配 iOS 标准宽度) |
| 内边距 | A1-A4: `16px 24px`; A5: `16px`; A6: `16px`; A7: `16px` |
| 按钮间距 | 12px |
| A6 每项宽度 | 99px |

### B. 辅助操作行布局
| 属性 | 值 |
| :--- | :--- |
| 容器宽度 | 428px |
| 行高 | 36px |
| 内边距 | `0 16px` |
| 对齐方式 | 居中 (center) |

---

## 6. 设计 Token (Design Tokens)

| Token 名称 | CSS 变量 | 值 |
| :--- | :--- | :--- |
| 品牌色 | `--品牌色-brand_standard` | `#0099FF` |
| 文字白 | `--文本色-text_allwhite` | `white` |
| 主文字 | `--文本色-text_primary` | `rgba(0, 0, 0, 0.90)` |
| 次文字 | `--文本色-text_secondary` | `rgba(60, 60, 67, 0.76)` |
| 链接色 | `--文本色-text_link` | `#214CA5` |
| 透明填充 | `--透明填充色-Tertiary` | `rgba(118, 118, 128, 0.12)` |
| 分隔线色 | — | `rgba(0, 0, 0, 0.08)` |

---

## 7. 资源映射 (Asset Mapping)

### Frame 1_9731 (操作行 A)
| 文件 | 用途 |
| :--- | :--- |
| `2.svg` | 图标按钮内图标 (24×24) |
| `6.svg` | 四宫格操作项图标 (24×24) |
| `9.svg` | 勾选框图标 (20×20) |

### Frame 1_9746 (辅助操作行 B)
| 文件 | 用途 |
| :--- | :--- |
| `1.svg` | Checkbox 勾选框 (16×16) |
| `3.svg` | Action 分隔线 SVG |

---

## 8. 使用场景 (Usage Scenarios)

| 场景 | 推荐变体 |
| :--- | :--- |
| 半屏浮层确认操作 | A1 (双按钮) 或 A3 (单一级按钮) |
| 表单提交 | A3 (单一级按钮) + B1 (勾选+协议文案) |
| 多操作选择 | A2 (三按钮) |
| 分享/收藏等快捷操作 | A5 (图标按钮组) 或 A6 (四宫格) |
| 底部辅助链接 | B3-B5 (Action 文字链) |
| 协议勾选+说明 | B1 (勾选+文案+文字链) |

---

## 9. CSS 实现代码块

### 9.1 操作容器

```css
.action-container {
    width: 428px;
    display: flex;
    flex-direction: column;
}
```

### 9.2 按钮行 (A 类)

```css
.action-button-row {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 16px 24px;
    background: white;
    width: 428px;
    box-sizing: border-box;
    gap: 12px;
}
.action-button-row.grid-row {
    padding: 16px;
    gap: 0;
    justify-content: flex-start;
}
.action-button-row.mixed-row {
    padding: 16px;
    justify-content: space-between;
}
```

### 9.3 按钮样式

```css
.action-btn-primary {
    height: 52px;
    background: #0099FF;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 17px;
    font-weight: 600;
    color: white;
    flex: 1;
    min-width: 0;
}
.action-btn-primary.fixed-width {
    flex: 0 0 auto;
    padding: 0 24px;
}
.action-btn-primary.small {
    height: 36px;
    font-size: 14px;
    font-weight: 500;
    padding: 0 14px;
    flex: 0 0 72px;
}
.action-btn-secondary {
    height: 52px;
    background: rgba(118, 118, 128, 0.12);
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 17px;
    font-weight: 600;
    color: rgba(0, 0, 0, 0.90);
    flex: 1;
    min-width: 0;
}
.action-icon-btn {
    width: 52px;
    height: 52px;
    background: rgba(118, 118, 128, 0.12);
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.action-icon-btn img {
    width: 24px;
    height: 24px;
}
```

### 9.4 宫格操作项

```css
.action-grid-item {
    width: 99px;
    height: 72px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
}
.action-grid-item img {
    width: 24px;
    height: 24px;
}
.action-grid-item span {
    font-size: 17px;
    font-weight: 400;
    color: rgba(0, 0, 0, 0.90);
}
```

### 9.5 辅助操作行 (B 类)

```css
.action-row {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 36px;
    padding: 0 16px;
    background: white;
    width: 428px;
    gap: 0;
}
.action-row .action-link {
    font-size: 14px;
    font-weight: 500;
    color: #214CA5;
    white-space: nowrap;
}
.action-row .action-separator {
    width: 1px;
    height: 14px;
    background: rgba(0, 0, 0, 0.08);
    margin: 0 8px;
    flex-shrink: 0;
}
.action-row .action-checkbox {
    width: 16px;
    height: 16px;
    margin-right: 4px;
    flex-shrink: 0;
}
.action-row .action-text {
    font-size: 14px;
    color: rgba(60, 60, 67, 0.76);
}
.action-row .action-textlink {
    font-size: 14px;
    color: #214CA5;
}
```
