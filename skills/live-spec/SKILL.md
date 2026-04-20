---
name: live-spec
description: LiveSpec 是"活的设计规范"工作台。当用户要求生成/还原一个界面时自动调用，除了生成页面本身，还在右侧以 Figma Inspector 风格（Tab: Style / 组件）罗列样式 Token 和组件规格，并支持 Edit 模式下点选画布组件实时编辑参数。触发关键词："生成 XX 页面"、"做一个界面"、"根据 Basic 1.0 / QUI 生成..."、"还原 Figma 设计"、"仿 Figma 右侧面板"、"列出 Token / 样式清单"、"可编辑预览 / 走查原型"、"LiveSpec"。产出包含两份文件：纯页面 HTML（含 data-component 标注 + Edit 模式脚本） + 带左画布右 Inspector 的工作台 HTML（含 postMessage 通信）。
---

# LiveSpec · 活的设计规范

> **L**ive preview + design **Spec** = **LiveSpec**
> 一个让设计规范从"PDF 静态文档"变成"可点选、可走查、可实时修改"的交互式工作台。

在生成任何一个界面（页面级、组件级均可）时，除了输出界面本身，**必须**在同级目录再产出一份 LiveSpec 工作台 HTML，用 Figma 风格的 Tab 面板展示 Style Token + 组件规格，并支持 **Edit 模式**：点击顶部 Edit 按钮后，可在左画布点选任一组件，右侧 Inspector 实时展示该组件的 token 参数并允许修改尺寸类字段反馈到画布。

---

## 何时调用

- 用户要求生成/还原一个界面（Figma 回流、基于设计规范从零构建）
- 用户明确要求"列出 Token / 样式清单 / Inspector 面板 / 设计走查"
- 用户要求"仿 Figma 样式"、"类似 Figma 右侧面板"

## 何时不调用

- 仅修改单一 CSS 属性或小范围样式微调
- 纯 JS/逻辑层实现，不涉及视觉界面

---

## 工作流

### 1. 信息收集（先读不写）

并行完成：
- 读取 Figma 画布 HTML（如 `.codebuddy/figma/<nodeId>/figma.html`）
- 读取 Basic 1.0 规范核心文件：
  - `Basic 1.0/README.md`（全局约束）
  - `Basic 1.0/json/index.json`（Token 总表）
  - `Basic 1.0/md/DIVIDER_SPACING_COMPONENT_SPEC.md`（间距规则）
  - `Basic 1.0/css/Qdesign Color Tokens.css`（39 个颜色 Token）
- 按需读取各组件 MD（只读本页用到的组件）

### 2. 组件选型

对 Figma 画布每一个视觉区域，**必须严格映射到 Basic 1.0 的 21 个母组件之一**，并选定合法变体：

| Figma 元素类别 | 首选母组件 |
|---|---|
| 顶部状态（电池/时间） | StatusBar（系统级，不计组件数） |
| 顶部导航栏（返回/标题/操作） | NavBar（97 变体，L×C×R） |
| 搜索框 | Search（A1-B3 六变体） |
| 纯标题/摘要 | TextBlock（H1-H7 + C1-C6） |
| 表单式内容分组 | Grouped List |
| 通栏列表（头像+文本） | Plain List（L×C×R） |
| 横/竖排头像/图片网格 | Grid（A1-A9 平铺 / B1-B8 横滑） |
| 底部安全区 | Home Bar（系统级） |
| 组件之间留白 | Divider & Spacing（xs/s/m/l/xl/xxl） |

⚠️ **禁止自创组件**；若画布元素无法对应，改用最接近的母组件并在"设计审查清单"中记录。

### 3. 产物清单（始终输出两份文件）

| 文件名 | 内容 |
|---|---|
| `<page-name>.html` | 纯界面（428×926 iPhone 14 Pro Max 基准）+ `data-component` 标注 + Edit 模式脚本 + `COMPONENT_TOKENS` |
| `<page-name>-inspector.html` | 工作台：顶部工具栏 + 左画布 iframe + 右 Inspector（Tab 双模式 + Edit 交互） |

#### 产物必须同时满足以下清单（逐项检查）

