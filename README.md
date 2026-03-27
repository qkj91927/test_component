# 移动端设计系统资源包 v1.3

> **⚠️ AI 模型必读**：本文件是资源包的入口指南，定义了文件读取流程和生成前的强制检查清单。各组件的**硬性约束规则**定义在 `md/<COMPONENT>_SPEC.md` 中，必须在使用对应组件前读取。

---

## 一、设备基准

| 属性 | 值 |
|------|------|
| 设备平台 | iOS（iPhone 13 Pro Max 基准） |
| 屏幕宽度 | **428px** |
| 屏幕高度 | 926px |
| 系统状态栏高度 | 54px（`--device-status-bar-height`） |
| 底部安全区高度 | 34px（HomeBar） |
| 默认字体 | PingFang SC |
| 网格基准 | 4px（所有间距值必须为 4px 的整数倍） |

---

## 二、资源包结构

```
design-system-v1.3/
├── README.md                    ← 入口指南（读取流程 + 检查清单 + 全局约束）
├── component-matrix.html        ← 组件矩阵（所有子组件变体的可视化预览总览）
├── component-builder.html       ← 组件搭建器（拖拽式页面构建，所见即所得）
├── css/
│   ├── tokens.css               ← 全局设计 Token（设备 / 字体 / 间距 / 圆角 / 阴影 / 动效）
│   └── QQ_color_tokens.css      ← QQ 颜色 Token（qq-light / qq-dark 双主题）
├── json/
│   ├── index.json               ← 全局索引 + Token 定义 + 组合规则 + 背景色约束
│   └── components/              ← 各组件的结构化数据（20 个 JSON 文件）
├── md/                          ← 各组件的设计规范文档（20 个 MD 文件，含硬性约束）
├── icons/
│   ├── *.svg                    ← 结构图标（占位/功能性，29 枚）
│   └── QUI_24_icons/            ← QUI 图标库（436 枚，24px SVG）
└── assets/                      ← Figma 切图资源（按设计稿编号组织）
    ├── CodeBuddyAssets/         ← 主资源目录（含多个设计稿子目录）
    └── CodeBubbyAssets/         ← 辅助资源目录
```

### component-matrix.html 与 component-builder.html

| 文件 | 用途 | 说明 |
|------|------|------|
| `component-matrix.html` | 组件矩阵 | 以网格形式预览全部 20 个母组件及其所有子组件变体，用于快速查找和对比 |
| `component-builder.html` | 组件搭建器 | 交互式页面构建工具，支持从母组件列表中选择组件，拖入画布组装完整页面 |

两个文件中的**子组件数量、样式、ID 编码必须严格一致**，是镜像对应关系。

### 结构图标清单（icons/ 根目录）

| 图标文件 | 尺寸 | 用途 |
|----------|------|------|
| `Avatar_32.svg` / `Avatar_40.svg` / `Avatar_52.svg` | 32/40/52px | 头像占位图（列表、消息、卡片） |
| `Thumbnail_24.svg` / `Thumbnail_32.svg` / `Thumbnail_40.svg` / `Thumbnail_52.svg` | 24/32/40/52px | 缩略图占位图 |
| `empty_icon.svg` | 12-24px | 通用占位图标（**实际任务中必须替换为真实图标**） |
| `chevron_right.svg` / `chevron_left.svg` / `chevron_down.svg` | 24px | 方向箭头（跳转/返回/展开） |
| `close.svg` / `close_input.svg` / `Close_HalfScreen.svg` | 24px | 关闭按钮（通用/输入框/半屏浮层） |
| `Checkbox.svg` / `Checkbox_filled.svg` | 24px | 复选框（未选/已选） |
| `tick.svg` | 24px | 勾选标记 |
| `expand_list.svg` | 24px | 列表展开/下拉菜单 |
| `search.svg` | 24px | 搜索图标 |
| `more_upright.svg` | 24px | 更多操作 |
| `network.svg` / `wifi.svg` / `battery.svg` | - | 系统状态栏图标（信号/WiFi/电池） |
| `heart.svg` / `like.svg` / `star.svg` / `doc.svg` / `secondary.svg` / `remind_mute.svg` | 24px | 功能性图标（收藏/点赞/文档/辅助等） |

### 文件读取顺序

