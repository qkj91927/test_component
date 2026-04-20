# 组件卡片快速参考（Inspector Tab 2 用）

本文档收集 Basic 1.0 常用组件在 Inspector 组件 Tab 中的标准写法。
生成界面时，按实际用到的组件从此处挑选并填入实际数值。

---

## NavBar · L5 · C1 · R3（发送 / 标题 / 操作）

```html
<div class="comp-card">
  <div class="comp-head">
    <div class="comp-name"><span class="dot"></span>NavBar</div>
    <span class="comp-tag">L5 · C1 · R3</span>
  </div>
  <div class="row cols-2">
    <div class="field"><span class="lbl">W</span><span class="val">428 px</span></div>
    <div class="field"><span class="lbl">H</span><span class="val">44 px</span></div>
  </div>
  <div class="padding-box">
    <div class="padding-head"><span>Padding</span><span class="arrow">▲</span></div>
    <div class="padding-grid">
      <div class="cell"><span class="lbl">T</span><span class="val">0 px</span></div>
      <div class="cell"><span class="lbl">R</span><span class="val">16 px</span></div>
      <div class="cell"><span class="lbl">B</span><span class="val">0 px</span></div>
      <div class="cell"><span class="lbl">L</span><span class="val">16 px</span></div>
    </div>
  </div>
  <div class="row cols-2">
    <div class="field"><span class="lbl">L5 关闭</span><span class="val">17/400</span></div>
    <div class="field"><span class="lbl">Color</span><span class="val">text-primary</span></div>
  </div>
  <div class="row cols-2">
    <div class="field"><span class="lbl">C1 标题</span><span class="val">17/600</span></div>
    <div class="field"><span class="lbl">Color</span><span class="val">text-primary</span></div>
  </div>
  <div class="row cols-2">
    <div class="field"><span class="lbl">R3 操作</span><span class="val">17/400</span></div>
    <div class="field"><span class="lbl">Color</span><span class="val">text-primary</span></div>
  </div>
</div>
```

## Search · A1 一级默认

关键字段：W 396 / H 36 / Radius 12 / Fill fill-tertiary / Align center / Icon 18×18 / Placeholder 17/400 text-tertiary

## Search · B1 二级默认（带返回）

关键字段：W 328 / H 36 / 左箭头 24×24 chevron_left.svg / Placeholder 17/400 / Align left

## TextBlock · H2 一级标题

关键字段：W 428 / Min H 36 / Padding 0·16·0·16 / Title 20/600 text-primary / Line 28

## Plain List · L3 + C1（头像 + 单行）

```html
<div class="comp-card">
  <div class="comp-head">
    <div class="comp-name"><span class="dot"></span>Plain List</div>
    <span class="comp-tag">L3 · C1 · R0</span>
  </div>
  <div class="row cols-2">
    <div class="field"><span class="lbl">Row W</span><span class="val">428 px</span></div>
    <div class="field"><span class="lbl">Row H</span><span class="val">52 px</span></div>
  </div>
  <div class="padding-box">
    <div class="padding-head"><span>Padding</span><span class="arrow">▲</span></div>
    <div class="padding-grid">
      <div class="cell"><span class="lbl">T</span><span class="val">0 px</span></div>
      <div class="cell"><span class="lbl">R</span><span class="val">16 px</span></div>
      <div class="cell"><span class="lbl">B</span><span class="val">0 px</span></div>
      <div class="cell"><span class="lbl">L</span><span class="val">16 px</span></div>
    </div>
  </div>
  <div class="row cols-2">
    <div class="field"><span class="lbl">L3 头像</span><span class="val">32 × 32</span></div>
    <div class="field"><span class="lbl">Radius</span><span class="val">50%</span></div>
  </div>
  <div class="row cols-2">
    <div class="field"><span class="lbl">L→C Gap</span><span class="val">12 px</span></div>
    <div class="field"><span class="lbl">C→R Gap</span><span class="val">12 px</span></div>
  </div>
  <div class="row cols-2">
    <div class="field"><span class="lbl">Title</span><span class="val">17/400</span></div>
    <div class="field"><span class="lbl">Color</span><span class="val">text-primary</span></div>
  </div>
  <div class="row cols-1">
    <div class="field"><span class="lbl">Divider</span><span class="val">0.5px · inset 60 / 0</span></div>
  </div>
</div>
```

## Plain List · L3 + C1 + R1（头像 + 单行 + 辅助文字）

额外补一行：
```html
<div class="row cols-2">
  <div class="field"><span class="lbl">R1 辅助</span><span class="val">17/400</span></div>
  <div class="field"><span class="lbl">Color</span><span class="val">text-secondary</span></div>
</div>
```

## Grid · B6 横滑圆形 6 列

关键字段：W 428 / H 112 / Gap 16 / Thumb 60×60 Radius 50% / Label 12/400 / Gap T/L 8

## Grouped List · 通用卡片

关键字段：W 396 / Bg white / Radius 12 / Row H 56 / 页面背景必须 bg-secondary

## Button · 主要按钮

关键字段：H 52 / Bg brand-standard / Color text-white / Font 17/500 / Radius 14

## ActionSheet

关键字段：W 396 / Radius 16 / Padding T 16 R 16 B 34 L 16 / Action Row H 60 / Divider 0.5px

## Home Bar

关键字段：W 428 / H 34 / Indicator 144×5 / Radius 2.5px / Color text-primary

---

# Style Tab · Color Tokens 片段

以下片段直接复制到 `<!-- TEMPLATE:COLOR_TOKENS -->` 处：

```html
<div class="row cols-1">
  <div class="field">
    <span class="swatch" style="background:#0099ff"></span>
    <span class="lbl">brand-standard</span><span class="val">#0099FF</span>
  </div>
</div>
<div class="row cols-1">
  <div class="field">
    <span class="swatch" style="background:#000"></span>
    <span class="lbl">text-primary</span><span class="val">#000000</span>
  </div>
</div>
<div class="row cols-1">
  <div class="field">
    <span class="swatch" style="background:rgba(60,60,67,0.6)"></span>
    <span class="lbl">text-secondary</span><span class="val">60,60,67 / .6</span>
  </div>
</div>
<div class="row cols-1">
  <div class="field">
    <span class="swatch" style="background:#214ca5"></span>
    <span class="lbl">text-link</span><span class="val">#214CA5</span>
  </div>
</div>
<div class="row cols-1">
  <div class="field">
    <span class="swatch" style="background:rgba(118,118,128,0.12)"></span>
    <span class="lbl">fill-tertiary</span><span class="val">118,118,128 / .12</span>
  </div>
</div>
<div class="row cols-1">
  <div class="field">
    <span class="swatch" style="background:rgba(0,0,0,0.12)"></span>
    <span class="lbl">border-weak</span><span class="val">0,0,0 / .12</span>
  </div>
</div>
```

只保留本页实际用到的 token，未用到的请删除。
