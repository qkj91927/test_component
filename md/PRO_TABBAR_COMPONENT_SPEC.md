# 底部导航栏Pro TabBarPro — 组件设计规范

> **组件层级**：高级组件 · 导航  
> **组件 ID**：`PRO_tabbar`  
> **替代关系**：无对应默认组件，为高级组件库新增

---

## 一、组件概述

底部导航栏Pro 是高级组件库中的底部导航组件，采用**胶囊容器 + 圆形浮动按钮(FAB)**的设计语言，固定在页面底部，为用户提供主要功能的快速切换入口。共 9 种固定变体，分为 A.FAB模式（100px）和 B.纯Tab模式（92px）两大类。

### 设计特征

| 特征 | 说明 |
|------|------|
| FAB 按钮 | 60×60px 圆形，`rgba(120,120,128,0.08)` 液态玻璃背景，圆角 9999px，`backdrop-filter: saturate(180%) blur(20px)` + `border: 0.5px solid rgba(255,255,255,0.6)` + `box-shadow` |
| FAB 图标尺寸 | 28×28px，居中于 60px 圆形按钮内（padding 16px） |
| 胶囊容器 | 圆角 296px，`rgba(120,120,128,0.08)` 液态玻璃背景 + `backdrop-filter` + border + box-shadow，外层 padding 4px |
| Tab项 | 图标(24px) + 文字(10px)，选中态带 `rgba(120,120,128,0.24)` 深色液态玻璃圆角背景 |
| 背景 | 透明，组件自带淡灰色半透明效果，白色/有色背景上均可见 |
| 资源路径 | `assets/CodeBuddyAssets/3575_4084/` |

---

## 二、子组件矩阵（9种变体）

### A. FAB模式（5种）— 高度 100px

带左侧和/或右侧 60px 圆形浮动按钮，Tab胶囊容器与 FAB 并排。

| 编号 | 左FAB | Tab数 | 右FAB | 胶囊宽度 | Tab宽度 | Tab位置 |
|------|-------|--------|-------|----------|---------|---------|
| T1 | 有 | 0 | 有 | — | — | — |
| T2 | 有 | 2 | 有 | 190px | 100px | 居中 |
| T3 | 无 | 2 | 有 | 190px | 100px | 左对齐(24px) |
| T4 | 无 | 3 | 有 | 280px | 100px | 左对齐(24px) |
| T5 | 无 | 4 | 有 | 296px | 81.5px | 左对齐(24px) |

### B. 纯Tab模式（4种）— 高度 92px

无 FAB 按钮，Tab胶囊容器在 428px 宽度内居中。

| 编号 | Tab数 | 胶囊宽度 | Tab宽度 | Tab位置 |
|------|--------|----------|---------|---------|
| T6 | 2 | 190px | 100px | 居中 |
| T7 | 3 | 280px | 100px | 居中 |
| T8 | 4 | 380px | 102.5px | 居中 |
| T9 | 5 | 380px | 84px | 居中 |

---

## 三、属性约束

### 3.1 FAB 按钮规格

| 属性 | 值 |
|------|------|
| 尺寸 | 60×60px |
| 圆角 | 9999px（全圆） |
| 背景 | `rgba(255, 255, 255, 0.72)` 毛玻璃 |
| 模糊 | `backdrop-filter: saturate(180%) blur(20px)` |
| 图标尺寸 | 28×28px |
| 图标内边距 | 16px |
| 左FAB X坐标 | 24px |
| 右FAB X坐标 | 344px |

### 3.2 胶囊容器规格

| 属性 | 值 |
|------|------|
| 高度 | 52px（内层），60px（外层含 4px padding） |
| 圆角 | 296px |
| 背景 | `rgba(120, 120, 128, 0.08)` 液态玻璃 |
| 模糊 | `backdrop-filter: saturate(180%) blur(20px)` |
| 边框 | `0.5px solid rgba(255,255,255,0.6)` |
| 阴影 | `0 0.5px 2px rgba(0,0,0,0.06), inset 0 0.5px 0 rgba(255,255,255,0.25)` |
| 外层 padding | 4px |