**页面 HTML（`<page-name>.html`）检查项**：
- [ ] body 背景 `transparent`（R1）
- [ ] `.device` 使用黑色 `border` 非 `box-shadow`（R2）
- [ ] 每个母组件容器加 `data-component="<组件名>"` + `data-variant="<变体>"`（R8）
- [ ] CSS 含 3 条 Edit 模式规则（hover 虚线 / selected 实线）（R8）
- [ ] 脚本声明 `COMPONENT_TOKENS`，每个 data-component 对应一个 tokens 对象（R8）
- [ ] 脚本监听 `click` / `message`，发送 `READY` / `SELECT` / `DESELECT`（R8）

**Inspector HTML（`<page-name>-inspector.html`）检查项**：
- [ ] Grid 布局 `minmax(480px,1fr) 420px`（R3）
- [ ] `html, body { height:100%; overflow:hidden }`（R7）
- [ ] 响应式 <860px 切列并 Inspector 置顶（R4）
- [ ] Inspector 宽度 420px，白底（R5 视觉规范）
- [ ] Tab 双面板 Style / 组件（R6）
- [ ] Edit 按钮 `id="editToggle"`，iframe `id="stage"`（R8）
- [ ] `.canvas` 内有 `#selectionOverlay` 浮层（R8）
- [ ] Inspector 内有 `#selectionCard` / `.edit-empty` / `#editPanel`（R8）
- [ ] 脚本声明 `TOKEN_META` 白名单（R8）

### 4. 文件落位

- 放在**工作区根目录**（或用户指定目录）
- 文件名使用 kebab-case（如 `contact-picker.html`、`settings-page-inspector.html`）
- Inspector 文件名 = 界面文件名 + `-inspector`

---

## 硬性规则（避免踩坑）

### R1. 界面 HTML 的 body 必须透明
```css
html, body {
  background: transparent;  /* 绝对不要 #F5F5F7、#E9E9EE 等灰色 */
  margin: 0; padding: 0;
}
```
**理由**：该文件会被 iframe 嵌入 Inspector，body 灰色会把整个 iframe 区域染灰。

### R2. 设备外壳用黑色边框，不用阴影
```css
.device {
  border: 6px solid #1a1a1a;
  border-radius: 48px;
  /* ❌ 禁止 box-shadow: 0 20px 80px rgba(0,0,0,.18); */
}
```
**理由**：`box-shadow` 在浅底上会产生灰色晕染，影响画布整洁度。

### R3. Inspector 必须用 CSS Grid 保宽，不用 flex
```css
body {
  display: grid;
  grid-template-columns: minmax(480px, 1fr) 360px;
  grid-template-rows: 44px 1fr;
  grid-template-areas:
    "topbar topbar"
    "canvas inspector";
}
```
**理由**：`display: flex` 在窄屏会压缩 Inspector 直至不可见。

### R4. 响应式下 Inspector 置顶，不是沉底
```css
@media (max-width: 860px) {
  body {
    grid-template-columns: 1fr;
    grid-template-areas: "topbar" "inspector" "canvas";
  }
}
```

### R5. 颜色 Token 来源唯一
所有颜色必须来自 `Basic 1.0/css/Qdesign Color Tokens.css`（39 个 QBasicToken），**禁止**在产物里硬编码色值（`rgba(0,0,0,.9)` 等），除了：
- Inspector 自身的 UI（工具栏、面板边框等，非设计系统内容）
- 手机外壳的黑色边框

### R6. Inspector 必须是 Tab 双面板
- **Tab 1 · Style**：TYPOGRAPHY / SIZE / LAYOUT / BOX / Color Tokens / Spacing Scale / Radius Scale / Typography Scale
- **Tab 2 · 组件**：本页每个母组件一张卡片（含 W/H、Padding 折叠盒、字体、颜色、变体 tag）

