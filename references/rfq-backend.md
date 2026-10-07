# RFQ 后端详细手册（Worker + Turnstile + MailChannels）

## 架构
表单 → Cloudflare Turnstile（前端）→ Worker `POST /api/inquiry`（服务端验签）→ MailChannels → `info@tianyastone.com`。

## Worker 要点（模板 `assets/rfq-worker.js`）
- honeypot 字段短路假成功；缺 token → `400 captcha_required`；`siteverify` 传 `secret`/`response`/`remoteip`（`CF-Connecting-IP`），失败 → `403 captcha_failed`。
- **MailChannels 失败必须穿透**：`!res.ok` 时返回 `502 {success:false, error:'email_failed'}`，让 `success:true` 真正等于"邮件被接走"。
- 发件人 `rfq@<domain>`；CORS 放行站点源并处理 `OPTIONS`；`GET /api/health` 存活检查。
- Secrets（API 设置）：`TURNSTILE_SECRET_KEY`、`NOTIFICATION_EMAIL`。

## 前端接线（`main.js`）
- payload 必须带 `formData.get('cf-turnstile-response')`（Turnstile 组件自动注入的隐藏字段），否则永远 `captcha_required`。
- Worker 成功 → `turnstile.reset()` + 成功提示 + `form.reset()`；`captcha_required`/`captcha_failed` → 显示真实错误、**保留用户输入**；绝不展示未经后端确认的成功消息；绝不静默兜底到第三方中继。

## 三段式验收（全部通过才算完工）
1. **假 token 探针**：`403 captcha_failed`（Worker 存活且在验签）。
2. **真机提交**：人工点过 Turnstile（无头/自动点击会被风控判机器人"验证失败"，必须用户接管）→ 成功提示、表单清空、无验证码错误。
3. **客户确认邮箱收到测试邮件**。
之后才删旧中继：表单 `action`、JS fallback、`_subject`/`_template` 等专用字段；重建后全站 `grep` 确认零残留。

## 已知限制
- Worker 无 KV/D1，询盘无持久归档（可选增强）。
- 部署中的 Worker 以线上为准，`assets/rfq-worker.js` 与线上不一致时先从线上同步回来再改。