### 3.3 Tab项规格

| 属性 | 值 |
|------|------|
| 高度 | 52px |
| 圆角 | 100px（全圆角胶囊） |
| 选中态背景 | `rgba(120, 120, 128, 0.08)` 同色 + `border: 0.5px solid rgba(255,255,255,0.8)` + `box-shadow: 0 2px 8px rgba(0,0,0,0.10), inset 0 1px 0 rgba(255,255,255,0.5)` 更强立体感 |
| 未选中态背景 | 透明 |
| 选中态图标 | 主题蓝 `#0A84FF`（通过 CSS filter 上色） |
| 未选中态图标 | `opacity: 0.45` 淡灰 |
| 图标尺寸 | 24×24px |
| 图标+文字容器 | 24×40px，top:6px |
| 选中态文字 | 10px / PingFang SC / **500** / `#0A84FF` 主题蓝 |
| 未选中态文字 | 10px / PingFang SC / 400 / `rgba(0, 0, 0, 0.45)` 淡灰 |
| 文字距图标 | top:26px（相对图标容器） |
| 点击交互 | 点击 Tab 项切换选中态，选中态毛玻璃背景跟随切换 |

### 3.4 整体布局

| 属性 | A类(FAB模式) | B类(纯Tab模式) |
|------|-------------|---------------|
| 总高度 | 100px | 92px |
| Tab容器 top | 20px | 16px |
| FAB top | 16px | — |
| 组件宽度 | 428px | 428px |

---

## 四、CSS 实现代码块

### 4.1 液态玻璃效果（iOS 26 Liquid Glass）

```css
/* 固定底部导航栏区域 — 吸底容器（透明，液态玻璃在子元素上） */
.phone-tabbar-fixed {
    flex-shrink: 0;
    width: 428px;
}

/* FAB 浮动按钮 — 60px 圆形液态玻璃 */
.pro-tabbar-fab {
    width: 60px;
    height: 60px;
    border-radius: 9999px;
    background: rgba(120, 120, 128, 0.08);
    backdrop-filter: saturate(180%) blur(20px);
    -webkit-backdrop-filter: saturate(180%) blur(20px);
    border: 0.5px solid rgba(255, 255, 255, 0.5);
    box-shadow: 0 0.5px 2px rgba(0, 0, 0, 0.06),
                inset 0 0.5px 0 rgba(255, 255, 255, 0.25);
}

/* 胶囊容器背景 — 液态玻璃 */
.pro-tabbar-capsule-bg {
    border-radius: 296px;
    background: rgba(120, 120, 128, 0.08);
    backdrop-filter: saturate(180%) blur(20px);
    -webkit-backdrop-filter: saturate(180%) blur(20px);
    border: 0.5px solid rgba(255, 255, 255, 0.5);
    box-shadow: 0 0.5px 2px rgba(0, 0, 0, 0.06),
                inset 0 0.5px 0 rgba(255, 255, 255, 0.25);
}

/* Tab 项 — 可点击，选中态液态玻璃 */
.pro-tabbar-item {
    position: absolute;
    height: 52px;
    cursor: pointer;
}

/* Tab 项选中态背景（同色底+更强立体感） */
.pro-tabbar-item.selected .pro-tabbar-item-bg {
    background: rgba(120, 120, 128, 0.08);
    backdrop-filter: saturate(180%) blur(20px);
    -webkit-backdrop-filter: saturate(180%) blur(20px);
    border: 0.5px solid rgba(255, 255, 255, 0.8);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.10),
                0 0.5px 2px rgba(0, 0, 0, 0.06),
                inset 0 1px 0 rgba(255, 255, 255, 0.5);
    border-radius: 100px;
}

/* 选中态图标+文字 — 主题蓝 */
.pro-tabbar-item.selected img {
    filter: brightness(0) saturate(100%) invert(40%) sepia(90%) saturate(2000%) hue-rotate(200deg) brightness(105%);
    opacity: 1;
}
.pro-tabbar-item.selected span {
    color: #0A84FF;
    font-weight: 500;
}

/* 未选中态图标+文字 — 淡灰 */
.pro-tabbar-item img { opacity: 0.45; }
.pro-tabbar-item span { color: rgba(0, 0, 0, 0.45); font-weight: 400; }

/* Tab 项未选中态 */
.pro-tabbar-item-bg {
    border-radius: 100px;
}
```

