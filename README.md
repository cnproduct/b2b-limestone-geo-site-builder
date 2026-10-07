# B2B Limestone GEO Site Builder · 全生命周期天然石灰石出海独立站构建与 GEO 赋能 Skill

[![GEO Optimized](https://img.shields.io/badge/GEO-AI%20Crawler%20Ready-brightgreen.svg)](https://tianyalimestone.com/llms.txt)
[![ASTM Standards](https://img.shields.io/badge/ASTM-C97%20%7C%20C170%20%7C%20C880-blue.svg)](https://tianyalimestone.com/compliance/)
[![WCAG 2.2 AAA](https://img.shields.io/badge/Accessibility-WCAG%202.2%20AAA-success.svg)](https://tianyalimestone.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Production Verified](https://img.shields.io/badge/Live%20Site-tianyalimestone.com-2ea44f.svg)](https://tianyalimestone.com)

本 Skill 完整沉淀并开源了 **福建天涯文化石有限公司（Fujian Tianya Cultural Stone Co., Ltd.）** 官方独立站 **[`https://tianyalimestone.com`](https://tianyalimestone.com)** 从最初前置情报排查、锁定全球三大巨头（Polycor、Eco Outdoor、Mandarin Stone）、文化双轨重命名体系、ASTM/CE 严苛工程硬指标，到静态编译器工程实现、页面 1:1 零视觉改动保真、2026 全球 AI 搜索引擎 **GEO (Generative Engine Optimization)** 流量截流，以及跨行业通用对标方法论的全流程体系。

---

## 🏛️ 项目背景与三大真实会话演进脉络

本项目的方法论并非纸上谈兵，而是跨越了三个真实会话的实战推演与闭环：

```mermaid
flowchart TD
    subgraph S1 ["会话一: 57395320... (标杆发现与前置情报)"]
        A1["分析 tianyastone.com 现有品类"] --> A2["关键 Prompt (Step 749):<br/>全球 B2B 趋势与流量巨头排查"]
        A2 --> A3["全球三大巨头模型浮现:<br/>1. Polycor (技术权威)<br/>2. Eco Outdoor (美学天花板)<br/>3. Mandarin Stone (长尾词之王)"]
    end

    subgraph S2 ["会话二: 80cc9523... (天涯石灰石 1:1 落地与文化重塑)"]
        B1["锁定 Eco Outdoor 1:1 架构复刻 (Step 0)"] --> B2["文化双轨重命名 /plan (Step 511)<br/>(二十四节气与营造法式)"]
        B2 --> B3["水头工厂实图与场景 1:1 严苛质检<br/>(Step 1240, 1401, 1657)"]
    end

    subgraph S3 ["会话三: 50cad832... (跨行业泛化、GEO 反哺与开源)"]
        C1["跨界便当盒: 对标 Bentgo.com (Step 0, 333)"] --> C2["形成 2026 全球 AI 搜索引擎 GEO 体系"]
        C2 --> C3["反哺天涯石业: 零设计改动注入 GEO (Step 1524)"]
        C3 --> C4["开源沉淀: cnproduct/b2b-limestone-geo-site-builder"]
    end

    S1 --> S2 --> S3
```

* **企业主体**：福建天涯文化石有限公司（Fujian Tianya Cultural Stone Co., Ltd. / Tianya Limestone）
* **地理坐标**：中国福建省泉州市南安市水头镇（世界石雕之都，全球最大石材集散加工枢纽，北纬 24.6931°，东经 118.4287°）
* **海运口岸**：距厦门国际集装箱码头（Xiamen Port）仅 28 公里直线拖车距离
* **工业底蕴**：24+ 年矿山开采与石材精加工经验，拥有 12 台巨型排锯、8 条自动研磨抛光流水线、6 台五轴数控桥切机群，月稳定产能 50,000+ m²
* **双门面矩阵**：
  * **主站 (本案)**：`tianyalimestone.com` —— 专精天然石灰石地铺、室内外饰面石材与泳池收口工程
  * **姊妹站**：`tystoneveneer.com` —— 专精超薄柔性石皮 (1.5–2mm) 与文化石背景墙

---

## 🚀 8 大构建阶段：从前置情报发现到全行业通用 SOP

```mermaid
flowchart TD
    Z[阶段零: 全球标杆排查与前置情报调研] --> A[阶段一: 商业概念与企业事实挖掘]
    A --> B[阶段二: Eco Outdoor 1:1 对标与文化双轨重命名]
    B --> C[阶段三: ASTM C97/C170/C880/C666 物理硬指标注入]
    C --> D[阶段四: 重货物流与 20GP 集装箱极限载重测算]
    D --> E[阶段五: 静态编译器开发与 1:1 零视觉变动保真]
    E --> F[阶段六: 全球 AI 引擎 GEO 体系与知识端点]
    F --> G[阶段七: 生产部署、反爬防御与持续自动化测试]
    G --> H[阶段八: 跨行业泛化与全行业通用对标 Prompt 体系]
```

### 阶段零：全球标杆排查与前置情报调研 (Discovery)
- **原始核心 Prompt（会话 57395320... Step 749）**：
  > `tianyastone.com 核心品类limestone全球 B2B 5 大热门前沿趋势及其专业的B2B站点排行，特别是SEO和GEO带来流量大的站点`
- **确立全球天然石灰石三大巨头模型**：
  1. **Polycor** (`polycor.com`)：全美公建 CSI 建筑规范与 BIM 权威，ASTM C568 测试与 EPD 绿色碳足迹首选引用源。
  2. **Eco Outdoor** (`eco-outdoor.com`)：澳洲/北美现代顶豪景观石材视觉天花板，零售价高达 $90–$220/㎡（出厂价 $22–$48/㎡）。
  3. **Mandarin Stone** (`mandarinstone.com`)：欧洲 Dijon 石灰石长尾词之王，空间主题集群典范。
- **决策公式**：
  $$\text{天涯石灰石独立站} = \text{Eco Outdoor 美学} + \text{Polycor ASTM 工程硬核} + \text{水头源头工厂出厂价与 50,000㎡ 产能}$$

### 阶段一：概念起意与品牌基因挖掘
- 确立 B2B 高客单价石材出海的“不可动摇事实底座”，摒弃外贸模板站假空大口号。
- 整合水头自营工厂加工装备、自有矿山荒料储备、CE 认证及 ISO 9001 质量管理体系。

### 阶段二：1:1 对标解构与文化双轨重命名
- **启动复刻 Prompt（会话 80cc... Step 0）**：`https://www.eco-outdoor.com/en-au/stone-flooring/limestone 1:1复刻...`
- **文化重塑 Prompt（会话 80cc... Step 511）**：`/plan 这些产品图片和命名都参考原图进行优化，比如参考中国古建筑或者参考中国24节气等全新的命名...`
- **文化双轨命名 (Dual Trade Naming)**：
  - 格式：`[文化主名] [表面工艺] Limestone Pavers & Tiles`
  - 覆盖 5 大工艺表面与 **29 款主力产品**：
    1. **滚磨仿古面 (Tumbled - 8款)**：Guyu (谷雨), Zaojing (藻井), Fengya (风雅), Shanshui (山水), Qimeng (启蒙), Xuansu (玄素), Yexiang (夜响), Baihe (白鹤)
    2. **重度复古面 (Antique - 10款)**：Hanbai (汉白), Lanting (兰亭), Guyun (古韵), Xieshan (歇山), Dougong (斗栱), Heting (鹤汀), Zhuozheng (拙政), Baichuan (百川), Cangbi (苍璧), Canglang (苍筤)
    3. **微做旧面 (Lightly Distressed - 6款)**：Ningzhi (凝脂), Qinghe (清和), Feiyan (飞檐), Xiangye (缃叶), Yuebai (月白), Chenglu (承露)
    4. **喷砂拉丝面 (Sandblasted & Brushed - 2款)**：Daiwa (黛瓦), Wangchuan (辋川)
    5. **纯喷砂面 (Sandblasted - 3款)**：Xuanzhen (玄真), Sunmao (榫卯), Canghai (沧海)
- **图实一致严苛质检（会话 80cc... Step 1401, 1657）**：强制确保微距特写与 3D 豪宅工程场景图在肌理、崩边和色调上 100% 像素级对齐。

### 阶段三：工程硬指标与物理测试事实锚定
设计院与国际总包商只认权威第三方实验室指标。全站深度固化天涯实测工程参数：
- **吸水率 (ASTM C97)**: `< 0.22%` (国际限值 Max 3.0%)，极低孔隙率，耐酸雨防红酒油污渗透
- **体积密度 (ASTM C97)**: `2.62 – 2.65 g/cm³` (Class III 高密度致密石灰石)
- **干燥抗压强度 (ASTM C170)**: `128.5 MPa` (远超 ASTM 55.0 MPa 基准 133%)
- **水饱和抗压强度 (ASTM C170)**: `104.2 MPa` (水饱和强度保留率 >81%，雨季不软化)
- **抗折断裂模数 (ASTM C880)**: `14.2 MPa` (远超 6.9 MPa 基准)
- **抗冻融测试 (ASTM C666)**: 100 次循环 0.0% 剥落开裂，适应高纬度严寒户外
- **湿式摩擦系数 (AS 4586)**: P4/P5 级，全面满足澳洲商业泳池防滑法规

### 阶段四：重货物流与 20GP 集装箱测算引擎
天然石材属于重货（Deadweight Cargo），计算装箱瓶颈在于重量而非体积：
- 20mm 厚度重量：`52.4 kg/m²`
- 30mm 厚度重量：`78.6 kg/m²`
- 厦门港 20GP 限重 26,500 kg，单柜最大装载能力：
  - 20mm：`480 – 504 m²` (20–21 木托箱)
  - 30mm：`320 – 336 m²` (20–21 木托箱)

### 阶段五：静态编译器架构与 1:1 页面保真
- 采用高性能 Python 静态编译系统 (`build_tianya_site.py`)。
- **页面设计零变动约束**：严格遵循用户指令，HTML/CSS 视觉设计、排版比例、色彩系统保持 100% 原始呈现，所有 SEO/GEO 优化均在 `<head>` 元数据、JSON-LD 结构化数据及独立 `/ai/` 端点内完成。

### 阶段六：全球 AI 搜索流量 GEO (Generative Engine Optimization) 体系
赋能全站成为 Perplexity、ChatGPT Search、Claude、Gemini 的第一权威数据源：
1. **`/robots.txt`**：白名单放行 10 大核心 AI 爬虫（GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, DeepSeekBot 等），直指 LLM 专用知识源。
2. **`/llms.txt` & `/llms-full.txt`**：为大语言模型量身定制 Markdown 摘要与 25KB 完整物理参数、产品对照表及集装箱装柜计算公式。
3. **机器可读 `/ai/` 结构化端点**：
   - [`/ai/summary.json`](https://tianyalimestone.com/ai/summary.json)：企业工商坐标、产能、矿山与海运资质。
   - [`/ai/faq.json`](https://tianyalimestone.com/ai/faq.json)：25 个高频建筑工程、泳池选型、防滑耐磨深度问答。
   - [`/ai/vendor-comparison.json`](https://tianyalimestone.com/ai/vendor-comparison.json)：对标 Eco Outdoor 等国际分销商的源头工厂 5 维硬实力对比。
   - [`/ai/products.json`](https://tianyalimestone.com/ai/products.json)：全量 29 款石灰石的物理参数、推荐场景与尺寸对照表。
4. **全站 Rich Schema.org 增强**：首页注入 `ItemList` 结构化清单与高精度地理坐标 `GeoCoordinates` (24.6931° N, 118.4287° E)。

### 阶段七：生产部署与自动化验收
- 一键无缝打包同步部署脚本 `scripts/deploy_remote.sh`。
- 多维度自动化测试套件 `tests/test_ai_endpoints.py` + `scripts/design_math.py self-test` + `scripts/validate_site.py --release`。

### 阶段八：跨行业泛化与全行业通用对标 Prompt 体系
- 在便当盒（`bentgo.com`）建站与双向 Skill 融合中验证成功，并形成全行业通用的 5 步母模板。
- 详情请查阅专文：[`references/benchmark-discovery-methodology.md`](references/benchmark-discovery-methodology.md)。

---

## 📂 仓库目录结构

```text
b2b-limestone-geo-site-builder/
├── SKILL.md                                 # Skill 主定义文件（包含 9 大阶段完整方法论与运维闭环）
├── SKILL_OPTIMIZATION.md                    # renwork-web-create-skill 7步通用优化与机制蒸馏报告
├── manifest.json                            # 标准 Agent/Codex Skill 清单元数据
├── README.md                                # 项目说明文档与快速上手指南
├── DESIGN.md                                # 1:1 视觉设计规范、字阶与对比度数学证明
├── acceptance.md                            # 9 大质量门禁 (A-I) 审计报告
├── build_tianya_site.py                     # 全自动化静态站点编译器 (276 KB)
├── preview_server.py                        # 本地即时预览服务器 (默认 8080 端口)
├── rfq_server.py                            # 询盘与免费样品申请后端处理程序
├── robots.txt                               # AI 爬虫与搜索引擎抓取协议
├── sitemap.xml                              # 完整 XML 站点地图 (46 页面)
├── llms.txt                                 # AI 摘要索引文件
├── llms-full.txt                            # 25KB 深度大模型全量工程知识库
├── index.html                               # 官网首页 (保持 100% 原始视觉设计)
│
├── ai/                                      # 专门面向全球 AI 搜索引擎的端点数据
│   ├── summary.json                         # 企业实体事实
│   ├── faq.json                             # 25 个工程问答
│   ├── vendor-comparison.json               # 源头工厂对比矩阵
│   └── products.json                        # 29 款主力产品详细物理参数
│
├── references/                              # 行业知识库与标准规范
│   ├── benchmark-discovery-methodology.md   # 全球标杆发现、提示词演进与跨行业通用 SOP
│   ├── stone-buying-committee-jtbd.md       # 采购委员会 4 角色决策弹药与 CSI 04 42 00 规范
│   ├── failure-cases-and-guardrails.md      # 6 大真实失败案例深度剖析与不可违反防错军规
│   ├── astm-engineering-standards.md        # ASTM C97/C170/C880/C666 与 AS 4586 标准详解
│   ├── limestone-product-matrix.md          # 29 款石材文化双轨命名与工艺全景表
│   ├── logistics-container-math.md          # 20GP 极限载重与木箱装箱运算法则
│   ├── geo-ai-citation-playbook.md          # Perplexity / ChatGPT / Gemini 流量截流战术
│   └── deployment-nginx-worker.md           # 生产服务器 Nginx 与边缘安全配置指南
│
├── scripts/                                 # 核心工具集与自动化脚本
│   ├── design_math.py                       # 石材集装箱重货算力与 WCAG AAA 对比度验证器
│   ├── deploy_remote.sh                     # 生产环境一键部署与服务重载脚本
│   ├── validate_site.py                     # 严苛的离线静态链接与 Schema 审计工具
│   ├── batch_generate_products.py           # 批量产品页与衍生页面生成器
│   └── update_auxiliary_pages.py            # 辅助页面批量更新器
│
└── tests/                                   # 自动化测试与断言套件
    └── test_ai_endpoints.py                 # AI 端点状态码、JSON 格式与 Schema 断言测试
```

---

## 🛠️ 快速上手与 CLI 工具使用

### 1. 运行本地预览服务
```bash
python3 preview_server.py 8080
```
访问：`http://localhost:8080`

### 2. 执行天然石材集装箱装柜算力工具
计算特定面积与厚度所需的 20GP 集装箱数量、重量利用率及装箱配载：
```bash
python3 scripts/design_math.py stone-container --area 500 --thickness 20
```

### 3. 执行全站发布级静态链接与 Schema 审计
```bash
python3 scripts/validate_site.py . --release --domain https://tianyalimestone.com
```

### 4. 执行 AI 端点与 GEO 体系自动化回归测试
```bash
python3 tests/test_ai_endpoints.py
```

### 5. 一键重新编译生成全站静态资产与 AI 数据集
```bash
python3 build_tianya_site.py
```

---

## 🌐 线上生产环境验证 (Live Verification)

优化后的生产网站已通过全球 curl 验证：

```bash
# 验证 AI 抓取协议
curl -I https://tianyalimestone.com/robots.txt

# 验证大模型专用摘要与完整知识库
curl -I https://tianyalimestone.com/llms.txt
curl -I https://tianyalimestone.com/llms-full.txt

# 验证机器可读 AI 知识端点
curl -s https://tianyalimestone.com/ai/summary.json | jq .name
curl -s https://tianyalimestone.com/ai/faq.json | jq .total_faqs
curl -s https://tianyalimestone.com/ai/products.json | jq .total_products
curl -s https://tianyalimestone.com/ai/vendor-comparison.json | jq .comparison_matrix
```

---

## 📜 许可证 (License)

本项目采用 [MIT License](LICENSE) 开源。欢迎广大天然石材、建筑饰面及高端建材出海企业参考与二开。