### R7. 左右双列必须独立滚动
```css
html, body { height: 100%; overflow: hidden; }  /* 锁定视口 */
.canvas    { min-height: 0; height: 100%; overflow: auto; }
.inspector { min-height: 0; height: 100%; overflow: hidden; display: flex; flex-direction: column; }
.tab-panel { flex: 1; overflow-y: auto; }       /* 真正滚动的内层 */
```
**理由**：在 `<body>` 整页可滚时，拖动右侧 Inspector 会连带整个 body 一起滚动，使左侧画布一起上移。必须用 grid 固定视口 + 每列独立 `overflow: auto`，让滚动事件局限在各自容器内。
窄屏响应式（<860px）下**恢复** `html, body { height: auto; overflow: visible; }`，此时 Inspector 和 Canvas 垂直堆叠，共用整页滚动。

### R8. Edit 模式（父 ↔ iframe postMessage）

点击顶部 `Edit` 按钮切换编辑态，左画布可点选组件、右 Inspector 动态显示并允许修改参数。

**消息协议（双向）**：
| 方向 | type | payload | 说明 |
|------|------|---------|------|
| 父 → 子 | `ENTER_EDIT` | — | 进入编辑模式 |
| 父 → 子 | `EXIT_EDIT` | — | 退出编辑模式 |
| 父 → 子 | `APPLY_STYLE` | `{styles: {cssProp: value}}` | 将样式应用到当前选中元素 |
| 子 → 父 | `READY` | — | iframe 加载完成 |
| 子 → 父 | `SELECT` | `{component, variant, tokens, rect}` | 用户点选了某组件 |
| 子 → 父 | `DESELECT` | — | 取消选中 |

**数据源消息来源标识**：父页 `source: 'figma-inspector'`，子页 `source: 'figma-canvas'`，用于过滤其他脚本的消息。

**子页（纯界面 HTML）必备**：
1. 每个母组件容器加 `data-component="<组件名>"` 和 `data-variant="<变体>"`
2. Body 类 `edit-mode` 控制 hover 虚线 + selected 实线
3. 内嵌脚本：监听 click 发送 SELECT；监听 APPLY_STYLE 改自身 style

**父页（Inspector）必备**：
1. `Edit` 按钮切 `.active` 态并派发 ENTER/EXIT 消息
2. `.selection-overlay` 浮层画在 `.canvas` 内绝对定位（以 iframe 在 canvas 中的偏移为坐标系）
3. Edit 模式下 Tab 区域隐藏，改为显示 `.selection-card` + `.edit-panel`
4. `.edit-panel` 中把 tokens 按 `TOKEN_META` 分成可编辑/只读两组渲染，Enter/blur 触发 `APPLY_STYLE`

**约定可编辑键**（TOKEN_META 映射表）：W→width / H→height / MinH→min-height / PaddingX→左右 padding / Gap→gap / Radius→border-radius / LineHeight→line-height。其余字段（字体、颜色、文本）默认只读。

---

## 组件卡片内容模板（Tab 2 每项）

每个组件卡片**至少**包含以下行：

1. **标题行**：组件名 + 变体 tag（如 `L5 · C1 · R3`）
2. **尺寸**：W / H（两列）
3. **Padding**（如有）：T/R/B/L 四格折叠盒
4. **字体**：每个文本层一行 `label + size/weight` + 下一行 `Color + token`
5. **特殊属性**（按组件类型补充）：
   - 列表：L→C Gap / C→R Gap / Divider
   - 输入框：Radius / Fill / Icon 尺寸
   - 宫格：Thumb 尺寸 / Radius / Gap

---

## Inspector 视觉规范（必须严格遵守）

| 元素 | 值 |
|---|---|
| Inspector 宽度 | 420px |
| Inspector 背景 | `#FFFFFF` |
| Inspector 左边框 | 1px `#E5E5EA` |
| 画布背景 | `#F3F3F5`（淡灰地台） |
| 顶部工具栏高度 | 44px |
| 分节标题 | 10px / 600 / `#9A9A9E` / uppercase / letter-spacing: 0.08em |
| 字段框 | 30px 高 / 1px `#E5E5EA` / radius 4px / 白底 |
| 字段 label | 12px `#5A5A5E` |
| 字段 value | 11px `SF Mono, Menlo, monospace` `#1A1A1A` 右对齐 |
| Mixed 值样式 | 12px italic `#9A9A9E`（非等宽） |
| Tab 激活态 | 下边框 2px `#1A1A1A` |
| 色卡 swatch | 14×14px / radius 2px / 1px 浅描边 |

