# 半屏浮层 HalfScreenOverlay 组件设计规范

## 1. 组件概述

半屏浮层（HalfScreenOverlay）是从屏幕底部弹出、约占半屏高度的模态容器组件。它用于承载二级内容、表单、选择器等场景，支持下滑关闭和点击蒙层关闭。分为**标准型**（A3单关闭半屏导航栏）和**把手型**（拖拽把手条）两种子组件。

## 2. 组件结构

### 2.1 标准型（HSO-A）

```
┌──────────────────────────────┐
│        半屏遮罩层 Overlay       │
│   var(--color-overlay-dark)        │
│                              │
│                              │
├──────────────────────────────┤  ← border-radius: 20px (顶部)
│ ┌──────────────────────────┐ │
│ │                    [✕]   │ │  ← 54px A3半屏导航栏（仅关闭按钮，右对齐）
│ ├──────────────────────────┤ │
│ │                          │ │
│ │      内容区域（可滚动）      │ │  ← 高度 = 面板高度 - 54 - 34
│ │                          │ │
│ ├──────────────────────────┤ │
│ │    ▬▬▬ Home Bar ▬▬▬      │ │  ← 安全区域 34px
│ └──────────────────────────┘ │
└──────────────────────────────┘
```

### 2.2 把手型（HSO-B）

```
┌──────────────────────────────┐
│        半屏遮罩层 Overlay       │
│   var(--color-overlay-dark)        │
│                              │
│                              │
├──────────────────────────────┤  ← border-radius: 20px (顶部)
│ ┌──────────────────────────┐ │
│ │       ━━ 把手 ━━          │ │  ← 20px 把手区域（指示条 36×5px）
│ ├──────────────────────────┤ │
│ │                          │ │
│ │      内容区域（可滚动）      │ │  ← 高度 = 面板高度 - 20 - 34
│ │                          │ │
│ ├──────────────────────────┤ │
│ │    ▬▬▬ Home Bar ▬▬▬      │ │  ← 安全区域 34px
│ └──────────────────────────┘ │
└──────────────────────────────┘
```

## 3. 设计 Token

### 3.1 尺寸规范

| 属性 | 值 | 说明 |
|------|-----|------|
| 面板宽度 | 428px | 与设备等宽 |
| 标准型高度 | 360px ~ 720px | 最小 360px，最大 720px，默认 420px，超出内容区可滚动 |
| 把手型高度 | 720px | 固定高度，超出内容区可滚动 |
| 顶部圆角 | 20px | 仅左上、右上 |
| A3半屏导航栏高度（标准型） | 54px | 仅含关闭按钮，无标题 |
| 关闭按钮尺寸 | 30 × 30px | 圆角 50%（正圆），右对齐，水平内边距 16px |
| 关闭图标尺寸 | 16 × 16px | 内联 SVG X 形图标 |
| 把手区域高度（把手型） | 20px | 垂直居中 |
| 把手指示条尺寸 | 36 × 5px | 圆角 2.5px |
| Home Bar 高度 | 34px | 底部安全区域 |
| Home Bar 指示条 | 168.92 × 5.71px | 圆角 2.85px |

### 3.2 颜色规范

| 元素 | 色值 | Token |
|------|------|-------|
| 遮罩层 | rgba(0, 0, 0, 0.50) | 叠加色-overlay_dark |
| 面板背景 | #FFFFFF | 背景色-Primary |
| 关闭按钮背景 | rgba(0, 0, 0, 0.04) | — |
| 把手指示条 | rgba(60, 60, 67, 0.30) | — |
| Home Bar 指示条 | rgba(0, 0, 0, 0.90) | 文本-Text-ultrastrong |

### 3.3 关闭按钮（A3 半屏导航栏样式）

| 属性 | 值 |
|------|-----|
| 位置 | 导航栏右侧，水平内边距 16px，垂直居中 |
| 尺寸 | 30 × 30px |
| 背景 | rgba(0, 0, 0, 0.04) |
| 圆角 | 50%（正圆） |
| 图标 | 16×16px 内联 SVG X 形关闭图标 |
| 图标颜色 | rgba(0, 0, 0, 0.90) |

## 4. 子组件类型定义

### 4.1 标准型（HSO-A）

- **导航区域**: 54px 高度，A3 半屏导航栏（仅关闭按钮，右对齐）
- **面板高度范围**: 360px ~ 720px，默认 420px
- **内容区高度**: sheetHeight - 54（导航栏）- 34（Home Bar），默认 420px 时为 **332px**，超出内容区可滚动
- **适用场景**: 需要明确关闭操作的内容展示、表单填写
- **关闭方式**: 点击关闭按钮、点击蒙层、下滑手势

