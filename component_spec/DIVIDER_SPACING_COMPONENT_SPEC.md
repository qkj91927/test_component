# 分隔与间距 Divider & Spacing · 组件规范

## 概述

**分隔与间距**是用于在界面中分隔内容层级、控制视觉节奏的基础布局组件。包含两类子组件：

- **A. 分割线 Divider**：以细线形式分隔同一区域内的列表条目或内容块
- **B. 间距 Spacing**：以透明空白区域分隔不同内容模块，控制页面纵向节奏

## 子组件清单（共 7 种）

| 分类 | ID | 名称 | 说明 |
|------|-----|------|------|
| A. 分割线 | A1 | 分割线 Divider | 基础样式统一，通栏/缩进/方向为使用参数 |
| B. 间距 | B1 | 间距 4px | 最小间距，用于紧凑排列 |
| B. 间距 | B2 | 间距 8px | 小间距，用于同组内容间 |
| B. 间距 | B3 | 间距 12px | 中小间距，用于相关内容间 |
| B. 间距 | B4 | 间距 16px | 标准间距，用于不同组之间 |
| B. 间距 | B5 | 间距 24px | 大间距，用于模块之间 |
| B. 间距 | B6 | 间距 32px | 最大间距，用于主要板块之间 |

## A. 分割线 Divider

### 视觉规范

| 属性 | 值 |
|------|-----|
| 高度 | 0.5px |
| 颜色 | `rgba(0, 0, 0, 0.08)` — `--separator` |
| 背景 | 透明（跟随父容器背景） |

### 使用参数

分割线只有一种基础样式，通栏/缩进/方向不影响基本视觉，仅为使用时的参数变化：

| 模式 | 宽度 | 偏移 | 使用场景 |
|------|------|------|----------|
| 通栏 Full Width | 428px | 无偏移 | 分隔独立内容板块、通栏列表顶底边界 |
| 左缩进 Inset Left | 376px | 左偏移 52px | 列表最常用，与内容文字对齐 |
| 居中 Inset Both | 396px | 左右各缩进 16px | 无左侧图标的列表或卡片内部行间 |

方向支持：水平 (horizontal)、垂直 (vertical)。

### 设计约束

1. 分割线高度固定为 0.5px（Retina 显示屏上的 1 物理像素）
2. 颜色不可自定义，统一使用系统分隔色 `rgba(0, 0, 0, 0.08)`
3. 列表最后一行的底部不显示分割线
4. 同一列表内只使用一种分割线样式
5. 通栏/缩进/方向不构成独立变体

## B. 间距 Spacing

### 视觉规范

| 属性 | 值 |
|------|-----|
| 宽度 | 428px（撑满屏幕宽度） |
| 背景色 | 透明 — `transparent` |
| 高度 | 4px 的整数倍，共 6 种：4 / 8 / 12 / 16 / 24 / 32px |

### 间距梯度

| ID | 高度 | 用途 | 典型场景 |
|----|------|------|----------|
| B1 | 4px | 微间距 | 紧凑排列的辅助信息之间 |
| B2 | 8px | 小间距 | 同组内容块之间、标签与内容之间 |
| B3 | 12px | 中小间距 | 相关联的不同内容组之间 |
| B4 | 16px | 标准间距 | 不同功能组之间的默认间距 |
| B5 | 24px | 大间距 | 不同功能模块之间 |
| B6 | 32px | 超大间距 | 主要板块之间、页面底部留白 |

### 设计约束

1. 间距高度为 4px 的整数倍，遵循 4px 网格系统
2. 间距区域始终为透明背景，不可添加任何可见元素
3. 间距区域横向撑满屏幕宽度
4. 不可使用非标准间距值（如 5px、10px、20px 等）

## Figma 属性映射

### Divider

| Figma 属性 | 类型 | 可选值 |
|------------|------|--------|
| Width Mode | Enum | `FullWidth` / `InsetLeft` / `InsetBoth` |
| Orientation | Enum | `Horizontal` / `Vertical` |

### Spacing

| Figma 属性 | 类型 | 可选值 |
|------------|------|--------|
| Size | Enum | `4` / `8` / `12` / `16` / `24` / `32` |

## 使用指南

### 分割线 vs 间距

| 场景 | 推荐 | 说明 |
|------|------|------|
| 同一列表内条目之间 | 分割线 (A1) | 分割线保持视觉连续性 |
| 不同列表/模块之间 | 间距 (B2-B6) | 间距创造层级区分 |
| 卡片内部行间 | 分割线 (A1) 居中模式 | 居中分割线匹配卡片内边距 |
| 导航栏与内容之间 | 分割线 (A1) 通栏模式 | 通栏分割线标记区域边界 |
| 操作区与内容之间 | 间距 (B4/B5) | 间距留白突出操作区 |

### 组合示例

```
[导航栏 NavBar]
[分割线 A1 · 通栏]
[通栏列表行 1]
[分割线 A1 · 左缩进]
[通栏列表行 2]
[分割线 A1 · 左缩进]
[通栏列表行 3]
[间距 B4 · 16px]
[通栏列表行 4]
[分割线 A1 · 左缩进]
[通栏列表行 5]
[间距 B5 · 24px]
[操作行 Action]
```

---

## CSS 实现代码块

### 分割线

```css
.divider-container {
    width: 428px;
    background: white;
    position: relative;
    display: flex;
    align-items: center;
}
.divider-line {
    height: 0.5px;
    background: rgba(0, 0, 0, 0.08);
}
.divider-line.inset-both {
    width: 396px;
    margin: 0 auto;
}
```

### 间距

```css
.spacing-container {
    width: 428px;
    background: transparent;
    position: relative;
}
.spacing-block-inner {
    width: 428px;
    background: transparent;
}
/* 间距标注（仅设计稿展示用） */
.spacing-annotation {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    font-size: 10px;
    font-family: 'SF Mono', 'Menlo', monospace;
    color: rgba(0, 153, 255, 0.6);
    pointer-events: none;
    white-space: nowrap;
}
.spacing-bg-stripe {
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 100%;
    background: repeating-linear-gradient(
        135deg,
        rgba(0, 153, 255, 0.15),
        rgba(0, 153, 255, 0.15) 2px,
        rgba(0, 153, 255, 0.04) 2px,
        rgba(0, 153, 255, 0.04) 6px
    );
}
```
