# 顶部导航栏设计与技术规范 (NavBar Component Spec)

本文件定义了移动端顶部导航栏母组件的系统化构建逻辑、属性定义及 UI 规范。

---

## 1. 组件构成 (Anatomy)

顶部导航栏（NavBar）采用三段式布局，各区域高度固定，逻辑独立：
- **左侧区域 (Left Area)**：功能动作（如返回、关闭）或个人标识（头像）。
- **中间区域 (Middle Area)**：核心内容展示（如标题、分段选择）。
- **右侧区域 (Right Area)**：页面级操作入口（如分享、提交、更多）。

---

## 2. 属性定义 (Properties)

### 2.1 左侧区域 (L)
| 标识 | 属性名 | 视觉特征 |
| :--- | :--- | :--- |
| L1 | 返回 | 基础返回箭头图标 |
| L2 | 返回+气泡 | 返回箭头 + 数字气泡 (Badge，中性灰色) |
| L3 | 关闭 | 关闭图标 (X) |
| L4 | 图标 | 其他功能性图标 |
| L5 | 操作 | 17px 纯文字按钮 (如“操作”) |
| L6 | 头像 | 个人资料布局：36x36 头像 + 昵称 + 描述信息 |

### 2.2 中间区域 (C)
| 标识 | 属性名 | 视觉特征 |
| :--- | :--- | :--- |
| C0/Empty | Empty | 空白，用于左右分布或自定义 |
| C1 | 标题 | 17px 粗体居中标题 |
| C2 | 下拉标题 | 标题文字 + 向下箭头图标 |
| C3 | 标题+副标题 | 主标题 + 11px 辅助描述 |
| C4 | 标题+可点击副标题 | 主标题 + 黑色 11px 副标题 (具备点击态) |
| C5 | 分段选择 | 分段控制器 (Segmented Control)，胶囊背景 + 选中滑块 |

### 2.3 右侧区域 (R)
| 标识 | 属性名 | 视觉特征 |
| :--- | :--- | :--- |
| R0/Empty | Empty | 不显示任何内容 |
| R1 | 图标 | 单个功能操作图标 |
| R2 | 双图标 | 两个横向排列的操作图标 |
| R3 | 操作 | 黑色 17px 动作文字 (如“完成”) |
| R4 | 按钮 | 胶囊形高亮动作按钮 |
| R5 | 图标+按钮 | 功能图标与按钮的组合展示 |
| R6 | 勾选 | 选中状态标识：蓝色圆形背景 + 白色勾选图标 |

---

## 3. 属性约束 (Constraints)

1. **[L2/返回+气泡] 强绑定**：
   - 只能与中间区域 **[C1/标题]** 或 **[C4/标题+可点击副标题]** 组合。
   - 只能与右侧区域 **[R1/图标]** 组合。（注：在配合 C4 时，允许组合 R3/操作）
2. **[L5/操作] 约束**：
   - 只能与右侧区域 **[R3/操作]** 组合（形成“取消/完成”或“取消/发送”等经典布局）。
3. **[L6/头像] 约束**：
   - 只能与中间区域 **[C0/Empty]** 组合。
   - 只能与右侧区域 **[R1/图标]** 或 **[R2/双图标]** 组合.
4. **[C4/标题+可点击副标题] 强绑定**：
   - 只能与左侧 **[L2/返回+气泡]** 和 right **[R3/操作]** 同时组合.
   - **UI 结构**: 副标题采用与 L6 描述组一致的双 icon + 分隔点结构.
5. **[C5/分段选择] 约束**：
   - 只能与左侧 **[L1/返回]** 或 **[L3/关闭]** 组合.
   - 只能与右侧 **[R1/图标]** 或 **[R0/Empty]** 组合.

---

## 4. 变体矩阵逻辑 (Variants Matrix)

根据 Figma 属性定义，该组件理论全量排列组合为：
- **理论组合总数**: 6 (L) × 6 (C) × 7 (R) = **252 种**。
- **约束过滤后有效变体数**: 应用第 3 节属性约束后，实际有效组合为 **97 种变体**。
- **渲染原则**: HTML 层仅渲染约束过滤后的有效变体，确保三层（HTML / JSON / MD）一致。

---

## 5. UI 设计规格 (Design Specs)

- **容器高度 (Height)**: 44px
- **左右安全区 (Padding)**: 16px
- **布局逻辑**: 
  - **中间内容绝对居中**: 采用 `absolute` 定位，确保标题始终处于容器几何中心，不受左右侧按钮宽度不平衡的影响。
- **区域占位**:
  - 左右区域最小宽度: 60px (确保点击热区)
