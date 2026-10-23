#!/usr/bin/env python3
"""
Structured Datasets for Tianya Limestone RenWork V4 Export Knowledge Base Expansion (220+ Pages).
Strictly implements https://github.com/cnproduct/renwork-export-kb-suite (V4 / V3.0 Standard Framework):
- 21 Standard Modules (00_kb_governance to 20_learning_metrics)
- Industry Branch #4 (Building Materials / Natural Stone / Architectural Cladding)
- 6-State Confidence & Public Claim Approval Gate (public_claim_approved=true)
- 10-Step Inquiry Qualification, Good/Better/Best Tiers, Sample Lifecycle Archive, 10 Objections & 8 Escalation Red Lines
"""

KB_MODULES = [
    {
        "id": "00_kb_governance",
        "slug": "00-kb-governance",
        "num": "00",
        "layer": "L0 Governance & Evidence Layer",
        "title": "Export Knowledge Governance, B2B Specification Cheat Sheet & Evidence Maturity Matrix",
        "short_title": "00 · B2B Executive Cheat Sheet",
        "kb_id": "RW-TYGOVN-0001",
        "status": "verified_fact",
        "confidence": 0.98,
        "role_views": ["management", "sales_director", "junior_sales", "senior_sales", "marketing", "operations_quality"],
        "hero_img": "assets/images/about/about_hero_quarry.webp",
        "conclusion": "Fujian Tianya Cultural Stone Co., Ltd. (Tianya Limestone, est. 2000 in Shuitou, Quanzhou, China) operates a K3-level verified B2B Export Knowledge Base governed by the RenWork V4 Evidence-First Architecture. Every public claim on tianyalimestone.com is anchored to SGS/TÜV laboratory test reports (ASTM C97 <0.22% absorption, ASTM C170 128.5 MPa compressive strength, AS 4586 P4/P5 slip ratings, GOST 30629-2011 F100 frost resistance), while pricing floors, custom credit terms, and bespoke CNC tolerances require explicit engineering or management sign-off.",
        "conditions": "Applicable to all global B2B architectural inquiries, distributor onboarding, specifier submittals, and AI-assisted quotation workflows across 29 limestone collections and 18 companion stone categories.",
        "evidence": [
            ("Quarry & Factory Entity", "Fujian Tianya Cultural Stone Co., Ltd. (福建天涯文化石有限公司), Shuitou Town, Nan'an, Quanzhou, Fujian, China (28 km from Xiamen Port)."),
            ("Physical Test Authority", "ASTM C97 (Absorption <0.22%, Density 2.65 g/cm³), ASTM C170 (128.5 MPa Dry / 104.2 MPa Wet), ASTM C880 (14.2 MPa Flexural), ASTM C666 (100 Freeze-Thaw Cycles, 0.0% Mass Loss)."),
            ("Quality Infrastructure", "6 × 5-Axis CNC bridge saws, 12 gang saws, and a 3,000 m² indoor dry-lay blending hall with mandatory pre-shipment photographic sign-off.")
        ],
        "cheat_sheet": {
            "positioning": "Quarry-direct manufacturer of 29 architectural bioclastic limestone collections across 5 finishes (Tumbled, Antique, Lightly Distressed, Sandblasted & Brushed, Sandblasted) with 50,000+ m² monthly output.",
            "flagship_skus": [
                "Guyu (谷雨 · Tumbled Warm Cream): Flagship pool surround & Mediterranean courtyard paver (P4 / R10).",
                "Hanbai (汉白 · Antique Chalk Ivory): Heritage castle-worn pillowed edge stone for French provincial estates.",
                "Ningzhi (凝脂 · Lightly Distressed Crema): Large-format indoor-outdoor villa slab with minimal edge distress.",
                "Daiwa (黛瓦 · Sandblasted & Brushed Charcoal): Velvet-touch P5 / R11 wet-zone infinity pool coping & deck stone.",
                "Canghai (沧海 · Sandblasted Wave Grey): Heavy-duty P5 / R11-R12 commercial plaza & ramp stone."
            ],
            "mandatory_5_questions": [
                "1. Project Location & Climate Zone (Freeze-thaw cycles, coastal salt spray, or high-UV desert exposure?)",
                "2. Application & Structural Load (Pedestrian patio 20–30mm, saltwater pool coping, or vehicular driveway 40–50mm?)",
                "3. Target Surface Area (m²), Format (600×400mm, French Pattern, or custom CNC cut-to-size) & Edge Profile?",
                "4. Destination Port / Delivery Terms (FOB Xiamen, CIF Port, or Eurasian Rail to Almaty/Moscow/Tashkent)?",
                "5. Target Construction Schedule & Physical Sample Kit Delivery Address?"
            ],
            "eight_red_lines": [
                "Red Line 1: Never quote below authorized factory floor pricing without Sales Director approval.",
                "Red Line 2: Never promise Open Account (OA) or D/P deferred credit without Finance & Executive written approval.",
                "Red Line 3: Never initiate mass custom CNC production before written customer sign-off on Sample Archive ID (SMP-) and CAD shop drawings.",
                "Red Line 4: Never claim unheld local municipal certifications; state 'Available / Test-Supported / Pending Project Submittal' accurately.",
                "Red Line 5: Never alter corporate beneficiary bank account details via email without dual-channel video/telephone verification.",
                "Red Line 6: Never commit to free custom CNC tooling or oversized slab sampling for unverified leads.",
                "Red Line 7: Never grant regional or national exclusivity without a signed annual container volume KPI agreement.",
                "Red Line 8: Never issue unilateral financial compensation commitments on P1 transit or installation incidents before joint QC investigation."
            ]
        },
        "faq": [
            ("How does Tianya Limestone separate verified quarry facts from project estimates?",
             "All physical test parameters (ASTM C97, C170, C880, C666, EN 1341/1469, AS 4586, GOST 30629-2011) and standard container loading metrics are Verified Quarry Facts. Freight rates, landed duties, and custom CNC fabrication lead times are provided as indicative estimates until confirmed by a formal Proforma Invoice (PI)."),
            ("What are the 6 role-based views in the Tianya Export Knowledge Base?",
             "Our knowledge base organizes technical and commercial data for: (1) Landscape Architects & Specifiers, (2) Stone Importers & Wholesalers, (3) Commercial EPC Contractors, (4) Luxury Villa Developers, (5) Quality & Inspection Engineers, and (6) Logistics & Customs Brokers.")
        ]
    },
    {
        "id": "01_sources_permissions",
        "slug": "01-sources-terminology",
        "num": "01",
        "layer": "L0 Governance & Evidence Layer",
        "title": "Architectural Limestone Terminology Dictionary, Bilingual Stone Glossary & Evidence Registry",
        "short_title": "01 · Stone Terminology Dictionary",
        "kb_id": "RW-TYTERM-0002",
        "status": "verified_fact",
        "confidence": 0.99,
        "role_views": ["junior_sales", "senior_sales", "marketing", "operations_quality"],
        "hero_img": "assets/images/compliance/lab_testing.webp",
        "conclusion": "Standardized terminology eliminates costly specification errors between architects, stone fabricators, and customs authorities. Module 01 defines 40+ essential petrographic, surface-processing, installation, and international trade terms used across Tianya Limestone's technical submittals.",
        "conditions": "Use this standardized bilingual glossary across all CAD drawings, CSI 04 43 00 specifications, Proforma Invoices, and customs HS code declarations.",
        "evidence": [
            ("Petrographic Classification", "Bioclastic Calcite Limestone (CaCO3 > 94%) with compacted marine micro-fossils and sparry calcite cementation."),
            ("International Standards", "Cross-referenced with ASTM C119 (Standard Terminology Relating to Dimension Stone), EN 12670 (Natural Stone Terminology), and GOST 30629-2011."),
            ("Trade & Logistics", "Aligned with Incoterms 2020, WCO Harmonized System Chapter 68 (6802.21 / 6802.91 / 6801.00), and ISPM-15 phytosanitary standards.")
        ],
        "glossary_table": [
            ("Bioclastic Limestone (生物碎屑石灰石)", "Dense sedimentary carbonate rock formed from compacted marine shell fragments and crystalline calcite, yielding <0.22% water absorption.", "All 29 Collections"),
            ("Tumbled Finish (滚磨仿古面)", "Mechanical rotary drum tumbling with abrasive media and water to create softened, pillowed edges and a weathered matte surface (P4 / R10).", "Guyu, Zaojing, Fengya, Shanshui, Qimeng, Xuansu, Yexiang, Baihe"),
            ("Antique Hand-Dressed (手工凿毛古建面)", "Artisanal hand-chiseling of paver arrises combined with chemical/brush distressing to replicate centuries-old European flagstone.", "Hanbai, Lanting, Guyun, Xieshan, Dougong, Heting, Zhuozheng, Baichuan, Cangbi, Canglang"),
            ("Lightly Distressed (微仿古柔光面)", "Precision-sawn flat slab with micro-softened edges and velvet honed texture for contemporary indoor-outdoor minimalism.", "Ningzhi, Qinghe, Feiyan, Xiangye, Yuebai, Chenglu"),
            ("Sandblasted & Brushed (喷砂加刷荔枝柔面)", "High-pressure silica-free abrasive blasting followed by diamond rotary brushing for P5/R11 wet slip grip and barefoot comfort.", "Daiwa, Wangchuan"),
            ("Sandblasted High-Grip (高防滑喷砂面)", "Uniform micro-granular textured surface delivering maximum wet pendulum traction (SRV > 54, P5 / R11-R12).", "Xuanzhen, Sunmao, Canghai"),
            ("Drop-Face / Rebated Coping (L型挂边泳池压顶石)", "Monolithic or CNC-mitred L-profile pool coping (e.g., 600×400×20/60mm) that conceals the concrete pool beam.", "Pool Surrounds & Steps"),
            ("French Pattern / Opus Romain (法式四件套模数拼花)", "Interlocking 4-size repeating ashlar module (600×400, 400×400, 400×200, 200×200mm = 0.72m² or 1.44m² per set).", "Courtyards & Terraces"),
            ("3,000 m² Dry-Lay Blending (三千平工厂预排版)", "Pre-shipment factory floor layout where crates are blended across quarry benches and photographed for architect approval.", "All Project Orders"),
            ("Efflorescence (返碱/白华)", "Crystalline salt deposit carried to the stone surface by capillary moisture from unsealed cement beds; prevented via C2S1 white adhesive and impregnating sealers.", "Installation QC")
        ],
        "faq": [
            ("Why is accurate HS code terminology critical on commercial invoices?",
             "Using the exact tariff description (e.g., HS 6802.21 / 6802.91 for worked monumental/building limestone vs. HS 6801.00 for flagstones and setts) prevents customs classification delays and ensures correct application of preferential FTA duty rates such as ChAFTA (0% in Australia) or Form E (ASEAN)."),
            ("What is the difference between a penetrating sealer and a topical sealer?",
             "A penetrating (impregnating) silane/siloxane or fluoropolymer sealer chemically bonds inside the stone's capillary pores without blocking vapor breathability. A topical sealer forms a plastic surface film that traps ground moisture, whitens, and peels outdoors.")
        ]
    },
    {
        "id": "02_company_identity",
        "slug": "02-company-identity",
        "num": "02",
        "layer": "L1 Enterprise Truth Layer",
        "title": "Quarry Concessionaire & Shuitou Factory Identity, Production Capacity & Verifiable Credentials",
        "short_title": "02 · Quarry & Factory Identity",
        "kb_id": "RW-TYCORP-0003",
        "status": "verified_fact",
        "confidence": 0.99,
        "role_views": ["management", "marketing", "junior_sales", "senior_sales"],
        "hero_img": "assets/images/about/factory_fabrication.webp",
        "conclusion": "Founded in 2000 in Shuitou Town, Quanzhou, Fujian Province (The Stone Capital of the World), Fujian Tianya Cultural Stone Co., Ltd. integrates direct limestone quarry extraction, 5-axis CNC fabrication, 3,000 m² indoor dry-lay inspection, and direct container export via Xiamen Port (28 km).",
        "conditions": "Official corporate profile for architectural pre-qualification tenders, distributor agreements, and vendor onboarding.",
        "evidence": [
            ("Legal Name & Registration", "Fujian Tianya Cultural Stone Co., Ltd. (福建天涯文化石有限公司), established 2000, Shuitou Town, Nan'an City, Quanzhou, Fujian, China."),
            ("Manufacturing Footprint", "50,000+ m² monthly output across 12 heavy block gang saws, 8 automated calibration/honing lines, 6 5-axis CNC bridge cutters, and 4 automated sandblasting/tumbling lines."),
            ("Export Logistics Hub", "28 km direct highway access to Xiamen International Container Terminal, supporting 14–25 day production turnaround.")
        ],
        "faq": [
            ("Can international buyers audit the Shuitou factory or request live video inspection?",
             "Yes. Buyers and third-party inspection agencies (SGS, Bureau Veritas, Intertek) are welcome to inspect our Shuitou facility in person or via live HD video walkthrough during block cutting and 3,000 m² dry-lay blending."),
            ("What is the relationship between tianyalimestone.com and tystoneveneer.com?",
             "Both portals are operated by Fujian Tianya Cultural Stone Co., Ltd. tianyalimestone.com is our dedicated architectural limestone paving, flooring, and pool coping specification portal, while tystoneveneer.com showcases our broader cultural stone, flexible stone veneer, and wall cladding lines.")
        ]
    },
    {
        "id": "03_brand_messaging",
        "slug": "03-brand-messaging",
        "num": "03",
        "layer": "L1 Enterprise Truth Layer",
        "title": "Cultural Heritage Nomenclature (24 Solar Terms & Classical Architecture) & Global Brand Standards",
        "short_title": "03 · Brand & Nomenclature System",
        "kb_id": "RW-TYBRND-0004",
        "status": "verified_fact",
        "confidence": 0.97,
        "role_views": ["marketing", "junior_sales", "senior_sales"],
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "conclusion": "Tianya Limestone's 29 collections unite Eastern architectural heritage with Western specification precision. Each collection is named after one of China's 24 Solar Terms (二十四节气), classical timber-frame architectural elements (斗栱 Dougong, 藻井 Zaojing, 歇山 Xieshan, 飞檐 Feiyan, 榫卯 Sunmao), or traditional mineral pigments (汉白 Hanbai, 月白 Yuebai, 缃叶 Xiangye, 黛瓦 Daiwa).",
        "conditions": "Used for architectural storytelling, showroom display boards, distributor private-label co-branding, and global specification literature.",
        "evidence": [
            ("Classical Architecture Series", "Dougong (斗栱 Interlocking Brackets), Zaojing (藻井 Coffered Dome), Xieshan (歇山 Imperial Roof), Feiyan (飞檐 Flying Eaves), Sunmao (榫卯 Mortise & Tenon)."),
            ("Solar Terms & Scholarly Landscapes", "Guyu (谷雨 Grain Rain), Lanting (兰亭 Orchid Pavilion), Zhuozheng (拙政 Humble Administrator's Garden), Wangchuan (辋川 River Villa), Shanshui (山水 Mountain & Water)."),
            ("Traditional Mineral & Poetic Tones", "Hanbai (汉白 Alabaster White), Ningzhi (凝脂 Creamy Jade), Yuebai (月白 Moonlit Dove Grey), Xiangye (缃叶 Autumn Mulberry Ochre), Daiwa (黛瓦 Ink Roof Tile).")
        ],
        "faq": [
            ("Can distributors use their own private-label collection names on crate markings?",
             "Yes. Under our OEM/ODM distributor program, crates, sample boards, and packing lists can carry your custom collection names alongside Tianya batch traceability codes."),
            ("Why do architects appreciate the cultural dual-track naming system?",
             "Each name encodes both the tactile visual character of the stone (e.g., Hanbai for soft chalk white, Daiwa for charcoal roof-tile grey) and an authentic architectural story for luxury residential and hospitality clients.")
        ]
    },
    {
        "id": "04_product_catalog",
        "slug": "04-product-taxonomy",
        "num": "04",
        "layer": "L1 Enterprise Truth Layer",
        "title": "3-Tier Product Architecture: Core Limestone Pavers, Companion Cladding & Custom CNC Opportunity Pool",
        "short_title": "04 · Product Taxonomy & Portfolio",
        "kb_id": "RW-TYPROD-0005",
        "status": "verified_fact",
        "confidence": 0.98,
        "role_views": ["junior_sales", "senior_sales", "marketing", "operations_quality"],
        "hero_img": "assets/images/categories/mixed_container_loading.webp",
        "conclusion": "In accordance with RenWork Module 04, Tianya's portfolio is strictly partitioned into (1) Verified Core Running Lines (29 Limestone Collections + 6 Companion Stone Lines), (2) Capability-Extended Custom CNC Profiles (Bullnose/Drop-Face Coping, Slotted Drain Grates, Mitred Treads, Kerfed Facade Slabs), and (3) Controlled Opportunity Pool items requiring project-specific engineering validation.",
        "conditions": "Prevents sales or specifiers from confusing standard running-line MOQs (100 m²) with custom 5-axis CNC architectural elements.",
        "evidence": [
            ("Tier 1 Traffic-Driver Running Lines", "Standard 600×400mm, 600×600mm, and French Pattern sets in 15mm, 20mm, and 30mm thicknesses across Guyu, Hanbai, Lanting, Ningzhi, Qinghe, and Daiwa."),
            ("Tier 2 Margin & Project Value Lines", "Matching 30mm–50mm Bullnose & Rebated Drop-Face Pool Copings, Step Treads, Cobblestones on Mesh, and Split-Face Ashlar Walling."),
            ("Tier 3 Bespoke CNC & Companion Lines", "5-Axis CNC Fluted Wall Panels, Slotted Stone Trench Grates, Ultra-Thin 1.5–2.0mm Flexible Stone Veneer, and MCM Class-A Fireproof Panels.")
        ],
        "faq": [
            ("Can we mix multiple limestone finishes and companion stone products in a single 20GP container?",
             "Yes. Our Mixed-Container Consolidation Program allows importers and project contractors to combine up to 3–4 stone collections (e.g., 30mm pool pavers + drop-face coping + flexible stone veneer) within one 26-ton 20GP container."),
            ("What is the minimum order quantity for custom CNC profiles?",
             "When ordered alongside field pavers, custom pool copings and stair treads have no separate container MOQ (minimum 30 linear meters per profile).")
        ]
    },
    {
        "id": "05_manufacturing_quality",
        "slug": "05-manufacturing-quality",
        "num": "05",
        "layer": "L1 Enterprise Truth Layer",
        "title": "5-Axis CNC Fabrication, 3,000 m² Dry-Lay Blending, AQL Inspection Nodes & Batch Traceability SOP",
        "short_title": "05 · Manufacturing & Dry-Lay QC",
        "kb_id": "RW-TYMFGQ-0006",
        "status": "verified_fact",
        "confidence": 0.99,
        "role_views": ["operations_quality", "senior_sales", "management"],
        "hero_img": "assets/images/compliance/quality_inspection.webp",
        "conclusion": "Natural limestone is a geological material with inherent vein and fossil movement. Tianya eliminates job-site shade shock through a mandatory 6-Stage Quality Control Gate culminating in a 3,000 m² indoor dry-lay pre-blending inspection where tiles from multiple blocks are mixed, numbered, and photographed before crating.",
        "conditions": "Mandatory QC protocol for all architectural project orders and full-container distributor shipments.",
        "evidence": [
            ("Dimensional Calibration", "Infrared bridge saws and multi-head diamond calibrators hold thickness tolerance to ±1.0 mm (15–20mm tiles) and ±1.5 mm (30–50mm pavers), exceeding EN 1341 Class T2."),
            ("Moisture & Efflorescence Control", "Kiln/air-cured below 1.5% residual moisture prior to optional factory 6-sided pre-sealing and polyethylene-lined crating."),
            ("Batch Traceability", "Every crate bears a unique QR/barcode linking back to the quarry bench, gang-saw block number, CNC operator, and dry-lay inspection photo set.")
        ],
        "faq": [
            ("How does pre-shipment dry-lay blending save installation labor on site?",
             "By pre-blending tonal variations across crates in our 3,000 m² hall, installers can pull directly from sequential crates without sorting hundreds of heavy slabs on a cramped job site, reducing laying time by 20–30%."),
            ("What happens if a slab fails dimensional or visual AQL inspection during dry-lay?",
             "Any slab exhibiting structural micro-fissures, corner spalls >2mm, or out-of-range calcite blotches is rejected on the factory floor and replaced from the same quarry block before crating.")
        ]
    },
    {
        "id": "06_certification_compliance",
        "slug": "06-certification-compliance",
        "num": "06",
        "layer": "L1 Enterprise Truth Layer",
        "title": "Product × Market × Certification Matrix: ASTM C97/C170/C880/C666, EN 1341/1469 CE, AS 4586 & GOST 30629",
        "short_title": "06 · Global Compliance Matrix",
        "kb_id": "RW-TYCERT-0007",
        "status": "verified_fact",
        "confidence": 0.99,
        "role_views": ["marketing", "senior_sales", "operations_quality", "management"],
        "hero_img": "assets/images/compliance/lab_testing.webp",
        "conclusion": "Architectural stone specification requires region-specific regulatory compliance. Module 06 maps Tianya Limestone's verified laboratory test data across North American (ASTM), European/UK (CE/UKCA EN 1341 & EN 1469), Australian/NZ (AS 4586 & AS/NZS 4456), and Eurasian EAEU (GOST 30629-2011 & GOST 30108-94) standards.",
        "conditions": "Used for architectural tender submittals, municipal code approvals, and customs import clearance.",
        "evidence": [
            ("North America (USA & Canada)", "ASTM C97 (Absorption <0.22%, Density 2.65 g/cm³), ASTM C170 (128.5 MPa Dry Compressive), ASTM C880 (14.2 MPa Flexural), ASTM C666 (100 Freeze-Thaw Cycles), ASTM E84 Class A Flame Spread."),
            ("Australia & New Zealand", "AS 4586:2013 Wet Pendulum Slip Resistance: P5 (Sandblasted / Sandblasted & Brushed, SRV 56–62) and P4 (Tumbled / Antique, SRV 44–49); AS 4456.10 Salt Attack Resistance."),
            ("European Union, UK & CIS/EAEU", "CE Declaration of Performance per EN 1341 (Exterior Paving) & EN 1469 (Facade Slabs); EN 13501-1 Class A1 Non-Combustible; GOST 30629-2011 F100 Frost Grade & GOST 30108-94 Class I Radiation Safety (<45 Bq/kg).")
        ],
        "faq": [
            ("Which finish is legally required for commercial swimming pool surrounds in Australia?",
             "Under the National Construction Code (NCC) and HB 198 / AS 4586, wet barefoot pool surrounds and ramps require a minimum P4 or P5 wet pendulum rating. Our Sandblasted and Sandblasted & Brushed finishes achieve P5, while Tumbled and Antique achieve P4."),
            ("Do you provide ISPM-15 fumigation certificates for timber crates?",
             "Yes. Every export shipment includes official IPPC ISPM-15 heat-treatment/fumigation stamping and phytosanitary documentation required by Australian DAFF, US CBP, EU, and New Zealand MPI biosecurity.")
        ]
    },
    {
        "id": "07_commercial_delivery",
        "slug": "07-commercial-delivery",
        "num": "07",
        "layer": "L1 Enterprise Truth Layer",
        "title": "Commercial Trade Policy, MOQ Tiers, Quotation Variables, Incoterms & Wire-Transfer Security Protocol",
        "short_title": "07 · Commercial & Delivery Policy",
        "kb_id": "RW-TYCOMM-0008",
        "status": "verified_fact",
        "confidence": 0.96,
        "role_views": ["sales_director", "senior_sales", "junior_sales", "operations_quality", "management"],
        "hero_img": "assets/images/about/export_crates_logistics.webp",
        "conclusion": "Transparent commercial rules protect both international buyers and factory production schedules. Module 07 defines Tianya Limestone's standard MOQ tiers (100 m² trial / 1×20GP container optimal), the 6 variables governing stone pricing, Incoterms 2020 responsibility boundaries, and our mandatory multi-channel anti-fraud wire verification rule.",
        "conditions": "Applies to all formal quotations, Proforma Invoices (PI), and international container shipments.",
        "evidence": [
            ("MOQ & Container Economics", "Trial MOQ: 100 m² (LCL or mixed load). Optimal unit cost: 1×20GP FCL (26,000 kg payload = 480–520 m² of 20mm tiles or 320–340 m² of 30mm pavers)."),
            ("Quotation Variables", "Unit price is governed by: (1) Stone Collection & Block Yield, (2) Surface Finish, (3) Thickness (15/20/30/40/50mm), (4) Format/Cut-to-Size Waste Ratio, (5) Edge Profiling/CNC Work, and (6) Incoterm & Currency (USD, EUR, AUD, CNY, RUB)."),
            ("Wire-Transfer Security Red Line", "Tianya Limestone NEVER changes beneficiary bank account details via email alone. Any bank change notice must be treated as potential cyber-fraud and verified via live video call with our General Manager.")
        ],
        "faq": [
            ("What are the standard payment terms for international container orders?",
             "Standard terms are 30% T/T deposit upon Proforma Invoice and CAD drawing sign-off, with the 70% balance payable against copy of the Bill of Lading (B/L) and pre-shipment dry-lay inspection report. Irrevocable L/C at sight is available for multi-container project contracts."),
            ("How long is a formal factory quotation valid?",
             "FOB Xiamen stone quotations are valid for 30 calendar days. Ocean and rail freight components on CIF/CFR quotes are valid for 14 days due to carrier bunker adjustment fluctuations.")
        ]
    },
    {
        "id": "08_market_intelligence",
        "slug": "08-market-intelligence",
        "num": "08",
        "layer": "L2 Market Decision Layer",
        "title": "Global Architectural Limestone Market Intelligence & Supplier-Side Annual Procurement Calendar",
        "short_title": "08 · Market Intelligence & Calendar",
        "kb_id": "RW-TYMKTI-0009",
        "status": "strategy_recommendation",
        "confidence": 0.94,
        "role_views": ["management", "sales_director", "marketing", "senior_sales"],
        "hero_img": "assets/images/contact/xiamen_port_logistics.webp",
        "conclusion": "Outdoor paving and facade stone procurement is highly seasonal, driven by Northern and Southern Hemisphere construction windows. Module 08 maps the 60-to-90-day lead-time offset between factory block cutting in Shuitou and peak installation months across Australia, North America, Europe, the Middle East, and CIS.",
        "conditions": "Used by importers, stocking distributors, and project managers to lock in quarry block allocation and avoid peak-season shipping bottlenecks.",
        "evidence": [
            ("Northern Hemisphere (US, UK, EU, Canada, CIS)", "Peak site installation: April–September. Optimal factory order & CAD sign-off window: December–March (ahead of spring thaw)."),
            ("Southern Hemisphere (Australia, NZ, South Africa)", "Peak summer pool & patio completion: October–February. Optimal factory order window: June–September."),
            ("GCC & Middle East (UAE, Saudi Arabia, Qatar)", "Peak outdoor construction & hospitality handover: October–April (cooler winter season). Optimal factory order window: July–November.")
        ],
        "faq": [
            ("How far in advance should a landscape contractor order custom limestone for a spring pool project?",
             "Allow 2–3 weeks for sample evaluation and CAD sign-off, 3 weeks for CNC fabrication and dry-lay blending, and 2–5 weeks for ocean transit and customs clearance — totaling 7–11 weeks before on-site laying."),
            ("Does quarry block extraction slow down during Chinese New Year?",
             "Yes. Quarry bench extraction and gang-saw schedules pause for 2–3 weeks during late January/February. Importers needing March/April site delivery should confirm orders by early December.")
        ]
    },
    {
        "id": "09_icp_buyer_personas",
        "slug": "09-icp-buyer-personas",
        "num": "09",
        "layer": "L2 Market Decision Layer",
        "title": "B2B Buyer Personas & Specifier Decision Committee Guide: Architects, Importers, EPC Contractors & Developers",
        "short_title": "09 · Buyer Personas & Specifiers",
        "kb_id": "RW-TYICPB-0010",
        "status": "strategy_recommendation",
        "confidence": 0.95,
        "role_views": ["marketing", "senior_sales", "junior_sales", "sales_director"],
        "hero_img": "assets/images/hero/scene-living.webp",
        "conclusion": "Architectural stone purchasing involves a multi-stakeholder Buying Committee. A landscape architect cares about tactile finish, slip compliance, and seamless indoor-outdoor transitions; a stone wholesaler cares about crate yield, shade consistency, and margin protection; an EPC contractor cares about dimensional tolerance and on-time sequential delivery.",
        "conditions": "Guides tailored technical submittals and commercial proposals for our 4 primary B2B buyer archetypes.",
        "evidence": [
            ("Archetype A+ · National Stone Importers & Showroom Distributors", "Annual volume: 10–50+ containers/year. Key priorities: Exclusive regional naming, 20GP weight optimization, zero shade claims, fast sample replenishment."),
            ("Archetype A · Landscape Architects & Design Studios", "Key priorities: AS 4586 P4/P5 & ASTM test certificates, BIM/CAD hatch files, physical control sample kits, matching indoor-outdoor finishes."),
            ("Archetype A · Commercial Hospitality & Luxury Villa EPC Contractors", "Project volume: 500–8,000 m². Key priorities: Cut-to-size CNC accuracy (±1mm), 3,000 m² dry-lay numbering, phased container shipping, <0.5% transit breakage.")
        ],
        "faq": [
            ("What documentation package does a Principal Landscape Architect need to specify Tianya Limestone?",
             "Architects receive our 4-part Specifier Kit: (1) Physical 150×150mm stone swatch box, (2) Product Technical Data Sheet (TDS) with ASTM/EN/AS 4586 lab data, (3) Copy-ready CSI 04 43 00 / 32 14 40 3-Part Specification text, and (4) 2D CAD hatch patterns."),
            ("How do you support stone distributors who operate retail showrooms?",
             "We supply custom-labeled architectural sample boards, high-resolution unwatermarked room-scene photography, and guaranteed quarry bench reservation for repeat stocking orders.")
        ]
    },
    {
        "id": "10_buyer_intent_signals",
        "slug": "10-project-readiness-signals",
        "num": "10",
        "layer": "L2 Market Decision Layer",
        "title": "Architectural Project Readiness Signals, Submittal Timelines & Lead-Time Planning Matrix",
        "short_title": "10 · Project Readiness & Timelines",
        "kb_id": "RW-TYSIGN-0011",
        "status": "strategy_recommendation",
        "confidence": 0.93,
        "role_views": ["senior_sales", "sales_director", "operations_quality"],
        "hero_img": "assets/images/resources/cad_blueprints.webp",
        "conclusion": "Matching engineering support to the exact project stage prevents wasted time and accelerates specification lock-in. Module 10 maps the 4 project readiness stages — Concept Design, Tender & Value Engineering, Submittal & Sample Sign-Off, and Container Dispatch — to concrete engineering deliverables.",
        "conditions": "Used by project developers and Tianya engineering sales to synchronize sample dispatch, CAD take-offs, and quarry block reservation.",
        "evidence": [
            ("Stage 1 · Concept & Moodboard (6–12 Months Out)", "Deliverable: Digital high-res swatch library, SRI thermal data, and preliminary 5-piece finish sample box."),
            ("Stage 2 · Tender & Value Engineering (3–6 Months Out)", "Deliverable: Good/Better/Best thickness & format matrix, 1:1 European limestone replacement cost comparison, and 20GP container freight budget."),
            ("Stage 3 · Final Submittal & Pre-Production (6–10 Weeks Out)", "Deliverable: Signed Control Sample (SMP-ID), finalized CAD cut-to-size shop drawings, and 30% deposit block lock.")
        ],
        "faq": [
            ("What if our project is at the Value Engineering stage and over budget on European limestone?",
             "Send us your current stone schedule. Within 12 hours, our engineering team will map a 1:1 quarry-direct Tianya equivalent (matching density, tone, and finish) that typically reduces landed material cost by 35–55%."),
            ("Can you reserve raw blocks from the same quarry vein for a multi-phase project?",
             "Yes. Once the master project contract is confirmed, we quarry and tag raw blocks from the identical geological stratum to guarantee tonal continuity across Phase 1 and Phase 2 deliveries.")
        ]
    },
    {
        "id": "11_competitors_differentiation",
        "slug": "11-stone-comparative-differentiation",
        "num": "11",
        "layer": "L2 Market Decision Layer",
        "title": "Quarry-Direct Bioclastic Limestone vs. European Quarries, Travertine, Sandstone, Bluestone & Porcelain",
        "short_title": "11 · Stone Comparative Matrix",
        "kb_id": "RW-TYDIFF-0012",
        "status": "verified_fact",
        "confidence": 0.96,
        "role_views": ["senior_sales", "junior_sales", "marketing"],
        "hero_img": "assets/images/hero/scene-garden.webp",
        "conclusion": "Every paving and cladding material has physical trade-offs. Module 11 provides an objective, evidence-backed engineering comparison between Tianya high-density bioclastic limestone (<0.22% absorption, 128.5 MPa) and European quarries, porous travertine, quartz sandstone, basalt bluestone, and 20mm outdoor porcelain.",
        "conditions": "Used for value-engineering presentations and material selection workshops with architects and property owners.",
        "evidence": [
            ("vs. European Quarries (Burgundy / Moleanos / Jura)", "Matches or exceeds ASTM C97/C170 density while reducing FOB cost by 40–60% and cutting custom CNC lead time from 12+ weeks to 2–3 weeks."),
            ("vs. 20mm Outdoor Porcelain Tiles", "Natural limestone stays 8–12°C cooler underfoot in full sun, carries solid through-body color for bullnose/drop-face coping without glued mitre joints, and develops an authentic patina."),
            ("vs. Unfilled Travertine & High-Porosity Shell Stone", "Sub-0.22% absorption prevents freeze-thaw spalling and salt-crystal pitting without requiring resin filler patching.")
        ],
        "faq": [
            ("Why do many luxury projects switch from dark bluestone (basalt) to light-toned limestone around pools?",
             "Dark basalt absorbs intense solar radiation, reaching 55–65°C in summer sun and burning bare feet, whereas light cream and silver-grey limestone (Guyu, Hanbai, Qinghe, Yuebai) reflects solar heat and stays comfortable barefoot."),
            ("How does Tianya differ from third-party stone trading companies?",
             "Trading companies broker orders across fragmented small workshops without unified block selection or dry-lay space, leading to thickness variations and shade mismatch. Tianya controls the quarry block, 5-axis CNC sawing, and 3,000 m² dry-lay hall under one roof.")
        ]
    },
    {
        "id": "12_product_market_application_fit",
        "slug": "12-product-market-application-fit",
        "num": "12",
        "layer": "L2 Market Decision Layer",
        "title": "Master Product × Climate × Channel × Application Fit Matrix (All 29 Limestone Collections Mapped)",
        "short_title": "12 · Product × Market × Scene Fit",
        "kb_id": "RW-TYPMFM-0013",
        "status": "verified_fact",
        "confidence": 0.97,
        "role_views": ["senior_sales", "junior_sales", "marketing", "operations_quality"],
        "hero_img": "assets/images/hero/scene-facade.webp",
        "conclusion": "Module 12 serves as the central decision matrix connecting all 29 Tianya Limestone collections to their optimal climate zones, architectural applications, required thicknesses, and slip ratings.",
        "conditions": "Consult before selecting a finish or thickness for wet zones, freeze-thaw climates, or vehicular traffic.",
        "evidence": [
            ("Saltwater Pools & Coastal Wet Zones (AU, US Sunbelt, Mediterranean, UAE)", "Primary recommendation: Sandblasted & Brushed (Daiwa, Wangchuan) and Sandblasted (Xuanzhen, Sunmao, Canghai) for P5/R11 grip, or Tumbled (Guyu, Fengya, Shanshui) for P4/R10 courtyard surrounds in 30mm thickness."),
            ("Severe Freeze-Thaw & Alpine Climates (Canada, Northern US, UK, Germany, Russia/Kazakhstan)", "Primary recommendation: High-density 30mm–50mm pavers and ventilated facade slabs (ASTM C666 100 cycles / GOST F100) installed on drained mortar beds or mechanical kerf anchors."),
            ("Seamless Indoor-Outdoor Modern Villas", "Primary recommendation: Lightly Distressed 20mm interior slabs (Ningzhi, Qinghe, Yuebai) paired with matching 30mm Tumbled or Sandblasted exterior patio pavers.")
        ],
        "faq": [
            ("Can the same limestone collection be produced in both Lightly Distressed (for indoors) and Sandblasted (for the pool deck)?",
             "Yes! Because we fabricate directly from raw quarry blocks in Shuitou, any of our limestone beds can be processed with a smooth Lightly Distressed finish for interior living rooms and a P5 Sandblasted or Tumbled finish for the adjoining outdoor pool terrace."),
            ("What minimum thickness is required for residential vs. commercial driveways?",
             "Residential passenger-car driveways require minimum 40mm (ideally 50mm) limestone pavers in smaller formats (e.g., 300×300mm, 400×200mm, or cobblestone setts) laid on a reinforced concrete slab.")
        ]
    },
    {
        "id": "13_lead_discovery",
        "slug": "13-supplier-verification-guide",
        "num": "13",
        "layer": "L3 Customer & Execution Layer",
        "title": "L1/L2/L3 Stone Supplier Due Diligence & Quarry Verification Checklist for International Buyers",
        "short_title": "13 · Buyer Due Diligence Guide",
        "kb_id": "RW-TYVRFY-0014",
        "status": "verified_fact",
        "confidence": 0.96,
        "role_views": ["senior_sales", "management", "operations_quality"],
        "hero_img": "assets/images/about/craftsman_stonemason.webp",
        "conclusion": "International stone buyers face significant risk when sourcing from unverified middlemen. Module 13 reverses the traditional L1/L2/L3 verification framework into a transparent Self-Audit Dossier so overseas buyers can verify Tianya Limestone's quarry ownership, lab reports, and production capacity in under 15 minutes.",
        "conditions": "Provided to procurement directors, quantity surveyors, and trade compliance teams during vendor qualification.",
        "evidence": [
            ("L1 Rapid Entity Verification (5 Min)", "Verify Unified Social Credit Code, Shuitou industrial address (24.6931° N, 118.4287° E), customs export registration, and ISO 9001:2015 certificate."),
            ("L2 Technical Capability Audit (20 Min)", "Verify SGS/TÜV test reports (ASTM C97/C170/C880/C666), 5-axis CNC equipment list, and sample kit batch consistency."),
            ("L3 Deep Project Due Diligence", "Live video inspection of raw block inventory, 3,000 m² dry-lay floor verification, and third-party pre-shipment SGS/BV loading supervision.")
        ],
        "faq": [
            ("How can a buyer verify that a Chinese stone supplier is a real factory and not a trading broker?",
             "Request a live video call walking from the raw block yard through the gang saws, 5-axis CNC bridge cutters, and indoor dry-lay hall, and verify that the factory's business license address is in an industrial stone zone like Shuitou Town rather than a downtown office tower."),
            ("Do you accept third-party inspection (SGS / Bureau Veritas / TUV) before balance payment?",
             "Yes, 100%. Third-party inspectors are welcome to verify dimensions, surface finish, moisture content, dry-lay blending, and container crate bracing prior to shipment.")
        ]
    },
    {
        "id": "14_customer_asset_lifecycle",
        "slug": "14-account-reorder-lifecycle",
        "num": "14",
        "layer": "L3 Customer & Execution Layer",
        "title": "Long-Term Distributor Stocking, Shade-Batch Continuity & Multi-Phase Project Reorder Lifecycle",
        "short_title": "14 · Distributor & Reorder Lifecycle",
        "kb_id": "RW-TYLIFE-0015",
        "status": "verified_fact",
        "confidence": 0.95,
        "role_views": ["sales_director", "senior_sales", "operations_quality"],
        "hero_img": "assets/images/categories/mixed_container_loading.webp",
        "conclusion": "For stone wholesalers and multi-phase real estate developers, the biggest post-purchase risk is reorder shade drift. Module 14 details how Tianya maintains Golden Master Account Records, sealed Reference Master Samples (SMP-ID), and quarry stratum logs so reorders 6 or 24 months later match the original shipment.",
        "conditions": "Applies to stocking distributors, retail stone showrooms, and multi-stage resort/residential developments.",
        "evidence": [
            ("Dual-Sample Retention Archive", "For every shipped order, one physical signed control sample is sealed in our Shuitou QC vault for 36 months alongside spectrophotometric L*a*b* color readings."),
            ("Quarry Vein & Bench Mapping", "Each account's historical orders are linked to specific quarry bench coordinates and tumbling/sandblasting media parameters."),
            ("Proactive Stock Replenishment Alerts", "Distributors receive seasonal lead-time alerts 90 days ahead of spring construction peaks and pre-Chinese New Year shipping cutoffs.")
        ],
        "faq": [
            ("How do you ensure a distributor's 5th container of Guyu Tumbled matches their 1st container?",
             "Before cutting any reorder, our QC engineer retrieves your physical Master Control Sample from our archive, selects raw blocks from the matching quarry bench, and lays new production tiles directly beside the retained master sample under standardized D65 daylight lamps."),
            ("Can we set up a rolling quarterly container schedule with locked FOB pricing?",
             "Yes. Stocking distributors ordering 4+ containers annually can establish a 6-to-12-month frame agreement with reserved block inventory and stabilized FOB Xiamen pricing.")
        ]
    },
    {
        "id": "15_inquiry_qualification",
        "slug": "15-inquiry-qualification-sop",
        "num": "15",
        "layer": "L3 Customer & Execution Layer",
        "title": "10-Step Architectural Stone Inquiry Qualification & L1/L2/L3 Technical Discovery Protocol",
        "short_title": "15 · 10-Step Inquiry SOP",
        "kb_id": "RW-TYINQR-0016",
        "status": "verified_fact",
        "confidence": 0.98,
        "role_views": ["junior_sales", "senior_sales", "sales_director"],
        "hero_img": "assets/images/contact/sample_kit_box.webp",
        "conclusion": "Implements the RenWork V4 10-Step Inquiry Diagnostic Checklist and L1/L2/L3 Three-Layer Technical Discovery Method. Instead of overwhelming buyers with a 20-question form, our engineering desk focuses first on the 2–3 critical technical parameters that govern structural safety, slip compliance, and landed container cost.",
        "conditions": "Standard operating procedure for all incoming RFQs via tianyalimestone.com, email (info@tianyastone.com), and WhatsApp.",
        "evidence": [
            ("10-Point Diagnostic Checklist", "1. Country/Climate -> 2. Buyer Role -> 3. Stone Collection/Tone -> 4. Custom CNC Depth -> 5. Thickness & Format -> 6. Area (m²) & 20GP Count -> 7. Crate/Pallet Labelling -> 8. Target Site Date -> 9. Incoterm & Port -> 10. Single Next Action (Sample / Conditional Quote)."),
            ("L1 Fact Layer", "What application (pool deck, patio, driveway, facade), square meterage, and destination port are you planning for?"),
            ("L2 Impact Layer & L3 Driver Layer", "What challenges have you experienced with current stone suppliers (shade variation, breakage, lead time, or high local importer markups), and what is your project handover milestone?")
        ],
        "faq": [
            ("What if I don't have a finalized CAD cutting list yet—can I still get a price?",
             "Yes. Under our Conditional Quotation Rule (Module 16), simply tell us the approximate area (m²), preferred stone collection, and destination port. We will provide an immediate Good/Better/Best conditional quote based on standard 20mm and 30mm formats within 12 hours."),
            ("How fast does the Tianya engineering desk respond to new inquiries?",
             "All inquiries sent to info@tianyastone.com or WhatsApp (+86 189 6036 6169) receive a dedicated engineering response within 12 hours.")
        ]
    },
    {
        "id": "16_solution_quotation",
        "slug": "16-good-better-best-quotation-samples",
        "num": "16",
        "layer": "L3 Customer & Execution Layer",
        "title": "Good/Better/Best Stone Specification Tiers, Custom CNC Depth Levels & Sample Archive Lifecycle",
        "short_title": "16 · Good/Better/Best & Samples",
        "kb_id": "RW-TYQUOT-0017",
        "status": "verified_fact",
        "confidence": 0.99,
        "role_views": ["senior_sales", "junior_sales", "sales_director", "operations_quality"],
        "hero_img": "assets/images/contact/sample_kit_box.webp",
        "conclusion": "Rather than sending a single rigid price, Tianya Limestone delivers structured Good / Better / Best engineering options alongside a strict 5-Level Customization Depth Standard and a traceable Sample Archive Lifecycle (`SMP-YYYYMM-XXX`).",
        "conditions": "Governs all conditional and formal quotations, custom CNC orders, and physical sample sign-offs.",
        "evidence": [
            ("Good / Better / Best Framework", "Good: Standard 15–20mm running-line field tiles (600×400mm). Better: 30mm exterior pavers / French Pattern + matching Bullnose or Drop-Face pool coping. Best: 40–50mm heavy vehicular pavers + 5-axis CNC bespoke treads, drain grates & 6-sided factory pre-sealing."),
            ("5 Customization Depth Levels", "Level 1: Standard Running SKU -> Level 2: Custom Crate Labelling/Barcode -> Level 3: Custom Cut-to-Size Dimensions & Edge Profiles -> Level 4: Bespoke 5-Axis CNC 3D Profiling from CAD -> Level 5: Multi-SKU Project Kit Consolidation."),
            ("Mandatory Pre-Production Sample Rule", "Every custom project is assigned a unique Sample Archive ID (e.g., SMP-202610-018). Mass production NEVER starts without written customer confirmation of the physical control sample and CAD shop drawings.")
        ],
        "faq": [
            ("How much do physical limestone sample kits cost?",
             "Physical stone sample kits (100×100mm or 150×150mm swatches across your selected finishes) are complimentary from the factory; the buyer only covers express DHL/FedEx courier shipping, which is 100% credited back on your first container order."),
            ("What is included in a Conditional Quotation?",
             "A Conditional Quotation clearly states the assumed thickness (20mm vs 30mm), format, crate weight, 20GP container utilization, FOB Xiamen price, estimated ocean freight to your port, and validity period.")
        ]
    },
    {
        "id": "17_objection_negotiation",
        "slug": "17-commercial-faq-escalation-boundaries",
        "num": "17",
        "layer": "L3 Customer & Execution Layer",
        "title": "Top 10 B2B Stone Procurement Concerns, Value-Engineering Trade-offs & 8 Mandatory Approval Red Lines",
        "short_title": "17 · 10 B2B Concerns & Red Lines",
        "kb_id": "RW-TYOBJN-0018",
        "status": "verified_fact",
        "confidence": 0.97,
        "role_views": ["senior_sales", "junior_sales", "sales_director", "management"],
        "hero_img": "assets/images/about/export_crates_logistics.webp",
        "conclusion": "Overseas buyers understandably ask tough questions about freight cost, MOQ, transit breakage, shade consistency, and customs compliance. Module 17 addresses all 10 core B2B procurement concerns with transparent engineering solutions and value-engineering trade-offs.",
        "conditions": "Reference guide for procurement negotiations, value engineering, and risk mitigation.",
        "evidence": [
            ("Concerns 1–4 (Price, MOQ, Lead Time, Freight)", "Resolved via Good/Better/Best thickness optimization (e.g., 20mm on mortar slab vs 30mm), Mixed-Container 100 m² trial consolidation, and 26-ton full 20GP weight utilization."),
            ("Concerns 5–8 (Shade Variation, Breakage, Compliance, Custom Tooling)", "Resolved via 3,000 m² dry-lay photo sign-off, ISPM-15 steel-strapped crates (<0.5% breakage + 2% spare tiles recommended), SGS ASTM/CE/GOST reports, and CNC diamond profiling."),
            ("Concerns 9–10 (Payment Security & Exclusivity)", "Protected via 30%/70% B/L terms, dual-channel video bank verification, and KPI-backed regional distributor agreements.")
        ],
        "faq": [
            ("How can we reduce total landed cost per m² without sacrificing stone quality?",
             "If you are laying pavers over a reinforced concrete slab, switching from 30mm (320 m²/20GP) to 20mm (500 m²/20GP) increases the square meterage per container by 56%, cutting both FOB material cost and sea freight cost per m² by over 30%."),
            ("What if our project only needs 120 m² and cannot fill a full 20GP container?",
             "Our MOQ is 100 m². We can ship 4–6 crates via LCL (Less than Container Load) consolidated sea freight from Xiamen Port, or combine your patio pavers, pool coping, and wall cladding into a single mixed 20GP container.")
        ]
    },
    {
        "id": "18_sales_content_templates",
        "slug": "18-specifier-toolkits-multilingual-faq",
        "num": "18",
        "layer": "L3 Customer & Execution Layer",
        "title": "Architectural Specifier CSI/NBS Templates, Submittal Packages & Multi-Stage Buyer FAQ Matrix",
        "short_title": "18 · Specifier CSI Templates & FAQ",
        "kb_id": "RW-TYTMPL-0019",
        "status": "verified_fact",
        "confidence": 0.98,
        "role_views": ["marketing", "senior_sales", "junior_sales"],
        "hero_img": "assets/images/resources/modular_pattern_diagram.webp",
        "conclusion": "Architects and specification writers need copy-ready master specification clauses and structured submittal checklists. Module 18 provides CSI MasterFormat (04 43 00 Stone Masonry / 32 14 40 Stone Unit Paving) templates and a 6-stage decision FAQ matrix.",
        "conditions": "Ready for direct inclusion in architectural tender manuals, BIM object properties, and contractor submittals.",
        "evidence": [
            ("CSI MasterFormat Part 1 (General)", "Defines ASTM C97, C170, C880, C666, EN 1341/1469, and AS 4586 submittal requirements, 3,000 m² dry-lay mock-up approval, and ISPM-15 delivery storage."),
            ("CSI MasterFormat Part 2 (Products)", "Specifies Fujian Tianya Cultural Stone Co., Ltd. high-density bioclastic limestone, exact collection name, finish, dimensional tolerances (±1.0mm), and edge profile."),
            ("CSI MasterFormat Part 3 (Execution)", "Specifies substrate preparation, C2S1 white flexible polymer adhesive with 100% back-buttering, movement joints, and 14-day post-installation penetrating silane/siloxane sealing.")
        ],
        "faq": [
            ("Where can I find the specific CSI 04 43 00 specification text for each of the 29 limestone collections?",
             "Visit our 29-SKU Technical Data Sheet Hub (/specifications/), where every individual stone collection has its own dedicated CSI 3-Part specification page."),
            ("Are your FAQ and technical specifications available in Russian for EAEU/CIS tenders?",
             "Yes. Our Russian & CIS Engineering Portal (/ru/ and /ru/cis-central-asia/) provides complete GOST 30629-2011, SNiP/SP, and TN VED specifications in Russian.")
        ]
    },
    {
        "id": "19_order_execution_qc_aftersales",
        "slug": "19-order-execution-qc-aftersales",
        "num": "19",
        "layer": "L3 Customer & Execution Layer",
        "title": "15-Node Order Execution SOP, ISPM-15 Crate Loading & P1/P2/P3 After-Sales Claims Protocol",
        "short_title": "19 · 15-Node Order & After-Sales SOP",
        "kb_id": "RW-TYORDR-0020",
        "status": "verified_fact",
        "confidence": 0.99,
        "role_views": ["operations_quality", "senior_sales", "sales_director", "management"],
        "hero_img": "assets/images/about/export_crates_logistics.webp",
        "conclusion": "Flawless stone delivery requires rigorous execution from Proforma Invoice sign-off to job-site unloading. Module 19 documents our 15-Node Order Execution SOP and our transparent P1 (24h) / P2 (48h) / P3 (72h) After-Sales Triage & Evidence Protocol.",
        "conditions": "Applies to all commercial orders, export crating, container loading, and post-delivery technical support.",
        "evidence": [
            ("15-Node Execution Chain", "1. PI & Spec Confirmation -> 2. Deposit Verification -> 3. Control Sample (SMP-ID) Sign-Off -> 4. CAD Shop Drawing Freeze -> 5. Quarry Block Selection -> 6. Gang-Saw Slabbing -> 7. Surface Texturing -> 8. 5-Axis CNC Sizing -> 9. 3,000 m² Dry-Lay & Photo Approval -> 10. Kiln Drying & Optional Pre-Sealing -> 11. ISPM-15 Crating -> 12. 20GP Container Bracing -> 13. Customs & CO/Form E/ChAFTA -> 14. B/L Dispatch -> 15. Site Installation Guidance."),
            ("P1 / P2 / P3 After-Sales SLA", "P1 Critical (Structural transit damage or major spec deviation): 24h executive & QC joint response. P2 Important (Localized crate damage or shade sorting query): 48h QC evidence review & replacement/credit plan. P3 Routine (Sealer choice, cleaning, or cutting advice): 72h engineering guide response."),
            ("After-Sales Evidence Package", "Requires Crate QR/ID label photo, unopened crate exterior photo in container, close-up defect measurement photo, and Bill of Lading number.")
        ],
        "faq": [
            ("How do you brace heavy stone crates inside a 20GP container to prevent ocean transit damage?",
             "Crates are constructed from ISPM-15 heat-treated hardwood, wrapped in waterproof polyethylene, strapped with high-tensile PET/steel bands, and interlocked inside the 20GP container using heavy timber dunnage wedges and floor chocks."),
            ("What should a site supervisor do upon receiving a container at the job site?",
             "Photograph the container seal number before opening, photograph the crate arrangement inside the container, and inspect crate labels against the Packing List and Dry-Lay Layout Map before unstrapping.")
        ]
    },
    {
        "id": "20_learning_metrics",
        "slug": "20-project-case-benchmarks-learning",
        "num": "20",
        "layer": "L4 Continuous Learning Layer",
        "title": "Architectural Limestone Project Benchmarks, Quality Feedback Loop & Continuous Specification Optimization",
        "short_title": "20 · Project Benchmarks & Learning",
        "kb_id": "RW-TYLRNG-0021",
        "status": "verified_fact",
        "confidence": 0.96,
        "role_views": ["management", "sales_director", "operations_quality", "marketing"],
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "conclusion": "Every completed architectural project feeds back into our quarry selection, CNC calibration, and specification guides. Module 20 presents verified architectural application benchmarks and our 4-Dimension Post-Project Review Loop (Material, Fabrication, Packaging, Site Installation).",
        "conditions": "Demonstrates how field performance across coastal, alpine, and desert installations continuously refines Tianya Limestone specifications.",
        "evidence": [
            ("Coastal Saltwater Pool Benchmark", "Verified zero spalling and P5 wet slip retention on 30mm Sandblasted & Brushed (Daiwa / Wangchuan) and Tumbled (Guyu) pool decks when sealed with penetrating fluoropolymer sealers."),
            ("Continental Freeze-Thaw Benchmark", "Verified F100 / 100-cycle frost integrity on 30mm–40mm calibrated pavers and mechanically anchored rainscreen facades in -30°C to -40°C winters."),
            ("Continuous KB Governance Audit", "Tested against the RenWork V4 35-Case Governance Benchmark (30 B2B technical/commercial queries + 5 mandatory anti-hallucination escalation tests).")
        ],
        "faq": [
            ("What are the 5 Negative Hallucination Red-Line Tests in the Tianya Knowledge Base?",
             "Our system strictly refuses to fabricate: (1) Unauthorized below-floor pricing, (2) Unheld local certifications, (3) Unapproved OA 90-day credit terms, (4) Physically impossible production lead times, or (5) Email-only bank account changes."),
            ("How often is the Tianya Export Knowledge Base updated?",
             "Laboratory test reports and compliance matrices are audited quarterly; container freight benchmarks and engineering blog guides are updated monthly based on live Xiamen Port departures and architect inquiries.")
        ]
    }
]


