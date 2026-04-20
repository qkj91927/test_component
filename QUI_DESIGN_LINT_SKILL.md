# QUI Design Lint

> 设计任务完成后的合规自检。适用于任何 AI 平台，无外部依赖。
> 基于 QUI Basic 1.0（21 个母组件，428px iPhone 基准）。

## 使用方法

将生成的代码 + 本文件一起发给 AI：
> 请按 QUI Design Lint 逐项检查我的代码，输出报告。

---

## 检查哲学：两级违规制

所有检查项采用**两级违规**判定，严格程度递增：

| 级别 | 含义 | 示例 | 输出标记 |
|------|------|------|---------|
| **⚠️ WARN** | 值碰巧正确，但没有通过 Token/变量引用 | `border-radius: 12px` 值正确但应写 `var(--radius-m)` | ⚠️ 值正确但未绑定 Token |
| **⛔ ERROR** | 值本身就不在合法范围内 | `font-size: 15px` 不在 11 档合法字号中 | ⛔ 值非法 |

> **核心原则**（借鉴 figma-design-audit）：**即使值碰巧正确，只要没有通过 Token 变量引用，就视为违规。**
> 因为当 Token 值更新时，硬编码无法自动同步，会导致系统性不一致。

---

## 第一步：组件合法性验证（最重要）

**逐个检查代码中使用的每个 UI 元素，必须能在下方「组件注册表」中找到匹配。**

### 视觉参照

所有组件变体的**权威视觉样式**以 `component-matrix.html` 为准。
检查时应将生成的代码与 matrix 中对应变体的 UI 表现逐一比对：
- 尺寸（宽/高/间距）是否一致
- 颜色（前景/背景/描边）是否一致
- 字体（字号/字重/行高）是否一致
- 圆角是否一致
- 图标/占位图是否使用了 `icons/` 中的标准资源

### FORBIDDEN 模式：禁止行为 ⛔

以下行为**绝对禁止**，发现即判 ERROR：

| 代号 | 禁止行为 | 典型 AI 犯错示例 |
|------|---------|-----------------|
| F1 | **发明组件**：使用注册表中不存在的组件 | `<TabBar>`, `<Drawer>`, `<FloatingButton>`, `<Carousel>`, `<Stepper>` |
| F2 | **魔改结构**：修改组件的维度/区域/插槽 | 给 NavBar 添加第四个区域、给 List 行添加第三行描述 |
| F3 | **跨组件嫁接**：将 A 组件的子元素放到 B 组件中 | 把 Card 的九宫格放进 List 行 |
| F4 | **自创变体**：使用不在变体矩阵中的排列组合 | NavBar L6+C5（约束中已过滤） |
| F5 | **修改固定值**：更改组件的固定尺寸 | NavBar 高度改为 48px、ActionSheet 行高改为 60px |
| F6 | **硬编码颜色**：使用 `#xxx`/`rgb()` 代替 Token | `color: #333333` 代替 `var(--text-primary)` |
| F7 | **非法字号**：使用 11 档之外的 font-size | `font-size: 15px`、`font-size: 13px` |
| F8 | **非法间距**：使用非 4 倍数的间距值 | `padding: 10px`、`margin: 15px` |
| F9 | **缺少 StatusBar**：页面顶部没有 428×54px 状态栏 | 页面直接从 NavBar 开始 |
| F10 | **模态嵌套**：Dialog/ActionSheet/HalfScreenOverlay 互相嵌套 | Dialog 中弹出 ActionSheet |

### FORBIDDEN 模式：常见 AI 错误写法 ❌ vs 正确写法 ✅

```
❌ .card-title { color: #333333; font-size: 15px; border-radius: 14px; }
✅ .card-title { color: var(--text-primary); font-size: 17px; border-radius: var(--radius-m); }

❌ .btn { background: #0099FF; padding: 10px 15px; }
✅ .btn { background: var(--brand-standard); padding: var(--spacing-m) var(--spacing-l); }

❌ <div class="tab-bar">...</div>                 ← 组件库不存在 TabBar
✅ <div class="navbar L1_C5_R0">...</div>          ← 使用 NavBar C5 分段选择

❌ .bubble { border-radius: 10px; }               ← 值正确但没用 Token
⚠️ → ✅ .bubble { border-radius: var(--radius-m); } ← 10px→12px 已在之前修正，现在是 12px
```