### 4.2 把手型（HSO-B）

- **导航区域**: 20px 高度，包含居中的把手指示条
- **面板高度**: 固定 720px
- **内容区高度**: 720 - 20（把手条）- 34（Home Bar）= **666px**，超出内容区可滚动
- **适用场景**: 支持手势拖拽调整高度的临时内容展示
- **关闭方式**: 下滑手势超过阈值、点击蒙层

## 5. 变体矩阵

**共 2 种子组件**

| 编号 | 变体 ID | 类型 | 顶部区域 | 名称 |
|------|---------|------|---------|------|
| 1 | HSO-A | 标准型 | A3半屏导航栏（54px） | 标准型 |
| 2 | HSO-B | 把手型 | 拖拽把手条（20px） | 把手型 |

## 6. 交互行为

### 6.1 弹出动效
- 面板从底部滑入，遮罩层同步淡入
- 动效曲线: cubic-bezier(0.32, 0.72, 0.35, 1)
- 入场时长: 420ms

### 6.2 收起动效
- 面板向下滑出，遮罩层同步淡出
- 退场时长: 300ms

### 6.3 关闭触发
- **标准型**: 点击关闭按钮 / 点击蒙层 / 下滑手势
- **把手型**: 下滑手势（超过阈值） / 点击蒙层

### 6.4 内容滚动
- 内容区域支持纵向滚动
- 滚动到顶部时，继续下拉触发面板关闭手势
- 支持 -webkit-overflow-scrolling: touch（120Hz 流畅滚动）

### 6.5 组件构建器特有行为
- HalfScreenOverlay 为模态容器组件，拖入画布时自动创建模态覆盖层
- 面板底部对齐覆盖层底部（`align-items: flex-end`）
- 内容区域（`.hs-overlay-drop-content`）可接受其他非模态子组件拖入（如列表、表单等）
- 侧边栏预览使用 0.45 缩放（`scale(0.45)`），仅展示面板部分不含遮罩
- 侧边栏提供分段选择器切换"标准型 / 把手型"

## 7. 布局规则

1. 面板始终底部对齐，顶部圆角 20px
2. 遮罩层覆盖整个屏幕（matrix 中 outer 容器高度 926px = iPhone 屏幕高度）
3. **标准型高度**: 360px ~ 720px，默认 420px，可随内容增加自动撑高至最大 720px，超出内容区可滚动（`overflow-y: auto`）
4. **把手型高度**: 固定 720px，不可调整，超出内容区可滚动（`overflow-y: auto`）
5. 内容区域允许其他**非模态**组件拖入（如列表、表单等），**禁止**嵌套其他模态组件（ActionSheet、Dialog）
6. 标准型导航栏：采用 A3 半屏导航栏样式，关闭按钮右对齐（30×30px 圆形，内边距 16px）
7. 把手型把手条：指示条固定在顶部区域居中
8. Home Bar 指示条固定在底部安全区域居中

## 8. CSS 实现参考

### 8.1 matrix 中的外层容器（含遮罩）

```css
.hs-overlay-outer {
    width: 428px;
    height: 926px;               /* iPhone 屏幕高度 */
    position: relative;
    background: var(--叠加色-overlay_dark, var(--color-overlay-dark));  /* 遮罩色 */
    overflow: hidden;
}
```

### 8.2 白色面板

```css
.hs-overlay-sheet {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 428px;
    height: /* sheetHeight */;
    background: var(--color-bg-item);
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    overflow: hidden;
}
```

### 8.3 builder 中的面板容器（无遮罩，flex 布局）

```css
/* builder 使用 inline style 而非 class */
{
    width: 428px;  /* 或 100% */
    min-height: 360px;   /* 标准型最小高度 */
    max-height: 720px;
    background: var(--color-bg-item);
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
}
```

### 8.4 标准型导航栏 A3

```css
.hs-overlay-navbar-a3 {
    width: 428px;
    height: 54px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding: 0 16px;
    background: var(--color-bg-item);
    box-sizing: border-box;
}
.hs-overlay-close-btn-a3 {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: var(--color-fill-pressed);
    display: flex;
    align-items: center;
    justify-content: center;
}
```

### 8.5 把手条

```css
.hs-overlay-handle-bar {
    width: 428px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.hs-overlay-handle-indicator {
    width: 36px;
    height: 5px;
    background: var(--color-handle);
    border-radius: 2.5px;
}
```

### 8.6 底部安全区

```css