---

## 顶部工具栏元素（固定 5 组）

从左到右：

1. **左图标组**：`↺ 重置` · `↶ 撤销` · `↷ 重做`（28×28，最后一个 disabled 态）
2. **Tweaks 开关**：文字 + 26×16 蓝色滑块（`#0099FF` on / `#D0D0D4` off），可点击
3. **Comment**：描边胶囊 + 对话气泡 SVG 图标
4. **Edit**：`#E0462C` 实心胶囊 + 前置白色圆点
5. **Draw**：文字 + 画笔 SVG 图标
6. 分隔线 1×18px
7. **100%**：`#1A1A1A` 深色胶囊 + 前置白色放大镜 SVG + 等宽字体

---

## 生成流程骨架（伪代码）

```
1. 读取 Figma HTML + Basic 1.0 规范
2. 分析视觉层级 → 列出用到的母组件清单（含变体 ID）
3. 生成 <page-name>.html （基于 templates/page-template.html）
   ├─ 遵守 R1/R2 + Basic 1.0 所有约束
   ├─ R8: 每个母组件加 data-component + data-variant
   └─ R8: 在 COMPONENT_TOKENS 中为每个 data-component 填写 tokens 对象
4. 生成 <page-name>-inspector.html （基于 templates/inspector-template.html）
   ├─ grid layout: topbar(44) + canvas(1fr) + inspector(420)
   ├─ topbar: 左图标组 + 右按钮组（Edit 按钮带 id="editToggle"）
   ├─ canvas: iframe (#stage) 引入 <page-name>.html + #selectionOverlay
   └─ inspector: Tab(Style|组件) + Edit 相关 #selectionCard/.edit-empty/#editPanel
5. 启动本地静态服务（python3 -m http.server PORT）
6. preview_url 打开 inspector 文件让用户查看
7. 输出设计审查清单（缺失组件 / 缺失变体 / 主流对比）
8. 口头告知用户：可点击顶部 Edit 按钮进入编辑模式
```

## 扩展方向（未来版本可加入）

- **颜色可编辑**：TOKEN_META 加入 color 类型，Inspector 渲染取色器
- **字体可编辑**：加入 size/weight 两个 input，修改后应用到 font-size / font-weight
- **历史记录**：父页维护 undo/redo 栈，配合顶栏的 ↺↶↷ 图标激活
- **导出配置**：把当前所有修改导出为 JSON，支持复用到其他界面
- **多选编辑**：shift + click 选中多个同类组件，批量修改

---

## 参考模板

- `templates/page-template.html` — 页面底座（含 Edit 脚本 + COMPONENT_TOKENS 示例）
- `templates/inspector-template.html` — Inspector 工作台（含 postMessage 通信 + TOKEN_META）
- `references/component-cards.md` — 常用组件的 Inspector 卡片片段（Tab 2 用）
- `references/edit-mode-protocol.md` — **Edit 模式完整通信协议**（消息类型、schema、扩展指南）

生成新页面时，建议按以下顺序参考：
1. 复制 `page-template.html` → 改名 + 填入内容（注意每个组件加 `data-component`）
2. 复制 `inspector-template.html` → 替换 `{{PAGE_FILE}}`、`{{PAGE_NAME}}` 占位符
3. 查 `component-cards.md` 填充 Tab 2 的每个组件卡
4. 如需扩展可编辑字段，查 `edit-mode-protocol.md` 第 3 节

---

## 设计审查清单（生成后必须附在对话末尾）

按 Basic 1.0 README 第八章要求，对每次产物做四维审查：

1. **缺失组件**：当前 21 个母组件无法覆盖的需求
2. **缺失变体**：现有组件的变体不足以满足场景
3. **不合理之处**：规范与需求之间的冲突
4. **主流设计系统对比**：vs Apple HIG / Material 3 / One UI，指出差异与可借鉴点

无问题的维度注明"无缺失 / 符合主流规范"。