# ==============================================================================
# 2. 24 ARCHITECTURAL APPLICATION ENGINEERING GUIDES (/applications/{slug}/)
# ==============================================================================
APPLICATIONS_DATA = [
    {
        "slug": "saltwater-pool-surrounds-coping",
        "title": "Saltwater Pool Decks & Bullnose / Drop-Face Coping Engineering Guide",
        "category": "Pool & Aquatic Architecture",
        "kb_id": "RW-TYAPPL-0101",
        "recommended_finish": "Tumbled / Sandblasted & Brushed",
        "recommended_skus": ["guyu", "daiwa", "wangchuan", "qinghe"],
        "thickness": "30mm Field Pavers + 30/75mm Drop-Face or 30mm Full Bullnose Coping",
        "slip_rating": "AS 4586 P5 / DIN 51097 Class C / ANSI A326.3 DCOF ≥ 0.62",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Engineering specification for coastal and residential saltwater swimming pool surrounds, infinity edges, and cantilevered drop-face coping using high-solar-reflectance (SRI 64–78), salt-resistant bioclastic limestone.",
        "substrate": "150mm reinforced concrete pool bond beam & deck slab with waterproof membrane, bonded via C2S1 white flexible polymer-modified mortar (100% back-buttered) and flexible silicone expansion joint at the coping-to-deck perimeter.",
        "sealer": "6-sided factory or site-applied fluoropolymer / silane-siloxane penetrating consolidating sealer (ASTM C672 salt-crystallization resistant)."
    },
    {
        "slug": "ventilated-exterior-rainscreen-facades",
        "title": "Mechanically Anchored Ventilated Limestone Rainscreen Facades (EN 1469 / GOST 30629)",
        "category": "Exterior Facade Cladding",
        "kb_id": "RW-TYAPPL-0102",
        "recommended_finish": "Sandblasted & Brushed / Chiseled / Bush-Hammered",
        "recommended_skus": ["xieshan", "sunmao", "wangchuan", "canglang"],
        "thickness": "30mm / 40mm Calibrated Facade Panels with CNC Kerf Slots or Undercut Anchor Pockets",
        "slip_rating": "EN 1469 / ASTM C1242 Dowel & Undercut Pull-Out Verified",
        "hero_img": "assets/images/hero/scene-facade.webp",
        "summary": "Structural design and CNC kerf-slotting specification for multi-story commercial, institutional, and luxury residential ventilated rainscreen facades using AISI 316 (A4) stainless steel brackets.",
        "substrate": "Structural concrete or steel stud backup wall with exterior mineral wool insulation, 40–60mm ventilated air cavity, and AISI 316 stainless steel kerf/dowel or Fischer FZP undercut anchor sub-frame.",
        "sealer": "Breathable hydrophobic silane-siloxane facade impregnator (water vapor permeable Sd < 0.1m) preventing atmospheric soot and pollution staining."
    },
    {
        "slug": "vehicular-driveways-porte-cocheres",
        "title": "Heavy-Duty Vehicular Driveways, Porte-Cochères & Motor Courts (40mm–60mm)",
        "category": "Vehicular & Civic Paving",
        "kb_id": "RW-TYAPPL-0103",
        "recommended_finish": "Bush-Hammered / Tumbled / Natural Split Cobbles",
        "recommended_skus": ["canghai", "xuanzhen", "guyu", "lanting"],
        "thickness": "40mm / 50mm / 60mm Small-Format Pavers & Cobblestones (100×100mm to 300×150mm)",
        "slip_rating": "AS 4586 P5 / DIN 51130 R12 (High-Traction Vehicular Grade)",
        "hero_img": "assets/images/products/canghai_scene.webp",
        "summary": "Load-bearing thickness and aspect-ratio engineering for luxury residential motor courts, hotel porte-cochères, and municipal vehicular plazas subject to SUV and delivery truck axle loads.",
        "substrate": "150–200mm reinforced concrete structural slab with full-bed C2S1 mortar bonding (aspect ratio length:thickness ≤ 6:1) and 8–10mm polymer-modified structural jointing.",
        "sealer": "Oleophobic + hydrophobic fluorochemical penetrating sealer for tire-mark and motor-oil resistance."
    },
    {
        "slug": "freeze-thaw-alpine-courtyards",
        "title": "Freeze-Thaw & Alpine Climate Courtyards, Plazas & Snow-Melt Terraces (F100 / ASTM C666)",
        "category": "Cold-Climate Landscape",
        "kb_id": "RW-TYAPPL-0104",
        "recommended_finish": "Bush-Hammered / Sandblasted & Brushed",
        "recommended_skus": ["canghai", "canglang", "wangchuan", "xuansu"],
        "thickness": "30mm / 40mm Calibrated Pavers",
        "slip_rating": "AS 4586 P4–P5 / ASTM C666 100-Cycle & GOST 30629 F100 Certified",
        "hero_img": "assets/images/hero/scene-garden.webp",
        "summary": "Zero-spalling specification for Canada, Northern US, Northern Europe, Russia, and Kazakhstan projects operating under -30°C to -40°C winter freeze-thaw cycles and hydronic snow-melt systems.",
        "substrate": "Drained concrete slab with 2% minimum cross-slope or open-graded crushed granite drainage bed (zero standing water below stone bed); compatible with embedded hydronic or electric snow-melt loops.",
        "sealer": "Deep-penetrating solvent-free silane monomer sealer + mandatory exclusion of NaCl rock salt (use CaMg(Ac)2 or hydronic melting)."
    },
    {
        "slug": "seamless-indoor-outdoor-living-transitions",
        "title": "Five-Star Hotel & Resort Verandas, Loggias & Indoor-Outdoor Seamless Transitions",
        "category": "Hospitality Architecture",
        "kb_id": "RW-TYAPPL-0105",
        "recommended_finish": "Sandblasted & Brushed / Tumbled",
        "recommended_skus": ["wangchuan", "daiwa", "hanbai", "guyu"],
        "thickness": "20mm Interior Loggia + 30mm Exterior Terrace (Matched Quarry Vein Batch)",
        "slip_rating": "Interior P3/R10 -> Exterior P4–P5/R11 Visual Continuity",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Achieving seamless architectural continuity across sliding glass thresholds by pairing 20mm velvet-brushed interior limestone with 30mm high-traction exterior pavers cut from the exact same quarry block batch.",
        "substrate": "Interior screed with underfloor heating + exterior sloped waterproof terrace slab separated by an architectural threshold drainage slot.",
        "sealer": "Natural-look (non-color-enhancing) breathable fluoropolymer impregnator for coffee, red wine, and sunscreen stain protection."
    },
    {
        "slug": "alfresco-outdoor-patios-courtyards",
        "title": "Versailles / French Pattern (4-Size Modular) Garden Patios & Mediterranean Courtyards",
        "category": "Residential & Estate Landscape",
        "kb_id": "RW-TYAPPL-0106",
        "recommended_finish": "Tumbled / Chiseled-Edge Brushed",
        "recommended_skus": ["guyu", "qinghe", "shanshui", "guyun"],
        "thickness": "20mm (Mortar Bed on Slab) / 30mm (Exterior Heavy Duty)",
        "slip_rating": "AS 4586 P4 / DIN 51130 R11",
        "hero_img": "assets/images/products/guyu_scene.webp",
        "summary": "Complete layout engineering for 0.74 m² (8 sq.ft) interlocking 4-size French Pattern modules (610×406, 406×406, 406×203, 203×203mm) that break up long sightlines and eliminate continuous 4-corner intersections.",
        "substrate": "100–150mm concrete patio slab with full-bed white polymer adhesive or 40mm semi-dry Trass-lime mortar bed over compacted base.",
        "sealer": "Either natural matte penetrating sealer or Subtle Color-Enhancing sealer to deepen warm fossil and golden-beige tones."
    },
    {
        "slug": "rooftop-terraces-pedestal-paver-systems",
        "title": "Adjustable Pedestal Raised Rooftop Terraces, Podium Decks & Penthouse Balconies",
        "category": "Commercial & High-Rise Podiums",
        "kb_id": "RW-TYAPPL-0107",
        "recommended_finish": "Sandblasted & Brushed / Bush-Hammered",
        "recommended_skus": ["wangchuan", "canglang", "canghai", "yexiang"],
        "thickness": "30mm / 40mm CNC-Calibrated Pavers with Optional Fiberglass Mesh Safety Backing",
        "slip_rating": "AS 4586 P4–P5 / EN 1341 Breaking Load Verified",
        "hero_img": "assets/images/about/factory_fabrication.webp",
        "summary": "Structural span calculation, breaking-load safety factors, and anti-fracture backing mesh specifications for elevated pedestal paver systems over EPDM/TPO roof membranes.",
        "substrate": "Adjustable polypropylene or non-combustible aluminum screw-jack pedestals (spaced at corners and mid-span for 600×600mm or 600×400mm pavers) with 3mm acoustic rubber shims.",
        "sealer": "Factory pre-sealed 6-sided breathable water-repellent treatment."
    },
    {
        "slug": "exterior-landscape-steps-staircases",
        "title": "Monolithic Landscape Steps, Bullnose Stair Treads, Risers & Anti-Slip Grooves",
        "category": "Circulation & Hardscape",
        "kb_id": "RW-TYAPPL-0108",
        "recommended_finish": "Bush-Hammered / Sandblasted & Brushed with CNC Grip Grooves",
        "recommended_skus": ["canghai", "wangchuan", "guyu", "canglang"],
        "thickness": "30mm / 50mm Treads (1200–1500×350mm) or 150×350mm Solid Block Steps",
        "slip_rating": "AS 4586 P5 / ADA & UK Building Regs Part M Visual Nosing Contrast",
        "hero_img": "assets/images/hero/scene-garden-detail.webp",
        "summary": "Precision CNC fabrication of one-piece stair treads with bullnose, pencil-round, or rock-pitched nosings and dual 5mm abrasive/grooved anti-slip safety strips.",
        "substrate": "Cast-in-place reinforced concrete stair stringers bonded with full-bed C2S1 structural adhesive and 1% forward drainage pitch per tread.",
        "sealer": "High-traffic penetrating sealer resistant to foot-traffic abrasion and de-icing agents."
    },
    {
        "slug": "crazy-paving-garden-pathways",
        "title": "Organic Crazy Paving (Random Flagstone) Garden Pathways, Stepping Stones & Courtyards",
        "category": "Organic Landscape Design",
        "kb_id": "RW-TYAPPL-0109",
        "recommended_finish": "Natural Split / Tumbled Random Flagstone",
        "recommended_skus": ["zaojing", "guyu", "lanting", "dougong"],
        "thickness": "20–30mm Calibrated or 25–35mm Natural Split Thickness",
        "slip_rating": "AS 4586 P5 / DIN 51130 R11–R12",
        "hero_img": "assets/images/related/crazy-paving.webp",
        "summary": "Pre-sorted random polygonal limestone flagstones (3–5 pieces per m²) for coastal Australian villas, Mediterranean gardens, and organic resort walkways.",
        "substrate": "Mortared over concrete slab with wide 15–30mm coarse sand-cement or polymer joints, or set as large 600–900mm stepping pads in gravel/dichondra lawn.",
        "sealer": "Breathable penetrating sealer to prevent soil, leaf-tannin, and irrigation water staining."
    },
    {
        "slug": "split-face-retaining-feature-walls",
        "title": "Split-Face Limestone Ledgestone, Retaining Wall Veneer & Fireplace Surrounds",
        "category": "Vertical Stone Masonry",
        "kb_id": "RW-TYAPPL-0110",
        "recommended_finish": "Natural Split-Face / Hand-Chiseled / Fluted",
        "recommended_skus": ["xieshan", "sunmao", "zhuozheng", "dougong"],
        "thickness": "20–35mm Split-Face Veneer + Matching Pre-Cut 90° L-Corner Quoin Returns",
        "slip_rating": "ASTM C97 / EN 771-6 Exterior Masonry Veneer Compliant",
        "hero_img": "assets/images/related/ledger-stone.webp",
        "summary": "Tactile 3D shadow-line wall cladding with seamless interlocking L-corner returns that replicate full-bed dry-stack stone masonry at 20% of the structural dead weight.",
        "substrate": "CMU blockwork, poured concrete retaining walls (with positive rear waterproofing & drainage mat), or cement-board sheathing with stainless steel lath.",
        "sealer": "Vapor-permeable silane-siloxane water repellent to prevent efflorescence from retaining wall backfill."
    },
    {
        "slug": "spa-hammam-wet-rooms",
        "title": "Luxury Spa, Hammam, Thermal Bath & Wet-Room Limestone Surfaces",
        "category": "Wellness & Hospitality Interiors",
        "kb_id": "RW-TYAPPL-0111",
        "recommended_finish": "Sandblasted & Brushed / Honed-Velvet",
        "recommended_skus": ["wangchuan", "hanbai", "daiwa", "shanshui"],
        "thickness": "20mm Wall & Floor Panels + 5-Axis CNC Carved Basins & Drain Channels",
        "slip_rating": "DIN 51097 Class B/C Barefoot Wet-Room Certified",
        "hero_img": "assets/images/products/wangchuan_scene.webp",
        "summary": "Skin-friendly, non-abrasive barefoot traction and moisture-managed detailing for wellness resorts, Turkish hammams, thermal spas, and luxury master bathrooms.",
        "substrate": "Continuous sheet waterproofing membrane (Schluter Kerdi / Laticrete Hydro Ban) with 100% white C2S1 adhesive coverage and epoxy or anti-microbial flexible grout.",
        "sealer": "Spa-grade hydro-oleophobic impregnator resistant to essential oils, soap scum, and continuous high humidity."
    },
    {
        "slug": "outdoor-kitchens-bbq-pavilion",
        "title": "Alfresco Outdoor Kitchens, BBQ Pavilions, Dining Terraces & Bar Counters",
        "category": "Outdoor Living & Entertaining",
        "kb_id": "RW-TYAPPL-0112",
        "recommended_finish": "Sandblasted & Brushed / Tumbled",
        "recommended_skus": ["wangchuan", "guyu", "xuansu", "canglang"],
        "thickness": "20mm / 30mm Floor Pavers + 30mm / 40mm CNC-Mitered Countertop & Island Cladding",
        "slip_rating": "AS 4586 P4 / High Oil & Food-Stain Protection Protocol",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Designing stain-protected, UV-stable outdoor culinary pavilions and dining terraces that resist grease splatters, red wine, citrus, and thermal shock.",
        "substrate": "Concrete patio slab and masonry/steel outdoor kitchen island framing with cement-board backing.",
        "sealer": "Dual-coat premium fluorochemical oleophobic (oil-repellent) + anti-etch penetrating sealer."
    },
    {
        "slug": "commercial-plazas-civic-promenades",
        "title": "Public Civic Plazas, Museum Forecourts, Retail Boulevards & Urban Promenades",
        "category": "Civic & Commercial Hardscape",
        "kb_id": "RW-TYAPPL-0113",
        "recommended_finish": "Bush-Hammered / Chiseled / Heavy Sandblasted",
        "recommended_skus": ["canghai", "canglang", "xuanzhen", "xieshan"],
        "thickness": "40mm / 50mm / 60mm Heavy Commercial Pavers + Tactile Guidance Tiles",
        "slip_rating": "AS 4586 P5 / EN 1341 Heavy Pedestrian & Emergency Vehicle Class",
        "hero_img": "assets/images/products/canglang_scene.webp",
        "summary": "High-abrasion, low-glare limestone paving systems engineered for millions of annual footfalls, municipal street-sweeping machines, and emergency fire-lane loads.",
        "substrate": "200mm reinforced concrete municipal slab with bonded structural mortar bed and movement joints every 4.5–6.0 meters.",
        "sealer": "Anti-graffiti, oil-repellent municipal fluoropolymer surface protector."
    },
    {
        "slug": "architectural-columns-balustrades-porticos",
        "title": "5-Axis CNC Architectural Columns, Roman Pillars, Balustrades, Cornices & Window Surrounds",
        "category": "Classical & Bespoke Architectural Millwork",
        "kb_id": "RW-TYAPPL-0114",
        "recommended_finish": "Honed / Sandblasted & Brushed / Hand-Carved",
        "recommended_skus": ["daiwa", "wangchuan", "guyu", "shanshui"],
        "thickness": "Custom 5-Axis CNC Solid or Hollow-Core Cladding Segments per CAD Shop Drawings",
        "slip_rating": "±0.5mm CNC Interlocking Joint Precision + 100% Factory Dry-Fit",
        "hero_img": "assets/images/about/craftsman_stonemason.webp",
        "summary": "Custom CAD-to-BIM 5-axis CNC lathe and milling fabrication for classical villa porticos, fluted columns, Corinthian/Ionic capitals, window architraves, and parapet balustrades.",
        "substrate": "Structural steel or reinforced concrete column cores anchored via stainless steel dowels, threaded rods, and structural epoxy.",
        "sealer": "Breathable architectural facade water repellent preserving crisp carved shadow lines."
    },
    {
        "slug": "winery-cellars-tasting-courtyards",
        "title": "Estate Winery Cellars, Barrel Rooms, Tasting Courtyards & Vineyard Terraces",
        "category": "Hospitality & Agricultural Estates",
        "kb_id": "RW-TYAPPL-0115",
        "recommended_finish": "Tumbled / Chiseled / Antique Brushed",
        "recommended_skus": ["guyu", "guyun", "qinghe", "zaojing"],
        "thickness": "20mm / 30mm French Pattern & Large-Format Cobbles",
        "slip_rating": "AS 4586 P4–P5 / High Thermal Mass & Tannin-Stain Sealed",
        "hero_img": "assets/images/hero/scene-garden.webp",
        "summary": "Authentic Old-World limestone flooring and masonry that harmonizes with limestone-rich vineyard terroir in Napa, Bordeaux, Barossa Valley, and Waiheke Island.",
        "substrate": "Concrete cellar slab with floor drains and exterior vineyard terrace sub-base.",
        "sealer": "Oleophobic penetrating sealer formulated to resist red wine anthocyanin and grape must absorption."
    },
    {
        "slug": "coastal-seawall-marine-terraces",
        "title": "Coastal Oceanfront Villas, Marine Terraces & Salt-Spray Promenade Cladding",
        "category": "Coastal & Marine Architecture",
        "kb_id": "RW-TYAPPL-0116",
        "recommended_finish": "Sandblasted & Brushed / Bush-Hammered",
        "recommended_skus": ["wangchuan", "daiwa", "canghai", "guyu"],
        "thickness": "30mm / 40mm Pavers & Coping (ASTM C97 Absorption ≤ 1.8%)",
        "slip_rating": "AS 4586 P5 / Marine Salt-Fog & Sub-Surface Consolidation Protected",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Preventing sub-florescence and salt-spalling in oceanfront estates located within 500 meters of breaking surf in Florida, Sydney, Gold Coast, Mediterranean, and Gulf coastlines.",
        "substrate": "Waterproofed marine-grade concrete slab with 6-sided stone dip-sealing prior to mortar installation and AISI 316L marine stainless steel fixings.",
        "sealer": "6-sided deep-consolidating ethyl-silicate + silane-siloxane marine stone protector."
    },
    {
        "slug": "desert-arid-cool-touch-hardscape",
        "title": "Middle East & Southwest Desert Cool-Touch Pool Decks, Majlis Courtyards & Palace Facades",
        "category": "Arid & High-Solar-Load Architecture",
        "kb_id": "RW-TYAPPL-0117",
        "recommended_finish": "Sandblasted & Brushed / Tumbled Light-Tone",
        "recommended_skus": ["daiwa", "hanbai", "wangchuan", "shanshui"],
        "thickness": "30mm Pavers & Ventilated Facade Panels (High SRI 68–78)",
        "slip_rating": "SASO / Dubai Green Building SRI & Barefoot Thermal Comfort Verified",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Thermal performance engineering for Riyadh, Dubai, Abu Dhabi, Doha, Phoenix, and Las Vegas where ambient summer temperatures reach +50°C and dark stone becomes untouchable.",
        "substrate": "Insulated concrete deck or ventilated facade cavity with UV-resistant movement joints every 3.5–4.0 meters to accommodate diurnal thermal swings.",
        "sealer": "UV-stable, non-yellowing aliphatic silane sealer resistant to sandstorm abrasion."
    },
    {
        "slug": "interior-radiant-heated-living-floors",
        "title": "Luxury Residential Interior Living Floors, Foyers & Radiant Underfloor Heating Systems",
        "category": "Interior Architectural Flooring",
        "kb_id": "RW-TYAPPL-0118",
        "recommended_finish": "Sandblasted & Brushed (Velvet Finish) / Softly Tumbled",
        "recommended_skus": ["wangchuan", "hanbai", "daiwa", "xuansu"],
        "thickness": "15mm / 20mm Calibrated Large-Format Tiles (600×600mm, 900×600mm, French Pattern)",
        "slip_rating": "AS 4586 P3 / DIN 51130 R10 Velvet Barefoot Finish (λ = 2.1 W/m·K)",
        "hero_img": "assets/images/products/wangchuan_scene.webp",
        "summary": "Maximizing thermal conductivity and tactile comfort over hydronic and electric radiant floor heating in open-plan villas, galleries, and penthouses.",
        "substrate": "Heated cementitious screed with uncoupling membrane (e.g., Ditra), S1/S2 deformable white adhesive, and perimeter expansion strips.",
        "sealer": "Zero-VOC water-based interior penetrating stain-stop sealer."
    },
    {
        "slug": "infinity-edge-overflow-pool-channels",
        "title": "Infinity-Edge Weir Walls, Lautner Knife-Edge Slots & CNC Slotted Stone Drain Grates",
        "category": "Pool & Aquatic Architecture",
        "kb_id": "RW-TYAPPL-0119",
        "recommended_finish": "Sandblasted & Brushed / Precision CNC Slotted",
        "recommended_skus": ["wangchuan", "daiwa", "canglang", "guyu"],
        "thickness": "30mm / 40mm CNC-Slotted Drain Covers & Weir Capstones",
        "slip_rating": "AS 4586 P5 + Continuous Water Immersion Tested",
        "hero_img": "assets/images/resources/cad_blueprints.webp",
        "summary": "Eliminating unsightly plastic drain grates around luxury swimming pools by integrating 30mm CNC-slotted removable limestone trench covers and precision-leveled weir caps.",
        "substrate": "Waterproofed concrete overflow gutter ledges with ±0.5mm laser-leveled weir tolerances.",
        "sealer": "6-sided immersion-grade hydrophobic consolidant."
    },
    {
        "slug": "sunken-fire-pit-lounges-seating",
        "title": "Sunken Fire-Pit Lounges, Cantilevered Bench Caps & Garden Amphitheater Seating",
        "category": "Outdoor Living & Entertaining",
        "kb_id": "RW-TYAPPL-0120",
        "recommended_finish": "Sandblasted & Brushed / Chiseled Edge",
        "recommended_skus": ["guyu", "wangchuan", "xieshan", "canglang"],
        "thickness": "30mm / 50mm Bullnose or Rock-Faced Bench Caps + 20–35mm Split-Face Seat Risers",
        "slip_rating": "Thermal-Shock & Outdoor Weathering Compliant",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Detailing cantilevered limestone seat bench caps, gas/wood fire-pit coping rings (with inner refractory liner), and curved amphitheater steps.",
        "substrate": "Reinforced CMU masonry bench walls with 50mm refractory air gap/brick liner inside fire bowls.",
        "sealer": "Soot-release and oil-repellent penetrating stone sealer."
    },
    {
        "slug": "botanical-water-features-reflecting-ponds",
        "title": "Architectural Reflecting Ponds, Cascade Water Walls & Koi Courtyard Basins",
        "category": "Landscape Water Features",
        "kb_id": "RW-TYAPPL-0121",
        "recommended_finish": "Chiseled / Natural Split / Bush-Hammered",
        "recommended_skus": ["canglang", "xieshan", "xuansu", "canghai"],
        "thickness": "30mm Dark-Tone Pond Liners (Creating Mirror Reflection) + 30–50mm Chiseled Spillways",
        "slip_rating": "Aquatic Safe (Non-Toxic Neutral CaCO3 Buffering)",
        "hero_img": "assets/images/hero/scene-garden-detail.webp",
        "summary": "Using dark charcoal-grey limestone (`Canglang`, `Modai`) to create deep optical mirror reflections in shallow reflecting pools and rhythmic laminar ripples over chiseled cascade walls.",
        "substrate": "Waterproofed concrete basin with 100% void-free epoxy-modified or submerged-rated C2S1 adhesive.",
        "sealer": "Aquatic-safe, solvent-free hydrophobic impregnator."
    },
    {
        "slug": "permeable-eco-paving-systems",
        "title": "SUDS / Permeable Open-Joint Limestone Paving & Sustainable Urban Drainage Landscapes",
        "category": "Sustainable & LEED Landscape",
        "kb_id": "RW-TYAPPL-0122",
        "recommended_finish": "Tumbled / Bush-Hammered",
        "recommended_skus": ["canghai", "guyu", "lanting", "xuanzhen"],
        "thickness": "40mm / 50mm Heavy Calibrated Pavers with 6–10mm Permeable Aggregate/Resin Joints",
        "slip_rating": "AS 4586 P5 / LEED & BREEAM Stormwater Credit Compatible",
        "hero_img": "assets/images/products/canghai_scene.webp",
        "summary": "Meeting municipal stormwater runoff mandates (SUDS / LEED v4 Rainwater Management) using thick-bed limestone pavers over open-graded no-fines aggregate sub-bases.",
        "substrate": "150–250mm compacted ASTM No. 57 open-graded angular crushed stone reservoir base + 40mm ASTM No. 8 bedding layer and permeable resin-bound quartz jointing.",
        "sealer": "Breathable eco-certified water-based silane sealer."
    },
    {
        "slug": "boutique-retail-art-gallery-flooring",
        "title": "Flagship Luxury Retail Boutiques, Art Galleries, Museums & Corporate Lobbies",
        "category": "Commercial Interior Architecture",
        "kb_id": "RW-TYAPPL-0123",
        "recommended_finish": "Sandblasted & Brushed / Honed Matte",
        "recommended_skus": ["wangchuan", "daiwa", "xuansu", "canglang"],
        "thickness": "20mm Large-Format Architectural Slabs (900×600mm, 1200×600mm)",
        "slip_rating": "ANSI A326.3 Commercial Interior DCOF ≥ 0.48 / Zero Specular Glare",
        "hero_img": "assets/images/products/wangchuan_scene.webp",
        "summary": "Museum-grade, zero-glare architectural limestone flooring that provides a quiet, monolithic backdrop for gallery track lighting and luxury retail displays.",
        "substrate": "Self-leveled commercial concrete slab with crack-isolation membrane, 1.5–2.0mm rectified grout joints, and color-matched cementitious grout.",
        "sealer": "Commercial high-traffic matte polyurethane/fluoropolymer sacrificial wear & stain barrier."
    },
    {
        "slug": "heritage-restoration-chateau-conservation",
        "title": "Historic Building Restoration, Heritage Facade Conservation & Chateau Courtyard Matching",
        "category": "Heritage & Conservation Architecture",
        "kb_id": "RW-TYAPPL-0124",
        "recommended_finish": "Antique Tumbled / Hand-Chiseled / Custom Bush-Hammered",
        "recommended_skus": ["guyu", "qinghe", "xieshan", "canghai"],
        "thickness": "Custom Heritage Ashlar Blocks, Quoins, Cobbles & Flagstones per Conservation Brief",
        "slip_rating": "NHL 3.5 Hydraulic Lime Mortar & Breathable Conservation Compatible",
        "hero_img": "assets/images/products/guyu_scene.webp",
        "summary": "Custom petrographic, color, and hand-tooled texture matching for listed heritage buildings, European-style estates, and historic civic streetscapes.",
        "substrate": "Traditional NHL 3.5 / NHL 5.0 Natural Hydraulic Lime mortar beds (zero Portland cement trapping moisture in historic walls).",
        "sealer": "Vapor-open mineral silicate / conservation-grade water repellent."
    }
]