1. **`README.md`**（本文件）— 了解整体结构、全局约束和检查流程
2. **`json/index.json`** — Token 体系、组件索引、组合规则、背景色约束
3. **`css/tokens.css`** — 非颜色 Token（设备 / 字体 / 间距 / 圆角 / 阴影 / 动效）
4. **`css/QQ_color_tokens.css`** — 颜色 Token（QQ 品牌色系，qq-light / qq-dark）
5. **`icons/QUI_24_icons/`** — QUI 图标库（按需浏览）
6. **`md/<COMPONENT>_SPEC.md`** — 使用哪个组件就读哪个文档，**约束规则在这里**
7. **`json/components/<component>.json`** — 组件结构化数据（尺寸/间距/层级等）

---

## 三、母组件列表（20个）

按 **导航 → 数据 → 操作 → 模态** 四大类排序：

| 大类 | ID | 名称 | 变体数 | 规范文档 | JSON 数据 |
|------|----|------|--------|----------|-----------|
| 导航 | `navbar` | 导航栏 NavBar | 97 | `NAVBAR_COMPONENT_SPEC.md` | `navbar.json` |
| 导航 | `hs_navbar` | 半屏导航栏 HalfScreen NavBar | 7 | `HS_NAVBAR_COMPONENT_SPEC.md` | `hs-navbar.json` |
| 数据 | `list` | 通栏式列表 Plain List | 67 | `LIST_COMPONENT_SPEC.md` | `plain-list.json` |
| 数据 | `form` | 卡片式列表 Grouped List | 33 | `GROUPED_LIST_COMPONENT_SPEC.md` | `grouped-list.json` |
| 数据 | `card` | 卡片 Card | 10 | `CARD_COMPONENT_SPEC.md` | `card.json` |
| 数据 | `message` | 消息 Message | 4×2 | `MESSAGE_COMPONENT_SPEC.md` | `message.json` |
| 数据 | `text_block` | 文本块 TextBlock | 13 | `TEXT_BLOCK_COMPONENT_SPEC.md` | `text-block.json` |
| 数据 | `image_block` | 图片块 ImageBlock | 10 | `IMAGE_BLOCK_COMPONENT_SPEC.md` | `image-block.json` |
| 数据 | `data_filter` | 数据筛选 DataFilter | 16 | `DATA_FILTER_COMPONENT_SPEC.md` | `data-filter.json` |
| 数据 | `grid` | 宫格 Grid | 17 | `GRID_COMPONENT_SPEC.md` | `grid.json` |
| 数据 | `divider_spacing` | 分隔与间距 Divider & Spacing | 7 | `DIVIDER_SPACING_COMPONENT_SPEC.md` | `divider-spacing.json` |
| 操作 | `button` | 按钮 Button | 12 | `BUTTON_COMPONENT_SPEC.md` | `button.json` |
| 操作 | `action` | 操作组合 ActionCombo | 13 | `ACTION_COMPONENT_SPEC.md` | `action-combo.json` |
| 操作 | `menu` | 菜单 Menu | 15 | `MENU_COMPONENT_SPEC.md` | `menu.json` |
| 操作 | `search` | 搜索框 Search | 6 | `SEARCH_COMPONENT_SPEC.md` | `search.json` |
| 操作 | `textfield` | 输入框 Textfield | 20 | `TEXTFIELD_COMPONENT_SPEC.md` | `textfield.json` |
| 操作 | `aio_input` | AIO 输入框 AIOInput | 3 | `AIO_INPUT_COMPONENT_SPEC.md` | `ai-input.json` |
| 模态 | `action_sheet` | 操作面板 ActionSheet | 22 | `ACTION_SHEET_COMPONENT_SPEC.md` | `action-sheet.json` |
| 模态 | `dialog` | 对话框 Dialog | 15 | `DIALOG_COMPONENT_SPEC.md` | `dialog.json` |
| 模态 | `half_screen_overlay` | 半屏浮层 HalfScreenOverlay | 2 | `HALF_SCREEN_OVERLAY_COMPONENT_SPEC.md` | `half-screen-overlay.json` |