### ALLOWED 模式：合法用法速查

| 类别 | ALLOWED（仅以下值/方式合法） |
|------|---------------------------|
| **组件** | 仅注册表中 21 个母组件的 492 种变体 |
| **颜色** | 仅 `var(--token)` 形式引用 39 个颜色 Token |
| **字号** | 仅 10·12·14·16·17·18·20·22·26·28·34 px（11 档） |
| **间距** | 仅 4 的整数倍：4·8·12·16·24·32 px → `var(--spacing-*)` |
| **圆角** | 仅 4·8·12·16·20·24·1000 px → `var(--radius-*)` |
| **背景色** | Card/Grouped List 页 → `#F0F0F2`；Message 页 → `#F0F0F2`(aio)；其余 → `#FFFFFF` |
| **图标** | 仅 `icons/` 目录中的 SVG 文件 |
| **设备宽度** | 全宽元素 = 428px |

### 验证流程

对代码中**每个 UI 元素**执行：

```
1. 识别 → 在注册表中找母组件
   ├─ 找到 → 继续步骤 2
   └─ 找不到 → ⛔ 非法组件 → 执行「替代方案」

2. 匹配变体 → 确认子组件 ID 在变体空间中
   ├─ 存在 → 继续步骤 3
   └─ 不存在 → ⛔ 非法变体 → 给出最近合法变体建议

3. 比对 UI → 与 component-matrix.html 中对应变体视觉比对
   ├─ 一致 → ✅ 通过
   └─ 不一致 → ⛔ UI 不规范 → 列出差异并给出修正
```

### ⛔ 非法组件的替代方案（必须执行）

发现非法组件时，**不能简单删除**，必须分析其产品意图并用合法组件替代：

| 常见非法组件 | 产品意图 | 推荐替代方案 |
|------------|---------|------------|
| 底部 TabBar | 多页面切换 | NavBar C5 分段选择 + 页面级切换 |
| 抽屉菜单/侧边栏 | 导航入口集合 | HalfScreenOverlay HSO-A + 内嵌 Grouped List |
| 浮动操作按钮 (FAB) | 主操作入口 | ActionCombo A1(单主按钮) 固定在页面底部 |
| 轮播 Banner | 图片循环展示 | ImageBlock A2(通栏轮播) 或 B2(嵌入轮播) |
| 底部弹出选择器 | 单选/多选 | ActionSheet 或 HalfScreenOverlay + Grouped List(勾选) |
| 进度条/步骤条 | 流程进度 | TextBlock H6(摘要文本) 描述当前步骤 + 多页面 NavBar 导航 |
| 徽标/红点通知 | 未读提示 | NavBar L2(返回+气泡) 的 Badge 数字组件 |
| 评分/星级 | 评价打分 | 不支持，需向设计师申请新增组件 |
| 下拉刷新 | 内容更新 | 交互行为，不属于静态组件范畴，代码中处理但不体现为 UI 组件 |
| 自定义卡片 | 信息聚合 | Card C1-C10 中选择最接近的变体 |

**替代原则**：
1. 先分析非法组件要解决的**用户需求**
2. 在 21 个母组件中找到能满足同一需求的组件
3. 如果确实无法替代，在报告中标注 `🔶 需求缺口` 并建议向设计师反馈

---

## 组件注册表（21 个母组件，492 种变体）

> 📖 视觉参照：`component-matrix.html`（可在浏览器打开查看所有变体的精确 UI）

### 导航（2 个）

| ID | 名称 | 变体数 | 结构 | 变体空间 |
|----|------|--------|------|---------|
| `navbar` | 导航栏 NavBar | 97 | 左(L)×中(C)×右(R) 三段式，高 44px | L1-L6 × C0-C5 × R0-R6，经约束过滤。约束：L2 只配 C1/C4+R1；L5 只配 R3；L6 只配 C0+R1/R2；C5 只配 L1/L3+R0/R1 |
| `hs_navbar` | 半屏导航栏 | 7 | 一级(A)/二级(B) | A1-A4 + B1-B3 |

### 数据（9 个）