> ⚠️ **选中态设计原则**：选中态不通过加深底色来区分，而是通过 ① 图标+文字变为主题蓝色 `#0A84FF` ② 更强的立体玻璃感（更大阴影 + 更亮边框 + 内发光）来凸显。

### 4.2 Tab 项文字样式

```css
.pro-tabbar-item-icon {
    width: 24px;
    height: 24px;
}
.pro-tabbar-item-label {
    font-size: 10px;
    font-family: PingFang SC;
    font-weight: 400;
    color: rgba(0, 0, 0, 0.90);
    text-align: center;
}
```

### 4.3 点击切换交互（JavaScript）

```javascript
// 全局事件委托 — PRO TabBar 点击切换选中态
document.addEventListener('click', function(e) {
    const tabbarItem = e.target.closest('.pro-tabbar-item');
    if (tabbarItem) {
        const capsule = tabbarItem.parentElement;
        if (capsule) {
            // 清除所有选中态
            capsule.querySelectorAll('.pro-tabbar-item').forEach(t => {
                t.classList.remove('selected');
                const bg = t.querySelector('.pro-tabbar-item-bg');
                if (bg) {
                    bg.style.background = '';
                    bg.style.backdropFilter = '';
                    bg.style.webkitBackdropFilter = '';
                    bg.style.border = '';
                    bg.style.boxShadow = '';
                }
                // 未选中：灰色图标+文字
                const content = t.querySelector('.pro-tabbar-item-content');
                if (content) {
                    const img = content.querySelector('img');
                    if (img) { img.style.filter = ''; img.style.opacity = '0.45'; }
                    const span = content.querySelector('span');
                    if (span) { span.style.color = 'rgba(0,0,0,0.45)'; span.style.fontWeight = '400'; }
                }
            });
            // 设置当前选中态（同色底+更强立体感+主题蓝色图标文字）
            tabbarItem.classList.add('selected');
            const bg = tabbarItem.querySelector('.pro-tabbar-item-bg');
            if (bg) {
                bg.style.background = 'rgba(120,120,128,0.08)';
                bg.style.backdropFilter = 'saturate(180%) blur(20px)';
                bg.style.webkitBackdropFilter = 'saturate(180%) blur(20px)';
                bg.style.border = '0.5px solid rgba(255,255,255,0.8)';
                bg.style.boxShadow = '0 2px 8px rgba(0,0,0,0.10), 0 0.5px 2px rgba(0,0,0,0.06), inset 0 1px 0 rgba(255,255,255,0.5)';
            }
            const content = tabbarItem.querySelector('.pro-tabbar-item-content');
            if (content) {
                const img = content.querySelector('img');
                if (img) { img.style.filter = 'brightness(0) saturate(100%) invert(40%) sepia(90%) saturate(2000%) hue-rotate(200deg) brightness(105%)'; img.style.opacity = '1'; }
                const span = content.querySelector('span');
                if (span) { span.style.color = '#0A84FF'; span.style.fontWeight = '500'; }
            }
        }
    }
});
```

---

## 五、使用规则

1. **固定在页面最底部**：位于 HomeBar（34px）之上，不参与内容滚动
2. **液态玻璃效果**：FAB、胶囊容器、Tab选中态均采用 iOS 26 液态玻璃设计（淡灰色半透明背景 + 细边框 + 内外阴影），在白色/有色背景上均可见
3. **图标必须替换**：SVG 资源为占位图标，实际使用时必须替换
4. **第一个 Tab 默认选中**：选中态显示圆角深色背景
5. **A类与B类不可同页混用**：选择一种模式
6. **FAB 按钮为独立操作入口**：不参与 Tab 切换逻辑
