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
| 导航 | `navbar` | 导航栏 NavBar | 8 | `NAVBAR_COMPONENT_SPEC.md` | `navbar.json` |
| 导航 | `hs_navbar` | 半屏导航栏 HalfScreen NavBar | 7 | `HS_NAVBAR_COMPONENT_SPEC.md` | `hs-navbar.json` |
| 数据 | `list` | 通栏式列表 Plain List | 42 | `LIST_COMPONENT_SPEC.md` | `plain-list.json` |
| 数据 | `form` | 卡片式列表 Grouped List | 18 | `GROUPED_LIST_COMPONENT_SPEC.md` | `grouped-list.json` |
| 数据 | `card` | 卡片 Card | 9 | `CARD_COMPONENT_SPEC.md` | `card.json` |
| 数据 | `message` | 消息 Message | 4×2 | `MESSAGE_COMPONENT_SPEC.md` | `message.json` |
| 数据 | `text_block` | 文本块 TextBlock | 10 | `TEXT_BLOCK_COMPONENT_SPEC.md` | `text-block.json` |
| 数据 | `image_block` | 图片块 ImageBlock | 5 | `IMAGE_BLOCK_COMPONENT_SPEC.md` | `image-block.json` |
| 数据 | `data_filter` | 数据筛选 DataFilter | 16 | `DATA_FILTER_COMPONENT_SPEC.md` | `data-filter.json` |
| 数据 | `grid` | 宫格 Grid | 6 | `GRID_COMPONENT_SPEC.md` | `grid.json` |
| 数据 | `divider_spacing` | 分隔与间距 Divider & Spacing | 6 | `DIVIDER_SPACING_COMPONENT_SPEC.md` | `divider-spacing.json` |
| 操作 | `button` | 按钮 Button | 12 | `BUTTON_COMPONENT_SPEC.md` | `button.json` |
| 操作 | `action` | 操作组合 ActionCombo | 6 | `ACTION_COMPONENT_SPEC.md` | `action-combo.json` |
| 操作 | `menu` | 菜单 Menu | 15 | `MENU_COMPONENT_SPEC.md` | `menu.json` |
| 操作 | `search` | 搜索框 Search | 6 | `SEARCH_COMPONENT_SPEC.md` | `search.json` |
| 操作 | `textfield` | 输入框 Textfield | 8 | `TEXTFIELD_COMPONENT_SPEC.md` | `textfield.json` |
| 操作 | `aio_input` | AIO 输入框 AIOInput | 3 | `AIO_INPUT_COMPONENT_SPEC.md` | `ai-input.json` |
| 模态 | `action_sheet` | 操作面板 ActionSheet | 22 | `ACTION_SHEET_COMPONENT_SPEC.md` | `action-sheet.json` |
| 模态 | `dialog` | 对话框 Dialog | 15 | `DIALOG_COMPONENT_SPEC.md` | `dialog.json` |
| 模态 | `half_screen_overlay` | 半屏浮层 HalfScreenOverlay | 2 | `HALF_SCREEN_OVERLAY_COMPONENT_SPEC.md` | `half-screen-overlay.json` |

> **变体数说明**：Message 组件为 4 类内容（A通用文本/B图文长描述/C图文短标题/D图标消息）× 2 态（主态/客态）= 8 种子组件，分段选择器默认显示 4 个变体（客态），可切换为主态。

---

## 四、⚠️ 页面背景色约束

页面背景色根据包含的组件类型**强制确定**，不可随意选择：

| 背景色 | Token | 色值 | 触发条件 |
|--------|-------|------|----------|
| 浅灰色 | `bg_bottom_standard` | `#F0F0F2` | 页面包含**卡片式列表（Grouped List）**或**卡片（Card）**时必须使用 |
| 白色 | `bg_bottom_light` | `#FFFFFF` | 默认背景色，仅当页面不包含卡片式列表和卡片组件时使用 |
| 品牌蓝 | `bg_bottom_brand` | `#EFF4FF` | 品牌定制页面，按业务需要使用 |

> **优先级规则**：当页面同时包含需要灰色背景和白色背景的组件时，以灰色背景（`#F0F0F2`）为准。

---

## 五、⚠️ 生成前强制检查清单

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
- 颜色 Token 独立于 `css/tokens.css`，存放在 `css/QQ_color_tokens.css` 中
- 在 `<html>` 上设置 `data-theme="qq-light"`（浅色模式）或 `data-theme="qq-dark"`（深色模式）
- 所有颜色值必须使用 Token 定义的值，禁止自行编造色值
- 页面背景色须遵守上方"第四章 页面背景色约束"规则

### 步骤 4：检查通用规则
- 同一通栏式列表内所有行的 L/C/R 组合必须一致
- 模态组件（ActionSheet / Dialog / HalfScreenOverlay）之间不可嵌套
- 分割线不在列表最后一行底部显示
- 间距值必须为 4px 的整数倍

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

## 六、系统状态栏 StatusBar

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

## 七、版本日志

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.3 | 2026-03-25 | README 优化：新增设备基准章节、变体数量速查、页面背景色约束规则、结构图标清单、工具文件说明；修复 spec 文档路径引用；删除旧组件 AI_INPUT，替换为 AIO_INPUT（`aio_input`） |
| v1.3 | 2026-03-25 | Message 组件左右间距修复：从居中 32px 改为客态靠左 12px、主态靠右 12px，与 Figma 设计稿对齐 |
| v1.3 | 2026-03-24 | 精简资源包：移除额外颜色主题文件（iOS / Material），仅保留 QQ 颜色 Token；移除额外图标库（Core / Feather / Flex / Material3），仅保留 QUI_24_icons，图标库路径调整为 icons/QUI_24_icons/ |
| v1.2 | 2026-03-23 | 图标库补充切换机制说明：默认使用 QUI，支持通过形状和表意映射在 5 套图标库间切换，与颜色 Token 切换独立 |
| v1.2 | 2026-03-23 | 颜色 Token 从 tokens.css 拆分至三套独立主题文件（QQ / iOS / Material），支持 data-theme 切换；tokens.css 仅保留设备/字体/间距/圆角/阴影/动效 Token |
| v1.1 | 2026-03-23 | 新增系统状态栏 StatusBar 章节（100% UI 还原 HTML 片段 + 使用规则） |
| v1.1 | 2026-03-23 | Flex 图标库重命名为 Flex_48_icons，与 Flex_24_icons 合并说明；补充同套混用规则及 48px→24px 缩放要求 |
| v1.1 | 2026-03-20 | 新增 Icons_Library 多风格图标库说明及图标替换规则（步骤 5） |
| v1.1 | 2026-03-19 | 创建 README.md 入口指南；新增页面背景色约束；补充各组件 MD 文档约束规则 |
| v1.0 | 2026-03-18 | 初始版本 |
