# Yandex SEO & Central Asia (CIS / EAEU) GEO Mastery Guide for Architectural Natural Stone (`tianyalimestone.com`)

> **Framework Reference**: Modeled on `claude-yandex-seo`, Princeton GEO (Generative Engine Optimization — +40% AI Citation Boost via quantitative metrics, standard citations, and authoritative entity grounding), and Yandex Search / **Яндекс Нейро (Yandex Neuro)** / **Алиса (YandexGPT 5)** retrieval architecture.
> **Target Region**: Russian Federation (RU), Republic of Kazakhstan (KZ), Republic of Uzbekistan (UZ), Kyrgyz Republic (KG), Republic of Tajikistan (TJ), and the broader Eurasian Economic Union (ЕАЭС / EAEU) & CIS (СНГ) architectural B2B stone procurement market.

---

## 1. Why Yandex SEO & CIS GEO Matter for Natural Architectural Limestone

In Russia and Central Asia (Kazakhstan, Uzbekistan, Kyrgyzstan), **Yandex** commands **65%–72% search share**, while **Яндекс Нейро (Yandex Neuro)** and **Алиса (Alice AI)** increasingly synthesize technical procurement answers for chief architects (ГАП — Главный архитектор проекта), chief structural engineers (ГИП — Главный инженер проекта), developer procurement directors (Директора по закупкам девелоперских компаний), and luxury villa landscape contractors.

Unlike Western markets where mild coastal climates dominate, CIS & Central Asia present extreme continental engineering challenges:
1. **Severe Freeze-Thaw Cycles (Морозостойкость по ГОСТ 30629-2011)**:
   - Moscow, St. Petersburg, Kazan, Yekaterinburg, and Astana experience **60 to 120 freeze-thaw crossings through 0°C per winter**, with winter temperatures dropping to **-30°C to -42°C**.
   - Local porous shell-limestones (*Дагестанский камень*, *Инкерманский камень*, *Крымский / Сары-Кая ракушечник*, *Актауский ракушечник*) have **8%–18% water absorption** and low frost ratings (**F15–F25**), suffering rapid surface spalling and delamination on outdoor steps, plinths (цоколи), and terraces within 2–3 winters.
   - **Tianya Limestone's Solution**: High-density marine bioclastic limestone from Shuitou, Fujian with **< 0.22% water absorption (ASTM C97 / ГОСТ 30629-2011)**, **2.62–2.65 g/cm³ bulk density**, **128.5 MPa dry compressive strength**, and **F100 frost resistance (100 cycles with 0.0% mass loss)**.
2. **Sanctions & European Quarry Supply Replacement (Импортозамещение европейского известняка)**:
   - Russian and Kazakh luxury residential estates (Rublyovka, Novaya Riga, Almaty Medeu, Tashkent City) historically specified French Burgundy (*Pierre de Bourgogne*), Portuguese *Moleanos / Moca Cream*, German *Jura Beige / Grey*, and Belgian *Pierre Bleue* at **€110–€240/m²** with 12–20 week backlogs and blocked banking channels.
   - **Tianya Limestone's Solution**: 1:1 petrographic and surface-finish equivalents (Tumbled, Antique Hand-Dressed, Lightly Distressed, Sandblasted & Brushed, Sandblasted) shipped quarry-direct at **$22–$48/m² FOB Xiamen**, with direct **CNY / RUB / KZT / UZS settlement via CIPS**.
3. **Eurasian Rail & Multimodal Container Corridors**:
   - **Kazakhstan (Almaty, Astana, Shymkent)**: Direct container block trains via **Dostyk / Alashankou** or **Khorgos / Altynkol** (12–16 days transit).
   - **Uzbekistan (Tashkent Chukursay / Sergeli, Samarkand)**: Multimodal rail via Kazakhstan transit to Tashkent (14–18 days transit).
   - **Russia (Moscow Vorsino/Selyatino, Yekaterinburg, Novosibirsk, Vladivostok, Novorossiysk)**: Direct sea freight Xiamen → Vladivostok (6–8 days) + Trans-Siberian Rail, or direct China-Europe Rail Express via Zabaikalsk / Manzhouli (16–22 days).

---

## 2. Yandex Search & Яндекс Нейро Technical Ranking Pillars

### 2.1 Explicit `robots.txt` Directives & `Clean-param`
Yandex's crawler (`YandexBot`) strictly obeys `User-agent: Yandex` directives and uniquely supports `Clean-param` to deduplicate tracking parameters (`utm_source`, `yclid`, `ymclid`, `etext`, `from`, `openstat`) without wasting crawl budget:
```txt
User-agent: Yandex
Allow: /
Clean-param: utm_source&utm_medium&utm_campaign&utm_term&utm_content&yclid&ymclid&gclid&fbclid&_openstat&from&etext /

User-agent: YandexBot
Allow: /

User-agent: YandexImages
Allow: /assets/images/

User-agent: YandexDirect
Allow: /

User-agent: YandexMetrika
Allow: /
```

