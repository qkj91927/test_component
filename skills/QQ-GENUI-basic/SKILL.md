---
name: QQ-GENUI-basic
description: 当用户生成界面（页面/UI/组件）或局部调整界面（增删组件、修改样式、替换图标等）时必须触发。基于 QQ_GenUI 设计系统远程资源产出移动端页面与组件方案；所有资源通过 GitHub 远程按需读取，不下载到本地；强制 Gate 流程逐步验收，不可跳步，最多3轮回归修复，若仍不合规则继续交付并附问题清单。
---

# QQ-GENUI-basic

## 概述

使用本 skill 将 `QQ_GenUI` 设计系统转化为"强约束可执行流程"。
所有设计资源（规范文档、Token、图标）均通过 GitHub **远程按需读取**，不克隆仓库、不下载到用户本地。
执行过程中必须通过 Gate 校验，禁止跳步、禁止并步；若 3 轮回归后仍有剩余问题，允许交付并显式列出未修复项。

## 何时使用

在以下场景必须触发（**无需用户显式指定本 skill，匹配即自动激活**）：

### 生成界面（全量）

- 用户要求"生成页面/界面/UI/组件"——无论是否提及本设计系统
- 用户要求"用组件库拼装页面并输出 HTML"
- 用户提供 Figma 截图/线框图/口头描述，要求产出可运行的移动端页面

### 局部调整界面

- 用户要求对已有界面进行**局部修改**，包括但不限于：
  - 增删组件、调整组件顺序或嵌套关系
  - 修改颜色、间距、圆角、字号等视觉属性
  - 替换图标、更换主题（Light ↔ Dark）
  - 修改文案、状态栏、导航栏等局部元素
  - 修复界面中的样式或布局问题
- 用户要求"微调/优化/美化/对齐"等隐含界面调整的表述

### 合规与校验

- 用户要求"检查组件组合是否合法"或"检查 Token/背景色是否合规"
- 用户要求"替换占位图标 `empty_icon.svg` 为真实图标"

### 触发判定规则

> **核心原则：凡涉及界面生成或界面修改，均必须触发本 skill。**
>
> 即使用户未明确提及"设计系统"或"QQ_GenUI"，只要请求的产出物是 UI 界面（HTML/页面/组件），就必须走本 skill 的 Gate 流程，以确保输出符合设计系统规范。

在以下场景**不**触发：

- 纯后端任务（API、数据库、服务端逻辑等）
- 与界面无关的通用前端问题（打包配置、性能优化、纯 JS 逻辑等）
- 纯文档编写、纯数据处理

## 远程资源访问约定

### Base URL

```
https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/
```

### 文件映射表

| 资源 | 远程路径 |
|------|----------|
| 入口指南 | `README.md` |
| 全局索引 | `json/index.json` |
| 颜色 Token | `css/QQ_color_tokens.css` |
| 通用 Token | `css/tokens.css` |
| 组件规范 | `md/<COMPONENT>_SPEC.md` |
| 组件数据 | `json/components/<component>.json` |
| 图标库目录 | `icons/QUI_24_icons/`（通过 GitHub 页面或 API 获取列表） |
| 单个图标 | `icons/QUI_24_icons/<icon-name>.svg` |
| 结构图标 | `icons/<icon-name>.svg` |

### 远程读取规则

- 使用 `web_fetch` 或等效工具读取 `raw.githubusercontent.com` 上的文件
- **禁止** `git clone`、`git pull` 或任何将仓库文件写入用户本地的操作
- **按需读取**：仅在当前 Gate 需要时才获取对应文件，不要一次性读取全部资源
- 若远程读取失败（网络问题/404），在当前 Gate 输出问题报告并暂停

## 强制执行契约（GATE）

### 总则

- 从 Gate 1 开始顺序执行，必须 `1 → 2 → 3 → ...`。
- 每个 Gate 必须满足通过条件后才能进入下一 Gate。
- 默认不要求在每个 Gate 后输出验证证据。
- 仅当某个 Gate 遇到问题导致无法继续时，输出该 Gate 的问题报告（问题、影响、处理建议）。
- 失败时优先修复并重测，不得跳过当前 Gate 直接前进。

### 失败处理

- Gate 失败 → 停止前进 → 修复当前 Gate 所属问题 → 重新执行当前 Gate。
- 若 Gate 9 在第 3 轮后仍有未修复项，继续进入 Gate 10 完成交付，并附未修复问题清单。

## Gate 流程（不可跳过）

### Gate 1：远程读取入口指南（必做）

- 通过 `web_fetch` 远程读取 `README.md`（完整内容）
- URL：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/README.md`
- 理解设计系统全局结构、设备基准、组件列表、背景色约束、检查清单
- **禁止克隆或下载仓库到本地**

通过条件：

- 已成功远程读取 `README.md` 完整内容
- 已理解 20 个母组件列表、背景色规则、文件读取顺序

### Gate 2：锁定目标与组件候选

- 明确页面类型、信息层级、关键交互
- 从 20 个母组件中选择候选
- 标记是否包含 `Grouped List` 或 `Card`
- 确定需要远程读取哪些组件的 SPEC 文档

通过条件：

- 组件候选列表完整
- 背景色触发条件已明确
- 待读取的 SPEC 文件清单已列出

### Gate 3：远程读取组件硬约束

- 根据 Gate 2 确定的候选组件，远程读取对应 `md/<COMPONENT>_SPEC.md`
  - URL 格式：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/md/<COMPONENT>_SPEC.md`
