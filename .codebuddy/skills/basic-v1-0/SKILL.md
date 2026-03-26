---
name: basic-v1-0
description: 该 skill 用于基于 basic-v1.0 设计系统资源包产出移动端页面与组件方案；当用户要求按仓库规范生成 UI、校验组件组合合法性、选择 Token 与图标替换时应触发。
---

# basicV1.0

## 概述

使用本 skill 将 `basic-v1.0` 资源包转化为可执行的页面/组件产出流程，确保组件选择、组合约束、Token 使用、图标替换、状态栏与背景色规则全部符合规范。

## 何时使用

在以下场景触发：

- 用户要求“按该仓库规范生成页面/UI/组件”
- 用户要求“用组件库拼装页面并输出 HTML”
- 用户要求“检查组件组合是否合法”或“检查 Token/背景色是否合规”
- 用户要求“替换占位图标 `empty_icon.svg` 为真实图标”

在以下场景不触发：

- 纯后端任务
- 与本仓库设计系统无关的通用前端问题

## 必须先读取的文件顺序

按顺序读取并建立上下文：

1. `README.md`
2. `json/index.json`
3. `css/tokens.css`
4. `css/QQ_color_tokens.css`
5. `icons/QUI_24_icons/`（按需检索）
6. `md/<COMPONENT>_SPEC.md`（使用哪个组件读哪个）
7. `json/components/<component>.json`

## 执行流程（强制）

在开始生成任何界面前，必须先触发本 skill，并严格从步骤 1 开始执行。

### 步骤 1：拉取组件仓库（必做）

- 先拉取组件仓库：`https://github.com/qkj91927/test_component/tree/basic1.0`
- 优先确保本地工作目录基于远程 `basic1.0` 最新内容
- 若本地已存在仓库，先同步再继续后续步骤

### 步骤 2：锁定页面目标与组件候选

- 明确页面类型、信息层级、交互动作
- 从 20 个母组件中选择候选组件
- 记录是否包含 `Grouped List` 或 `Card`（用于背景色判定）

### 步骤 3：逐组件读取硬性约束

- 读取对应 `md/*_SPEC.md` 的“属性约束”
- 对 `List / Grouped List / NavBar / 模态` 优先执行组合合法性检查
- 发现组合不合法时立即替换为合法变体，不输出违规结构

### 步骤 4：应用 Token 与主题

- 在 `<html>` 设置 `data-theme="qq-light"` 或 `data-theme="qq-dark"`
- 颜色仅使用 `css/QQ_color_tokens.css` 中定义值
- 非颜色 Token（间距/圆角/阴影/动效）使用 `css/tokens.css`
- 间距必须为 4px 整数倍

### 步骤 5：执行背景色强约束

- 页面含 `Grouped List` 或 `Card` 时，背景强制 `bg_bottom_standard`（`#F0F0F2`）
- 页面不含上述组件时默认 `bg_bottom_light`（`#FFFFFF`）
- 品牌页可使用 `bg_bottom_brand`（`#EFF4FF`）
- 冲突时灰底优先

### 步骤 6：注入状态栏并对齐导航

- 页面顶部必须放置 iOS StatusBar（428×54）
- 时间固定 `9:41`，图标使用 `icons/network.svg`、`icons/wifi.svg`、`icons/battery.svg`
- 状态栏背景色与紧随其后的 NavBar 背景保持一致

### 步骤 7：图标替换与路径校验

- 将所有 `empty_icon.svg` 替换为真实图标
- 图标从 `icons/QUI_24_icons/` 选择
- 使用路径格式：`icons/QUI_24_icons/<icon-name>.svg`

### 步骤 8：输出与审查结论

在最终回复末尾附“审查与完善建议”清单，覆盖：

- 缺失组件
- 缺失变体
- 不合理之处
- 与 Apple HIG / Material Design 3 / Samsung One UI 的对比建议

无问题项标注“无缺失”或“符合主流规范”。

## 输出格式约定

按以下结构组织输出：

1. 页面结构说明（组件树 + 关键状态）
2. 关键规则校验结果（逐条）
3. HTML/CSS 产出（如用户要求代码）
4. 审查与完善建议（四维度）

## 禁止项

- 禁止跳过 `md/*_SPEC.md` 直接拼组件
- 禁止使用未定义颜色值
- 禁止在列表末行显示底部分割线
- 禁止模态组件互相嵌套
- 禁止保留 `empty_icon.svg` 作为最终方案图标

## 参考资料

- `references/component-index.md`：20 个母组件速查与文件映射
- `references/checklist.md`：生成前后检查清单（可直接逐项执行）