> **变体数说明**：
> - **NavBar**（97）和 **Plain List**（67）：采用维度矩阵 × 约束排除方式定义变体，需查阅 MD 文档中的约束规则计算有效组合
> - **Grouped List**（33）= 27 个基础变体（L×R 矩阵）+ 6 个组合变体（Combo1-6）
> - **Card**（10）= C1-C10，其中 C10 为 Markdown 内容卡片（高度自适应）
> - **Message**（4×2）= 4 类内容（A通用文本/B图文长描述/C图文短标题/D图标消息）× 2 态（主态/客态）= 8 种子组件，分段选择器默认显示客态
> - **Textfield**（20）= 4 种类型（单行无标题/单行有标题/电话号码/多行文本）× 5 种状态（默认/激活/输入/完成/错误）
> - **AIOInput**（3）= I1默认态 / I2生成中态 / I3输入态，通过分段选择器切换

---

## 四、JSON 与 MD 文档分工指南

每个组件同时拥有 JSON 数据文件和 MD 规范文档，两者功能互补：

| 维度 | JSON（`json/components/`） | MD（`md/`） |
|------|---------------------------|-------------|
| **定位** | 机器可读的结构化数据 | 人/AI 可读的完整规范 |
| **内容** | 尺寸、间距、颜色Token、变体列表、区块定义 | 设计规范、约束规则、排列矩阵、使用场景、禁止组合 |
| **权威性** | 尺寸数值以 JSON 为准 | 变体数量、约束规则、组合合法性以 MD 为准 |
| **典型用途** | 自动生成 UI 代码时读取精确数值 | 理解组件用法、验证组合合法性、检查约束 |

### 快速引用规则

1. **生成 UI 代码**：先读 MD 了解规则 → 再读 JSON 获取精确数值
2. **查变体数量**：以 MD 文档中的"子组件矩阵"表格为准，JSON `totalVariants` 为辅助校验
3. **查约束规则**：仅在 MD 文档中定义（JSON 的 `constraints` 数组为摘要，非完整版）
4. **查尺寸/间距**：JSON `blocks` 对象中的数值为精确参考

---

## 五、组件间关系与联动

部分组件之间存在触发、嵌套或互斥关系，在页面设计中需注意：

### 5.1 触发关系

| 触发源 | 触发目标 | 说明 |
|--------|----------|------|
| DataFilter 下拉筛选按钮（C1） | Menu（无图标类） | 点击下拉筛选按钮后弹出菜单，菜单内容为筛选选项 |
| Grouped List R2（箭头跳转行） | Menu-C（勾选类菜单） | 列表行右侧箭头可触发弹出菜单选择 |
| NavBar 右侧操作按钮 | Menu / ActionSheet | 导航栏右侧"更多"按钮可触发菜单或操作面板 |
| Button（主要/次要按钮） | Dialog / ActionSheet | 按钮点击可触发确认对话框或操作面板 |

### 5.2 嵌套关系

| 外层组件 | 可嵌套的内层组件 | 说明 |
|----------|-----------------|------|
| HalfScreenOverlay（半屏浮层） | Grouped List / Button / Textfield | 半屏浮层内部可放置列表、按钮、输入框等 |
| Card（卡片） | Grid / Button / TextBlock（C10限定） | 卡片内可包含九宫格、按钮、Markdown文本块 |

### 5.3 互斥关系

| 规则 | 说明 |
|------|------|
| 模态组件不可嵌套 | ActionSheet、Dialog、HalfScreenOverlay 三者之间不可互相嵌套 |
| 背景色互斥 | Card/Grouped List 要求灰底（#F0F0F2），不可与白底组件同页使用白底 |
| AIOInput 固定底部 | AIOInput 固定在页面底部，不可嵌入其他组件内部 |

---

## 六、⚠️ 页面背景色约束

页面背景色根据包含的组件类型**强制确定**，不可随意选择：

| 背景色 | Token | 色值 | 触发条件 |
|--------|-------|------|----------|
| 浅灰色 | `bg_bottom_standard` | `#F0F0F2` | 页面包含**卡片式列表（Grouped List）**或**卡片（Card）**时必须使用 |
| 白色 | `bg_bottom_light` | `#FFFFFF` | 默认背景色，仅当页面不包含卡片式列表和卡片组件时使用 |
| 品牌蓝 | `bg_bottom_brand` | `#EFF4FF` | 品牌定制页面，按业务需要使用 |

