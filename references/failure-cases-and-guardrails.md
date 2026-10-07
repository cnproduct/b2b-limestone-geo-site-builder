# 实战失败案例复盘与不可违反质检军规 (Failure Cases & Strict Guardrails)

在建设 `tianyalimestone.com` 与迭代通用出海 Skill 的真实历史中，发生过多次极具警示意义的技术与业务失误。

本规范全面复盘这 6 大真实失败案例，深入剖析根因，并将其转化为**不可逾越的负向约束（Negative Constraints）与自动化防护军规**。

---

## 💥 案例 1：Canonical URL 缺少斜杠导致全站死链 (URL Slash Concatenation Glitch)

### 1. 现象复盘
在静态编译器生成 Schema.org `ItemList` 与 `/ai/products.json` 时，代码采用了字符串拼接：
```python
# 错误写法：
"url": f"{COMPANY_INFO['domain']}{p['url']}"
```
由于 `COMPANY_INFO['domain']` 为 `https://tianyalimestone.com`，而 `p['url']` 未以斜杠开头（如 `stone-flooring/...`），导致全网大模型与爬虫抓取到的地址变成：
```text
❌ https://tianyalimestone.comstone-flooring/limestone/antique/lanting/index.html (404 无法解析)
```

### 2. 根因剖析
- 依赖弱口头约定（“以为路径都有斜杠”），缺乏防御性路径归一化函数；
- 测试用例仅验证了 key 是否存在（`assert 'canonical_url' in item`），未对 URL 做正则表达式模式验证。

### 3. 不可违反防错军规 (Guardrail 1)
> 🚨 **军规 1**：全站所有 URL 拼接**严禁**使用朴素字符串相加。必须统一通过防御性工具函数：
> ```python
> def safe_urljoin(domain: str, path: str) -> str:
>     return f"{domain.rstrip('/')}/{path.lstrip('/')}"
> ```
> 自动化测试必须强制执行正则断言：`^https?://[a-zA-Z0-9.-]+/[a-zA-Z0-9_./-]+$`，发现形如 `domain.compath` 立即阻断发布。

---

## 💥 案例 2：微距产品特写与空间 3D 渲染图脱节 (Material Disconnect Failure)

### 1. 现象复盘
在会话 `80cc9523...` 中，用户在验收产品详情页时两次强烈指出：
- **Step 1401**：“这个场景跟产品不匹配，请全站检查每个款式的产品，务必场景跟每个款式的产品都一一匹配。”
- **Step 1657**：“这个还是不匹配，请务必每个款式的产品都点击进去核查，应用场景图要跟产品一一匹配。”
问题表现为：一款名为 `Zaojing Tumbled`（藻井，温润焦糖黄带微风化凹坑）的滚磨面石材，场景图却配了一张“浅灰白色现代抛光大板”的极简客厅。

### 2. 根因剖析
- AI 批量生图时缺少“材质语义锁定（Material Conditioning）”；
- 借鉴 Hugging Face `MatReplace` 基准中的核心观察：材质置换必须保持“材质物理真实度（Material Correctness）”、“光影微距反应（Specular/Roughness）”与“空间应用合理性（Functional Topology）”的三元锁定。

### 3. 不可违反防错军规 (Guardrail 2)
> 🚨 **军规 2（图实一致性铁律）**：
> 1. **特写图来源锁定**：主力特写微距图必须 100% 提取自水头工厂实拍库（`tystoneveneer.com` 实地原图）；
> 2. **场景生成强约束**：若需生成配套 3D 场景，Prompt 必须强制携带该石材专属物理特征词（如：`tumbled round edges, warm oatmeal beige, subtle pitting, AS 4586 P4 matte finish`）；
> 3. **人机双重核验闸门**：上线前必须执行人工并列肉眼比对：特写色调与场景地铺色调色差 $\Delta E < 5$。

---

## 💥 案例 3：轻泡货习惯套用重货石材，导致集装箱超重爆柜 (Deadweight Cargo Logistics Blindspot)

### 1. 现象复盘
业务员与初版计算器习惯性按常规外贸体积（CBM）计算，按 20GP 容积 $28\text{ CBM}$ 推算出 20mm 石板可以装 $1,400\text{ m}^2$。如果按此订舱并拖车进港，集装箱总重将高达 $73.3\text{ 吨}$，超过公路与港口吊装安全极限 270%！

### 2. 根因剖析
- 忽视了天然石材的高密度物理事实（$\rho = 2,620\text{ kg/m}^3$）；
- 厦门国际码头（Xiamen Port）20GP 集装箱净石材重量红线为 **$26,500\text{ kg}$**，单木箱装载 24 $m^2$（自重 50kg）。