# ==============================================================================
# 3. 18 COMPANION STONE & CNC PROFILE CATEGORIES (/stone-flooring/other-categories/{slug}/)
# ==============================================================================
COMPANION_CATEGORIES_DATA = [
    {
        "slug": "pool-coping-profiles",
        "title": "Full Bullnose & Half Bullnose Limestone Pool Coping Stones",
        "code": "TY-CAT-01",
        "kb_id": "RW-TYCCAT-0201",
        "dimensions": "600×300×30mm, 600×350×30mm, 600×400×30mm, 900×350×30mm (R15mm / R20mm Radius)",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Smooth CNC-profiled 180° full-radius and 90° half-radius bullnose swimming pool coping stones with matching internal/external 90° corner blocks and Roman-end radial segments.",
        "applications": "Residential & resort saltwater swimming pools, spa overflow edges, and curved kidney/Roman pool perimeters.",
        "crate_yield": "Approx. 320–350 m² (or ~900 linear meters of 350mm coping) per 20GP container."
    },
    {
        "slug": "drop-face-rebated-pool-coping",
        "title": "Drop-Face (Rebated L-Profile) Limestone Pool Coping Stones",
        "code": "TY-CAT-02",
        "kb_id": "RW-TYCCAT-0202",
        "dimensions": "600×350×30/75mm, 600×400×30/80mm, 900×400×30/100mm (Monolithic or Epoxy-Mitered)",
        "hero_img": "assets/images/resources/cad_blueprints.webp",
        "summary": "Contemporary architectural L-profile drop-face coping that creates the visual illusion of a massive 75mm–100mm thick stone slab along the pool waterline while keeping deck dead weight low.",
        "applications": "Modern architectural lap pools, infinity-edge perimeters, and cantilevered step nosings.",
        "crate_yield": "Approx. 650–780 linear meters per 20GP container in foam-interleaved hardwood crates."
    },
    {
        "slug": "versailles-french-pattern-kits",
        "title": "Pre-Packaged Versailles / French Pattern Modular Limestone Paver Sets",
        "code": "TY-CAT-03",
        "kb_id": "RW-TYCCAT-0203",
        "dimensions": "1 Set = 0.743 m² (8 sq.ft): 1×(610×406), 2×(406×406), 1×(406×203), 2×(203×203mm) in 20mm or 30mm",
        "hero_img": "assets/images/resources/modular_pattern_diagram.webp",
        "summary": "Crate-sorted interlocking 4-size modular French Pattern kits bundled in exact installation ratios so site masons can lay directly from each crate without sorting delays.",
        "applications": "Mediterranean courtyards, pool decks, garden patios, and rustic interior country floors.",
        "crate_yield": "20mm: 500 m² (672 sets) / 20GP | 30mm: 320 m² (430 sets) / 20GP."
    },
    {
        "slug": "crazy-paving",
        "title": "Crazy Paving (Random Polygonal Flagstone) Limestone Pavers",
        "code": "TY-CAT-04",
        "kb_id": "RW-TYCCAT-0204",
        "dimensions": "Random polygonal slabs Ø 350–750mm (3–5 pcs/m²), Thickness: 20–30mm Calibrated or 25–35mm Split",
        "hero_img": "assets/images/related/crazy-paving.webp",
        "summary": "Organic free-form polygonal limestone flagstones pre-selected for balanced size distribution and minimal site trimming.",
        "applications": "Australian coastal villas, organic pool surrounds, garden pathways, and feature walls.",
        "crate_yield": "Approx. 340–420 m² per 20GP container depending on thickness."
    },
    {
        "slug": "natural-ledger-stone",
        "title": "Split-Face Limestone Wall Cladding, Ledgestone & Z-Stone Panels",
        "code": "TY-CAT-05",
        "kb_id": "RW-TYCCAT-0205",
        "dimensions": "600×150×20–35mm Panels, Free-Length Strips (100/150/200mm H), & Pre-Cut 90° L-Corners",
        "hero_img": "assets/images/related/ledger-stone.webp",
        "summary": "High-relief hand-split and machine-guillotined limestone wall veneer with matching solid L-corner quoins for authentic dry-stack and mortared masonry facades.",
        "applications": "Exterior facade accents, retaining walls, gate pillars, and indoor/outdoor fireplaces.",
        "crate_yield": "Approx. 420–480 m² per 20GP container."
    },
    {
        "slug": "monolithic-step-treads-risers",
        "title": "Monolithic Limestone Step Treads, Risers & Solid Block Steps",
        "code": "TY-CAT-06",
        "kb_id": "RW-TYCCAT-0206",
        "dimensions": "Treads: 1000–1800×350×30/50mm | Risers: 1000–1800×150×20mm | Solid Blocks: 1200×350×150mm",
        "hero_img": "assets/images/hero/scene-garden-detail.webp",
        "summary": "Custom-length staircase treads featuring CNC anti-slip grip grooves, bullnose or rock-pitched front edges, and color-matched risers.",
        "applications": "Villa entry staircases, terraced garden steps, and civic amphitheater seating.",
        "crate_yield": "Custom-crated by staircase flight with numbered CAD shop-drawing labels."
    },
    {
        "slug": "driveway-cobblestones-setts",
        "title": "Heavy-Duty Limestone Driveway Cobblestones, Porphyry-Style Setts & Fan Kits",
        "code": "TY-CAT-07",
        "kb_id": "RW-TYCCAT-0207",
        "dimensions": "100×100×40/50mm, 100×200×50mm, 150×150×50mm, 200×200×50mm (Loose or Mesh-Backed)",
        "hero_img": "assets/images/products/canghai_scene.webp",
        "summary": "High-compressive-strength (>105 MPa) tumbled, bush-hammered, and natural-split limestone cobbles for vehicular driveways and heritage streetscapes.",
        "applications": "Vehicular driveways, motor courts, porte-cochères, apron borders, and tree pits.",
        "crate_yield": "40mm: 240 m² / 20GP | 50mm: 190 m² / 20GP."
    },
    {
        "slug": "architectural-columns-pillars-balustrades",
        "title": "5-Axis CNC Limestone Architectural Columns, Capitals, Bases & Balustrades",
        "code": "TY-CAT-08",
        "kb_id": "RW-TYCCAT-0208",
        "dimensions": "Ø 300mm to Ø 1200mm (Solid or Hollow-Core Cladding); Custom Heights per CAD",
        "hero_img": "assets/images/about/craftsman_stonemason.webp",
        "summary": "Precision 5-axis CNC turned and hand-finished classical and contemporary stone columns, Roman capitals, entablatures, and turned balusters.",
        "applications": "Luxury villa porticos, hotel colonnades, balcony balustrades, and estate entry gates.",
        "crate_yield": "100% pre-assembled at factory for dry-fit verification prior to numbered crating."
    },
    {
        "slug": "fluted-ribbed-3d-wall-panels",
        "title": "CNC Fluted, Ribbed, Bamboo-Grooved & 3D Textural Limestone Wall Panels",
        "code": "TY-CAT-09",
        "kb_id": "RW-TYCCAT-0209",
        "dimensions": "600×300×20/25mm, 600×400×25mm, 900×300×30mm (Scallop, Reeding, & Linear Flute Profiles)",
        "hero_img": "assets/images/hero/scene-facade.webp",
        "summary": "Contemporary architectural CNC-milled linear flutes, concave scallops, and rhythmic 3D stone reliefs designed to catch grazing LED and natural sunlight.",
        "applications": "Hotel reception feature walls, boutique retail facades, fireplace chimneys, and bar fronts.",
        "crate_yield": "Approx. 450–500 m² per 20GP container."
    },
    {
        "slug": "cnc-slotted-pool-drain-grates",
        "title": "CNC-Slotted Limestone Pool Trench Drain Grates & Linear Slot Covers",
        "code": "TY-CAT-10",
        "kb_id": "RW-TYCCAT-0210",
        "dimensions": "600×200×30mm, 600×250×30mm, 600×300×30/40mm (Waterjet / CNC Drainage Slots & Holes)",
        "hero_img": "assets/images/resources/cad_blueprints.webp",
        "summary": "Removable solid limestone drain grating that replaces plastic or metal trench covers with seamless stone matching the surrounding pool deck.",
        "applications": "Overflow swimming pool perimeters, terrace drainage trenches, and spa wet rooms.",
        "crate_yield": "Shipped in mixed containers alongside matching pool pavers and coping."
    },
    {
        "slug": "wall-capping-pier-caps-parapets",
        "title": "Limestone Wall Coping, Apex Pier Caps & Drip-Grooved Parapet Stones",
        "code": "TY-CAT-11",
        "kb_id": "RW-TYCCAT-0211",
        "dimensions": "Wall Caps: 600–1000×250–450×40/50mm | Pier Caps: 500×500 to 900×900mm (Flat or 4-Way Apex)",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Weather-shedding limestone wall cappings and gate-pillar pier caps fabricated with dual underside 8×8mm water-drip grooves (throating) to protect masonry walls below from rainwater streaking.",
        "applications": "Garden boundary walls, retaining wall tops, rooftop parapets, and gate pillars.",
        "crate_yield": "Custom-sized to wall thickness + 50–80mm overhang."
    },
    {
        "slug": "window-sills-architraves-lintels",
        "title": "Limestone Window Sills, Door Architraves, Keystones & Facade Mouldings",
        "code": "TY-CAT-12",
        "kb_id": "RW-TYCCAT-0212",
        "dimensions": "Custom lengths up to 2200mm; Thickness 30mm–120mm per Architectural Elevation CAD",
        "hero_img": "assets/images/about/craftsman_stonemason.webp",
        "summary": "Precision CNC-profiled exterior window sills (with integrated water-shedding slope and drip groove), door surrounds, cornice mouldings, and belt courses.",
        "applications": "Neo-classical villas, townhome facades, and heritage commercial buildings.",
        "crate_yield": "Numbered by elevation and window opening ID on every crate."
    },
    {
        "slug": "garden-stepping-stones-zen-pads",
        "title": "Large-Format Limestone Garden Stepping Stones, Zen Pavers & Lawn Pads",
        "code": "TY-CAT-13",
        "kb_id": "RW-TYCCAT-0213",
        "dimensions": "900×450×40mm, 1000×500×40/50mm, 1200×600×50mm, & Organic Round/Pebble Pads",
        "hero_img": "assets/images/related/crazy-paving.webp",
        "summary": "Thick-gauge monolithic limestone stepping pads heavy enough to sit stably in gravel, turf, or shallow water basins without shifting.",
        "applications": "Japanese Zen gardens, resort water-crossing walkways, and lawn pathways.",
        "crate_yield": "Approx. 200–250 m² per 20GP container."
    },
    {
        "slug": "travertine-pavers",
        "title": "Limestone Landscape Kerbstones, Driveway Edging & Flush Garden Borders",
        "code": "TY-CAT-14",
        "kb_id": "RW-TYCCAT-0214",
        "dimensions": "1000×150×250mm, 1000×120×200mm, 600×100×150mm (Chamfered, Bullnose, or Split-Top)",
        "hero_img": "assets/images/products/canghai_scene.webp",
        "summary": "Solid limestone kerbing and radial curve segments that restrain vehicular cobblestone driveways and frame planting beds.",
        "applications": "Driveway edge restraint, municipal streetscapes, and formal parterre gardens.",
        "crate_yield": "Approx. 450–650 linear meters per 20GP container."
    },
    {
        "slug": "carved-stone-basins-sinks-planters",
        "title": "5-Axis CNC Solid-Block Carved Limestone Washbasins, Freestanding Tubs & Planters",
        "code": "TY-CAT-15",
        "kb_id": "RW-TYCCAT-0215",
        "dimensions": "Basins: 500–900×400×150mm | Planters: 600×600×600mm to 1200×500×500mm",
        "hero_img": "assets/images/about/factory_fabrication.webp",
        "summary": "Carved from a single solid block of dense limestone—eliminating glue joints—for luxury hotel powder rooms, spa courtyards, and architectural terrace planters.",
        "applications": "Boutique hotels, wellness spas, outdoor shower pavilions, and villa entryways.",
        "crate_yield": "Individually foam-crated; ideal for consolidating into empty volume space in paver containers."
    },
    {
        "slug": "sandstone-pavers",
        "title": "ADA / AS 1428.4 CNC-Milled Limestone Tactile Ground Surface Indicators (TGSI)",
        "code": "TY-CAT-16",
        "kb_id": "RW-TYCCAT-0216",
        "dimensions": "300×300×30/40mm, 400×400×40mm, 600×400×40mm (Hazard Studs & Directional Bars)",
        "hero_img": "assets/images/products/canglang_scene.webp",
        "summary": "Monolithic CNC-carved limestone hazard blisters and directional guidance bars that meet municipal accessibility laws without resorting to peeling plastic or steel inserts.",
        "applications": "Civic plazas, transit stations, museum steps, and commercial building ramps.",
        "crate_yield": "Available in contrasting light (`Daiwa` LRV ~62%) and dark (`Modai` LRV ~18%) limestone for >30% luminance contrast."
    },
    {
        "slug": "flexible-stone-veneer",
        "title": "Natural Irregular Fieldstone & Thin-Sawn Boulder Veneer Cladding",
        "code": "TY-CAT-17",
        "kb_id": "RW-TYCCAT-0217",
        "dimensions": "Random Irregular Pieces Ø 150–500mm, Sawn Flat Back 25–40mm Thickness + 90° Corners",
        "hero_img": "assets/images/hero/scene-garden-detail.webp",
        "summary": "Weathered quarry-face limestone fieldstones sawn flat on the back to reduce wall load to ~75 kg/m² while delivering the appearance of 300mm-thick historic dry-stone walls.",
        "applications": "Alpine lodges, winery estates, lodge fireplaces, and retaining wall facades.",
        "crate_yield": "Approx. 350–400 m² per 20GP container."
    },
    {
        "slug": "mcm-flexible-panels",
        "title": "Bespoke Mixed-Container Complete Villa & Resort Hardscape Consolidation Packages",
        "code": "TY-CAT-18",
        "kb_id": "RW-TYCCAT-0218",
        "dimensions": "Custom Multi-SKU Kit: Pavers + Pool Coping + Steps + Wall Cladding + Drain Grates in 1×20GP",
        "hero_img": "assets/images/about/export_crates_logistics.webp",
        "summary": "Turnkey single-container stone consolidation service where our engineering desk fabricates and dry-lays all exterior & interior stone elements for an entire villa or boutique resort from the same quarry vein.",
        "applications": "Custom luxury villas, landscape design-build contractors, and boutique hotel developments.",
        "crate_yield": "100% weight utilization (26–27 MT / 320–500 m² combined) with room-by-room crate labelling."
    }
]