> **优先级规则**：当页面同时包含需要灰色背景和白色背景的组件时，以灰色背景（`#F0F0F2`）为准。

---

## 七、⚠️ 生成前强制检查清单

在输出任何 UI 组件 HTML 之前，**必须按以下步骤逐项验证**：

### 步骤 1：读取组件规范
- 确认要使用的组件，读取其 `md/<COMPONENT>_SPEC.md`
- 重点阅读文档中的 **"属性约束"** 章节

### 步骤 2：检查组合合法性
- 通栏式列表 → 检查 `LIST_COMPONENT_SPEC.md` §3 属性约束（L×C×R 组合过滤）
- 卡片式列表 → 检查 `GROUPED_LIST_COMPONENT_SPEC.md` §3 属性约束（L×R 组合 + 嵌套规则）
- 导航栏 → 检查 `NAVBAR_COMPONENT_SPEC.md` §3 属性约束（L×C×R 强绑定）
- 模态组件 → 检查各自 SPEC 中的控件联动规则

### 步骤 3：检查颜色 Token
- `css/tokens.css` 仅包含非颜色 Token（设备/字体/间距/圆角/阴影/动效）
- 颜色 Token 定义在 `css/QQ_color_tokens.css` 中，通过 `data-theme` 属性切换主题
- 在 `<html>` 上设置 `data-theme="qq-light"`（默认浅色模式）或 `data-theme="qq-dark"`（深色模式）
- 所有颜色值必须使用 Token 定义的值，禁止自行编造色值
- 页面背景色须遵守上方"第六章 页面背景色约束"规则

### 步骤 4：检查通用规则
- 同一通栏式列表内所有行的 L/C/R 组合必须一致
- 模态组件（ActionSheet / Dialog / HalfScreenOverlay）之间不可嵌套
- 分割线不在列表最后一行底部显示
- 间距值必须为 4px 的整数倍，共 6 档（4/8/12/16/24/32px），组件间间距选择规则详见 `DIVIDER_SPACING_COMPONENT_SPEC.md`

### 步骤 5：图标替换
- 组件 JSON / MD 中出现的 `empty_icon.svg` 是**占位图标**，在实际设计任务中**必须替换**为图标库中的真实图标
- 图标库位于 `icons/QUI_24_icons/`，共 436 枚 24px SVG 图标
- 引用路径格式：`icons/QUI_24_icons/<图标名>.svg`

### 步骤 6：输出审查与完善建议
- 完成设计任务后，审视最终方案，以清单形式附在回复末尾，涵盖以下维度：
  - **缺失组件**：当前 20 个母组件无法覆盖的设计需求（如需要但不存在的组件类型）
  - **缺失变体**：现有组件的变体不足以满足场景（如缺少某种尺寸、状态或布局）
  - **不合理之处**：组件规范与实际设计需求之间的冲突或不适配
  - **主流设计系统对比**：将当前方案与国际主流设计系统（Apple HIG、Material Design 3、Samsung One UI 等）进行对比，从交互模式、视觉美学、动效规范、无障碍等方面指出差异，并给出可借鉴的完善建议
- 无问题的维度注明"无缺失"或"符合主流规范"

---

## 八、系统状态栏 StatusBar

iOS 系统状态栏是每个页面最顶部的固定元素，**每次设计任务必须在界面最顶部放置**，且背景色需与紧随其后的导航栏保持一致。

### 规格

| 属性 | 值 |
|------|------|
| 宽度 | 428px（与设备宽度一致） |
| 高度 | 54px（`--device-status-bar-height`） |
| 背景色 | 与导航栏背景色相同（默认透明，由导航栏决定） |
| 时间字体 | SF Pro / -apple-system / sans-serif，17px，font-weight: 600 |
| 图标 | `icons/network.svg` + `icons/wifi.svg` + `icons/battery.svg` |

### HTML 代码片段（可直接复制使用）