| ID | 名称 | 变体数 | 结构 | 变体空间 |
|----|------|--------|------|---------|
| `list` | 通栏式列表 | 110 | 左(L)×内容(C)×右(R)，通栏 428px | L0-L7 × C1-C3 × R0-R9，67 默认态+43 多选态。约束：L0 禁 C3 且 R 限 R1/R4/R5/R6；R2 限 L1+C1；R3 限 C1；R7/R8 限 L4；R9 限 L5+C2 |
| `form` | 卡片式列表 | 52 | 左(L)×右(R)，圆角容器 396px | L1-L11 × R0-R5，46 基础+6 Combo。约束：L5/L6 限 R1/R2/R4；L7 限 R0/R5；L8-L11 限 R0-R3 |
| `text_block` | 文本块 | 13 | 纯文本排版 | H1-H7(居左) + C1-C6(居中) |
| `image_block` | 图片块 | 10 | 图片展示 | A1-A5(通栏) + B1-B5(嵌入) |
| `data_filter` | 数据筛选 | 16 | 五类子组件 | A1-A4(页签) + B1-B4(分段选择) + C1(下拉筛选) + D1-D5(标签) + E1-E2(面包屑) |
| `grid` | 宫格 | 17 | 网格排列 | A1-A9(平铺) + B1-B8(横滑) |
| `divider_spacing` | 分隔与间距 | 7 | 分割/留白 | A1(分割线) + spacing-xs/s/m/l/xl/xxl(间距) |
| `card` | 卡片 | 10 | 区块自由组合，容器 396px | C1-C10，每种由头像行/图片区/标题区/辅助行等固定区块组合 |
| `message` | 消息 | 8 | 内容×角色 | A-D(文本/图文长/图文短/图标) × 主态/客态 |

### 操作（8 个）

| ID | 名称 | 变体数 | 结构 | 变体空间 |
|----|------|--------|------|---------|
| `button` | 按钮 | 12 | 尺寸×类型 | S1-S4(大/中/小/mini) × T1-T3(一级/二级/警示) |
| `action` | 操作组合 | 15 | 按钮型+文字链型 | A1-A8(按钮型) + B1-B7(辅助操作行) |
| `menu` | 菜单 | 15 | 类型×选项数 | I/NI/C(有图标/无图标/有勾选) × 2-6 项，编码 `{类型}-{数量}` |
| `search` | 搜索框 | 6 | 层级×状态 | A1-A3(一级) + B1-B3(二级) |
| `textfield` | 输入框 | 50 | 类型×状态 | A-D 基础(×5 态=20) + E1-E6 复合(×5 态=30) |
| `aio_input` | AIO 输入框 | 3 | 交互状态 | I1(默认) / I2(生成中) / I3(输入) |
| `toast` | 轻提示 | 5 | 功能类型 | T1(加载中) / T2(成功) / T3(失败) / T4(中性文字) / T5(带操作) |

### 模态（3 个）

| ID | 名称 | 变体数 | 结构 | 变体空间 |
|----|------|--------|------|---------|
| `action_sheet` | 操作面板 | 22 | 操作数×提示×警示 | `AS-{0-10}{T?}{D?}`，常规+警示≥1 |
| `dialog` | 对话框 | 15 | 标题×正文×操作 | `{T|NT}-{P|C|I}-{S|D|T}`，输入框类(I)必须有标题(T) |
| `half_screen_overlay` | 半屏浮层 | 2 | 容器类型 | HSO-A(标准型) / HSO-B(把手型) |

---

## 第二步：Token 与样式检查（两级违规）

### Token 合法值速查

**间距** `--spacing-`: xs=4 s=8 m=12 l=16 xl=24 xxl=32 (px)
**圆角** `--radius-`: xs=4 s=8 m=12 l=16 xl=20 xxl=24 full=1000 (px)
**字号** (px): 10 · 12 · 14 · 16 · 17 · 18 · 20 · 22 · 26 · 28 · 34