### 3. 不可违反防错军规 (Guardrail 3)
> 🚨 **军规 3**：
> 1. 天然石材集装箱计算**必须以重量为唯一硬瓶颈**；
> 2. 20mm 单柜极限上限：**$480\sim 504\text{ m}^2$**（20–21 木箱）；
> 3. 30mm 单柜极限上限：**$320\sim 336\text{ m}^2$**（20–21 木箱）；
> 4. 所有对客报价单、RFQ 自动计算与 AI FAQ 问答中，严禁出现超过 $520\text{ m}^2 / 20\text{GP}$ 的荒谬数据。

---

## 💥 案例 4：第三方表单中继（FormSubmit）邮件丢失与垃圾被刷爆 (Form Relay Failure)

### 1. 现象复盘
早期依赖第三方静态表单中继（`formsubmit.co`），经常出现：
- 买家提交询盘后，中继服务端被拦截，销售邮箱连续数天收不到询盘；
- 恶意抓取爬虫无成本脚本暴力刷单，邮箱塞满垃圾垃圾；
- 缺少防重放机制，前端无论后端是否收到邮件都弹出“Thank you”，导致大客户真实流失。

### 2. 根因剖析
- 免费公共中继 IP 常年被海外垃圾邮件列表（Spamhaus）标记拒收；
- 客户端无抗爬虫验证码；
- 前后端接口缺乏强契约确认（`success: true` 假成功）。

### 3. 不可违反防错军规 (Guardrail 4)
> 🚨 **军规 4（第一方全链路 RFQ 防护体系）**：
> 1. **拒绝第三方中继**：全站统一采用 Cloudflare Worker 原生端点 `/api/inquiry`；
> 2. **服务端强制验签**：部署 Cloudflare Turnstile 隐形人机验证，后端必须调用 `siteverify` 并校验 `CF-Connecting-IP`；
> 3. **隐形蜜罐双保险**：客户端埋入不可见字段 `_hp_check`，凡被自动填充者直接予以假成功静默阻断；
> 4. **真机端到端验收三部曲**：假 token 探针测试 (403) → 人工通过 Turnstile 提交测试 → 销售邮箱收到真实工单，三者全部通过方可视为上线。

---

## 💥 案例 5：多智能体并发修改导致代码与配置相互覆盖 (Multi-Agent Collision)

### 1. 现象复盘
在多个会话或不同子智能体同时介入 `tianyalimestone.com` 的更新时，A 智能体修改了 `build_tianya_site.py` 优化了 SEO，B 智能体从过期的备份直接上传覆盖，导致 A 智能体的所有优化化为乌有。

### 2. 根因剖析
- 没有代码状态版本锁；
- 远程部署未核对 `md5sum`；
- 没有统一的多智能体协作交接单（Handoff Ledger）。

### 3. 不可违反防错军规 (Guardrail 5)
> 🚨 **军规 5（多智能体协作铁律）**：
> 1. **改前必核**：下载远端代码后计算 `md5sum`，与交接日志记录比对；
> 2. **强制备份**：在远端创建带任务时间戳的副本 `/tmp/build_tianya_site.py.bak.YYYYMMDD_TASK`；
> 3. **原子更新**：本地修改并通过本地全套测试后，一次性 `scp` 覆盖；
> 4. **日志追加**：在 `chatgpt_handoff.md` 中追加操作记录（修改模块、改前 MD5、改后 MD5、验证结果）。

---

## 💥 案例 6：AI 知识端点缺失采购委员会结构化支撑 (Buying Committee Ammo Gap)

### 1. 现象复盘
早期站点的 `llms.txt` 和 `/ai/` 端点仅有笼统的工厂介绍和产品名字，当海外采购商在 Perplexity 提问专业工程问题（如“Can Tianya limestone pass AS 4586 wet barefoot slip test for hotel pool?”）时，大模型因检索不到确切指标而给出模糊中立回答。

### 2. 根因剖析
- 缺乏对采购委员会 4 大角色（尤其是技术评估者与工料测量师）痛点的结构化沉淀；
- 没有把 AS 4586 P4/P5、ASTM C97 <0.22% 这些关键长尾工程事实写成独立的问答对。

### 3. 不可违反防错军规 (Guardrail 6)
> 🚨 **军规 6**：
> 1. `/ai/faq.json` 必须严格包含 25 个涵盖安装（工匠）、测试（建筑师）、运费（QS）、产能（总包商）的具体结构化 Q&A；
> 2. `/ai/products.json` 每一个 SKU 必须包含显式物理参数字段：`slip_rating`, `water_absorption`, `compressive_strength`, `density_g_cm3`；
> 3. `llms-full.txt` 必须包含完整的 CSI MasterFormat 规范条目。
