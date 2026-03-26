# 操作面板 ActionSheet 组件设计规范

## 1. 组件概述

操作面板（ActionSheet）是从屏幕底部弹出的模态面板，用于向用户提供一组可选操作。它通常在用户需要做出选择或确认操作时触发，是 iOS/移动端设计中的标准交互模式。

## 2. 组件结构

```
┌──────────────────────────────┐
│        半屏遮罩层 Overlay       │
│   var(--color-overlay-dark)        │
├──────────────────────────────┤  ← border-radius: 16px (顶部)
│   ┌──────────────────────┐   │
│   │    操作提示（可选）      │   │  ← 标题行 56px
│   ├──────────────────────┤   │  ← divider 0.5px
│   │    常规操作 Action     │   │  ← 操作行 56px × N (0~5)
│   ├──────────────────────┤   │  ← divider 0.5px
│   │    ...更多操作行...     │   │
│   ├──────────────────────┤   │  ← divider 0.5px
│   │    警示操作（可选）      │   │  ← 警示行 56px
│   └──────────────────────┘   │
│          10px 间距            │  ← 背景色 var(--color-bg-secondary) 露出
│   ┌──────────────────────┐   │
│   │       取消              │   │  ← 取消行 56px
│   │    ▬▬▬ Home Bar ▬▬▬   │   │  ← 安全区域 34px
│   └──────────────────────┘   │
└──────────────────────────────┘
```

## 3. 设计 Token

### 3.1 尺寸规范

| 属性 | 值 | 说明 |
|------|-----|------|
| 面板宽度 | 428px | 与设备等宽 |
| 顶部圆角 | 16px | 仅左上、右上 |
| 行高度 | 56px | 所有行统一高度 |
| 主区块与取消间距 | 10px | 由面板背景色填充 |
| Home Bar 高度 | 34px | 底部安全区域 |
| Home Bar 指示条 | 168.92 × 5.71px | 圆角 2.85px |
| 分割线高度 | 0.5px | 行间分割 |

### 3.2 颜色规范

| 元素 | 色值 | Token |
|------|------|-------|
| 遮罩层 | rgba(0, 0, 0, 0.50) | `--color-overlay-dark` |
| 面板背景 | #F3F3F7 | `--color-bg-secondary` |
| 行背景 | #FFFFFF | `--color-bg-item` |
| 操作提示文字 | rgba(60, 60, 67, 0.76) | `--color-text-secondary` |
| 常规操作文字 | rgba(0, 0, 0, 0.90) | `--color-text-primary` |
| 警示操作文字 | #F74C30 | `--color-feedback-error` |
| 取消文字 | rgba(0, 0, 0, 0.90) | `--color-text-primary` |
| 分割线 | rgba(0, 0, 0, 0.08) | `--color-separator` |
| Home Bar 指示条 | rgba(0, 0, 0, 0.90) | `--color-text-primary` |

### 3.3 字体规范

| 元素 | 字号 | 字重 | 字体 |
|------|------|------|------|
| 操作提示 | 14px | 400 (Regular) | PingFang SC |
| 常规操作 | 17px | 400 (Regular) | PingFang SC |
| 警示操作 | 17px | 400 (Regular) | PingFang SC |
| 取消 | 17px | 400 (Regular) | PingFang SC |

## 4. 行类型定义

### 4.1 标题行（操作提示）

- **样式属性**: `data-样式="标题"`
- **字号**: 14px
- **颜色**: text_secondary
- **对齐**: 水平居中
- **分割线**: 无（位于第一行时）
- **可选性**: 可移除

### 4.2 常规操作行

- **样式属性**: `data-样式="常规操作"`
- **字号**: 17px
- **颜色**: text_primary
- **对齐**: 水平居中
- **分割线**: 顶部 0.5px（非第一行时显示）
- **可选性**: 可移除（但至少保留取消按钮）

### 4.3 警示操作行