**颜色（39 个 Token）**:
品牌: `brand-standard` `brand-light` · 语义: `accent-green` `accent-orange` `accent-red`
文本: `text-primary` `-secondary` `-tertiary` `-quaternary` `-white` `-allwhite-secondary` `-allwhite-tertiary` `-link` `-link-dark`
图标: `icon-primary` `-secondary` `-tertiary` `-white` `-blue`
背景: `bg-bottom` `bg-secondary` `bg-top` `bg-bottom-brand` `bg-select` `fill-gray-primary`
填充: `fill-tertiary` `-secondary` `-primary` `-quaternary` `-destructive-strong` `-destructive-weak`
交互: `feedback-press` `feedback-hover` · 遮罩: `overlay-modal` `overlay-toast`
描边: `border-default` `border-weak` `border-invert` `border-white`

### 检查规则（两级违规）

| ID | 规则 | 两级判定 |
|----|------|---------|
| TK1 | 颜色必须用 `var(--token)` | ⛔ 硬编码 `#xxx`/`rgb()` 且值不在 39 个 Token 中 → ERROR · ⚠️ 值碰巧匹配某个 Token 但没用 `var()` → WARN |
| TK2 | 间距值必须是 4 的整数倍 | ⛔ 非 4 倍数 → ERROR · ⚠️ 是 4 倍数但没用 `var(--spacing-*)` → WARN |
| TK3 | font-size 只允许 11 档合法值 | ⛔ 值不在 11 档中 → ERROR |
| TK4 | 间距 4/8/12/16/24/32px 应用 Token | ⚠️ 值正确但硬编码 → WARN |
| TK5 | 圆角 4/8/12/16/20/24/1000px 应用 Token | ⚠️ 值正确但硬编码 → WARN |
| TK6 | font-family 必须包含 "PingFang SC" | ⛔ 使用其他字体 → ERROR |

### 正反例对比

```
── 颜色 ──
⛔ ERROR:  color: #FF5733;                     ← 值不在 Token 中
⚠️ WARN:   color: rgba(0, 0, 0, 0.9);          ← 值 = text-primary 但没用 var()
✅ PASS:   color: var(--text-primary);

── 间距 ──
⛔ ERROR:  padding: 10px;                      ← 非 4 倍数
⚠️ WARN:   padding: 16px;                      ← 值正确但没用 var()
✅ PASS:   padding: var(--spacing-l);

── 圆角 ──
⛔ ERROR:  border-radius: 14px;                ← 不在 7 档中
⚠️ WARN:   border-radius: 12px;                ← 值正确但没用 var()
✅ PASS:   border-radius: var(--radius-m);

── 字号 ──
⛔ ERROR:  font-size: 15px;                    ← 不在 11 档中
✅ PASS:   font-size: 17px;                    ← 字号暂不要求 var()，值正确即可
```

---

## 第三步：页面结构与约束检查

| ID | 规则 | 级别 |
|----|------|------|
| S1 | 顶部 StatusBar 428×54px（9:41、满格图标） | ⛔ |
| S2 | StatusBar 下方紧接 NavBar 44px | ⛔ |
| S3 | Home Bar 428×34px 全局唯一 | ⛔ |
| S4 | 全宽元素 width = 428px | ⛔ |
| S5 | 背景色：含 Card/Grouped List → #F0F0F2；含 Message → #F0F0F2(aio)；其余白色 | ⛔ |
| S6 | 相邻组件之间必须有间距或分割线 | ⛔ |
| S7 | 列表最后一行底部不显示分割线 | ⛔ |
| S8 | 模态组件不可嵌套 | ⛔ |
| S9 | 半屏浮层内只可嵌入非模态组件 | ⛔ |
| S10 | Hover: `--feedback-hover` 叠加，禁止改前景色 | ⛔ |
| S11 | Disabled: 仅 `opacity: 0.3` + `pointer-events: none` | ⛔ |
| S12 | 嵌套容器内层圆角 ≤ 外层圆角 | ⛔ |
| S13 | 同一容器内字号层级递减：标题 ≥ 正文 ≥ 描述 ≥ 注释 | ⚠️ |

---

## 第四步：合规评分

检查完成后，计算**合规评分**（满分 100），各维度权重如下：

| 维度 | 权重 | 计算方式 |
|------|------|---------|
| **组件合法性** | **40%** | `(合法组件数 / 总组件数) × 100`。有 1 个非法组件则此项不超过 60 分 |
| **Token 绑定率** | **25%** | `(使用 var() 的属性数 / 应使用 Token 的属性总数) × 100` |
| **值准确率** | **20%** | `(值在合法范围内的属性数 / 总属性数) × 100` |
| **结构合规** | **15%** | `(通过的结构规则数 / 总结构规则数) × 100` |

