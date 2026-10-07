# Turnstile 修复详细手册

## 正确 API 路径
- 基址 `https://api.cloudflare.com/client/v4`，`Authorization: Bearer $CF_TOKEN`（用户临时提供，env 传入）。
- **正确路径**：`/accounts/{account_id}/challenges/widgets`。`/turnstile/widgets` 返回 "No route for that URI"。
- 排查时先 `GET /user/tokens/verify` 区分 token 失效与路由错误。

## 诊断错配
`GET /accounts/{account_id}/challenges/widgets` 返回每个 widget 的 `name`/`sitekey`/`mode`/`domains`（**secret 永不返回**）。
把站点 HTML 里写死的 sitekey 和 Worker 里配的 secret 所属 widget 对上——曾出现的真实故障：站点用 widget#1 的 sitekey，Worker 里装的是 widget#2 的 secret。

## 修复（推荐：不重建站点）
```bash
# 1. 轮换"站点正在用的"那个 widget 的 secret（-d '{}' 必填，否则 EOF 错误）
curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT/challenges/widgets/$SITEKEY/rotate_secret" \
  -H "Authorization: Bearer $CF_TOKEN" -H "Content-Type: application/json" -d '{}'

# 2. 把返回的新 secret 装到 Worker
curl -X PUT "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT/workers/scripts/$SCRIPT/secrets" \
  -H "Authorization: Bearer $CF_TOKEN" -H "Content-Type: application/json" \
  -d '{"name":"TURNSTILE_SECRET_KEY","text":"<新secret>","type":"secret_text"}'
```

## 验收
假 token 探针 `POST {site}/api/inquiry` 必须返回 `403 {"success":false,"error":"captcha_failed"}`；之后真人提交成功即证明配对正确。

## 纪律
secret 只在 API 调用体内出现一次，绝不打印、落盘、进聊天记录或记忆；交接文档只记"某 widget 于某日轮换"，不记值。