- 重点阅读"属性约束"章节
- 对 `List / Grouped List / NavBar / 模态` 执行组合合法性检查
- 不合法组合必须替换为合法变体
- 按需远程读取对应 `json/components/<component>.json` 获取结构化数据
  - URL 格式：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/json/components/<component>.json`

通过条件：

- 所有已选组件均完成远程 SPEC 读取
- 组合合法性检查结论完整

### Gate 4：远程读取并应用 Token 与主题

- 远程读取 `css/QQ_color_tokens.css`
  - URL：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/css/QQ_color_tokens.css`
- 远程读取 `css/tokens.css`
  - URL：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/css/tokens.css`
- 在 `<html>` 设置 `data-theme="qq-light"` 或 `data-theme="qq-dark"`
- 颜色仅使用 `QQ_color_tokens.css` 中定义的值
- 非颜色 Token 使用 `tokens.css` 中定义的值
- 间距全部为 4px 整数倍

通过条件：

- 不存在自定义颜色值
- 不存在非 4px 网格间距

### Gate 5：背景色强约束

- 包含 `Grouped List` 或 `Card`：背景强制 `bg_bottom_standard`（`#F0F0F2`）
- 不包含上述组件：默认 `bg_bottom_light`（`#FFFFFF`）
- 品牌页可使用 `bg_bottom_brand`（`#EFF4FF`）
- 冲突时灰底优先

通过条件：

- 背景色选择与触发规则一致

### Gate 6：状态栏与导航一致性

- 顶部必须放置 iOS StatusBar（428×54）
- 时间固定 `9:41`
- 图标远程引用路径：
  - `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/network.svg`
  - `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/wifi.svg`
  - `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/battery.svg`
- 状态栏背景与紧随其后的 NavBar 背景一致

通过条件：

- 状态栏规格完整且与 NavBar 一致

### Gate 7：图标替换与路径校验

- 将所有 `empty_icon.svg` 替换为真实图标
- 必须使用项目图标库 `icons/` 内对应图标（优先 `icons/QUI_24_icons/`），禁止自绘图标
- 禁止使用 emoji 作为图标
- 远程浏览图标目录：`https://github.com/qkj91927/QQ_GenUI/tree/main/icons/QUI_24_icons`
- 图标引用路径格式：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/QUI_24_icons/<icon-name>.svg`
- 若找不到匹配图标，必须输出问题报告（缺失图标需求、影响位置、临时处理建议）

通过条件：

- 占位图标残留数量为 0
- 图标来源均为项目 `icons/` 图标库且无自绘/emoji
- 无匹配图标时已输出问题报告

### Gate 8：初次产出

- 完成页面生成与必要实现
- 完成内部规则检查并记录结果

通过条件：

- 页面生成完成且可进入回归流程

### Gate 9：回归测试与修复闭环（强制）

对"已生成结果"执行回归测试，按以下循环执行，最多 3 轮：

1. 依据已读取的 `README.md` + `md/*_SPEC.md` + `json/components/*.json` 做一致性比对
2. 统计不符合项并分类（组合/Token/背景/状态栏/图标/间距/其它）
3. 修复全部不符合项
4. 重新执行回归测试

停止条件：

- 任一轮回归结果达到 **100% 合规（不符合项 = 0）**，立即结束并进入 Gate 10
- 轮次达到 3 且仍有不符合项，结束回归并进入 Gate 10，交付结果并附未修复问题清单

硬约束：

- 回归测试 + 修复轮次最少 1 次，最多 3 次
- 每轮必须给出：问题数、修复数、剩余数
- 禁止跳过回归测试直接交付
- 第 3 轮后若仍不合规，必须明确列出未修复项与影响范围

### Gate 10：最终交付

Gate 10 在以下两种情况下均可执行：

- Gate 9 已达到 100% 合规
- Gate 9 已执行满 3 轮但仍有剩余问题

最终回复必须包含：

- Gate 执行摘要（Gate1~Gate10 通过情况）
- 回归轮次摘要（轮次与每轮问题数变化）
- 若未达100%：未修复问题清单（问题、影响、建议）
- 审查与完善建议（缺失组件/缺失变体/不合理之处/主流设计系统对比）

## 输出格式约定

按以下结构组织最终回复：

1. Gate 执行状态摘要（逐 Gate：通过/失败）
2. 回归测试记录（最多 3 轮）
3. 未修复问题清单（仅未达100%时）
4. 审查与完善建议（四维度）

## 禁止项

- 禁止克隆、下载或以任何方式将仓库文件写入用户本地
- 禁止跳过任何 Gate
- 禁止 Gate 未通过时进入下一 Gate
- 禁止跳过 `md/*_SPEC.md` 直接拼组件
- 禁止使用未定义颜色值
- 禁止在列表末行显示底部分割线
- 禁止模态组件互相嵌套
- 禁止保留 `empty_icon.svg` 作为最终图标
- 禁止在回归未达 100% 且未输出未修复问题清单时宣称完成

## 参考资料

- `references/component-index.md`：20 个母组件速查与文件映射
- `references/checklist.md`：Gate + 回归执行清单（可直接逐项执行）