### 评级标准

| 评级 | 分数 | 含义 | 行动 |
|------|------|------|------|
| 🟢 **A** | 90-100 | 完全合规，可直接交付 | 无需修改 |
| 🟡 **B** | 75-89 | 基本合规，有少量 WARN | 建议修复 WARN 项 |
| 🟠 **C** | 60-74 | 部分合规，有 ERROR 需修复 | 必须修复所有 ERROR |
| 🔴 **D** | <60 | 严重不合规 | 需重新审视设计方案 |

---

## 第五步：Skill Sync（持续优化）

每次 Lint 完成后，AI 应执行以下 Skill 知识同步：

### 1. 错误模式积累

如果本次检查发现了**新的 AI 常见错误模式**（不在 FORBIDDEN 表中），记录下来：

```
📝 新发现的 AI 错误模式：
- 模式：AI 将 HalfScreenOverlay 的把手型(HSO-B)用作底部抽屉
- 产品意图：底部弹出面板
- 正确做法：HSO-B 只是容器把手样式变体，不改变浮层行为
→ 建议补充到 FORBIDDEN 模式 F11
```

### 2. 需求缺口汇总

将所有 `🔶 需求缺口` 汇总为组件库演进建议：

```
📝 组件库演进建议（基于累计 N 次 Lint）：
- 星级评分组件：出现 3 次需求缺口，建议优先新增
- 步骤条/进度条：出现 2 次，当前用 TextBlock 替代但体验不佳
```

### 3. Token 偏差趋势

统计 WARN 最多的 Token 类别，反映团队/AI 的薄弱环节：

```
📝 Token 偏差趋势：
- 颜色硬编码：本次 5 处（最常见 #333333 → text-primary）
- 间距硬编码：本次 3 处（最常见 16px → spacing-l）
- 圆角硬编码：本次 0 处 ✅
```

---

## 输出格式

### 逐项报告（只输出有问题的项，通过的跳过）

```
⛔ F1 非法组件 · 代码中使用了"底部 TabBar"
  产品意图：多页面切换
  替代方案：使用 NavBar C5 分段选择 + 页面级视图切换
  修改建议：将 TabBar 替换为 navbar L1_C5_R0 变体

⛔ TK1 ERROR · .card-title { color: #FF5733; }
  值 #FF5733 不在 39 个颜色 Token 中
  → 确认设计意图后选择合适 Token，如 var(--text-primary)

⚠️ TK1 WARN · .card-desc { color: rgba(0,0,0,0.55); }
  值匹配 --text-secondary 但未使用 var()
  → 改为 var(--text-secondary)

⚠️ TK5 WARN · .msg-bubble { border-radius: 12px; }
  值正确(=radius-m)但未绑定 Token
  → 改为 var(--radius-m)

⛔ UI 不规范 · Card C3 的标题区字号与 matrix 不一致
  差异：代码 font-size: 15px / matrix font-size: 17px
  修复：改为 font-size: 17px（typo-body-l）

🔶 需求缺口 · 产品需要"星级评分"组件，QUI Basic 1.0 无法覆盖
  建议：向设计师反馈，申请新增评分组件
```

### 评分汇总

```
QUI Design Lint Report
═══════════════════════
组件合法性 ·· 90/100  (9/10 合法, 1 非法已提供替代)
Token 绑定 ·· 72/100  (18/25 使用 var(), 7 硬编码)
值准确率 ···· 95/100  (19/20 值正确, 1 非法值)
结构合规 ···· 100/100 (13/13 规则通过)
─────────────────────
总分 ········ 87/100  🟡 B 级 — 基本合规，建议修复 7 处 WARN

├─ ⛔ ERROR: 2 (1 非法组件 + 1 非法值)
├─ ⚠️ WARN:  7 (值正确但未绑定 Token)
├─ 🔶 缺口:  1 (已标注)
└─ Skill Sync: 1 条新错误模式 + 1 条演进建议
```

---

*v4.0 · QUI Basic 1.0 · 21 母组件 492 变体 · 视觉参照 component-matrix.html*
*检查哲学：即使值碰巧正确，未绑定 Token 也是违规*