```html
<!-- 系统状态栏 StatusBar — 428×54px -->
<div class="status-bar" style="width:428px; height:54px; position:relative; background:transparent;">
  <div style="width:428px; height:22px; left:0; top:21px; position:absolute;">
    <!-- 左：时间 -->
    <div style="width:152px; height:22px; left:0; top:0; position:absolute;">
      <div style="left:62.5px; top:0; position:absolute; text-align:center;">
        <span style="color:black; font-size:17px; font-family:'SF Pro',-apple-system,sans-serif; font-weight:600;">9:41</span>
      </div>
    </div>
    <!-- 中：灵动岛占位 -->
    <div style="width:124px; height:10px; left:152px; top:6px; position:absolute;"></div>
    <!-- 右：信号 + WiFi + 电池 -->
    <div style="width:152px; height:13px; left:276px; top:4.5px; position:absolute;">
      <div style="left:32.17px; top:0.39px; position:absolute;">
        <img src="icons/network.svg" style="display:block;">
      </div>
      <div style="left:58.37px; top:0.34px; position:absolute;">
        <img src="icons/wifi.svg" style="display:block;">
      </div>
      <div style="left:82.51px; top:0; position:absolute;">
        <img src="icons/battery.svg" style="display:block;">
      </div>
    </div>
  </div>
</div>
```

### 使用规则

1. **必须放置在页面最顶部**，紧接着放导航栏（NavBar）
2. **背景色跟随导航栏**：将 `background:transparent` 改为与导航栏相同的背景色值（如 `var(--color-bg-item)` 即 `#FFFFFF`）
3. 状态栏为**纯展示元素**，不可交互，不参与母组件列表计数
4. 时间固定显示 `9:41`，信号/WiFi/电池图标均为满格状态，不可修改

---

## 十、高级组件列表（QUI+ Pro 系列）

> **⚠️ 默认行为约束**：除非用户明确要求使用高级组件（如指定"Pro版"、"高级导航栏"、"QUI+"等关键词），AI 模型在设计任务中**默认只使用第三章中的 20 个 QUI 基础组件**。Pro 系列组件仅在以下情况使用：
> 1. 用户明确指定使用 Pro / 高级 / QUI+ 组件
> 2. 用户明确要求"沉浸式"、"iOS 26 风格"、"液态玻璃"等与 Pro 设计语言相关的描述
> 3. 用户要求使用底部导航栏（TabBar）时，可主动推荐 PRO_tabbar（因基础组件中无 TabBar）
>
> **禁止行为**：不得在用户未提及 Pro 组件时自行替换基础组件为 Pro 版本。

高级组件是对默认组件的**升级替换版本**，提供更现代化、更精致的设计语言（iOS 26 液态玻璃效果）。高级组件与默认组件**不耦合**，可根据设计需求选择性替换。

> **⚠️ 混用规则**：同一页面中，同一功能位置（如顶部导航）只能使用默认组件或高级组件中的一种，不可混用。

按 **导航 → 数据 → 操作 → 模态** 四大类排序：

| 大类 | ID | 名称 | 变体数 | 规范文档 | JSON 数据 | 可替代的默认组件 |
|------|----|------|--------|----------|-----------|-----------------|
| 导航 | `PRO_navbar` | 顶部导航栏Pro NavBarPro | 13 | `PRO_NAVBAR_COMPONENT_SPEC.md` | `PRO-navbar.json` | 导航栏 NavBar |
| 导航 | `PRO_tabbar` | 底部导航栏Pro TabBarPro | 9 | `PRO_TABBAR_COMPONENT_SPEC.md` | `PRO-tabbar.json` | 无（新增） |

> **变体数说明**：
> - **NavBarPro**（13）= A.小导航（7种，60px高度）+ B.大导航（6种，72px高度），采用圆形图标按钮+透明背景的沉浸式设计语言
> - **TabBarPro**（9）= A.FAB模式（5种，100px高度，带圆形浮动按钮）+ B.纯Tab模式（4种，92px高度），采用胶囊容器+圆角选中态设计

### 高级组件设计特征

| 特征 | 默认组件 | 高级组件 |
|------|----------|----------|
| 命名前缀 | 无 | `PRO_` |
| MD 文件前缀 | 无 | `PRO_` |
| JSON 文件前缀 | 无 | `PRO-` |
| 子组件编号前缀 | 按组件各自规则 | `P`（如 P1-P13） |
| 设计语言 | 标准 QUI 规范 | 更现代化、沉浸式 |

---

## 十一、版本日志

| 版本 | 日期 | 变更 |
|------|------|------|