# ==============================================================================
# 4. 25 GLOBAL COUNTRY & PORT IMPORT/COMPLIANCE GUIDES (/markets/{slug}/)
# ==============================================================================
MARKETS_DATA = [
    {
        "slug": "united-states-east-west-coast",
        "country": "United States",
        "region": "North America",
        "kb_id": "RW-TYMKTS-0301",
        "ports": "Los Angeles / Long Beach (14–16d), Houston (26–28d), Savannah (28–30d), New York / Newark (30–32d)",
        "standards": "ASTM C568 (Category III High-Density), ASTM C97, C170, C880, C666, ANSI A326.3 DCOF ≥ 0.60, ISPM-15",
        "hs_duty": "HTS 6802.21 / 6802.91 — Complete Commercial Invoice, Packing List, ISF 10+2 Filing (48h pre-vessel), Certificate of Origin",
        "top_skus": ["guyu", "wangchuan", "daiwa", "canghai"],
        "climate_notes": "Sunbelt states (FL, TX, CA, AZ) prioritize Tumbled & Sandblasted-Brushed French Pattern + 30/75mm Drop-Face pool coping; Northern states (NY, IL, CO, MA) require 30mm–40mm ASTM C666 freeze-thaw certified pavers."
    },
    {
        "slug": "australia-sydney-melbourne-brisbane",
        "country": "Australia",
        "region": "Oceania",
        "kb_id": "RW-TYMKTS-0302",
        "ports": "Sydney / Port Botany (12–14d), Melbourne (14–16d), Brisbane (11–13d), Fremantle / Perth (16–18d)",
        "standards": "AS 4586-2013 Wet Pendulum P4 / P5 Slip Rating, AS/NZS 4456 Masonry Units, DAFF Biosecurity BICON ISPM-15",
        "hs_duty": "0% Duty under ChAFTA (China-Australia Free Trade Agreement Certificate of Origin) + DAFF Clean Container & Fumigation Declaration",
        "top_skus": ["daiwa", "guyu", "zaojing", "wangchuan"],
        "climate_notes": "Strong demand for AS 4586 P5 saltwater pool pavers (600×400×30mm), Rebated Drop-Face Pool Coping (600×350×30/75mm), and Crazy Paving flagstone in warm coastal cream and silver-grey tones."
    },
    {
        "slug": "united-kingdom-london-felixstowe",
        "country": "United Kingdom",
        "region": "Europe",
        "kb_id": "RW-TYMKTS-0303",
        "ports": "Felixstowe (26–29d), Southampton (27–30d), London Gateway (28–31d)",
        "standards": "BS EN 1341 (Exterior Pavers), BS EN 1469 (Cladding), BS 7976-2 Pendulum PTV ≥ 36 (Wet), UKCA / CE DoP",
        "hs_duty": "UK Global Tariff 6802.91 / 6802.10 (0%–2% MFN) — EORI Registration, Commercial Invoice, Packing List, UKCA/CE DoP",
        "top_skus": ["guyu", "qinghe", "canghai", "guyun"],
        "climate_notes": "High demand for Cotswold-style warm honey/buff and antique blue-grey tumbled flagstone (600×Free-Length & Opus Romain/French Pattern) with frost resistance for damp UK winters."
    },
    {
        "slug": "germany-dach-din-en-standards",
        "country": "Germany, Austria & Switzerland (DACH)",
        "region": "Europe",
        "kb_id": "RW-TYMKTS-0304",
        "ports": "Hamburg (27–30d), Bremerhaven (28–31d), or via Rotterdam / Antwerp barge & rail",
        "standards": "DIN EN 1341, DIN EN 1469, DIN EN 12058, DIN 51130 (R11/R12) & DIN 51097 (Class B/C), Strict ±0.5mm CNC Tolerance",
        "hs_duty": "EU TARIC 6802.91 — CE Declaration of Performance (DoP), EN 12440 Petrographic Denomination, ISPM-15",
        "top_skus": ["wangchuan", "canghai", "canglang", "xuansu"],
        "climate_notes": "German and Swiss architects specify Jura-alternative and Muschelkalk-style honed, sandblasted-brushed, and bush-hammered grey/beige pavers and 30–40mm ventilated facade slabs with Fischer undercut anchors."
    },
    {
        "slug": "france-benelux-limestone-import-guide",
        "country": "France, Belgium & Netherlands",
        "region": "Europe",
        "kb_id": "RW-TYMKTS-0305",
        "ports": "Le Havre (26–29d), Marseille-Fos (23–26d), Antwerp (27–30d), Rotterdam (26–29d)",
        "standards": "NF EN 1341 / NBN EN 1341, CE Marking, Opus Romain (French Pattern) & Pierre Bleue Alternative Specifications",
        "hs_duty": "EU Customs Tariff 6802.21 / 6802.91 — CE DoP, Commercial Invoice, EUR-compliant Packing List",
        "top_skus": ["guyu", "qinghe", "canglang", "canghai"],
        "climate_notes": "Strong demand for Dalles Opus Romain (French Pattern) in warm Provence beige (`Guyu`, `Qingzhan`) and Belgian Blue Stone alternative (`Canglang`, `Zhulilin`) in bush-hammered and antique tumbled finishes."
    },
    {
        "slug": "canada-freeze-thaw-limestone-import-guide",
        "country": "Canada",
        "region": "North America",
        "kb_id": "RW-TYMKTS-0306",
        "ports": "Vancouver (13–15d), Prince Rupert (12–14d), Toronto / Montreal via rail or all-water (28–34d)",
        "standards": "ASTM C666 Freeze-Thaw (100 Cycles), CSA A231.1 / ASTM C568 III, CBSA eManifest & ISPM-15",
        "hs_duty": "Canadian Customs Tariff 6802.21 / 6802.91 — CCI (Canada Customs Invoice), B/L, ISPM-15 Certificate",
        "top_skus": ["canghai", "canglang", "wangchuan", "xuanzhen"],
        "climate_notes": "Requires low-absorption (≤ 1.8%), 30mm–50mm bush-hammered and sandblasted limestone pavers, step treads, and stone veneer engineered for severe Ontario, Quebec, and Alberta winter freeze-thaw cycles."
    },
    {
        "slug": "uae-dubai-abu-dhabi-gulf-projects",
        "country": "United Arab Emirates (Dubai & Abu Dhabi)",
        "region": "Middle East (GCC)",
        "kb_id": "RW-TYMKTS-0307",
        "ports": "Jebel Ali, Dubai (14–16d), Khalifa Port, Abu Dhabi (15–17d)",
        "standards": "Dubai Green Building Regulations (High SRI ≥ 64), Estidama Pearl Rating, ASTM C568 III / BS EN 1469",
        "hs_duty": "GCC Unified Tariff 5% CIF — Legalized Certificate of Origin (CCPIT) & Commercial Invoice, Packing List",
        "top_skus": ["daiwa", "hanbai", "wangchuan", "shanshui"],
        "climate_notes": "Focuses on cool-touch light cream/ivory limestone (`Daiwa`, `Tingxue`) for beachfront resort pool decks, royal villa facades, and CNC-carved mashrabiya & column cladding."
    },
    {
        "slug": "saudi-arabia-saber-saso-limestone-guide",
        "country": "Saudi Arabia (KSA)",
        "region": "Middle East (GCC)",
        "kb_id": "RW-TYMKTS-0308",
        "ports": "Jeddah Islamic Port (16–18d), King Abdulaziz Port Dammam (16–18d), Riyadh Dry Port",
        "standards": "SASO 2879 / Technical Regulation for Building Materials, SABER PCoC & SCoC, Mandatory Country of Origin Marking",
        "hs_duty": "GCC Tariff + Mandatory SABER Product & Shipment Certificate of Conformity (PCoC/SCoC) & Pallet/Crate Country of Origin Stamping",
        "top_skus": ["daiwa", "wangchuan", "shanshui", "guyu"],
        "climate_notes": "Supporting Vision 2030 hospitality, Red Sea coastal resorts, and Riyadh Diriyah-inspired heritage/contemporary villa developments with high-SRI limestone."
    },
    {
        "slug": "russia-moscow-st-petersburg-gost",
        "country": "Russian Federation",
        "region": "CIS & Eurasia (EAEU)",
        "kb_id": "RW-TYMKTS-0309",
        "ports": "Vladivostok / Vostochny (5–7d Sea + Rail to Moscow 18–22d), Novorossiysk (24–28d), St. Petersburg (32–36d), Manzhouli/Zabaikalsk Rail",
        "standards": "GOST 30629-2011 (Facing Slabs), GOST 9479-2011 (Blocks), Frost Grade F100, NRB-99/2009 Class 1 (<370 Bq/kg)",
        "hs_duty": "EAEU TN VED 6802 21 000 0 / 6802 91 000 0 — EAEU Declaration of Conformity, Radiation Hygiene Certificate, Bilingual RU/EN Packing List",
        "top_skus": ["canghai", "wangchuan", "canglang", "xieshan"],
        "climate_notes": "Requires F100 frost-resistant 30mm–40mm ventilated facade slabs (NVF) and heavy courtyard pavers in Moscow, St. Petersburg, Kazan, and Sochi resorts. Full Russian technical portal at /ru/."
    },
    {
        "slug": "kazakhstan-almaty-astana-limestone-guide",
        "country": "Kazakhstan",
        "region": "CIS & Central Asia (EAEU)",
        "kb_id": "RW-TYMKTS-0310",
        "ports": "Khorgos / Altynkol Rail Gateway (12–15d direct block train from China to Almaty & Astana)",
        "standards": "GOST 30629-2011 (F100 Frost Grade for Astana -40°C), SN RK 3.02-17-2011, NRB Class 1",
        "hs_duty": "EAEU Unified Customs Territory (TN VED 6802) — SMGS Railway Consignment Note, Certificate of Origin, GOST Passports",
        "top_skus": ["wangchuan", "canghai", "daiwa", "xieshan"],
        "climate_notes": "Astana requires F100 extreme freeze-thaw ventilated facade panels (30–40mm); Almaty requires seismic-safe mechanical anchoring and luxury villa landscaping stone."
    },
    {
        "slug": "uzbekistan-tashkent-samarkand-limestone-guide",
        "country": "Uzbekistan",
        "region": "CIS & Central Asia",
        "kb_id": "RW-TYMKTS-0311",
        "ports": "Tashkent / Sergeli & Samarkand via China-Kyrgyzstan-Uzbekistan Multimodal or Khorgos-Kazakhstan Rail (14–18d)",
        "standards": "O'z DSt / GOST 30629-2011, KMK 2.01.03-19 Seismic Facade Norms, High SRI Thermal Comfort",
        "hs_duty": "Uzbekistan Customs Code 6802 — Certificate of Origin (Form CT-1 / CCPIT), SMGS Rail Bill, Quality Passport",
        "top_skus": ["daiwa", "guyu", "wangchuan", "shanshui"],
        "climate_notes": "Booming hospitality and New Tashkent / Samarkand tourism projects specify warm sand-cream limestone facades, colonnades, and courtyard pavers."
    },
    {
        "slug": "new-zealand-limestone-import-guide",
        "country": "New Zealand",
        "region": "Oceania",
        "kb_id": "RW-TYMKTS-0312",
        "ports": "Auckland (15–17d), Tauranga (16–18d), Lyttelton / Christchurch (18–20d)",
        "standards": "NZBC D1 Access Routes (AS/NZS 4586 P4/P5), NZS 4210 Masonry Construction, MPI Biosecurity ISPM-15",
        "hs_duty": "0% Duty under NZ-China Free Trade Agreement (NZCFTA Certificate of Origin) + MPI Clean Container Declaration",
        "top_skus": ["guyu", "wangchuan", "zaojing", "canglang"],
        "climate_notes": "Auckland & Waiheke Island coastal lodges favor warm tumbled pavers and crazy paving; Queenstown & Wanaka alpine residences specify 30–40mm freeze-thaw bush-hammered stone."
    },
    {
        "slug": "singapore-tropical-limestone-import-guide",
        "country": "Singapore",
        "region": "Southeast Asia (ASEAN)",
        "kb_id": "RW-TYMKTS-0313",
        "ports": "Port of Singapore — PSA Pasir Panjang / Tuas (5–6d Express Sea Freight from Xiamen)",
        "standards": "BCA Slip Resistance (SS 485 / AS 4586 P4–P5), SGBC Green Mark SRI Credits, ASTM C568 III",
        "hs_duty": "0% Customs Duty (Form E ASEAN-China FTA) — Singapore GST applies on CIF",
        "top_skus": ["wangchuan", "daiwa", "xuansu", "canglang"],
        "climate_notes": "Good Class Bungalows (GCBs) in Sentosa Cove and Bukit Timah specify 6-sided factory-sealed tropical rain-resistant limestone pavers, fluted feature walls, and pool coping."
    },
    {
        "slug": "japan-jis-architectural-limestone-guide",
        "country": "Japan",
        "region": "East Asia",
        "kb_id": "RW-TYMKTS-0314",
        "ports": "Tokyo / Yokohama (4–5d), Osaka / Kobe (3–4d), Nagoya (4–5d)",
        "standards": "JIS A 5003 (Natural Building Stone), JIS A 1454 Slip Resistance, Ultra-Strict ±0.5mm Dimensional & Visual Sorting QC",
        "hs_duty": "0% Duty under RCEP Certificate of Origin — Complete Mill Test & 3,000 m² Dry-Lay Inspection Book",
        "top_skus": ["wangchuan", "canghai", "canglang", "zaojing"],
        "climate_notes": "High demand for wabi-sabi bush-hammered, chiseled, and stepping-stone limestone for boutique ryokans, museum courtyards, and luxury Tokyo residences."
    },
    {
        "slug": "south-korea-ks-limestone-import-guide",
        "country": "South Korea",
        "region": "East Asia",
        "kb_id": "RW-TYMKTS-0315",
        "ports": "Busan (2–3d), Incheon (3–4d), Pyeongtaek (3–4d)",
        "standards": "KS F 2518 / KS F 2519 (Absorption & Compressive Strength), Freeze-Thaw F100 for Seoul Winters",
        "hs_duty": "Reduced/0% Tariff under China-Korea FTA (FTA CO) or RCEP Certificate of Origin",
        "top_skus": ["daiwa", "wangchuan", "canghai", "xieshan"],
        "climate_notes": "30mm exterior facade panels and courtyard pavers for Jeju Island luxury resorts, Hannam-dong villas, and commercial retail buildings."
    },
    {
        "slug": "qatar-kuwait-bahrain-oman-gcc-limestone-guide",
        "country": "Qatar, Kuwait, Bahrain & Oman (GCC)",
        "region": "Middle East (GCC)",
        "kb_id": "RW-TYMKTS-0316",
        "ports": "Hamad Port Doha (16–18d), Shuwaikh Kuwait (17–19d), Khalifa Bin Salman Bahrain (16–18d), Sohar Oman (14–16d)",
        "standards": "QCS (Qatar Construction Specifications) Section 15/16, GSAS Sustainability SRI, ASTM C568 III",
        "hs_duty": "GCC Unified 5% Duty — CCPIT Legalized Certificate of Origin & Commercial Invoice",
        "top_skus": ["daiwa", "hanbai", "wangchuan", "guyu"],
        "climate_notes": "High-solar-reflectance ivory and sand-beige limestone for palace compounds, beachfront resorts, and ventilated curtain walls."
    },
    {
        "slug": "spain-portugal-italia-mediterranean-guide",
        "country": "Spain, Portugal & Italy",
        "region": "Southern Europe",
        "kb_id": "RW-TYMKTS-0317",
        "ports": "Valencia / Barcelona (21–24d), Algeciras (23–25d), Lisbon / Sines (25–27d), Genoa / La Spezia (20–23d)",
        "standards": "UNE-EN 1341 / UNI EN 1341, CTE DB-SUA Slip Resistance Class 3 (Rd > 45 for Outdoor Pools), CE DoP",
        "hs_duty": "EU Customs Tariff 6802 — CE Declaration of Performance, Commercial Invoice, ISPM-15",
        "top_skus": ["guyu", "qinghe", "canglang", "xieshan"],
        "climate_notes": "Marbella, Ibiza, Algarve, and Sardinia villa developers specify tumbled French Pattern, drop-face pool coping, and dark fossil limestone."
    },
    {
        "slug": "nordics-sweden-norway-denmark-finland-guide",
        "country": "Sweden, Norway, Denmark & Finland (Nordics)",
        "region": "Northern Europe",
        "kb_id": "RW-TYMKTS-0318",
        "ports": "Gothenburg (29–32d), Oslo (30–33d), Aarhus / Copenhagen (28–31d), Helsinki (31–34d)",
        "standards": "SS-EN 1341 / NS-EN 1341, EN 12371 Severe Freeze-Thaw (56–100 Cycles), Nordic Swan Eco-Compatible Sealer",
        "hs_duty": "EU / EEA Tariff 6802 (0% Duty in Norway for Natural Stone) — CE DoP & Frost Resistance Test Report",
        "top_skus": ["canglang", "xuansu", "wangchuan", "canghai"],
        "climate_notes": "Scandinavian architects prize muted grey/taupe honed and brushed limestone (Öland / Gotland limestone aesthetic) for interior heated floors and frost-rated terraces."
    },
    {
        "slug": "thailand-vietnam-indonesia-philippines-resort-guide",
        "country": "Thailand, Vietnam, Indonesia & Philippines",
        "region": "Southeast Asia (ASEAN)",
        "kb_id": "RW-TYMKTS-0319",
        "ports": "Laem Chabang / Bangkok (6–8d), Ho Chi Minh / Haiphong (4–6d), Jakarta / Surabaya (7–10d), Manila / Cebu (3–5d)",
        "standards": "ASTM C568 III, AS 4586 P5 Pool Deck Slip Resistance, Tropical Monsoon Efflorescence Prevention",
        "hs_duty": "0% Duty under ASEAN-China Free Trade Area (Form E Certificate of Origin)",
        "top_skus": ["guyu", "wangchuan", "zaojing", "xieshan"],
        "climate_notes": "Five-star beach resorts in Phuket, Koh Samui, Da Nang, Phu Quoc, Bali, and Boracay source mixed containers of pool pavers, crazy paving, split-face walls, and carved stone tubs."
    },
    {
        "slug": "malaysia-brunei-asean-limestone-guide",
        "country": "Malaysia & Brunei",
        "region": "Southeast Asia (ASEAN)",
        "kb_id": "RW-TYMKTS-0320",
        "ports": "Port Klang (5–7d), Penang (6–8d), Pasir Gudang / Johor (5–7d), Muara Brunei (6–8d)",
        "standards": "MS EN 1341 / SIRIM Building Material Guidelines, GBI (Green Building Index) SRI Credits",
        "hs_duty": "0% Import Duty with Form E (ACFTA) Certificate of Origin",
        "top_skus": ["wangchuan", "daiwa", "guyu", "canglang"],
        "climate_notes": "Kuala Lumpur, Johor Bahru, and Penang luxury semi-D and bungalow developments specify 20mm/30mm brushed limestone for car porches, lanai terraces, and lap pools."
    },
    {
        "slug": "mexico-caribbean-latin-america-resort-guide",
        "country": "Mexico, Caribbean & Latin America",
        "region": "Americas",
        "kb_id": "RW-TYMKTS-0321",
        "ports": "Manzanillo / Lázaro Cárdenas (18–21d), Veracruz / Altamira (28–32d), Kingston / Nassau / San Juan (26–30d)",
        "standards": "ASTM C568 III, Hurricane Wind-Load Facade Anchoring, Saltwater & High-UV Resistance",
        "hs_duty": "TIGIE / Mercosur 6802.21 / 6802.91 — Certificate of Origin, Spanish Commercial Invoice & Packing List",
        "top_skus": ["daiwa", "guyu", "wangchuan", "qinghe"],
        "climate_notes": "Los Cabos, Riviera Maya, Bahamas, and Turks & Caicos luxury resorts specify cool-touch cream/beige tumbled French Pattern and custom pool coping."
    },
    {
        "slug": "south-africa-indian-ocean-islands-guide",
        "country": "South Africa, Mauritius & Seychelles",
        "region": "Africa & Indian Ocean",
        "kb_id": "RW-TYMKTS-0322",
        "ports": "Durban (18–21d), Cape Town (21–24d), Port Louis Mauritius (14–16d), Victoria Seychelles (15–18d)",
        "standards": "SANS 10109 / BS EN 1341, AS 4586 P5 Coastal Pool Surrounds, ISPM-15",
        "hs_duty": "0% Duty to Mauritius (China-Mauritius FTA) / SARS Tariff 6802 — Certificate of Origin, Packing List",
        "top_skus": ["guyu", "wangchuan", "zaojing", "daiwa"],
        "climate_notes": "Cape Town coastal estates and Mauritius/Seychelles island resorts specify salt-resistant pool pavers, crazy paving, and natural split wall cladding."
    },
    {
        "slug": "israel-eastern-mediterranean-limestone-guide",
        "country": "Israel, Cyprus & Greece",
        "region": "Eastern Mediterranean",
        "kb_id": "RW-TYMKTS-0323",
        "ports": "Haifa / Ashdod (19–22d), Limassol Cyprus (20–22d), Piraeus Greece (19–21d)",
        "standards": "SI 2378 (Natural Stone Cladding), EN 1341 / EN 1469, Seismic Mechanical Dowel Fixing",
        "hs_duty": "HS 6802.21 / 6802.91 — CE DoP, SGS Test Reports, Certificate of Origin",
        "top_skus": ["daiwa", "guyu", "qinghe", "wangchuan"],
        "climate_notes": "High affinity for Jerusalem-stone-compatible warm cream, golden-buff, and fossil grey limestone in tumbled, chiseled, and bush-hammered finishes."
    },
    {
        "slug": "poland-czechia-central-europe-limestone-guide",
        "country": "Poland, Czechia, Hungary & Central Europe",
        "region": "Central Europe",
        "kb_id": "RW-TYMKTS-0324",
        "ports": "Gdansk / Gdynia (28–31d), Hamburg + Rail to Warsaw/Prague/Budapest, or China-Europe Express Rail to Malaszewicze (16–19d)",
        "standards": "PN-EN 1341, PN-EN 1469, ČSN EN 1341, Frost Resistance F100 / EN 12371",
        "hs_duty": "EU TARIC 6802 — CE Declaration of Performance, Commercial Invoice, Packing List",
        "top_skus": ["wangchuan", "canghai", "canglang", "guyu"],
        "climate_notes": "Growing demand for ventilated limestone facades, commercial plaza pavers, and luxury residential terraces across Warsaw, Krakow, Prague, and Budapest."
    },
    {
        "slug": "azerbaijan-georgia-armenia-caucasus-guide",
        "country": "Azerbaijan, Georgia & Armenia (South Caucasus)",
        "region": "CIS & Caucasus",
        "kb_id": "RW-TYMKTS-0325",
        "ports": "Poti / Batumi Georgia (22–25d Sea) or Trans-Caspian Middle Corridor Rail via Aktau to Baku & Tbilisi (16–20d)",
        "standards": "GOST 30629-2011 / EN 1469, Seismic Curtain Wall Norms, High Wind-Load Facade Fixing (Baku)",
        "hs_duty": "0% Duty to Georgia (China-Georgia FTA Certificate of Origin) / EAEU Tariff for Armenia / AZ Customs 6802",
        "top_skus": ["daiwa", "wangchuan", "shanshui", "xieshan"],
        "climate_notes": "Baku, Tbilisi, Batumi, and Yerevan projects specify warm cream and classical beige limestone for ventilated facades, colonnades, and seaside promenades."
    }
]


