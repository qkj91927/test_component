---
name: demo-to-phone
description: This skill should be used when the user wants to preview, experience, or test an HTML file on a mobile phone, or when the user mentions generating a QR code for a demo, publishing HTML to phone, or making a page scannable. It publishes the HTML file to COS via the ai-weed-publisher skill, appends QQ WebView parameters to the returned URL, and generates a QR code page for scanning with QQ.
---

# demo-to-phone

## 概述

将本地 HTML 文件发布到线上，生成带 QQ WebView 参数的访问链接，并自动创建二维码页面，用户使用 QQ 扫码即可在手机上体验 demo。

## 何时使用

在以下场景触发：

- 用户要求在手机上体验/预览/测试某个 HTML 文件
- 用户要求"生成二维码"、"发布到手机"、"扫码体验"
- 用户要求将 HTML demo 发布为可访问的链接
- 用户提及"demo 体验"、"手机预览"、"QQ 扫码"等表述

不触发的场景：

- 用户仅要求生成 HTML 文件但不要求手机体验
- 纯部署到服务器（非手机体验场景）

## 执行流程

> **⚠️ 关键约束：Step 0 → Step 1 → Step 2 → Step 3 必须在同一轮中连续完成，禁止在任何步骤之间中断等待用户确认或插入额外提示。所有附带说明（如资源依赖提醒、优化建议等）统一放在 Step 3 完成后的输出末尾。**

### Step 0：手机适配预处理（发布前必做）

在上传到 COS 之前，先对 HTML 文件进行以下四项适配处理，使其更适合在真实手机上体验。**修改原文件，不创建副本。**

**0.1 禁用双指放大和双击放大**

在 `<body>` 标签结束前（`</body>` 之前）插入以下脚本：

```html
<script>
// 禁用双指放大
document.documentElement.addEventListener('touchstart', function (event) {
    if (event.touches.length > 1) {
        event.preventDefault();
    }
}, { passive: false });

// 禁用双击放大
var lastTouchEnd = 0;
document.documentElement.addEventListener('touchend', function (event) {
    var now = Date.now();
    if (now - lastTouchEnd <= 500) {
        event.preventDefault();
    }
    lastTouchEnd = now;
}, { passive: false });
</script>
```

**0.2 隐藏状态栏内容（保留高度）**

手机本身已有系统状态栏，页面内的状态栏元素（时间、信号、WiFi、电池图标）会重叠。处理方式：
- **保持状态栏容器高度不变**（54px）
- 将状态栏内所有子元素（时间文字、信号/WiFi/电池图标）的颜色透明度改为 0%

在 `<style>` 中追加：

```css
/* 手机体验适配：隐藏状态栏内容，保留占位高度 */
.status-bar * {
    color: transparent !important;
    opacity: 0 !important;
}
```

**0.3 隐藏底部指示条（保留安全区高度）**

手机本身已有 Home Bar 小横条。处理方式：
- **保持安全区高度不变**（34px）
- 将指示条颜色的透明度改为 0%

在 `<style>` 中追加：

```css
/* 手机体验适配：隐藏指示条，保留安全区高度 */
.home-bar-indicator {
    opacity: 0 !important;
}
```

**0.4 移动端屏幕自适应**

当前界面基准宽度为 428px（iPhone 14 Pro Max），实际手机屏幕宽度各异。使用 viewport 缩放法实现等比适配：
- 以 428px 为设计稿基准宽度
- 通过 JS 动态计算缩放比例，所有元素等比缩放
- CSS 中的 px 值无需任何改动，保证与设计稿 100% 一致

在 `<head>` 中将现有的 `<meta name="viewport" ...>` 标签替换为：

```html
<meta name="viewport" content="width=428, initial-scale=1, maximum-scale=1, user-scalable=no">
```

在 `<body>` 标签结束前（`</body>` 之前）插入以下脚本（与 0.1 的脚本合并到同一个 `<script>` 标签中）：

```js
// 移动端自适应：以428px为基准等比缩放
(function() {
    var designWidth = 428;
    var scale = window.innerWidth / designWidth;
    var viewport = document.querySelector('meta[name="viewport"]');
    if (viewport) {
        viewport.content = 'width=' + designWidth + ', initial-scale=' + scale + ', maximum-scale=' + scale + ', user-scalable=no';
    }
})();
```

### Step 1：检查并使用发布器 Skill

使用 `ai-weed-publisher` skill 将用户指定的 HTML 文件发布到 COS。

调用 skill 时使用以下 prompt：
> "将用户指定的html文件发布到cos，不要发布到野草平台"

**若用户未安装 `ai-weed-publisher` skill**，先执行以下命令安装，安装完成后再开始发布：

```bash
npx --registry=https://mirrors.tencent.com/npm/ @tencent/qqai-market add-skill qq/business/web/ai-weed-publisher
```

### Step 2：加工访问链接

发布成功后，`ai-weed-publisher` 会返回 HTML 的线上访问链接，格式为：
```
https://light-app.ti.qq.com/cos/...xxx.html
```

在返回链接的 `.html` 后面追加 QQ WebView 参数：
```
?_wwv=204800&_wv=16786208
```

**示例**：
- 原始链接：`https://light-app.ti.qq.com/cos/ai-weed/6654f696e2fb/setting-standalone.html`
- 加工后链接：`https://light-app.ti.qq.com/cos/ai-weed/6654f696e2fb/setting-standalone.html?_wwv=204800&_wv=16786208`

### Step 3：生成二维码页面

使用加工后的链接，基于 `assets/qrcode-template.html` 模板生成二维码页面：

1. 读取 `assets/qrcode-template.html` 模板文件
2. 将模板中的 `{{QR_URL}}` 替换为加工后的链接
3. 将模板中的 `{{DEMO_NAME}}` 替换为 demo 名称（从 HTML 文件名推导，去掉 `.html` 后缀，将连字符/下划线替换为空格）
4. 将生成的文件保存为 `qrcode.html`，保存在用户指定 HTML 文件的同级目录下
5. 告知用户打开 `qrcode.html` 后使用 QQ 扫码即可在手机上体验

## 输出格式

执行完成后，**一次性**回复以下全部内容：

1. **发布结果**：原始链接和加工后的链接
2. **二维码文件路径**：`qrcode.html` 的位置
3. **使用说明**：提示用户打开 `qrcode.html`，使用 QQ 扫码体验
4. **风险提示（如有）**：如页面存在外部资源依赖、兼容性等问题，在此处附带说明

> 禁止在三步流程中间插入任何面向用户的提问、提醒或建议。

## 禁止项

- 禁止跳过 Step 0 手机适配预处理直接上传
- 禁止跳过 QQ WebView 参数追加步骤
- 禁止使用原始链接（未加参数的）生成二维码
- 禁止在未安装 `ai-weed-publisher` 的情况下尝试发布
- 禁止在 Step 0 → Step 1 → Step 2 → Step 3 之间中断流程（如插入提醒、等待用户确认等）
- **禁止发布到野草（ai-weed）平台**：`ai-weed-publisher` 仅用于上传文件到 COS 生成预览链接，不得将内容发布到野草平台