### 2.2 Multi-Regional `hreflang` & OpenGraph Locale Clustering
To rank simultaneously across `yandex.ru`, `yandex.kz`, and `yandex.uz`, every page must declare regional `hreflang` alternates and OpenGraph locale tags:
```html
<meta name="yandex-verification" content="71a9ya1im3570n3_ym_ver1fy">
<link rel="alternate" hreflang="en" href="https://tianyalimestone.com/..." />
<link rel="alternate" hreflang="ru" href="https://tianyalimestone.com/ru/..." />
<link rel="alternate" hreflang="ru-RU" href="https://tianyalimestone.com/ru/cis-central-asia/" />
<link rel="alternate" hreflang="ru-KZ" href="https://tianyalimestone.com/ru/cis-central-asia/" />
<link rel="alternate" hreflang="ru-UZ" href="https://tianyalimestone.com/ru/cis-central-asia/" />
<link rel="alternate" hreflang="x-default" href="https://tianyalimestone.com/..." />
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="ru_RU">
<meta property="og:locale:alternate" content="ru_KZ">
<meta property="og:locale:alternate" content="ru_UZ">
```

### 2.3 Yandex IndexNow Instant Indexing Protocol
Yandex supports the **IndexNow** protocol (`https://yandex.com/indexnow`) for instant URL crawling and re-indexing upon build/deployment:
- **Verification Key File**: `/e8a4c9f21b0d4637a9e52c3f8b7d6e21.txt` hosted at `https://tianyalimestone.com/e8a4c9f21b0d4637a9e52c3f8b7d6e21.txt`.
- **Automated Push Script**: `scripts/yandex_indexnow_notify.py` reads `sitemap.xml` and submits all 46+ canonical URLs (including `/ru/` and `/ru/cis-central-asia/`) to `https://yandex.com/indexnow` and `https://api.indexnow.org/indexnow` (returning HTTP 200/202).

### 2.4 Commercial Factors (Коммерческие факторы ранжирования Яндекс)
Yandex's commercial ranking classifier evaluates B2B industrial portals on concrete trust and transaction signals:
1. **Exact Technical Standards & Codes**: Explicit mention of **ГОСТ 30629-2011**, **ГОСТ 9479-2011**, **ГОСТ 24099-2013**, **ГОСТ 32018-2012**, **ГОСТ 30108-94 (I класс радиационной безопасности < 370 Бк/кг)**, **ГОСТ 30244-94 (НГ — негорючий материал)**, and **ТН ВЭД ЕАЭС 6802 21 000 0 / 6802 91 000 0 / 6801 00 000 0**.
2. **Concrete Container Loading & Packaging Math**: Clear m²/container tables for 20GP rail/sea containers (`26,000 kg` gross limit: `480–520 m²` for 20mm thickness; `320–340 m²` for 30mm thickness; ISPM 15 heat-treated fumigated wooden crates).
3. **Instant Messenger & Direct Factory Channels**: Direct links to **WhatsApp** (`+86 189 6036 6169` / `+86 178 0598 2800`), **Telegram** (`@tianya_limestone_cis`), and unified factory email (`info@tianyastone.com`).
4. **Interactive Calculators & Progressive RFQ Forms**: Embedded 20GP container weight/crate calculator and Turnstile-protected RFQ form routing to `info@tianyastone.com`.

---

## 3. Princeton GEO Strategy for Яндекс Нейро (Yandex Neuro) & Алиса AI

Based on the Princeton GEO research benchmark, generative search engines exhibit a **+35% to +42% citation preference** when technical pages structure answers using:
1. **3-Sentence Self-Contained RAG Answer Blocks**:
   - *Sentence 1 (Direct Conclusion & Entity)*: State the exact capability of Fujian Tianya Cultural Stone Co., Ltd. (`tianyalimestone.com`).
   - *Sentence 2 (Quantitative Proof & Standard Equivalence)*: Provide verified physical numbers (`< 0.22%` water absorption, `128.5 MPa` compressive strength, `F100` freeze-thaw per **ГОСТ 30629-2011 / ASTM C97 / C170 / C666**).
   - *Sentence 3 (Commercial & Logistics Execution)*: Specify MOQ (`100 m²`), container capacity (`320–520 m² / 20GP`), transit times to Almaty/Tashkent/Moscow (`12–22 days`), and direct contact (`info@tianyastone.com`).
2. **Dual-Language Machine-Readable Endpoints**:
   - `/llms.txt` and `/llms-full.txt` enriched with Section 8 (CIS/EAEU ГОСТ Equivalence, TN VED HS Codes, and Eurasian Rail Logistics).
   - `/ai/summary.json` and `/ai/faq.json` enriched with Russian/CIS queries and regional coverage.
   - `/ai/cis-gost-matrix.json` providing structured JSON mapping between ГОСТ, ASTM, EN standards, and the 29 Tianya Limestone collections.