# ==============================================================================
# 5. 40 NEW TECHNICAL & COMMERCIAL ENGINEERING BLOG GUIDES (/blog/{slug}/)
# ==============================================================================
NEW_BLOG_ARTICLES_DATA = [
    {
        "slug": "astm-c568-category-iii-high-density-limestone-explained",
        "title": "ASTM C568 Category III High-Density Limestone Explained for Architects",
        "category": "Standards & Testing",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0401",
        "hero_img": "assets/images/compliance/lab_testing.webp",
        "summary": "A deep dive into ASTM C568/C568M classification—comparing Category I (Low-Density), Category II (Medium-Density), and Category III (High-Density ≥ 2,560 kg/m³) limestone for exterior paving and load-bearing facades.",
        "key_takeaway": "Always specify ASTM C568 Category III (bulk density ≥ 2,560 kg/m³, absorption ≤ 3.0%, compressive strength ≥ 55 MPa) for outdoor pool decks, freeze-thaw climates, and vehicular paving; Tianya Limestone tests at 2,610–2,680 kg/m³ and 95–118 MPa."
    },
    {
        "slug": "limestone-vs-travertine-pool-decks-comparison",
        "title": "High-Density Limestone vs. Travertine Pool Decks: Density, Void Filling & Salt Resistance",
        "category": "Material Comparisons",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0402",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Engineering comparison between non-vesicular bioclastic limestone and porous travertine around saltwater swimming pools and freeze-thaw patios.",
        "key_takeaway": "Unlike travertine—whose natural Swiss-cheese cavities require cement or resin fillers that frequently pop out under pressure washing and frost—high-density limestone has a solid, non-cavernous matrix with ≤ 1.8% absorption."
    },
    {
        "slug": "limestone-vs-sandstone-exterior-pavers-durability",
        "title": "Limestone vs. Sandstone Exterior Pavers: Water Absorption, Algae & Delamination Analysis",
        "category": "Material Comparisons",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0403",
        "hero_img": "assets/images/hero/scene-garden.webp",
        "summary": "Comparing silicate sandstone (typically 4%–8% water absorption) against high-density calcium-carbonate/dolomitic limestone (0.85%–1.80% absorption) in damp and coastal environments.",
        "key_takeaway": "High-density limestone absorbs up to 75% less moisture than commercial landscape sandstone, drastically reducing green algae growth, winter delamination, and sub-surface salt spalling."
    },
    {
        "slug": "limestone-vs-bluestone-basalt-thermal-reflectance",
        "title": "Limestone vs. Dark Basalt (Bluestone): Solar Reflectance Index (SRI) & Barefoot Pool Deck Comfort",
        "category": "Thermal Performance",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0404",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Measuring surface temperature differentials under 38°C–45°C summer sun between dark volcanic basalt and light-to-medium tone architectural limestone.",
        "key_takeaway": "Cream and silver-grey limestone achieves an SRI of 58–78 and stays 12°C–18°C cooler underfoot than dark volcanic basalt, eliminating barefoot burn hazards around resort pools."
    },
    {
        "slug": "natural-limestone-vs-20mm-outdoor-porcelain-pavers",
        "title": "30mm Natural Limestone vs. 20mm Outdoor Porcelain Pavers: Acoustic, Thermal & Edge Aesthetics",
        "category": "Material Comparisons",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0405",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Why luxury villa architects and heritage estates continue to specify full-body 30mm natural limestone over printed 20mm porcelain tiles.",
        "key_takeaway": "Natural limestone is full-body through its entire 30mm–50mm thickness—allowing authentic bullnose, chiseled, and tumbled edges that never reveal an artificial printed edge or hollow acoustic clatter."
    },
    {
        "slug": "bullnose-vs-drop-face-rebated-pool-coping",
        "title": "Full Bullnose vs. Drop-Face (Rebated) Limestone Pool Coping: Structural & Hydraulic Detailing",
        "category": "Pool & Coping Engineering",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0406",
        "hero_img": "assets/images/resources/cad_blueprints.webp",
        "summary": "Detailed CAD profile comparison of 30mm Full Bullnose, 30mm Arris/Pencil-Edge, and 30/75mm Rebated Drop-Face limestone pool coping.",
        "key_takeaway": "Full Bullnose provides an ergonomic grab edge for family and resort pools, whereas 30/75mm Drop-Face coping delivers a thick, monolithic modern waterline profile over skimmer and infinity pools."
    },
    {
        "slug": "as4586-p5-din51130-r11-slip-resistance-testing-guide",
        "title": "Understanding AS 4586 P4/P5, DIN 51130 R11/R12 & ANSI A326.3 DCOF Slip Ratings for Stone",
        "category": "Standards & Testing",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0407",
        "hero_img": "assets/images/compliance/lab_testing.webp",
        "summary": "Cross-walking Australian Wet Pendulum (SRV/P-rating), German Oil-Wet Ramp (R-rating), Barefoot Ramp (A/B/C), and American Dynamic Coefficient of Friction (DCOF) tests.",
        "key_takeaway": "For exterior pool decks and sloped walkways, specify Bush-Hammered, Chiseled, or Sandblasted-Brushed limestone certified to AS 4586 P5 (SRV > 54) and DIN 51097 Class C."
    },
    {
        "slug": "preventing-efflorescence-picture-framing-limestone-paving",
        "title": "How to Prevent Efflorescence & 'Picture Framing' Moisture Halos on Exterior Limestone Pavers",
        "category": "Installation Engineering",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0408",
        "hero_img": "assets/images/compliance/quality_inspection.webp",
        "summary": "Root-cause chemical analysis of soluble alkali salts migrating from ordinary grey Portland cement beds into natural stone edges.",
        "key_takeaway": "Eliminate efflorescence and edge darkening by specifying (1) low-alkali white C2S1 adhesive or Trass-lime mortar, (2) 100% back-buttering (zero spot-bedding), (3) positive slab waterproofing, and (4) 6-sided breathable pre-sealing."
    },
    {
        "slug": "white-c2s1-adhesive-vs-sand-cement-mortar-bed-stone",
        "title": "White C2S1 Polymer Adhesive vs. Traditional Sand-Cement Mortar Beds for Limestone Installation",
        "category": "Installation Engineering",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0409",
        "hero_img": "assets/images/resources/modular_pattern_diagram.webp",
        "summary": "Comparing thin/medium-bed EN 12004 C2TES1 white flexible adhesives against thick-bed 4:1 sand-cement screeds.",
        "key_takeaway": "White C2S1 polymer-modified adhesive with 100% notched-trowel back-buttering prevents grey shadow bleed-through on light cream limestone (`Daiwa`, `Tingxue`) and accommodates thermal shear stress."
    },
    {
        "slug": "20gp-container-loading-calculator-limestone-pavers",
        "title": "20GP Container Weight & Square-Meterage Calculator for 20mm, 30mm & 50mm Limestone Pavers",
        "category": "Logistics & Procurement",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0410",
        "hero_img": "assets/images/categories/mixed_container_loading.webp",
        "summary": "Exact container payload math explaining why natural stone exports are governed by 20GP road/vessel weight limits (26–27.5 metric tons) rather than cubic volume.",
        "key_takeaway": "At ~2,650 kg/m³ density, a 27-ton 20GP container holds ~650 m² of 15mm tile, ~500 m² of 20mm pavers, ~320 m² of 30mm pavers, or ~190 m² of 50mm driveway cobbles."
    },
    {
        "slug": "how-3000m2-factory-dry-lay-inspection-eliminates-shade-claims",
        "title": "Inside Our 3,000 m² Factory Dry-Lay Hall: How Pre-Shipment Blending Eliminates Site Shade Claims",
        "category": "Quality Control",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0411",
        "hero_img": "assets/images/compliance/quality_inspection.webp",
        "summary": "Step-by-step walkthrough of how Tianya Limestone lays out every commercial project under calibrated daylight lamps before crating.",
        "key_takeaway": "Dry-laying allows our QC engineers to blend natural fossil movement across crates, replace outlier veins, number each piece against the CAD map, and obtain client photo/video approval before vessel booking."
    },
    {
        "slug": "mechanical-fixings-ventilated-limestone-facades-en1469",
        "title": "Designing Mechanically Fixed Limestone Ventilated Rainscreen Facades (EN 1469 & ASTM C1242)",
        "category": "Facade Engineering",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0412",
        "hero_img": "assets/images/hero/scene-facade.webp",
        "summary": "Engineering guide to Continuous Kerf Channels, Pin/Dowel Anchor Holes, and Fischer FZP Undercut Anchors in 30mm and 40mm limestone cladding.",
        "key_takeaway": "Always maintain a minimum 10mm residual stone thickness behind kerf/undercut slots, use AISI 316 (A4) stainless steel brackets, and verify flexural/pull-out safety factors per EN 1469."
    },
    {
        "slug": "gost-30629-2011-f100-frost-resistance-cis-russia-facades",
        "title": "GOST 30629-2011 & F100 Frost Resistance Requirements for Limestone in Russia & Kazakhstan",
        "category": "Global Compliance",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0413",
        "hero_img": "assets/images/compliance/lab_testing.webp",
        "summary": "How Tianya Limestone meets Russian and EAEU GOST 30629-2011 (F100 frost grade, <0.5% water absorption on dense grades, and NRB-99/2009 Class 1 radiation safety).",
        "key_takeaway": "Our dense limestone passes 100 freeze-thaw cycles (-20°C/+20°C saturation) with < 2.1% compressive strength loss and carries Class 1 (<370 Bq/kg) unrestricted residential/public building clearance."
    },
    {
        "slug": "chafta-form-e-rcep-zero-duty-stone-import-certificates",
        "title": "How to Claim 0% Customs Duty on Limestone Imports Using ChAFTA, Form E, RCEP & NZCFTA",
        "category": "Logistics & Procurement",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0414",
        "hero_img": "assets/images/about/export_crates_logistics.webp",
        "summary": "Documentation guide for stone importers in Australia, New Zealand, ASEAN, Japan, and South Korea to eliminate 5%–10% MFN customs tariffs.",
        "key_takeaway": "Tianya Limestone issues official CCPIT / Customs preferential Certificates of Origin (ChAFTA for Australia, Form E for ASEAN, RCEP for Japan/Korea) alongside every Bill of Lading at zero extra fee."
    },
    {
        "slug": "ispm-15-fumigated-crates-daff-australian-biosecurity-guide",
        "title": "ISPM-15 Heat-Treated Stone Crating & Australian DAFF / US CBP Biosecurity Compliance",
        "category": "Logistics & Procurement",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0415",
        "hero_img": "assets/images/categories/mixed_container_loading.webp",
        "summary": "Preventing costly port quarantine holds and re-fumigation demurrage in Sydney, Melbourne, Auckland, and Los Angeles.",
        "key_takeaway": "Every Tianya crate uses debarked, kiln-heated (56°C for 30 min) timber stamped with IPPC ISPM-15 marks, loaded into pressure-washed containers free of soil, bark, and snail/seed contamination."
    },
    {
        "slug": "choosing-limestone-thickness-15mm-20mm-30mm-50mm",
        "title": "How to Specify Limestone Thickness: 15mm vs. 20mm vs. 30mm vs. 50mm by Substrate & Load",
        "category": "Specification Guide",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0416",
        "hero_img": "assets/images/compliance/lab_testing.webp",
        "summary": "Structural thickness selection matrix based on pedestrian vs. vehicular axle loads and rigid concrete vs. flexible aggregate bedding.",
        "key_takeaway": "Use 15–20mm for interior floors and exterior patios bonded to concrete slabs; 30mm for pool decks, coping, pedestals, and sand/gravel beds; and 40–60mm for vehicular driveways."
    },
    {
        "slug": "tumbled-vs-sandblasted-brushed-vs-bush-hammered-limestone",
        "title": "Comparing 5 Architectural Limestone Finishes: Tumbled, Bush-Hammered, Chiseled, Split & Brushed",
        "category": "Surface Finishes",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0417",
        "hero_img": "assets/images/products/canglang_scene.webp",
        "summary": "Visual, tactile, and slip-resistance comparison of the 5 core mechanical textures fabricated on our diamond-CNC and rotary-brush lines.",
        "key_takeaway": "Choose Tumbled for Old-World warmth, Sandblasted & Brushed for barefoot resort elegance, Bush-Hammered for maximum P5 wet grip, Chiseled for linear shadow relief, and Natural Split for rustic walls."
    },
    {
        "slug": "how-to-install-crazy-paving-random-limestone-flagstone",
        "title": "How to Lay Limestone Crazy Paving (Random Flagstone): Sorting, Joint Widths & Grout Ratios",
        "category": "Installation Engineering",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0418",
        "hero_img": "assets/images/related/crazy-paving.webp",
        "summary": "Field guide for landscape contractors installing random polygonal limestone flagstones (`Tianlu`, `Guyu`) with tight, balanced organic joints.",
        "key_takeaway": "Dry-fit large anchor pieces first (3–5 pieces/m²), maintain consistent 15–25mm joint widths, back-butter 100% with white C2S1 adhesive, and pre-seal the top surface before grouting to speed up cleanup."
    },
    {
        "slug": "designing-limestone-driveways-aspect-ratio-subbase-engineering",
        "title": "Engineering Natural Limestone Driveways That Never Crack Under SUV & Truck Loads",
        "category": "Vehicular & Civic Paving",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0419",
        "hero_img": "assets/images/products/canghai_scene.webp",
        "summary": "Why paver aspect ratio (length-to-thickness ≤ 6:1) and full-bed mortar bonding are critical for residential and hotel driveways.",
        "key_takeaway": "Never lay large 600×600×20mm slabs on a driveway; specify 40mm–60mm small-format pavers or cobblestones (e.g., 100×100×50mm or 300×150×40mm) fully bonded to a 150mm reinforced concrete slab."
    },
    {
        "slug": "saltwater-chlorinator-pools-limestone-sealing-protocol",
        "title": "Do Saltwater Chlorinator Pools Damage Limestone? The Complete 6-Sided Consolidation Protocol",
        "category": "Pool & Coping Engineering",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0420",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Understanding sub-florescence (salt crystal expansion inside stone pores) and how dense stone selection + fluoropolymer sealing prevents it.",
        "key_takeaway": "High-density limestone (≤ 1.8% absorption) paired with 6-sided silane-siloxane/fluoropolymer dip-sealing blocks NaCl brine capillary uptake and prevents edge fretting around saltwater pools."
    },
    {
        "slug": "cnc-5-axis-stone-profiling-cad-to-bim-workflow",
        "title": "From Architect's CAD/BIM to 5-Axis CNC Stone Fabrication: Our Custom Millwork Workflow",
        "category": "Custom Fabrication",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0421",
        "hero_img": "assets/images/about/factory_fabrication.webp",
        "summary": "How our engineering desk converts DWG, DXF, and Revit files into precision-milled radial pool coping, fluted columns, and grand staircases.",
        "key_takeaway": "Every custom CNC element is assigned a unique piece code (`EL-A-101`), dry-assembled in our factory for ±0.5mm joint verification, and packed in installation sequence."
    },
    {
        "slug": "jura-limestone-vs-chinese-architectural-limestone-comparison",
        "title": "German Jura & Belgian Bluestone Alternatives: Comparing Petrography, ASTM Specs & Landed Cost",
        "category": "Material Comparisons",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0422",
        "hero_img": "assets/images/about/about_hero_quarry.webp",
        "summary": "Technical and commercial comparison between European quarry stones and Tianya quarry-direct beige and blue-grey bioclastic limestone.",
        "key_takeaway": "Collections like `Wangchuan`, `Daiwa`, `Canglang`, and `Zhulilin` match or exceed European limestone density (2.65 g/cm³) and flexural strength while reducing landed project cost by 35%–50%."
    },
    {
        "slug": "movement-expansion-joints-exterior-stone-paving-bs7533",
        "title": "Where to Place Movement & Expansion Joints in Large Exterior Limestone Terraces (BS 7533 / TCNA EJ171)",
        "category": "Installation Engineering",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0423",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Preventing thermal tenting and reflective slab cracking across sunlit outdoor terraces and pool decks.",
        "key_takeaway": "Install 8–10mm flexible polyurethane or neutral-cure silicone movement joints every 3.6–4.5m outdoors, along all building perimeters, and directly above every structural concrete slab control joint."
    },
    {
        "slug": "cleaning-maintaining-exterior-limestone-ph-neutral-guide",
        "title": "Commercial & Residential Limestone Maintenance Manual: pH-Neutral Cleaning, Poultices & Resealing",
        "category": "Care & Maintenance",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0424",
        "hero_img": "assets/images/products/wangchuan_scene.webp",
        "summary": "Step-by-step maintenance schedule for hotel facilities managers and homeowners, including organic leaf-tannin and oil stain removal.",
        "key_takeaway": "Never use hydrochloric acid, vinegar, or bleach on calcium-carbonate limestone; use pH-neutral (pH 7–9) stone cleaners, low-pressure fan rinsing (< 1,200 PSI), and reseal exterior pool decks every 3–5 years."
    },
    {
        "slug": "split-face-limestone-wall-cladding-installation-corners",
        "title": "How to Install Split-Face Limestone Wall Cladding & Interlocking 90° L-Corner Quoins",
        "category": "Facade Engineering",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0425",
        "hero_img": "assets/images/related/ledger-stone.webp",
        "summary": "Achieving authentic full-bed masonry corners and secure vertical bonding with `Luanshiban`, `Xinyan`, and `Linquan` split-face veneer.",
        "key_takeaway": "Always start from external corners alternating long and short legs of pre-cut 90° L-corner quoins, use non-sag C2TES1 adhesive, and add mechanical stainless steel ties for heights above 3.0 meters."
    },
    {
        "slug": "pedestal-paver-wind-uplift-breaking-load-calculations",
        "title": "Engineering Raised Pedestal Limestone Pavers for High-Rise Rooftops: Breaking Load & Mesh Backing",
        "category": "Commercial & High-Rise Podiums",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0426",
        "hero_img": "assets/images/about/factory_fabrication.webp",
        "summary": "Calculating flexural breaking load (EN 1341) and wind-uplift lock systems for 600×600mm and 600×400mm rooftop pedestal pavers.",
        "key_takeaway": "Specify minimum 30mm–40mm thickness with factory-applied epoxy fiberglass anti-fragmentation backing mesh and mid-span support pedestals for heavy rooftop terrace modules."
    },
    {
        "slug": "underfloor-heating-limestone-thermal-conductivity-screed",
        "title": "Installing Natural Limestone Over Hydronic & Electric Underfloor Heating: Thermal Conductivity & Screed Cure",
        "category": "Interior Architectural Flooring",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0427",
        "hero_img": "assets/images/products/wangchuan_scene.webp",
        "summary": "Commissioning protocol for heated screeds, uncoupling membranes, and 15mm–20mm brushed limestone floor tiles.",
        "key_takeaway": "With thermal conductivity λ ≈ 2.1 W/(m·K), dense limestone transfers radiant heat faster than timber or carpet; always run a gradual 5°C/day thermal commissioning cycle before and after tiling."
    },
    {
        "slug": "mixed-container-consolidation-guide-villa-contractors",
        "title": "How Landscape Contractors Save 35% by Consolidating Pavers, Coping, Steps & Cladding in One 20GP Container",
        "category": "Logistics & Procurement",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0428",
        "hero_img": "assets/images/about/export_crates_logistics.webp",
        "summary": "Real-world bill of quantities (BOQ) breakdown showing how a 320 m² villa hardscape package fits into a single 27-ton 20GP container from Xiamen.",
        "key_takeaway": "Our Mixed-Container Consolidation Program allows up to 4–5 stone profiles cut from the same quarry vein in one 20GP container—eliminating middleman distributor markups and color mismatches."
    },
    {
        "slug": "custom-limestone-stair-treads-nosing-profiles-anti-slip",
        "title": "Architectural Stair Tread Detailing: Bullnose, Mitred Drop-Apron & CNC Anti-Slip Grooves",
        "category": "Circulation & Hardscape",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0429",
        "hero_img": "assets/images/hero/scene-garden-detail.webp",
        "summary": "Specifying monolithic 30mm–50mm step treads and 150mm solid block steps for exterior staircases.",
        "key_takeaway": "Integrate triple CNC-milled 5×2mm grip grooves or a contrasting 50mm bush-hammered nosing band 25mm back from the leading edge to meet commercial stair safety codes."
    },
    {
        "slug": "concealed-slot-drainage-limestone-pool-grates-detailing",
        "title": "Replacing Plastic Trench Drains with CNC-Slotted Solid Limestone Drain Grates & Slot Channels",
        "category": "Pool & Coping Engineering",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0430",
        "hero_img": "assets/images/resources/cad_blueprints.webp",
        "summary": "Hydraulic open-area ratios and span thicknesses for removable 30mm/40mm CNC-slotted stone trench drain covers.",
        "key_takeaway": "30mm CNC-milled limestone grates with 8mm rounded drainage slots and chamfered finger-lift notches provide 100% visual continuity across luxury pool decks."
    },
    {
        "slug": "freeze-thaw-deicing-salts-winter-limestone-care",
        "title": "Winter Care for Exterior Limestone in Cold Climates: Which De-Icing Agents Are Safe?",
        "category": "Care & Maintenance",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0431",
        "hero_img": "assets/images/compliance/lab_testing.webp",
        "summary": "Chemical impact of sodium chloride (NaCl), calcium chloride (CaCl2), ammonium sulfate, and calcium magnesium acetate (CMA) on natural stone.",
        "key_takeaway": "Avoid rock salt (NaCl) and never use ammonium-based fertilizers/de-icers on limestone; use Calcium Magnesium Acetate (CMA), clean traction sand, or embedded hydronic snow-melt loops."
    },
    {
        "slug": "color-enhancing-vs-natural-look-invisible-stone-sealers",
        "title": "Natural-Look Invisible vs. Color-Enhancing Penetrating Sealers: Which Should You Specify?",
        "category": "Care & Maintenance",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0432",
        "hero_img": "assets/images/products/guyu_scene.webp",
        "summary": "Optical and chemical differences between invisible fluoropolymer impregnators and wet-look/color-enhancing siloxane sealers.",
        "key_takeaway": "Specify Natural-Look invisible impregnators to preserve pale chalky coastal tones (`Daiwa`, `Tingxue`), or Color-Enhancing penetrating sealers to deepen rich charcoal/bronze veins (`Canglang`, `Guyu`)."
    },
    {
        "slug": "understanding-fossil-shell-vein-characteristics-natural-limestone",
        "title": "Petrographic Guide to Bioclastic Fossils, Calcite Veins & Stylolites in Architectural Limestone",
        "category": "Geology & Petrography",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0433",
        "hero_img": "assets/images/about/about_hero_quarry.webp",
        "summary": "Educating architects and end-clients on the distinction between natural geological signatures (calcified shells, crystalline calcite veins) and structural cracks.",
        "key_takeaway": "Closed crystalline calcite veins and ancient marine shell fossils are fully calcified geological features with equal compressive strength to the surrounding stone matrix—whereas open structural fissures are 100% rejected during our dry-lay QC."
    },
    {
        "slug": "fob-xiamen-vs-cif-vs-ddp-incoterms-stone-importers",
        "title": "FOB Xiamen vs. CIF Port vs. DDP Job-Site: Choosing the Right Incoterm for Stone Procurement",
        "category": "Logistics & Procurement",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0434",
        "hero_img": "assets/images/about/export_crates_logistics.webp",
        "summary": "Comparing total landed cost, marine insurance coverage (ICC-A), and customs clearance responsibilities across FOB, CFR, CIF, and DAP/DDP terms.",
        "key_takeaway": "Established stone wholesalers typically prefer FOB Xiamen (`CNXMN`) using their own freight contracts, while villa developers and contractors prefer CIF Destination Port with Institute Cargo Clauses (A) all-risk marine insurance."
    },
    {
        "slug": "saso-saber-dubai-green-building-sri-limestone-middle-east",
        "title": "Exporting Architectural Limestone to Saudi Arabia & UAE: SABER PCoC/SCoC & High-SRI Compliance",
        "category": "Global Compliance",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0435",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Complete compliance checklist for KSA SASO Technical Regulation for Building Materials, SABER registration, country-of-origin engraving, and UAE Estidama SRI.",
        "key_takeaway": "Tianya Limestone coordinates QIMA/SGS/Intertek SABER inspection, permanent 'Made in China' crate/pallet marking, and CCPIT-legalized origin documents for seamless Jeddah, Dammam, and Jebel Ali clearance."
    },
    {
        "slug": "acoustic-absorption-textured-fluted-limestone-interiors",
        "title": "Acoustic Diffusion & Sound Scattering with Chiseled & CNC-Fluted Limestone Wall Cladding",
        "category": "Facade Engineering",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0436",
        "hero_img": "assets/images/hero/scene-facade.webp",
        "summary": "How multi-depth chiseled flutes and split-face relief break up flutter echo in double-height hotel lobbies, auditoriums, and luxury dining rooms.",
        "key_takeaway": "Unlike flat glass or polished marble that reflect harsh high-frequency sound waves, 3D fluted and hand-chiseled limestone (`Luanshiban`, `Xinyan`) scatters mid-to-high frequency reflections."
    },
    {
        "slug": "how-to-verify-stone-factory-authenticity-avoid-trading-markups",
        "title": "Quarry-Direct Factory vs. Trading Company: 7 Engineering Checks to Verify Your Stone Supplier",
        "category": "Logistics & Procurement",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0437",
        "hero_img": "assets/images/about/factory_fabrication.webp",
        "summary": "How overseas stone buyers verify raw block inventory, 5-axis CNC machinery, and dry-lay yard capacity before placing container deposits.",
        "key_takeaway": "Always request a live WhatsApp video walk-through of the raw block yard, gang-saw/CNC lines, and the 3,000 m² dry-lay hall, plus sample archive ID (`SMP-`) traceability."
    },
    {
        "slug": "leed-v4-breeam-epd-sustainability-credits-natural-limestone",
        "title": "Embodied Carbon & LEED v4 / BREEAM Sustainability Credits: Why Natural Limestone Beats Concrete & Ceramic",
        "category": "Sustainability & Green Building",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0438",
        "hero_img": "assets/images/about/about_hero_quarry.webp",
        "summary": "Comparing Cradle-to-Gate embodied carbon (kg CO2e/m²) between mechanically quarried natural limestone and kiln-fired porcelain or Portland cement pavers.",
        "key_takeaway": "Because natural limestone requires zero 1,200°C kiln firing or cement calcination, its embodied carbon footprint is 60%–75% lower than porcelain or concrete pavers, contributing to LEED v4 Heat Island (SRI) and Material credits."
    },
    {
        "slug": "wall-coping-pier-caps-drip-groove-throating-detailing",
        "title": "Why Underside Drip Grooves (Throating) Are Essential on Limestone Wall Coping & Parapet Caps",
        "category": "Specification Guide",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0439",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Preventing rainwater capillary run-back and dark vertical staining down rendered or stone-clad boundary walls.",
        "key_takeaway": "Specify a minimum 40–50mm overhang on both sides of wall cappings with CNC-cut 8×8mm underside drip grooves positioned 15–20mm inward from the outer edge."
    },
    {
        "slug": "complete-checklist-for-submitting-an-architectural-stone-rfq",
        "title": "The Architect & Importer's 10-Point RFQ Checklist for Fast, Accurate Limestone Container Quotes",
        "category": "Logistics & Procurement",
        "date": "2026-10-22",
        "kb_id": "RW-TYBLOG-0440",
        "hero_img": "assets/images/contact/sample_kit_box.webp",
        "summary": "How providing 5 core parameters enables our engineering desk to return a Good/Better/Best container breakdown within 12 hours.",
        "key_takeaway": "Share your (1) Application & Climate, (2) Preferred Collection/Color, (3) Format & Thickness, (4) Approximate Area (m²), and (5) Destination Port—and receive a complete FOB/CIF quotation within 12 hours."
    }
]