- **样式属性**: `data-样式="危险操作"`
- **字号**: 17px
- **颜色**: feedback_error (#F74C30)
- **对齐**: 水平居中
- **分割线**: 顶部 0.5px
- **可选性**: 可移除

### 4.4 取消行

- **样式属性**: `data-样式="常规操作"`
- **字号**: 17px
- **颜色**: text_primary
- **对齐**: 水平居中
- **分割线**: 无（独立区块）
- **可选性**: **不可移除**（始终存在）

## 5. 变体矩阵

操作数量(0-5) × 操作提示(有/无) × 警示操作(有/无) = **22 种变体**

> 约束：操作数量为 0 时，必须有警示操作（至少有一行可执行操作）。

| 编号 | 变体 ID | 操作提示 | 常规操作数 | 警示操作 | 名称 |
|------|---------|---------|-----------|---------|------|
| 1 | AS-0D | ✗ | 0 | ✓ | 警示 |
| 2 | AS-0TD | ✓ | 0 | ✓ | 提示+警示 |
| 3 | AS-1 | ✗ | 1 | ✗ | 1操作 |
| 4 | AS-1D | ✗ | 1 | ✓ | 1操作+警示 |
| 5 | AS-1T | ✓ | 1 | ✗ | 提示+1操作 |
| 6 | AS-1TD | ✓ | 1 | ✓ | 提示+1操作+警示 |
| 7 | AS-2 | ✗ | 2 | ✗ | 2操作 |
| 8 | AS-2D | ✗ | 2 | ✓ | 2操作+警示 |
| 9 | AS-2T | ✓ | 2 | ✗ | 提示+2操作 |
| 10 | AS-2TD | ✓ | 2 | ✓ | 提示+2操作+警示 |
| 11 | AS-3 | ✗ | 3 | ✗ | 3操作 |
| 12 | AS-3D | ✗ | 3 | ✓ | 3操作+警示 |
| 13 | AS-3T | ✓ | 3 | ✗ | 提示+3操作 |
| 14 | AS-3TD | ✓ | 3 | ✓ | 提示+3操作+警示 |
| 15 | AS-4 | ✗ | 4 | ✗ | 4操作 |
| 16 | AS-4D | ✗ | 4 | ✓ | 4操作+警示 |
| 17 | AS-4T | ✓ | 4 | ✗ | 提示+4操作 |
| 18 | AS-4TD | ✓ | 4 | ✓ | 提示+4操作+警示 |
| 19 | AS-5 | ✗ | 5 | ✗ | 5操作 |
| 20 | AS-5D | ✗ | 5 | ✓ | 5操作+警示 |
| 21 | AS-5T | ✓ | 5 | ✗ | 提示+5操作 |
| 22 | AS-5TD | ✓ | 5 | ✓ | 提示+5操作+警示 |

## 6. 交互行为

### 6.1 弹出/收起
- 从底部滑入，配合遮罩层淡入
- 点击遮罩层或"取消"按钮收起
- 收起时向下滑出，遮罩层淡出

### 6.2 操作反馈
- 点击常规操作行：执行对应操作并收起面板
- 点击警示操作行：可触发二次确认或直接执行
- 点击取消：关闭面板，不执行任何操作

### 6.3 组件构建器特有行为
- ActionSheet 为模态组件，拖入画布时自动创建模态覆盖层（`.modal-overlay`，半透明遮罩）
- 面板底部对齐覆盖层底部（`align-items: flex-end`）
- 覆盖层覆盖整个手机画框区域
- 侧边栏预览使用 0.5 缩放（`scale(0.5)`），仅展示面板部分不含遮罩

### 6.4 可配置性（控件对应关系）

组件构建器和变体矩阵中均提供以下控件，且行为严格一致：

| 控件类型 | 控件名称 | 选项 | 对应属性 |
|---------|---------|------|---------|
| 分段选择器 | 操作数量 | 0 / 1 / 2 / 3 / 4 / 5 | actionCount |
| 二态开关 | 操作提示 | 开/关 | hasTitle |
| 二态开关 | 警示操作 | 开/关 | hasDanger |

**约束规则**：当操作数量为 0 时，警示操作开关不可关闭（至少保留一行可执行操作）。

- 操作提示（标题行）：可移除
- 常规操作行：支持 0~5 行
- 警示操作行：可移除（操作数 > 0 时）
- 取消按钮：**不可移除**，始终固定在底部

### 6.4 模态组件嵌套约束
- **禁止**与其他模态组件（Dialog、HalfScreenOverlay）相互嵌套
- ActionSheet 打开时不可再弹出另一个 ActionSheet、Dialog 或 HalfScreenOverlay

## 7. 布局规则

1. **主操作区块**与**取消区块**之间固定 **10px** 间距，间距区域由 outer 容器的 `#F3F3F7` 背景色填充露出
2. 面板总高度 = 主区块高度 + 10px + 取消区块高度(90px)
3. 主区块高度 = 行数 × 56px（行数 = 标题行(0或1) + 常规操作行(0-5) + 警示行(0或1)）
4. 取消区块高度 = 取消行 56px + Home Bar 安全区 34px = **90px**
5. 分割线出现在**非第一行**的顶部（即第二行及以后的行在 `top: 0` 处绘制 0.5px 分割线）
6. 所有文本内容水平居中对齐（`text-align: center`）

## 8. CSS 实现参考

### 8.1 outer 容器

```css
.actionsheet-outer {
    width: 428px;
    height: /* totalHeight，由JS动态设置 */;
    position: relative;
    background: var(--color-bg-secondary);  /* 间距区域的背景色 #F3F3F7 */
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
    overflow: hidden;
}
```

### 8.2 主操作区块

```css
.actionsheet-main-block {
    position: absolute;
    left: 0;
    top: 0;
    width: 428px;
    height: /* mainBlockHeight，由JS动态设置 */;
    background: var(--color-bg-item);
}
```

### 8.3 操作行

```css
.actionsheet-row {
    width: 428px;
    height: 56px;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}
```

### 8.4 分割线与文字样式

```css
.actionsheet-row .as-divider {
    position: absolute;
    left: 0;
    top: 0;
    width: 428px;
    height: 0.5px;
    background: var(--color-separator);
}
.actionsheet-row .as-title-text {
    font-size: 14px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--color-text-secondary);
    text-align: center;
}
.actionsheet-row .as-action-text {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--color-text-primary);
    text-align: center;
}
.actionsheet-row .as-danger-text {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--color-feedback-error);
    text-align: center;
}
```

### 8.5 取消区块

```css
.actionsheet-cancel-block {
    position: absolute;
    left: 0;
    top: /* mainBlockHeight + 10 */px;
    width: 428px;
    background: var(--color-bg-item);
}
.actionsheet-cancel-row {
    width: 428px;
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.actionsheet-cancel-row .as-cancel-text {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--color-text-primary);
    text-align: center;
}
```

### 8.6 Home Bar 指示条

```css