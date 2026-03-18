# 半屏导航栏组件设计与技术规范 (HalfScreen NavBar Component Spec)

## 1. 组件概述 (Overview)

半屏导航栏是专用于半屏浮层（Bottom Sheet / Half-Screen Overlay）顶部的导航组件，承载标题展示、层级返回与关闭操作。与全屏顶部导航栏（NavBar）不同，半屏导航栏始终锚定在浮层内容区顶部，宽度跟随浮层容器而非全屏。

## 2. 组件分类

### A. 一级导航（Primary Level）

一级导航用于半屏浮层的首屏，无返回层级，右侧固定为关闭操作。

| ID | 名称 | 结构 | 高度 | 说明 |
|----|------|------|------|------|
| A1 | 标题+关闭 | 左侧标题 + 右侧关闭按钮(圆形底色) | 54px | 最常用的半屏导航形态 |
| A2 | 标题+副标题+关闭 | 左侧标题+副标题 + 右侧关闭按钮(圆形底色) | 65px | 需要补充说明信息时使用 |
| A3 | 单关闭 | 右侧关闭按钮(圆形底色)，无标题 | 54px | 内容自带标题或以图片开头时使用；遇到图片组件时叠在图片上不占高度 |
| A4 | 图标+标题+关闭 | 左侧App图标+标题 + 右侧功能图标 | 54px | 展示来源应用信息时使用 |

### B. 二级导航（Secondary Level）

二级导航用于半屏浮层内的子页面，左侧为返回操作，中间居中显示标题。

| ID | 名称 | 结构 | 高度 | 说明 |
|----|------|------|------|------|
| B1 | 返回+标题+操作 | 左侧返回箭头 + 居中标题 + 右侧文字操作 | 54px | 子页面带操作入口 |
| B2 | 返回+标题+关闭 | 左侧返回箭头 + 居中标题 + 右侧功能图标 | 54px | 子页面带功能图标 |
| B3 | 返回+标题 | 左侧返回箭头 + 居中标题 | 54px | 最简子页面导航 |

## 3. 布局规范

### 3.1 尺寸与间距

- **组件宽度**：跟随半屏浮层宽度（默认 100%）
- **基准高度**：54px（A2 副标题型为 65px）
- **水平内边距**：左右各 16px
- **关闭按钮**：30×30px 圆形，背景 rgba(0,0,0,0.04)，图标 16×16px
- **返回箭头**：24×24px
- **App图标**：24×24px，与标题间距 8px

### 3.2 文字规范

| 元素 | 字号 | 字重 | 颜色 |
|------|------|------|------|
| 标题 | 17px | Medium (500) | text_primary rgba(0,0,0,0.90) |
| 副标题 | 12px | Regular (400) | text_secondary rgba(60,60,67,0.76) |
| 操作文字 | 17px | Regular (400) | text_primary rgba(0,0,0,0.90) |
| 二级标题 | 17px | Medium (500) | text_primary rgba(0,0,0,0.90) |

### 3.3 对齐方式

- **一级导航**：标题左对齐，关闭按钮右对齐，垂直居中
- **二级导航**：返回箭头左对齐，标题绝对居中，操作/图标右对齐

## 4. 交互规范

### 4.1 A3 单关闭型特殊逻辑

A3 类型无标题文字，仅显示关闭按钮。在组合使用时遵循以下规则：

- **遇到图片组件（image_block）**：A3 叠在图片上方，设置为绝对定位，不占据内容流高度（`position: absolute; z-index: 10`），关闭按钮使用白色/半透明背景以保证可见性
- **遇到其他组件类型**：A3 正常占据一行高度（54px），按标准流式布局排列

### 4.2 关闭行为

- 点击关闭按钮：收起整个半屏浮层
- 点击返回箭头：返回半屏内上一层级页面

## 5. 变体矩阵

共 7 种子组件，由 A一级(4种) + B二级(3种) 构成。

```
A1  标题+关闭           → [标题]                    [X]
A2  标题+副标题+关闭    → [标题/副标题]              [X]
A3  单关闭              →                            [X]
A4  图标+标题+关闭      → [🔲 标题]                  [📷]
B1  返回+标题+操作      → [←]      [二级标题]     [操作]
B2  返回+标题+关闭      → [←]      [二级标题]      [📷]
B3  返回+标题           → [←]      [二级标题]
```

---

## 6. CSS 实现代码块

### 6.1 半屏导航栏行

```css
.hs-navbar-row {
    display: flex;
    align-items: center;
    width: 429px;
    background: white;
    position: relative;
    box-sizing: border-box;
}
.hs-navbar-row.level-1 {
    height: 54px;
    padding: 0 16px;
    justify-content: space-between;
}
.hs-navbar-row.level-1-subtitle {
    height: 65px;
    padding: 0 16px;
    justify-content: space-between;
}
.hs-navbar-row.level-2 {
    height: 54px;
    padding: 0 16px;
    justify-content: space-between;
}
```

### 6.2 三区域

```css
.hs-navbar-row .hs-left-area {
    display: flex;
    align-items: center;
    flex-shrink: 0;
}
.hs-navbar-row .hs-left-group {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.hs-navbar-row .hs-center-title {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 500;
    color: rgba(0, 0, 0, 0.90);
    line-height: 24px;
    text-align: center;
}
.hs-navbar-row .hs-right-area {
    display: flex;
    align-items: center;
    flex-shrink: 0;
}
```

### 6.3 文字与操作元素

```css
.hs-navbar-row .hs-title {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 500;
    color: rgba(0, 0, 0, 0.90);
    line-height: 24px;
}
.hs-navbar-row .hs-subtitle {
    font-size: 12px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: rgba(60, 60, 67, 0.76);
    line-height: 17px;
}
.hs-navbar-row .hs-close-btn {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: rgba(0, 0, 0, 0.04);
    display: flex;
    align-items: center;
    justify-content: center;
}
.hs-navbar-row .hs-close-btn svg {
    width: 16px;
    height: 16px;
}
.hs-navbar-row .hs-action-text {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: rgba(0, 0, 0, 0.90);
    line-height: 24px;
}
.hs-navbar-row .hs-back-icon {
    width: 24px;
    height: 24px;
}
.hs-navbar-row .hs-app-icon {
    width: 24px;
    height: 24px;
    margin-right: 8px;
}
```