# ==============================================================================
# 6. 11 NEW RUSSIAN / CIS GOST 30629-2011 TECHNICAL PAGES (/ru/{slug}/)
# ==============================================================================
RU_SUBPAGES_DATA = [
    {
        "slug": "gost-30629-2011-tablica-ispitanij",
        "title": "ГОСТ 30629-2011 и ГОСТ 9479-2011: Полная таблица физико-механических испытаний известняка Tianya",
        "short_title": "ГОСТ 30629-2011 Протоколы",
        "kb_id": "RW-TYRUCIS-0501",
        "hero_img": "assets/images/compliance/lab_testing.webp",
        "summary": "Официальные показатели плотности (2650 кг/м³), водопоглощения (0,85–1,80%), предела прочности при сжатии (95–118 МПа), морозостойкости F100 и I класса радиационной безопасности (НРБ-99/2009) для сертификации в РФ и странах ЕАЭС.",
        "spec_focus": "Сравнение ГОСТ 30629-2011, ГОСТ 31480, ASTM C568 III и EN 1469 для проектных институтов и застройщиков."
    },
    {
        "slug": "ventiliruemye-fasady-izvestnyak-f100",
        "title": "Навесные вентилируемые фасады (НВФ) из плотного известняка F100: Пропилы, Анкеры Кайль и СП 28.13330",
        "short_title": "НВФ Фасады F100",
        "kb_id": "RW-TYRUCIS-0502",
        "hero_img": "assets/images/hero/scene-facade.webp",
        "summary": "Инженерное руководство по проектированию и поставке фасадных плит из известняка толщиной 30 мм и 40 мм с торцевыми ЧПУ-пропилами и отверстиями под цанговые анкеры (Fischer FZP / Keil) для Москвы, Санкт-Петербурга и Астаны.",
        "spec_focus": "Морозостойкость F100, ветровые нагрузки, подсистемы из нержавеющей стали AISI 316 (A4) и допуски ЧПУ ±0,5 мм."
    },
    {
        "slug": "bruschatka-i-plitka-dlya-moshcheniya",
        "title": "Морозостойкие плиты мощения и брусчатка из известняка (30–50 мм) для климата России и Казахстана",
        "short_title": "Плиты мощения 30–50 мм",
        "kb_id": "RW-TYRUCIS-0503",
        "hero_img": "assets/images/products/canghai_scene.webp",
        "summary": "Тяжелые калиброванные плиты мощения (30/40/50 мм), Французский паттерн (Версаль) и колотая брусчатка с противоскользящей бучардированной (R12) и пескоструйно-брашированной (R11) поверхностью.",
        "spec_focus": "Укладка на бетонное основание с дренажным уклоном 2%, совместимость с системами снеготаяния и стойкость к реагентам."
    },
    {
        "slug": "arhitekturnyj-dekor-kolonny-balyasiny-chpu",
        "title": "5-осевая ЧПУ обработка известняка: Колонны, Капители, Балясины, Карнизы и Наличники по чертежам DWG",
        "short_title": "5-осевой ЧПУ Декор и Колонны",
        "kb_id": "RW-TYRUCIS-0504",
        "hero_img": "assets/images/about/craftsman_stonemason.webp",
        "summary": "Изготовление классического и современного фасадного декора из цельного массива известняка на 5-осевых станках с ЧПУ и 100% контрольной сухой сборкой на заводе перед отправкой.",
        "spec_focus": "Поэлементная маркировка ящиков по осям фасада (`EL-A-101`) и точность сопряжения деталей ±0,5 мм."
    },
    {
        "slug": "bassejny-i-spa-bortovoj-kamen-kapinos",
        "title": "Бортовой камень (Капинос), переливные решетки ЧПУ и противоскользящие плиты для бассейнов и СПА",
        "short_title": "Бассейны и Капиносы",
        "kb_id": "RW-TYRUCIS-0505",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Полный комплект камня для открытых и крытых бассейнов: радиусный профиль Bullnose, Г-образный профиль Drop-Face (30/75 мм), каменные переливные решетки и плиты с классом скольжения C (DIN 51097).",
        "spec_focus": "Стойкость к солевому электролизу, хлорированной воде и низкий нагрев на солнце (SRI 64–78) для курортов Сочи, Крыма, Алматы и Ташкента."
    },
    {
        "slug": "faktury-obrabotki-buchardirovannyj-antiko",
        "title": "5 архитектурных фактур известняка Tianya: Антико (Галтованный), Бучардированный, Тесаный, Колотый и Браш",
        "short_title": "5 Фактур обработки",
        "kb_id": "RW-TYRUCIS-0506",
        "hero_img": "assets/images/products/canglang_scene.webp",
        "summary": "Подробный технический обзор 5 видов фактурной обработки поверхности известняка, их коэффициентов трения (R10–R12) и сфер применения в фасадном и ландшафтном строительстве.",
        "spec_focus": "Подбор оптимальной фактуры под ТЗ архитектора из 29 базовых коллекций."
    },
    {
        "slug": "suhaya-raskladka-3000m2-kontrol-kachestva",
        "title": "Сухая раскладка 3000 м² (Dry-Lay QC): Как мы гарантируем однородность тона и геометрию партии",
        "short_title": "Сухая раскладка 3000 м²",
        "kb_id": "RW-TYRUCIS-0507",
        "hero_img": "assets/images/compliance/quality_inspection.webp",
        "summary": "Регламент предотгрузочного контроля качества на заводе Fujian Tianya: селекция блоков из одного пласта карьера, лазерная калибровка, сухая раскладка на площади 3000 м² и фото/видео приемка заказчиком.",
        "spec_focus": "Исключение разнотона, открытых трещин и отклонений геометрии до погрузки в контейнер."
    },
    {
        "slug": "logistika-zhd-i-more-rossiya-sng",
        "title": "Логистика и нормы загрузки 20GP контейнеров (26–27,5 т): Ж/Д через Маньчжурию/Забайкальск и море через Владивосток/Новороссийск",
        "short_title": "Логистика и расчет 20GP",
        "kb_id": "RW-TYRUCIS-0508",
        "hero_img": "assets/images/about/export_crates_logistics.webp",
        "summary": "Таблицы загрузки 20-футовых контейнеров по толщинам (15/20/30/40/50 мм), упаковка в термообработанные ящики ISPM-15 и маршруты доставки в Москву, Екатеринбург, Новосибирск, Алматы и Ташкент.",
        "spec_focus": "Расчет стоимости доставки за м² при загрузке 26,5–27,5 тонн нетто в 20GP."
    },
    {
        "slug": "tamozhennoe-oformlenie-tn-ved-6802-eaes",
        "title": "Таможенное оформление известняка в ЕАЭС: Коды ТН ВЭД 6802, Сертификат происхождения и Радиационный контроль",
        "short_title": "ТН ВЭД 6802 и Таможня ЕАЭС",
        "kb_id": "RW-TYRUCIS-0509",
        "hero_img": "assets/images/categories/mixed_container_loading.webp",
        "summary": "Полный пакет экспортных документов от завода-изготовителя для беспрепятственной таможенной очистки каменных плит и архитектурных изделий по кодам ТН ВЭД 6802 21 000 0 и 6802 91 000 0.",
        "spec_focus": "Двуязычный упаковочный лист (RU/EN), сертификат происхождения CCPIT, акт фумигации ISPM-15 и паспорт качества по ГОСТ 30629-2011."
    },
    {
        "slug": "kazahstan-astana-almaty-postavka-izvestnyaka",
        "title": "Прямые поставки архитектурного известняка в Казахстан (Астана, Алматы, Шымкент) через Хоргос / Алтынколь",
        "short_title": "Поставки в Казахстан (РК)",
        "kb_id": "RW-TYRUCIS-0510",
        "hero_img": "assets/images/hero/scene-garden.webp",
        "summary": "Оптимизированная ж/д и мультимодальная доставка фасадного и ландшафтного известняка Tianya в Республику Казахстан за 12–15 дней через погранпереход Хоргос / Алтынколь.",
        "spec_focus": "Морозостойкость F100 для экстремального климата Астаны (-40°C) и сейсмостойкие фасадные узлы для Алматы (СН РК)."
    },
    {
        "slug": "uzbekistan-tashkent-samarkand-postavka-izvestnyaka",
        "title": "Прямые поставки известняка с карьера в Узбекистан (Ташкент, Самарканд, Бухара): Фасады и Ландшафт",
        "short_title": "Поставки в Узбекистан (РУз)",
        "kb_id": "RW-TYRUCIS-0511",
        "hero_img": "assets/images/hero/scene-terrace.webp",
        "summary": "Фасадные плиты светло-кремовых и песочных оттенков (`Daiwa`, `Guyu`, `Wangchuan`, `Chongshan`), 5-осевые колонны и термокомфортные плиты мощения для жилых комплексов, отелей и государственных объектов в Новом Ташкенте и Самарканде.",
        "spec_focus": "Высокий индекс солнечного отражения (SRI 64–78), сейсмостойкость по КМК 2.01.03-19 и прямая ж/д доставка по накладной СМГС."
    }
]