- **字体规范**:
  - 标题: `font-size: 17px; font-weight: 600; color: rgba(0, 0, 0, 0.9)`
  - 副标题 (C3): `font-size: 11px; color: rgba(0, 0, 0, 0.9)`
  - 描述组 (C4/L6): `font-size: 10px; color: rgba(60, 60, 67, 0.56)`
  - 动作文字: `font-size: 17px; color: rgba(0, 0, 0, 0.9)`
- **图标尺寸**: 24x24px (大图标) / 10x10px (描述组图标)
- **品牌色**: `#0099FF`

---

## 6. CSS 实现代码块

### 6.1 导航栏行

```css
.navbar-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    width: 428px;
    height: 44px;
    background: var(--color-bg-item);
    position: relative;
}
```

### 6.2 三区域布局

```css
.navbar-row .left-area {
    min-width: 60px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    z-index: 2;
}
.navbar-row .middle-area {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 280px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    overflow: hidden;
    z-index: 1;
    pointer-events: none;
}
.navbar-row .middle-area > * {
    pointer-events: auto;
}
.navbar-row .right-area {
    min-width: 60px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 12px;
    z-index: 2;
}
```

### 6.3 文字与操作元素

```css
.navbar-row .nav-title {
    font-size: 17px;
    font-weight: 600;
    color: var(--color-text-primary);
    white-space: nowrap;
    line-height: 1.2;
}
.navbar-row .nav-subtitle {
    font-size: 11px;
    color: var(--color-text-tertiary);
    line-height: 1.2;
    margin-top: 1px;
}
.navbar-row .nav-text {
    font-size: 17px;
    color: var(--color-text-primary);
    cursor: pointer;
    line-height: 24px;
}
.navbar-row .nav-btn {
    background: var(--color-brand-standard);
    color: var(--color-text-allwhite);
    width: 72px;
    height: 32px;
    border-radius: 16px;
    font-size: 14px;
    font-weight: 500;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.navbar-row .nav-icon {
    width: 24px;
    height: 24px;
}
```

### 6.4 头像组件

```css
.nav-profile {
    display: flex;
    align-items: center;
    gap: 8px;
}
.nav-profile-avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    border: 1px solid rgba(0, 0, 0, 0.05);
}
.nav-profile-complex {
    display: flex;
    align-items: center;
    gap: 8px;
    height: 44px;
}
.nav-profile-avatar-wrapper {
    width: 36px;
    height: 36px;
    position: relative;
}
.nav-profile-img {
    width: 36px;
    height: 36px;
    border-radius: 50%;
}
.nav-profile-info {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.nav-profile-name {
    font-size: 17px;
    font-weight: 500;
    color: var(--color-text-primary);
    line-height: 1.2;
}
.nav-profile-desc-group {
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: 10px;
    color: var(--color-text-tertiary);
}
.navbar-row .nav-subtitle.clickable,
.nav-profile-desc-group.clickable {
    cursor: pointer;
    transition: opacity 0.2s;
}
```

### 6.5 搜索栏与分段选择

```css
.nav-search-bar {
    flex: 1;
    height: 32px;
    background: rgba(0, 0, 0, 0.05);
    border-radius: 8px;
    display: flex;
    align-items: center;
    padding: 0 10px;
    color: var(--color-text-tertiary);
    font-size: 14px;
    margin: 0 8px;
}
.nav-segmented-control {
    display: flex;
    width: 196px;
    height: 36px;
    background: var(--color-btn-bg);
    border-radius: 20px;
    padding: 4px;
    position: relative;
    align-items: center;
}
.nav-segment-item {
    flex: 1;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: 500;
    color: var(--color-text-primary);
    z-index: 1;
}
.nav-segment-item.active {
    background: var(--color-bg-item);
    border-radius: 16px;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.12), 0 3px 1px var(--color-fill-pressed);
}
```

### 6.6 徽章与勾选

```css
.nav-badge {
    background: var(--color-border-standard);
    color: var(--color-text-primary);
    font-size: 12px;
    padding: 2px 6px;
    border-radius: 10px;
    margin-left: 4px;
    font-weight: 500;
}
.nav-badge-neutral {
    background: var(--color-border-standard);
    color: var(--color-text-primary);
    font-size: 14px;
    font-family: "SF Pro Display", -apple-system, sans-serif;
    padding: 0 6px;
    height: 24px;
    min-width: 29px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.nav-checkbox-selected {
    width: 24px;
    height: 24px;
    background: var(--color-brand-standard);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--color-text-allwhite);
    border: 1.5px solid var(--color-bg-item);
    box-sizing: border-box;
}
```
