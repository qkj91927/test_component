# Edit 模式通信协议（R8）

Inspector（父页）与 iframe（界面页）之间的交互协议。所有消息通过 `window.postMessage` 传递，并带 `source` 字段做来源过滤。

---

## 1. 消息 Schema

所有消息统一格式：

```ts
interface Message {
  source: 'figma-inspector' | 'figma-canvas';
  type: string;
  [key: string]: any;
}
```

- `figma-inspector`：父页（Inspector）发出的消息
- `figma-canvas`：子页（iframe 界面）发出的消息

收到消息时**必须先校验 `source`**，避免与浏览器扩展/其他嵌入页的消息冲突。

---

## 2. 消息类型表

### 2.1 父 → 子（figma-inspector → figma-canvas）

| type | payload | 触发时机 | 子页行为 |
|------|---------|---------|---------|
| `ENTER_EDIT` | — | 用户点击 Edit 按钮 | `body.classList.add('edit-mode')` |
| `EXIT_EDIT` | — | 再次点击 Edit 按钮 | `body.classList.remove('edit-mode')` + 清除选中 + 回发 `DESELECT` |
| `APPLY_STYLE` | `{ styles: { [cssProp: string]: string } }` | 用户在 Inspector 修改某字段并按 Enter/失焦 | `selectedEl.style.setProperty(prop, val)` + 回发 `SELECT`（回显新尺寸） |

### 2.2 子 → 父（figma-canvas → figma-inspector）

| type | payload | 触发时机 | 父页行为 |
|------|---------|---------|---------|
| `READY` | — | 子页 DOMContentLoaded | 若 editOn 则重发 `ENTER_EDIT`（处理晚加载） |
| `SELECT` | `{ component, variant, tokens, rect: {x,y,w,h} }` | 用户点选某组件 / 尺寸变化重发 | 画 overlay + 渲染 edit-panel |
| `DESELECT` | — | 退出 Edit / 取消选中 | 隐藏 overlay + selection-card |

### 2.3 payload 字段定义

**SELECT.rect** — 选中元素在 iframe 视口内的坐标（由 `getBoundingClientRect()` 得到）：
```ts
{ x: number, y: number, w: number, h: number }
```

**SELECT.tokens** — 组件的展示 token 对象，来自子页 `COMPONENT_TOKENS[name]`：
```ts
{ W: '428 px', H: '44 px', PaddingX: '16 px', TitleFont: '17/600', ... }
```

**APPLY_STYLE.styles** — CSS 属性键值对：
```ts
{ 'width': '440px', 'padding-left': '20px', 'padding-right': '20px' }
```

---

## 3. 可编辑 Token 映射表（TOKEN_META）

父页 Inspector 脚本中的白名单，只有以下 key 会渲染为可输入的 `<input>`，其余字段只读展示。

| Token key | CSS 属性 | 输入示例 |
|-----------|---------|---------|
| `W` | `width` | `440 px` |
| `H` | `height` | `60 px` |
| `RowW` | `width` | `428 px` |
| `RowH` | `height` | `72 px` |
| `MinH` | `min-height` | `36 px` |
| `PaddingX` | `padding-left` + `padding-right` | `16 px` |
| `Gap` | `gap` | `12 px` |
| `Radius` | `border-radius` | `12 px` |
| `LineHeight` | `line-height` | `24 px` |

### 如何扩展可编辑字段

1. 在 Inspector 模板的 `TOKEN_META` 中添加 key → cssProp 映射
2. 在子页 `COMPONENT_TOKENS` 中对应组件补充该字段
3. （可选）在 `applyStyleUpdate` 中对值做预处理（如颜色合法性校验）

### 特殊 cssProp

- `padding-left-right` 是**虚拟属性**，handler 会自动拆成 `padding-left` + `padding-right` 两条
- 后续如需扩展 `margin-xy`、`inset-xy` 等可按此模式添加

---

## 4. 子页必备实现（检查清单）

任何通过本 Skill 生成的界面 HTML，**必须**满足：

- [ ] 每个母组件容器加 `data-component="<组件名>"` 和 `data-variant="<变体>"`
- [ ] CSS 中有 3 条 Edit 模式规则：
  - [ ] `body.edit-mode [data-component] { cursor: pointer }`
  - [ ] `body.edit-mode [data-component]:hover { outline: dashed }`
  - [ ] `body.edit-mode [data-component].selected { outline: solid }`
- [ ] `<script>` 中声明 `COMPONENT_TOKENS`（所有 data-component 对应的 token 对象）
- [ ] 监听 `click` / `message` 事件
- [ ] 挂载完成时发送 `READY`

---

## 5. 父页必备实现（检查清单）

Inspector HTML 必须满足：

- [ ] Edit 按钮带 `id="editToggle"` 且点击切换 `.active` 类
- [ ] iframe 带 `id="stage"`
- [ ] `.canvas` 内有 `<div id="selectionOverlay">` 浮层（含 `.sel-box` + `.sel-label`）
- [ ] Inspector 内有 `<div id="selectionCard">` / `<div class="edit-empty">` / `<div id="editPanel">`
- [ ] CSS 区分 3 态：`.inspector.edit-mode` / `.no-selection` / `.has-selection`
- [ ] 脚本中声明 `TOKEN_META` 白名单

---

## 6. 测试用例（手动）

完成 Skill 生成后，按此清单走一遍：

| # | 操作 | 预期 |
|---|------|------|
| 1 | 点击顶栏 Edit 按钮 | 按钮变蓝；Inspector Tab 隐藏；显示"请在画布点击组件"空态 |
| 2 | 鼠标移到画布某组件 | 出现蓝色虚线 hover 框 |
| 3 | 点击该组件 | 子页出现实线选中框；父页 overlay 同步画框；Inspector 显示该组件 tokens |
| 4 | 修改 `W` 为 `500 px` → Enter | 画布组件宽度变为 500px；overlay 选中框同步变宽 |
| 5 | 点击另一组件 | 原组件选中状态消失；新组件被选中；Inspector 切换参数 |
| 6 | 再次点击 Edit | 退出编辑；选中/overlay 全部清除；Tab 面板恢复显示 |
| 7 | 刷新页面 | 所有修改复原 |

---

## 7. 已知限制

1. **不持久化**：修改仅在内存中，刷新复原（故意的，避免误以为改源码）
2. **只支持数值尺寸**：颜色/字体/枚举值暂未支持编辑（后续扩展）
3. **选中框对齐依赖 iframe 内无 scroll**：若子页有滚动条，需在子页 `scroll` 事件里重发 SELECT（模板已内置）
4. **跨域限制**：子页必须与父页同源加载（本地服务器下 file:// 会失败）
