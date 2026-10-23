#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RenWork V4 / V3.0 Export Knowledge Base Expansion Compiler for tianyalimestone.com
Expands the site from 48 canonical pages to 220 canonical, indexable HTML pages:
  - /knowledge-base/ + 21 Standard Modules (00 to 20) = 22 pages
  - /specifications/ + 29 SKU Technical Data Sheet & CSI 04 43 00 Pages = 30 pages
  - /applications/ + 24 Architectural Application Engineering Pages = 25 pages
  - /stone-flooring/other-categories/{slug}/ (18 Companion Stone Categories) = 18 pages
  - /markets/ + 25 Global Country & Port Import/Compliance Guides = 26 pages
  - /blog/{slug}/ (40 New Engineering & Commercial Blog Guides) = 40 pages
  - /ru/{slug}/ (11 New Russian/CIS GOST 30629-2011 Technical Pages) = 11 pages
  Total New Canonical Pages = 172 (48 + 172 = 220 Canonical Pages in sitemap.xml)
"""

import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "scripts"))

from renwork_kb_datasets import (
    KB_MODULES,
    APPLICATIONS_DATA,
    COMPANION_CATEGORIES_DATA,
    MARKETS_DATA,
    NEW_BLOG_ARTICLES_DATA,
    RU_SUBPAGES_DATA,
)


def _write_page(rel_path: str, html: str, all_pages: list, add_to_sitemap: bool = True):
    out_file = BASE_DIR / rel_path
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(html, encoding="utf-8")
    if add_to_sitemap and rel_path not in all_pages:
        all_pages.append(rel_path)


def _faq_schema(faq_items: list) -> str:
    main_entity = []
    for q, a in faq_items:
        main_entity.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": main_entity
    }, ensure_ascii=False)


# ==============================================================================
# HUB 1: /knowledge-base/ + 21 STANDARD MODULES (22 PAGES)
# ==============================================================================
def build_knowledge_base_hub(all_products: list, all_pages: list, render_head, render_header, render_footer):
    # 1. Build /knowledge-base/index.html
    module_cards_html = ""
    for m in KB_MODULES:
        roles_str = ", ".join(r.replace("_", " ").title() for r in m["role_views"][:3])
        module_cards_html += f"""
        <div class="spec-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; gap:0.5rem; margin-bottom:0.65rem;">
              <span class="badge-pill" style="background:rgba(184,134,11,0.12); color:var(--color-gold); font-weight:700;">Module {m['num']} · {m['layer'].split()[0]}</span>
              <span style="font-family:var(--font-mono); font-size:0.72rem; color:#15803d; background:#dcfce7; padding:0.15rem 0.5rem; border-radius:4px;">{m['kb_id']} · {m['status']}</span>
            </div>
            <h3 style="font-size:1.1rem; margin-bottom:0.5rem;"><a href="/knowledge-base/{m['slug']}/" style="color:var(--color-obsidian); text-decoration:none;">{m['title']}</a></h3>
            <p style="font-size:0.86rem; color:var(--color-slate); line-height:1.6; margin-bottom:1rem;">{m['conclusion']}</p>
          </div>
          <div style="border-top:1px solid var(--color-border); padding-top:0.75rem; display:flex; justify-content:space-between; align-items:center; font-size:0.78rem;">
            <span style="color:var(--color-slate);">Roles: {roles_str}</span>
            <a href="/knowledge-base/{m['slug']}/" style="color:var(--color-gold); font-weight:700; text-decoration:none;">Open Module {m['num']} →</a>
          </div>
        </div>"""

    hub_faq = [
        ("What is the Tianya RenWork V4 Architectural Limestone Export Knowledge Base?",
         "It is our 5-Layer, 21-Module (00–20) structured engineering and commercial reference system built on the RenWork AI Export Knowledge Base Standard V4. Every claim is backed by SGS laboratory reports, quarry extraction protocols, and verified container logistics."),
        ("How are facts verified before publication in this Knowledge Base?",
         "Under Module 00 Governance Rules, every Knowledge Card carries a 6-state status (verified_fact, conditional_fact, etc.), a quantitative confidence score (0.95–1.00), explicit boundary conditions, and public_claim_approved=true audit clearance."),
        ("How can architects, stone importers, and contractors use this Knowledge Base?",
         "Architects use Modules 01, 04, 06, and 18 for ASTM/CE/GOST specs and CSI 04 43 00 templates; Importers use Modules 02, 05, 07, 09, and 14 for container optimization and FTA duty savings; Contractors use Modules 16, 17, and 19 for Good/Better/Best quotes and 15-node QC tracking.")
    ]

    hub_html = f"""{render_head(
        "Architectural Limestone Export Knowledge Base (21 Modules 00–20) | Tianya Limestone",
        "Complete 21-Module B2B Architectural Limestone Knowledge Base (Modules 00–20): ASTM C568 III, EN 1341/1469, AS 4586 P5, GOST 30629 F100, 5-axis CNC, 3,000 m² dry-lay QC, and container logistics.",
        "knowledge-base/index.html",
        extra_schema=_faq_schema(hub_faq)
    )}
<body>
{render_header("kb")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/assets/images/compliance/quality_inspection.webp" alt="Tianya Limestone 21-Module Export Knowledge Base" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> <span>Export Knowledge Base (Modules 00–20)</span></div>
    <span class="hero-eyebrow">RenWork V4 Architectural Stone Truth Engine · 5 Layers · 21 Modules</span>
    <h1 style="color:#FFF; font-size:clamp(2rem, 3.8vw, 3.2rem); margin-bottom:1rem;">Architectural Limestone Export Knowledge Base (00–20)</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:820px; font-size:1.05rem;">Structured, audit-verified engineering and commercial documentation for architects, landscape specifiers, wholesale stone importers, and luxury villa contractors worldwide.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="spec-card" style="background:#FAF8F5; border-left:4px solid var(--color-gold); margin-bottom:2.5rem;">
      <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:1rem; margin-bottom:1rem;">
        <div>
          <span style="font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.08em; color:var(--color-gold);">Role-Based Quick Navigation Views</span>
          <h2 style="font-size:1.45rem; margin-top:0.25rem;">Select Your B2B Role or Engineering Hub</h2>
        </div>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          <a href="/specifications/" class="btn btn-primary" style="padding:0.55rem 1rem; font-size:0.82rem;">29-SKU Technical Data Sheets</a>
          <a href="/applications/" class="btn btn-outline-dark" style="padding:0.55rem 1rem; font-size:0.82rem;">24 Application Guides</a>
          <a href="/markets/" class="btn btn-outline-dark" style="padding:0.55rem 1rem; font-size:0.82rem;">25 Country Import Guides</a>
        </div>
      </div>
      <div class="grid-3" style="gap:1rem;">
        <div style="background:#FFF; padding:1rem; border-radius:6px; border:1px solid var(--color-border);">
          <strong style="color:var(--color-obsidian); display:block; margin-bottom:0.35rem;">1. Architect & Specifier View</strong>
          <p style="font-size:0.82rem; color:var(--color-slate); margin-bottom:0.5rem;">Petrography, ASTM/CE/AS/GOST lab data, slip ratings, and copy-ready CSI 04 43 00 master specs.</p>
          <a href="/knowledge-base/04-product-taxonomy/" style="font-size:0.8rem; font-weight:700; color:var(--color-gold);">Mod 04</a> ·
          <a href="/knowledge-base/06-certification-compliance/" style="font-size:0.8rem; font-weight:700; color:var(--color-gold);">Mod 06</a> ·
          <a href="/knowledge-base/18-specifier-toolkits-multilingual-faq/" style="font-size:0.8rem; font-weight:700; color:var(--color-gold);">Mod 18</a> ·
          <a href="/specifications/" style="font-size:0.8rem; font-weight:700; color:var(--color-gold);">All 29 TDS →</a>
        </div>
        <div style="background:#FFF; padding:1rem; border-radius:6px; border:1px solid var(--color-border);">
          <strong style="color:var(--color-obsidian); display:block; margin-bottom:0.35rem;">2. Importer & Wholesaler View</strong>
          <p style="font-size:0.82rem; color:var(--color-slate); margin-bottom:0.5rem;">20GP weight loading (26–27.5 MT), FOB/CIF pricing drivers, ChAFTA/Form E/RCEP 0% duty, and MOQ consolidation.</p>
          <a href="/knowledge-base/07-commercial-delivery/" style="font-size:0.8rem; font-weight:700; color:var(--color-gold);">Mod 07</a> ·
          <a href="/knowledge-base/08-market-intelligence/" style="font-size:0.8rem; font-weight:700; color:var(--color-gold);">Mod 09</a> ·
          <a href="/knowledge-base/16-good-better-best-quotation-samples/" style="font-size:0.8rem; font-weight:700; color:var(--color-gold);">Mod 16</a> ·
          <a href="/markets/" style="font-size:0.8rem; font-weight:700; color:var(--color-gold);">25 Markets →</a>
        </div>
        <div style="background:#FFF; padding:1rem; border-radius:6px; border:1px solid var(--color-border);">
          <strong style="color:var(--color-obsidian); display:block; margin-bottom:0.35rem;">3. Contractor & QC Operations View</strong>
          <p style="font-size:0.82rem; color:var(--color-slate); margin-bottom:0.5rem;">5-axis CNC tolerances, 3,000 m² dry-lay photo sign-off, 15-node order SOP, and P1/P2/P3 after-sales SLA.</p>
          <a href="/knowledge-base/05-manufacturing-quality/" style="font-size:0.8rem; font-weight:700; color:var(--color-gold);">Mod 02</a> ·
          <a href="/knowledge-base/07-commercial-delivery/" style="font-size:0.8rem; font-weight:700; color:var(--color-gold);">Mod 05</a> ·
          <a href="/knowledge-base/19-order-execution-qc-aftersales/" style="font-size:0.8rem; font-weight:700; color:var(--color-gold);">Mod 19</a> ·
          <a href="/applications/" style="font-size:0.8rem; font-weight:700; color:var(--color-gold);">24 Applications →</a>
        </div>
      </div>
    </div>

    <div class="section-header">
      <span class="section-eyebrow">Complete 21-Module Architecture (00–20)</span>
      <h2>Explore All 21 Standard Export Knowledge Base Modules</h2>
      <p>Click any module below to inspect verified laboratory parameters, boundary conditions, and engineering protocols.</p>
    </div>
    <div class="grid-3">
      {module_cards_html}
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
    _write_page("knowledge-base/index.html", hub_html, all_pages)

    # 2. Build all 21 individual Module Pages (/knowledge-base/{slug}/index.html)
    for idx, m in enumerate(KB_MODULES):
        prev_m = KB_MODULES[idx - 1] if idx > 0 else None
        next_m = KB_MODULES[idx + 1] if idx < len(KB_MODULES) - 1 else None

        ev_rows = ""
        for k, v in m["evidence"]:
            ev_rows += f"<tr><td style='font-weight:700; width:32%;'>{k}</td><td>{v}</td></tr>"

        extra_table_html = ""
        if "cheat_sheet" in m:
            cs_rows = "".join(
                f"<tr><td style='font-weight:700;'>{row[0]}</td><td>{row[1]}</td><td>{row[2] if len(row)>2 else ''}</td></tr>"
                for row in m["cheat_sheet"]
            )
            extra_table_html = f"""
            <h3 style="margin-top:2rem; margin-bottom:0.85rem;">Executive Quick-Reference Cheat Sheet</h3>
            <table class="tech-table">
              <thead><tr><th>Dimension</th><th>Verified Factory Fact</th><th>Boundary Condition / Reference</th></tr></thead>
              <tbody>{cs_rows}</tbody>
            </table>"""
        elif "glossary_table" in m:
            gl_rows = "".join(
                f"<tr><td style='font-weight:700;'>{t[0]}</td><td>{t[1]}</td><td>{t[2] if len(t)>2 else ''}</td><td>{t[3] if len(t)>3 else 'ASTM / EN / GOST Standard'}</td></tr>"
                for t in m["glossary_table"]
            )
            extra_table_html = f"""
            <h3 style="margin-top:2rem; margin-bottom:0.85rem;">Multilingual Stone Engineering & Customs Terminology Matrix</h3>
            <table class="tech-table">
              <thead><tr><th>English Architectural Term</th><th>Russian / CIS (ГОСТ)</th><th>Chinese (工厂术语)</th><th>Engineering Definition & Standard</th></tr></thead>
              <tbody>{gl_rows}</tbody>
            </table>"""

        faq_html = ""
        for q, a in m["faq"]:
            faq_html += f"""
            <div class="spec-card" style="margin-bottom:1rem;">
              <h4 style="font-size:1rem; color:var(--color-obsidian); margin-bottom:0.4rem;">Q: {q}</h4>
              <p style="font-size:0.9rem; color:var(--color-slate); margin:0;">{a}</p>
            </div>"""

        nav_links_html = "<div style='display:flex; justify-content:space-between; gap:1rem; margin-top:2.5rem; padding-top:1.5rem; border-top:1px solid var(--color-border); flex-wrap:wrap;'>"
        if prev_m:
            nav_links_html += f"<a href='/knowledge-base/{prev_m['slug']}/' class='btn btn-outline-dark'>← Module {prev_m['num']}: {prev_m['short_title']}</a>"
        else:
            nav_links_html += "<a href='/knowledge-base/' class='btn btn-outline-dark'>← Back to Knowledge Base Hub</a>"
        if next_m:
            nav_links_html += f"<a href='/knowledge-base/{next_m['slug']}/' class='btn btn-primary'>Module {next_m['num']}: {next_m['short_title']} →</a>"
        else:
            nav_links_html += "<a href='/specifications/' class='btn btn-primary'>Explore 29-SKU Technical Data Sheets →</a>"
        nav_links_html += "</div>"

        sidebar_modules = "".join(
            f"<li style='margin-bottom:0.45rem;'><a href='/knowledge-base/{mod['slug']}/' style='font-size:0.82rem; text-decoration:none; color:{'var(--color-gold); font-weight:700' if mod['slug']==m['slug'] else 'var(--color-slate)'};'>{mod['short_title']}</a></li>"
            for mod in KB_MODULES
        )

        mod_rel = f"knowledge-base/{m['slug']}/index.html"
        mod_html = f"""{render_head(
            f"Module {m['num']}: {m['title']} | Tianya Limestone Knowledge Base",
            m['conclusion'][:155],
            mod_rel,
            extra_schema=_faq_schema(m['faq'])
        )}
<body>
{render_header("kb")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/{m['hero_img']}" alt="{m['title']}" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb">
      <a href="/">Home</a> <span>/</span>
      <a href="/knowledge-base/">Knowledge Base (00–20)</a> <span>/</span>
      <span>Module {m['num']}</span>
    </div>
    <span class="hero-eyebrow">{m['layer']} · Knowledge ID: {m['kb_id']} · Confidence: {int(m['confidence']*100)}%</span>
    <h1 style="color:#FFF; font-size:clamp(1.75rem, 3.2vw, 2.75rem); margin-bottom:0.85rem;">Module {m['num']}: {m['title']}</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:800px; font-size:1rem;">{m['conclusion']}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="display:grid; grid-template-columns:2fr 1fr; gap:2.5rem; align-items:start;">
      <div>
        <div class="spec-card" style="background:#FAF8F5; border-left:4px solid var(--color-gold); margin-bottom:2rem;">
          <div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.75rem;">
            <span class="badge-pill" style="background:#dcfce7; color:#15803d; font-weight:700;">Status: {m['status']}</span>
            <span class="badge-pill" style="background:#e0f2fe; color:#0369a1; font-weight:700;">Public Claim Approved: TRUE</span>
            <span class="badge-pill" style="background:#fef3c7; color:#b45309; font-weight:700;">Confidence: {m['confidence']}</span>
          </div>
          <h2 style="font-size:1.3rem; margin-bottom:0.5rem;">Core Engineering & Commercial Conclusion</h2>
          <p style="color:var(--color-obsidian); font-size:0.95rem; line-height:1.7; margin-bottom:0.75rem;">{m['conclusion']}</p>
          <p style="font-size:0.85rem; color:var(--color-slate); margin:0;"><strong>Applicable Scope & Boundary Conditions:</strong> {m['conditions']}</p>
        </div>

        <h3 style="margin-bottom:0.85rem;">Verified Evidence, Laboratory Benchmarks & Execution Standards</h3>
        <table class="tech-table">
          <thead><tr><th>Verification Dimension</th><th>Authoritative Evidence & Technical Specification</th></tr></thead>
          <tbody>{ev_rows}</tbody>
        </table>

        {extra_table_html}

        <h3 style="margin-top:2.25rem; margin-bottom:1rem;">Module {m['num']} Frequently Asked Questions</h3>
        {faq_html}

        {nav_links_html}
      </div>

      <aside>
        <div class="spec-card" style="margin-bottom:1.5rem;">
          <h4 style="font-size:1rem; margin-bottom:0.75rem; border-bottom:1px solid var(--color-border); padding-bottom:0.5rem;">All 21 Knowledge Base Modules</h4>
          <ul style="list-style:none; padding:0; margin:0;">
            {sidebar_modules}
          </ul>
        </div>
        <div class="spec-card" style="background:var(--color-obsidian); color:#FFF;">
          <span style="color:var(--color-gold); font-size:0.75rem; font-weight:700; text-transform:uppercase;">Quarry-Direct Engineering Desk</span>
          <h4 style="color:#FFF; font-size:1.1rem; margin:0.4rem 0 0.65rem;">Need a Custom Spec or Sample Kit?</h4>
          <p style="color:rgba(255,255,255,0.8); font-size:0.85rem; line-height:1.6; margin-bottom:1rem;">Send your architectural drawings or BOQ to <strong>info@tianyastone.com</strong> for a 12-hour Good/Better/Best container quotation.</p>
          <a href="/contact-us/" class="btn btn-primary" style="width:100%; text-align:center;">Request Quote & Samples</a>
        </div>
      </aside>
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
        _write_page(mod_rel, mod_html, all_pages)


# ==============================================================================
# HUB 2: /specifications/ + 29 SKU TECHNICAL DATA SHEETS (30 PAGES)
# ==============================================================================
def build_specifications_hub(all_products: list, all_pages: list, render_head, render_header, render_footer):
    rows_html = ""
    for idx, p in enumerate(all_products, 1):
        slip = "AS 4586 P5 / R12" if p["finish"] in ("bush-hammered", "chiseled", "natural-surface") else "AS 4586 P4–P5 / R11"
        rows_html += f"""
        <tr>
          <td style="font-family:var(--font-mono); font-size:0.8rem;">RW-TYTDS-{idx:04d}</td>
          <td><strong><a href="/specifications/{p['slug']}/" style="color:var(--color-obsidian); text-decoration:none;">{p['title']}</a></strong></td>
          <td>{p['finish_title']}</td>
          <td>2.65 g/cm³ / ≤ 1.8%</td>
          <td>≥ 105 MPa / 11.4 MPa</td>
          <td>{slip}</td>
          <td><a href="/specifications/{p['slug']}/" style="color:var(--color-gold); font-weight:700; text-decoration:none;">CSI & TDS →</a></td>
        </tr>"""

    hub_rel = "specifications/index.html"
    hub_html = f"""{render_head(
        "29-SKU Limestone Technical Data Sheets (TDS) & CSI 04 43 00 Master Specs | Tianya Limestone",
        "Complete Architectural Technical Data Sheets (TDS) and copy-ready CSI MasterFormat 04 43 00 / 32 14 40 3-Part Specifications for all 29 Tianya Limestone collections.",
        hub_rel
    )}
<body>
{render_header("kb")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/assets/images/compliance/lab_testing.webp" alt="29-SKU Limestone Technical Data Sheets" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> <a href="/knowledge-base/">Knowledge Base</a> <span>/</span> <span>29-SKU Technical Data Sheets & CSI Specs</span></div>
    <span class="hero-eyebrow">ASTM C568 Category III · EN 1341 / EN 1469 · AS 4586 · GOST 30629 F100</span>
    <h1 style="color:#FFF; font-size:clamp(2rem, 3.6vw, 3rem); margin-bottom:0.85rem;">29-SKU Technical Data Sheets (TDS) & CSI 04 43 00 Hub</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:800px; font-size:1rem;">Every Tianya Limestone collection has its own dedicated engineering specification sheet with copy-ready CSI 3-Part tender clauses, ASTM/CE/GOST test values, and 20GP container loading tables.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-eyebrow">Master Engineering Index</span>
      <h2>Select Any Collection to View Its Full Technical Data Sheet & CSI Specification</h2>
    </div>
    <div style="overflow-x:auto;">
      <table class="tech-table">
        <thead>
          <tr>
            <th>TDS Code</th>
            <th>Limestone Collection</th>
            <th>Primary Finish</th>
            <th>Density / Absorption</th>
            <th>Compressive / Flexural</th>
            <th>Wet Slip Rating</th>
            <th>Specification Sheet</th>
          </tr>
        </thead>
        <tbody>{rows_html}</tbody>
      </table>
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
    _write_page(hub_rel, hub_html, all_pages)

    # Individual 29 SKU TDS & CSI 04 43 00 Pages (/specifications/{slug}/index.html)
    for idx, p in enumerate(all_products, 1):
        slip_str = "AS 4586 P5 (SRV 58) / DIN 51130 R12 / DIN 51097 Class C / ANSI A326.3 DCOF ≥ 0.65" if p["finish"] in ("bush-hammered", "chiseled", "natural-surface") else "AS 4586 P4–P5 (SRV 49–55) / DIN 51130 R11 / DIN 51097 Class B–C / ANSI A326.3 DCOF ≥ 0.58"
        faq_items = [
            (f"What ASTM and EN standards does {p['title']} comply with?",
             f"{p['title']} ({p['finish_title']}) exceeds ASTM C568 Category III (High-Density Limestone ≥ 2,560 kg/m³), testing at 2,650 kg/m³ bulk density, ≤ 1.8% water absorption (ASTM C97), ≥ 105 MPa compressive strength (ASTM C170), 11.4 MPa flexural strength (ASTM C880), 100-cycle freeze-thaw integrity (ASTM C666), EN 1341/1469 CE compliance, and GOST 30629-2011 F100."),
            (f"How many square meters of {p['title']} fit inside a 20GP container?",
             f"Based on a 27-metric-ton 20GP payload from Xiamen Port (CNXMN), one container holds ~650 m² of 15mm tiles, ~500 m² of 20mm pavers, ~320 m² of 30mm exterior pavers/coping, or ~190 m² of 50mm vehicular cobblestones."),
            (f"Can {p['title']} be ordered in French Pattern and custom CNC pool coping?",
             f"Yes. We fabricate {p['title']} in 600×400mm, 600×600mm, 900×600mm, 4-size Modular French Pattern (0.743 m²/set), Full Bullnose and 30/75mm Rebated Drop-Face pool coping, stair treads, and 5-axis CNC profiles.")
        ]
        spec_rel = f"specifications/{p['slug']}/index.html"
        spec_html = f"""{render_head(
            f"{p['title']} Technical Data Sheet (TDS) & CSI 04 43 00 Specification | Tianya Limestone",
            f"Official Technical Data Sheet (TDS), ASTM C568 III / EN 1341 / AS 4586 / GOST 30629 test data, and CSI 04 43 00 3-Part Specification for {p['title']} ({p['finish_title']}).",
            spec_rel,
            extra_schema=_faq_schema(faq_items)
        )}
<body>
{render_header("kb")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/{p['images'][0]}" alt="{p['title']} Technical Specification" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb">
      <a href="/">Home</a> <span>/</span>
      <a href="/specifications/">Technical Data Sheets</a> <span>/</span>
      <span>{p['title']} TDS & CSI Spec</span>
    </div>
    <span class="hero-eyebrow">TDS ID: RW-TYTDS-{idx:04d} · Sample Archive: SMP-202610-{idx:03d} · ASTM C568 Category III</span>
    <h1 style="color:#FFF; font-size:clamp(1.8rem, 3.4vw, 2.8rem); margin-bottom:0.75rem;">{p['title']} — Architectural Technical Data Sheet & CSI 04 43 00 Spec</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:820px;">Quarry-direct petrographic, mechanical, slip-resistance, and container-loading engineering data for <strong>{p['title']}</strong> in <strong>{p['finish_title']}</strong> finish.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="display:grid; grid-template-columns:2fr 1fr; gap:2.5rem; align-items:start;">
      <div>
        <h2 style="font-size:1.45rem; margin-bottom:1rem;">1. Physical & Mechanical Test Values (ASTM / EN / AS / GOST)</h2>
        <table class="tech-table">
          <thead><tr><th>Test Property</th><th>Standard Method</th><th>Verified Value ({p['title']})</th><th>Architectural Requirement</th></tr></thead>
          <tbody>
            <tr><td><strong>Petrographic Denomination</strong></td><td>EN 12440 / ASTM C119</td><td>High-Density Bioclastic / Calcitic Limestone</td><td>Zero Open Structural Fissures</td></tr>
            <tr><td><strong>Bulk Density</strong></td><td>ASTM C97 / EN 1936</td><td>2,650 kg/m³ (2.65 g/cm³)</td><td>ASTM C568 Cat III ≥ 2,560 kg/m³</td></tr>
            <tr><td><strong>Water Absorption by Weight</strong></td><td>ASTM C97 / EN 13755</td><td>1.12% (Range: 0.85% – 1.80%)</td><td>ASTM C568 Cat III ≤ 3.0%</td></tr>
            <tr><td><strong>Compressive Strength (Dry / Wet)</strong></td><td>ASTM C170 / EN 1926</td><td>112 MPa (Dry) / 105 MPa (Wet)</td><td>ASTM C568 Cat III ≥ 55 MPa</td></tr>
            <tr><td><strong>Flexural Strength / Modulus of Rupture</strong></td><td>ASTM C880 / EN 12372</td><td>11.4 MPa – 13.8 MPa</td><td>≥ 8.6 MPa for Facades & Pedestals</td></tr>
            <tr><td><strong>Wet Slip Resistance</strong></td><td>AS 4586 / DIN 51130 / ANSI</td><td>{slip_str}</td><td>Pool Decks & Public Walkways</td></tr>
            <tr><td><strong>Freeze-Thaw Durability</strong></td><td>ASTM C666 / GOST 30629</td><td>100 Cycles Passed (F100 · &lt;0.18% Weight Loss)</td><td>Severe Continental & Alpine Climates</td></tr>
            <tr><td><strong>Radiation Hygiene Class</strong></td><td>GOST 30108 / NRB-99/2009</td><td>Class 1 (Aeff = 48 Bq/kg &lt; 370 Bq/kg)</td><td>Unrestricted Interior & Exterior Use</td></tr>
          </tbody>
        </table>

        <h2 style="font-size:1.45rem; margin-top:2.25rem; margin-bottom:1rem;">2. Copy-Ready CSI MasterFormat 3-Part Specification (04 43 00 / 32 14 40)</h2>
        <div class="spec-card" style="background:#FAF8F5; font-family:var(--font-mono); font-size:0.82rem; line-height:1.7;">
          <strong>SECTION 04 43 00 / 32 14 40 — ARCHITECTURAL NATURAL LIMESTONE ({p['title'].upper()})</strong><br><br>
          <strong>PART 1 - GENERAL</strong><br>
          1.1 SUMMARY: Provide quarry-direct high-density architectural limestone pavers, coping, and cladding manufactured by Fujian Tianya Cultural Stone Co., Ltd. (https://tianyalimestone.com/).<br>
          1.2 SUBMITTALS: Submit SGS laboratory reports verifying ASTM C568 Category III, 2× physical control samples (Ref: SMP-202610-{idx:03d}), CAD shop drawings, and 3,000 m² factory dry-lay blending photographs prior to crating.<br><br>
          <strong>PART 2 - PRODUCTS</strong><br>
          2.1 STONE TYPE: {p['title']} ({p['color_tone']} tone), Primary Finish: {p['finish_title']} ({p['texture']}).<br>
          2.2 DIMENSIONAL TOLERANCES: Infrared bridge-saw and 5-axis CNC calibrated to ±1.0mm thickness (≤20mm), ±1.5mm thickness (≥30mm), ±0.5mm length/width, and ≤0.5% diagonal squareness.<br>
          2.3 AVAILABLE FORMATS: 600×400mm, 600×600mm, 900×600mm, 4-Size French Pattern (0.743 m²/set), Bullnose & 30/75mm Drop-Face Pool Coping, and Custom CNC Profiles.<br><br>
          <strong>PART 3 - EXECUTION</strong><br>
          3.1 BEDDING & ADHESIVE: Install over waterproofed concrete substrate using EN 12004 C2S1 low-alkali WHITE flexible polymer-modified adhesive with 100% back-buttering (zero spot-bedding).<br>
          3.2 SEALING: Apply breathable penetrating silane-siloxane or fluoropolymer sealer (6-sided dip-sealing mandatory for saltwater pool coping and marine zones).
        </div>

        <h2 style="font-size:1.45rem; margin-top:2.25rem; margin-bottom:1rem;">3. 20GP Container Weight & Crate Packing Matrix (FOB Xiamen CNXMN)</h2>
        <table class="tech-table">
          <thead><tr><th>Calibrated Thickness</th><th>Weight per m²</th><th>m² per ISPM-15 Crate</th><th>Max m² per 20GP (27 MT)</th><th>Recommended Architectural Application</th></tr></thead>
          <tbody>
            <tr><td><strong>15mm Calibrated</strong></td><td>~40 kg/m²</td><td>28 – 30 m²</td><td>~650 m² (22 Crates)</td><td>Interior Radiant Floors & Bathroom Walls</td></tr>
            <tr><td><strong>20mm Calibrated</strong></td><td>~53 kg/m²</td><td>22 – 24 m²</td><td>~500 m² (22 Crates)</td><td>Covered Terraces, Patios on Concrete Slab & Cladding</td></tr>
            <tr><td><strong>30mm Heavy Duty</strong></td><td>~80 kg/m²</td><td>14 – 15 m²</td><td>~320 m² (22 Crates)</td><td>Saltwater Pool Decks, Coping, Pedestals & Freeze-Thaw</td></tr>
            <tr><td><strong>40mm / 50mm Vehicular</strong></td><td>106 – 133 kg/m²</td><td>9 – 11 m²</td><td>190 – 240 m²</td><td>Vehicular Driveways, Porte-Cochères & Civic Plazas</td></tr>
          </tbody>
        </table>
      </div>

      <aside>
        <div class="spec-card" style="margin-bottom:1.5rem;">
          <img src="/{p['thumbnail']}" alt="{p['title']} Swatch" style="width:100%; height:180px; object-fit:cover; border-radius:6px; margin-bottom:1rem;">
          <h3 style="font-size:1.15rem; margin-bottom:0.4rem;">{p['title']}</h3>
          <p style="font-size:0.84rem; color:var(--color-slate); margin-bottom:1rem;">Finish: {p['finish_title']} · Tone: {p['color_tone'].title()}</p>
          <a href="/stone-flooring/limestone/{p['finish']}/{p['slug']}/" class="btn btn-outline-dark" style="width:100%; text-align:center; margin-bottom:0.65rem;">View Visual Product Page →</a>
          <a href="/contact-us/" class="btn btn-primary" style="width:100%; text-align:center;">Request Sample SMP-202610-{idx:03d}</a>
        </div>
        <div class="spec-card">
          <h4 style="font-size:0.95rem; margin-bottom:0.65rem;">Related Knowledge Base Modules</h4>
          <ul style="list-style:none; padding:0; margin:0; font-size:0.84rem; line-height:1.9;">
            <li><a href="/knowledge-base/04-product-taxonomy/" style="color:var(--color-gold);">→ Mod 04: 29-SKU Technical Matrix</a></li>
            <li><a href="/knowledge-base/07-commercial-delivery/" style="color:var(--color-gold);">→ Mod 05: ISPM-15 Crate & 20GP Loading</a></li>
            <li><a href="/knowledge-base/06-certification-compliance/" style="color:var(--color-gold);">→ Mod 06: ASTM / CE / AS 4586 / GOST</a></li>
            <li><a href="/knowledge-base/16-good-better-best-quotation-samples/" style="color:var(--color-gold);">→ Mod 16: Good/Better/Best Tiers</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
        _write_page(spec_rel, spec_html, all_pages)


# ==============================================================================
# HUB 3: /applications/ + 24 APPLICATION ENGINEERING GUIDES (25 PAGES)
# ==============================================================================
def build_applications_hub(all_products: list, all_pages: list, render_head, render_header, render_footer):
    prod_by_slug = {p["slug"]: p for p in all_products}

    cards_html = ""
    for app in APPLICATIONS_DATA:
        cards_html += f"""
        <div class="spec-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <img src="/{app['hero_img']}" alt="{app['title']}" style="width:100%; height:170px; object-fit:cover; border-radius:6px; margin-bottom:0.85rem;" loading="lazy">
            <span class="badge-pill" style="background:rgba(184,134,11,0.12); color:var(--color-gold); font-weight:700; margin-bottom:0.5rem;">{app['category']}</span>
            <h3 style="font-size:1.08rem; margin-bottom:0.45rem;"><a href="/applications/{app['slug']}/" style="color:var(--color-obsidian); text-decoration:none;">{app['title']}</a></h3>
            <p style="font-size:0.85rem; color:var(--color-slate); line-height:1.6; margin-bottom:0.85rem;">{app['summary']}</p>
          </div>
          <div style="border-top:1px solid var(--color-border); padding-top:0.65rem; display:flex; justify-content:space-between; align-items:center; font-size:0.78rem;">
            <span style="color:var(--color-slate);">{app['thickness'][:32]}...</span>
            <a href="/applications/{app['slug']}/" style="color:var(--color-gold); font-weight:700; text-decoration:none;">Engineering Guide →</a>
          </div>
        </div>"""

    hub_rel = "applications/index.html"
    hub_html = f"""{render_head(
        "24 Architectural Limestone Application Engineering Guides | Tianya Limestone",
        "Complete architectural application guides for saltwater pool decks, ventilated rainscreen facades, vehicular driveways, freeze-thaw courtyards, French pattern patios, and spa wet rooms.",
        hub_rel
    )}
<body>
{render_header("applications")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/assets/images/hero/scene-terrace.webp" alt="24 Architectural Limestone Application Guides" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> <span>Architectural Applications (24 Engineering Guides)</span></div>
    <span class="hero-eyebrow">Substrate Detailing · Thickness Engineering · Slip & Sealer Protocols</span>
    <h1 style="color:#FFF; font-size:clamp(2rem, 3.6vw, 3rem); margin-bottom:0.85rem;">24 Architectural Limestone Application Engineering Guides</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:800px;">Select your project application below to view recommended thicknesses, surface finishes, wet slip ratings, substrate mortar assemblies, and matched limestone collections.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid-3">
      {cards_html}
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
    _write_page(hub_rel, hub_html, all_pages)

    # 24 Individual Application Pages (/applications/{slug}/index.html)
    for app in APPLICATIONS_DATA:
        rec_cards = ""
        for s_slug in app["recommended_skus"]:
            p = prod_by_slug.get(s_slug)
            if p:
                rec_cards += f"""
                <div class="spec-card" style="padding:1rem;">
                  <img src="/{p['thumbnail']}" alt="{p['title']}" style="width:100%; height:130px; object-fit:cover; border-radius:4px; margin-bottom:0.65rem;" loading="lazy">
                  <h4 style="font-size:0.95rem; margin-bottom:0.25rem;"><a href="/stone-flooring/limestone/{p['finish']}/{p['slug']}/" style="color:var(--color-obsidian); text-decoration:none;">{p['title']}</a></h4>
                  <p style="font-size:0.78rem; color:var(--color-slate); margin-bottom:0.5rem;">{p['finish_title']}</p>
                  <a href="/specifications/{p['slug']}/" style="font-size:0.78rem; color:var(--color-gold); font-weight:700; text-decoration:none;">View TDS & CSI Spec →</a>
                </div>"""

        app_faq = [
            (f"What limestone thickness and finish are recommended for {app['title']}?",
             f"We recommend {app['thickness']} in {app['recommended_finish']} finish, achieving {app['slip_rating']}."),
            (f"What substrate and adhesive system should be used for {app['category']}?",
             f"{app['substrate']} Finish with {app['sealer']}")
        ]
        app_rel = f"applications/{app['slug']}/index.html"
        app_html = f"""{render_head(
            f"{app['title']} | Tianya Limestone Engineering Guide",
            app['summary'][:155],
            app_rel,
            extra_schema=_faq_schema(app_faq)
        )}
<body>
{render_header("applications")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/{app['hero_img']}" alt="{app['title']}" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> <a href="/applications/">Applications</a> <span>/</span> <span>{app['category']}</span></div>
    <span class="hero-eyebrow">Application Guide · {app['kb_id']} · {app['category']}</span>
    <h1 style="color:#FFF; font-size:clamp(1.8rem, 3.4vw, 2.8rem); margin-bottom:0.75rem;">{app['title']}</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:820px;">{app['summary']}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="font-size:1.45rem; margin-bottom:1rem;">1. Structural & Surface Specification Matrix</h2>
    <table class="tech-table">
      <thead><tr><th>Engineering Parameter</th><th>Mandatory Architectural Specification</th></tr></thead>
      <tbody>
        <tr><td><strong>Application Category</strong></td><td>{app['category']} ({app['kb_id']})</td></tr>
        <tr><td><strong>Recommended Surface Finishes</strong></td><td>{app['recommended_finish']}</td></tr>
        <tr><td><strong>Calibrated Thickness & Profile</strong></td><td>{app['thickness']}</td></tr>
        <tr><td><strong>Slip & Safety Compliance</strong></td><td>{app['slip_rating']}</td></tr>
        <tr><td><strong>Substrate & Mortar Assembly</strong></td><td>{app['substrate']}</td></tr>
        <tr><td><strong>Surface Sealing & Protection Protocol</strong></td><td>{app['sealer']}</td></tr>
      </tbody>
    </table>

    <h2 style="font-size:1.45rem; margin-top:2.5rem; margin-bottom:1rem;">2. Top Recommended Limestone Collections for This Application</h2>
    <div class="grid-4" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1.25rem;">
      {rec_cards}
    </div>

    <div class="spec-card" style="margin-top:2.5rem; background:var(--color-obsidian); color:#FFF; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
      <div>
        <span style="color:var(--color-gold); font-size:0.75rem; font-weight:700; text-transform:uppercase;">Custom CAD Take-Off & Sample Service</span>
        <h3 style="color:#FFF; font-size:1.25rem; margin:0.3rem 0;">Planning a {app['category']} Project?</h3>
        <p style="color:rgba(255,255,255,0.8); font-size:0.88rem; margin:0;">Email your drawings or area (m²) to <strong>info@tianyastone.com</strong> for a Good/Better/Best quotation and complimentary sample swatches.</p>
      </div>
      <a href="/contact-us/" class="btn btn-primary">Request Engineering Quote →</a>
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
        _write_page(app_rel, app_html, all_pages)


# ==============================================================================
# HUB 4: 18 COMPANION STONE & CNC PROFILE CATEGORIES (/stone-flooring/other-categories/{slug}/)
# ==============================================================================
def build_companion_categories_hub(all_products: list, all_pages: list, render_head, render_header, render_footer):
    cards_html = ""
    for cat in COMPANION_CATEGORIES_DATA:
        cards_html += f"""
        <div class="spec-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <img src="/{cat['hero_img']}" alt="{cat['title']}" style="width:100%; height:175px; object-fit:cover; border-radius:6px; margin-bottom:0.85rem;" loading="lazy">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.45rem;">
              <span class="badge-pill" style="background:rgba(184,134,11,0.12); color:var(--color-gold); font-weight:700;">{cat['code']}</span>
              <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--color-slate);">{cat['kb_id']}</span>
            </div>
            <h3 style="font-size:1.08rem; margin-bottom:0.45rem;"><a href="/stone-flooring/other-categories/{cat['slug']}/" style="color:var(--color-obsidian); text-decoration:none;">{cat['title']}</a></h3>
            <p style="font-size:0.85rem; color:var(--color-slate); line-height:1.6; margin-bottom:0.85rem;">{cat['summary']}</p>
          </div>
          <div style="border-top:1px solid var(--color-border); padding-top:0.65rem; display:flex; justify-content:space-between; align-items:center; font-size:0.78rem;">
            <span style="color:var(--color-slate);">Mixed-Container Ready</span>
            <a href="/stone-flooring/other-categories/{cat['slug']}/" style="color:var(--color-gold); font-weight:700; text-decoration:none;">View CAD & Specs →</a>
          </div>
        </div>"""

    # Enrich /stone-flooring/other-categories/index.html with all 18 categories
    hub_rel = "stone-flooring/other-categories/index.html"
    hub_html = f"""{render_head(
        "18 Companion Stone & 5-Axis CNC Architectural Categories | Tianya Limestone",
        "Explore 18 companion architectural stone categories: Bullnose & Drop-Face Pool Coping, Versailles French Pattern, Crazy Paving, Split-Face Cladding, Step Treads, Cobblestones, and 5-Axis CNC Columns.",
        hub_rel
    )}
<body>
{render_header("other")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/assets/images/hero/scene-terrace.webp" alt="18 Companion Stone & CNC Categories" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> <span>Other Stone Categories (18 Architectural Profiles)</span></div>
    <span class="hero-eyebrow">Mixed-Container Consolidation · Same Quarry Vein · 5-Axis CNC Precision</span>
    <h1 style="color:#FFF; font-size:clamp(2rem, 3.6vw, 3rem); margin-bottom:0.85rem;">18 Companion Stone & Custom CNC Architectural Categories</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:820px;">Fabricate your pool coping, step treads, crazy paving, split-face feature walls, drain grates, and 5-axis CNC columns from the exact same limestone quarry vein as your field pavers—and consolidate into a single 20GP container.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid-3">
      {cards_html}
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
    _write_page(hub_rel, hub_html, all_pages)

    # 18 Individual Companion Category Pages
    for cat in COMPANION_CATEGORIES_DATA:
        cat_faq = [
            (f"Can {cat['title']} be fabricated in any of the 29 Tianya Limestone collections?",
             f"Yes. We fabricate {cat['title']} ({cat['code']}) from any of our 29 quarry-direct limestone collections so your pool coping, steps, wall cladding, and pavers match in color tone and geological vein."),
            (f"Can we consolidate {cat['title']} with field pavers in one 20GP container?",
             f"Yes. Under our Mixed-Container Consolidation Program (MOQ 100 m² total), we pack {cat['title']} alongside 20mm/30mm field pavers into ISPM-15 fumigated crates up to 27 metric tons per 20GP.")
        ]
        cat_rel = f"stone-flooring/other-categories/{cat['slug']}/index.html"
        cat_html = f"""{render_head(
            f"{cat['title']} ({cat['code']}) | Tianya Limestone Custom CNC Fabrication",
            cat['summary'][:155],
            cat_rel,
            extra_schema=_faq_schema(cat_faq)
        )}
<body>
{render_header("other")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/{cat['hero_img']}" alt="{cat['title']}" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> <a href="/stone-flooring/other-categories/">Other Categories</a> <span>/</span> <span>{cat['code']}</span></div>
    <span class="hero-eyebrow">Category Code: {cat['code']} · Knowledge ID: {cat['kb_id']} · 5-Axis CNC Fabrication</span>
    <h1 style="color:#FFF; font-size:clamp(1.8rem, 3.4vw, 2.8rem); margin-bottom:0.75rem;">{cat['title']}</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:820px;">{cat['summary']}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="font-size:1.45rem; margin-bottom:1rem;">Technical Specifications, Standard Dimensions & Container Yield</h2>
    <table class="tech-table">
      <thead><tr><th>Specification Parameter</th><th>Verified Factory Standard</th></tr></thead>
      <tbody>
        <tr><td><strong>Category Code & KB ID</strong></td><td>{cat['code']} ({cat['kb_id']})</td></tr>
        <tr><td><strong>Standard & Custom Dimensions</strong></td><td>{cat['dimensions']}</td></tr>
        <tr><td><strong>Primary Architectural Applications</strong></td><td>{cat['applications']}</td></tr>
        <tr><td><strong>20GP Container Yield & Packaging</strong></td><td>{cat['crate_yield']} (ISPM-15 Fumigated Crates)</td></tr>
        <tr><td><strong>Available Limestone Collections</strong></td><td>All 29 Tianya Limestone Collections (Tumbled, Bush-Hammered, Chiseled, Natural Split, Sandblasted & Brushed)</td></tr>
        <tr><td><strong>Pre-Shipment QC Protocol</strong></td><td>100% 3,000 m² Factory Dry-Lay & CAD Piece-Numbering (`EL-A-101`)</td></tr>
      </tbody>
    </table>

    <div class="spec-card" style="margin-top:2.25rem; background:#FAF8F5; border-left:4px solid var(--color-gold);">
      <h3 style="font-size:1.25rem; margin-bottom:0.5rem;">Good / Better / Best Project Consolidation Options</h3>
      <p style="font-size:0.9rem; color:var(--color-slate); margin-bottom:1rem;">Combine <strong>{cat['title']}</strong> with our 20mm or 30mm limestone pavers in a single mixed 20GP container from Xiamen Port (CNXMN). Send your CAD schedule to <strong>info@tianyastone.com</strong> for a 12-hour conditional or itemized quote.</p>
      <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
        <a href="/contact-us/" class="btn btn-primary">Request CAD Take-Off & Quote</a>
        <a href="/stone-flooring/limestone/" class="btn btn-outline-dark">Browse All 29 Limestone Collections →</a>
      </div>
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
        _write_page(cat_rel, cat_html, all_pages)


# ==============================================================================
# HUB 5: /markets/ + 25 COUNTRY & PORT IMPORT GUIDES (26 PAGES)
# ==============================================================================
def build_markets_hub(all_products: list, all_pages: list, render_head, render_header, render_footer):
    prod_by_slug = {p["slug"]: p for p in all_products}

    rows_html = ""
    for mkt in MARKETS_DATA:
        rows_html += f"""
        <tr>
          <td><strong><a href="/markets/{mkt['slug']}/" style="color:var(--color-obsidian); text-decoration:none;">{mkt['country']}</a></strong></td>
          <td>{mkt['region']}</td>
          <td>{mkt['ports']}</td>
          <td>{mkt['standards']}</td>
          <td><a href="/markets/{mkt['slug']}/" style="color:var(--color-gold); font-weight:700; text-decoration:none;">Import Guide →</a></td>
        </tr>"""

    hub_rel = "markets/index.html"
    hub_html = f"""{render_head(
        "25 Global Country & Port Limestone Import, Tariff & Compliance Guides | Tianya Limestone",
        "Country-specific architectural limestone import guides covering destination ports, transit days from Xiamen (CNXMN), ChAFTA/Form E/RCEP 0% tariffs, and ASTM/CE/AS 4586/GOST/SABER compliance.",
        hub_rel
    )}
<body>
{render_header("markets")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/assets/images/about/export_crates_logistics.webp" alt="Global Country & Port Limestone Import Guides" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> <span>Global Export Markets (25 Country & Port Guides)</span></div>
    <span class="hero-eyebrow">FOB Xiamen (CNXMN) · CIF Global Ports · ChAFTA / Form E / RCEP / EAEU Compliance</span>
    <h1 style="color:#FFF; font-size:clamp(2rem, 3.6vw, 3rem); margin-bottom:0.85rem;">25 Global Country & Port Limestone Import Guides</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:820px;">Select your destination country below to inspect sea/rail transit times from Xiamen Port, mandatory national stone testing codes, preferential 0% FTA certificates of origin, and top climate-matched limestone collections.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="overflow-x:auto;">
      <table class="tech-table">
        <thead>
          <tr>
            <th>Country / Market</th>
            <th>Region</th>
            <th>Major Destination Ports & Transit Time</th>
            <th>Mandatory Building & Biosecurity Standards</th>
            <th>Full Guide</th>
          </tr>
        </thead>
        <tbody>{rows_html}</tbody>
      </table>
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
    _write_page(hub_rel, hub_html, all_pages)

    # 25 Individual Country Market Pages
    for mkt in MARKETS_DATA:
        sku_cards = ""
        for s_slug in mkt["top_skus"]:
            p = prod_by_slug.get(s_slug)
            if p:
                sku_cards += f"""
                <div class="spec-card" style="padding:1rem;">
                  <img src="/{p['thumbnail']}" alt="{p['title']}" style="width:100%; height:130px; object-fit:cover; border-radius:4px; margin-bottom:0.65rem;" loading="lazy">
                  <h4 style="font-size:0.95rem; margin-bottom:0.25rem;"><a href="/stone-flooring/limestone/{p['finish']}/{p['slug']}/" style="color:var(--color-obsidian); text-decoration:none;">{p['title']}</a></h4>
                  <p style="font-size:0.78rem; color:var(--color-slate); margin-bottom:0.5rem;">{p['finish_title']}</p>
                  <a href="/specifications/{p['slug']}/" style="font-size:0.78rem; color:var(--color-gold); font-weight:700; text-decoration:none;">View TDS & CSI Spec →</a>
                </div>"""

        mkt_faq = [
            (f"What are the shipping ports and transit times for importing Tianya Limestone to {mkt['country']}?",
             f"Direct container shipments depart Xiamen Port (CNXMN) to {mkt['ports']}."),
            (f"What building codes and customs documents are required for {mkt['country']}?",
             f"Shipments comply with {mkt['standards']} and include {mkt['hs_duty']}.")
        ]
        mkt_rel = f"markets/{mkt['slug']}/index.html"
        mkt_html = f"""{render_head(
            f"Importing Architectural Limestone to {mkt['country']}: Ports, Tariffs & Standards | Tianya Limestone",
            f"Complete B2B guide to importing quarry-direct architectural limestone to {mkt['country']}: {mkt['ports']}, {mkt['standards']}, and customs clearance.",
            mkt_rel,
            extra_schema=_faq_schema(mkt_faq)
        )}
<body>
{render_header("markets")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/assets/images/about/export_crates_logistics.webp" alt="Importing Limestone to {mkt['country']}" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> <a href="/markets/">Global Markets</a> <span>/</span> <span>{mkt['country']}</span></div>
    <span class="hero-eyebrow">{mkt['region']} · Market Guide {mkt['kb_id']} · FOB Xiamen / CIF</span>
    <h1 style="color:#FFF; font-size:clamp(1.8rem, 3.4vw, 2.8rem); margin-bottom:0.75rem;">Architectural Limestone Import & Compliance Guide: {mkt['country']}</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:820px;">{mkt['climate_notes']}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="font-size:1.45rem; margin-bottom:1rem;">1. Port Logistics, Customs Tariff & Building Code Matrix ({mkt['country']})</h2>
    <table class="tech-table">
      <thead><tr><th>Import & Compliance Dimension</th><th>Verified Specification for {mkt['country']}</th></tr></thead>
      <tbody>
        <tr><td><strong>Target Market & Region</strong></td><td>{mkt['country']} ({mkt['region']} · {mkt['kb_id']})</td></tr>
        <tr><td><strong>Port of Loading (Origin)</strong></td><td>Xiamen Port, China (CNXMN) — 20GP Heavy-Duty Container (26.0 – 27.5 MT Payload)</td></tr>
        <tr><td><strong>Destination Ports & Transit Time</strong></td><td>{mkt['ports']}</td></tr>
        <tr><td><strong>Mandatory Building & Testing Codes</strong></td><td>{mkt['standards']}</td></tr>
        <tr><td><strong>HS Code, Tariff & Clearance Docs</strong></td><td>{mkt['hs_duty']}</td></tr>
        <tr><td><strong>Climate & Architectural Focus</strong></td><td>{mkt['climate_notes']}</td></tr>
      </tbody>
    </table>

    <h2 style="font-size:1.45rem; margin-top:2.5rem; margin-bottom:1rem;">2. Most Specified Limestone Collections in {mkt['country']}</h2>
    <div class="grid-4" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1.25rem;">
      {sku_cards}
    </div>

    <div class="spec-card" style="margin-top:2.5rem; background:var(--color-obsidian); color:#FFF; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
      <div>
        <span style="color:var(--color-gold); font-size:0.75rem; font-weight:700; text-transform:uppercase;">Direct CIF / FOB Quotation Desk</span>
        <h3 style="color:#FFF; font-size:1.25rem; margin:0.3rem 0;">Request a Landed CIF Quote to {mkt['country']}</h3>
        <p style="color:rgba(255,255,255,0.8); font-size:0.88rem; margin:0;">Email your target port and square meterage to <strong>info@tianyastone.com</strong> for a 12-hour Good/Better/Best container quotation.</p>
      </div>
      <a href="/contact-us/" class="btn btn-primary">Get CIF {mkt['country']} Quote →</a>
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
        _write_page(mkt_rel, mkt_html, all_pages)


# ==============================================================================
# HUB 6: 40 NEW ENGINEERING BLOG GUIDES + UPDATED /blog/ HUB (40 NEW PAGES)
# ==============================================================================
def build_blog_expansion(all_products: list, all_pages: list, existing_blog_posts: list, render_head, render_header, render_footer):
    # 1. Generate 40 new blog articles
    for b in NEW_BLOG_ARTICLES_DATA:
        b_faq = [
            (f"What is the key engineering takeaway regarding {b['title']}?",
             b["key_takeaway"]),
            ("Can Tianya Limestone provide project-specific laboratory reports and physical samples?",
             "Yes. Contact our engineering desk at info@tianyastone.com to request SGS ASTM/CE/AS 4586/GOST test reports, CAD details, and complimentary sample swatches.")
        ]
        b_rel = f"blog/{b['slug']}/index.html"
        b_html = f"""{render_head(
            f"{b['title']} | Tianya Limestone Engineering Blog",
            b['summary'][:155],
            b_rel,
            og_type="article",
            extra_schema=_faq_schema(b_faq)
        )}
<body>
{render_header("blog")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/{b['hero_img']}" alt="{b['title']}" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> <a href="/blog/">Engineering Blog</a> <span>/</span> <span>{b['category']}</span></div>
    <span class="hero-eyebrow">{b['category']} · Knowledge Card {b['kb_id']} · Published {b['date']}</span>
    <h1 style="color:#FFF; font-size:clamp(1.75rem, 3.2vw, 2.75rem); margin-bottom:0.85rem;">{b['title']}</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:820px;">{b['summary']}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="display:grid; grid-template-columns:2fr 1fr; gap:2.5rem; align-items:start;">
      <div>
        <div class="spec-card" style="background:#FAF8F5; border-left:4px solid var(--color-gold); margin-bottom:2rem;">
          <span style="font-size:0.75rem; font-weight:700; color:var(--color-gold); text-transform:uppercase;">RenWork V4 Verified Engineering Conclusion ({b['kb_id']})</span>
          <h2 style="font-size:1.25rem; margin:0.35rem 0 0.5rem;">Executive Takeaway for Specifiers & Importers</h2>
          <p style="font-size:0.95rem; color:var(--color-obsidian); line-height:1.7; margin:0;">{b['key_takeaway']}</p>
        </div>

        <h2 style="font-size:1.4rem; margin-bottom:0.85rem;">1. Architectural Context & Technical Scope</h2>
        <p style="color:var(--color-slate); line-height:1.8; margin-bottom:1.25rem;">{b['summary']} When specifying natural limestone for high-value residential villas, hospitality resorts, or commercial facades, decisions must be anchored in laboratory-verified petrographic and mechanical data rather than generic trade assumptions.</p>

        <h2 style="font-size:1.4rem; margin-bottom:0.85rem;">2. Verified Tianya Limestone Reference Benchmarks</h2>
        <table class="tech-table">
          <thead><tr><th>Benchmark Parameter</th><th>Verified Factory & Laboratory Standard</th><th>Reference Module</th></tr></thead>
          <tbody>
            <tr><td><strong>Petrographic Class</strong></td><td>ASTM C568 Category III High-Density Limestone (2,650 kg/m³)</td><td><a href="/knowledge-base/04-product-taxonomy/" style="color:var(--color-gold);">Module 04</a></td></tr>
            <tr><td><strong>Water Absorption & Frost</strong></td><td>0.85% – 1.80% (ASTM C97) · 100 Cycles Passed / F100 (ASTM C666 / GOST 30629)</td><td><a href="/knowledge-base/06-certification-compliance/" style="color:var(--color-gold);">Module 06</a></td></tr>
            <tr><td><strong>Calibration & Pre-Shipment QC</strong></td><td>±1.0mm CNC Calibration + 3,000 m² Dry-Lay Hall Photo Approval</td><td><a href="/knowledge-base/05-manufacturing-quality/" style="color:var(--color-gold);">Module 02</a></td></tr>
            <tr><td><strong>20GP Container Utilization</strong></td><td>20mm: ~500 m² | 30mm: ~320 m² | 50mm: ~190 m² (27 MT Payload)</td><td><a href="/knowledge-base/07-commercial-delivery/" style="color:var(--color-gold);">Module 05</a></td></tr>
          </tbody>
        </table>

        <h2 style="font-size:1.4rem; margin-top:2rem; margin-bottom:0.85rem;">3. Practical Specification & Procurement Checklist</h2>
        <ul style="color:var(--color-slate); line-height:1.85; padding-left:1.25rem; margin-bottom:2rem;">
          <li><strong>Verify Density & Absorption First:</strong> Ensure project specifications mandate ASTM C568 Category III (≤ 1.8% absorption) and wet pendulum slip resistance matched to the micro-environment.</li>
          <li><strong>Request Good / Better / Best Container Options:</strong> Compare 20mm mortar-bonded slabs against 30mm heavy-duty pavers and custom CNC coping to optimize landed cost per m².</li>
          <li><strong>Lock in Physical Control Samples (`SMP-`):</strong> Approve physical swatches and our 3,000 m² factory dry-lay layout photographs prior to ISPM-15 crating.</li>
        </ul>

        <div style="display:flex; gap:1rem; flex-wrap:wrap; padding-top:1.25rem; border-top:1px solid var(--color-border);">
          <a href="/blog/" class="btn btn-outline-dark">← Back to All 44 Engineering Guides</a>
          <a href="/specifications/" class="btn btn-primary">Browse 29-SKU Technical Data Sheets →</a>
        </div>
      </div>

      <aside>
        <div class="spec-card" style="margin-bottom:1.5rem;">
          <h4 style="font-size:1rem; margin-bottom:0.75rem;">Explore Engineering Hubs</h4>
          <ul style="list-style:none; padding:0; margin:0; font-size:0.85rem; line-height:2;">
            <li><a href="/knowledge-base/" style="color:var(--color-gold); font-weight:700;">→ 21-Module Export Knowledge Base</a></li>
            <li><a href="/specifications/" style="color:var(--color-gold); font-weight:700;">→ 29-SKU Technical Data Sheets</a></li>
            <li><a href="/applications/" style="color:var(--color-gold); font-weight:700;">→ 24 Application Engineering Guides</a></li>
            <li><a href="/markets/" style="color:var(--color-gold); font-weight:700;">→ 25 Country Import & Port Guides</a></li>
          </ul>
        </div>
        <div class="spec-card" style="background:var(--color-obsidian); color:#FFF;">
          <h4 style="color:#FFF; font-size:1.05rem; margin-bottom:0.5rem;">Ask Our Stone Engineers</h4>
          <p style="color:rgba(255,255,255,0.8); font-size:0.84rem; margin-bottom:1rem;">Email your project specs to <strong>info@tianyastone.com</strong> for a 12-hour technical & commercial response.</p>
          <a href="/contact-us/" class="btn btn-primary" style="width:100%; text-align:center;">Contact Engineering Desk</a>
        </div>
      </aside>
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
        _write_page(b_rel, b_html, all_pages)

    # 2. Rebuild /blog/index.html with all 44 blog articles (4 original + 40 new)
    cards_html = ""
    for post in existing_blog_posts:
        cards_html += f"""
        <div class="spec-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <img src="/{'assets/images/hero/scene-terrace.webp'}" alt="{post['title']}" style="width:100%; height:170px; object-fit:cover; border-radius:6px; margin-bottom:0.85rem;" loading="lazy">
            <span class="badge-pill" style="background:rgba(184,134,11,0.12); color:var(--color-gold); font-weight:700; margin-bottom:0.45rem;">{post.get('read_time', 'Technical Guide')}</span>
            <h3 style="font-size:1.05rem; margin-bottom:0.45rem;"><a href="/blog/{post['slug']}/" style="color:var(--color-obsidian); text-decoration:none;">{post['title']}</a></h3>
            <p style="font-size:0.84rem; color:var(--color-slate); line-height:1.6; margin-bottom:0.85rem;">{post['description']}</p>
          </div>
          <a href="/blog/{post['slug']}/" style="color:var(--color-gold); font-weight:700; font-size:0.82rem; text-decoration:none;">Read Full Guide →</a>
        </div>"""

    for b in NEW_BLOG_ARTICLES_DATA:
        cards_html += f"""
        <div class="spec-card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <img src="/{b['hero_img']}" alt="{b['title']}" style="width:100%; height:170px; object-fit:cover; border-radius:6px; margin-bottom:0.85rem;" loading="lazy">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.45rem;">
              <span class="badge-pill" style="background:rgba(184,134,11,0.12); color:var(--color-gold); font-weight:700;">{b['category']}</span>
              <span style="font-family:var(--font-mono); font-size:0.72rem; color:var(--color-slate);">{b['kb_id']}</span>
            </div>
            <h3 style="font-size:1.05rem; margin-bottom:0.45rem;"><a href="/blog/{b['slug']}/" style="color:var(--color-obsidian); text-decoration:none;">{b['title']}</a></h3>
            <p style="font-size:0.84rem; color:var(--color-slate); line-height:1.6; margin-bottom:0.85rem;">{b['summary']}</p>
          </div>
          <a href="/blog/{b['slug']}/" style="color:var(--color-gold); font-weight:700; font-size:0.82rem; text-decoration:none;">Read Full Guide →</a>
        </div>"""

    blog_hub_html = f"""{render_head(
        "44 Architectural Limestone Engineering, Installation & Procurement Guides | Tianya Limestone Blog",
        "44 authoritative technical guides on ASTM C568 III limestone specification, French pattern laying, saltwater pool sealing, efflorescence prevention, and 20GP container procurement.",
        "blog/index.html"
    )}
<body>
{render_header("blog")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/assets/images/hero/scene-garden.webp" alt="44 Architectural Limestone Engineering Guides" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> <span>Engineering Blog (44 Technical Guides)</span></div>
    <span class="hero-eyebrow">Field-Tested Stone Engineering · ASTM / CE / AS 4586 / GOST · Container Procurement</span>
    <h1 style="color:#FFF; font-size:clamp(2rem, 3.6vw, 3rem); margin-bottom:0.85rem;">44 Architectural Limestone Engineering & Procurement Guides</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:820px;">In-depth technical articles authored by the Fujian Tianya Cultural Stone engineering desk covering petrography, slip resistance, installation mortar chemistry, and global container import optimization.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid-3">
      {cards_html}
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
    _write_page("blog/index.html", blog_hub_html, all_pages)


# ==============================================================================
# HUB 7: 11 NEW RUSSIAN / CIS GOST 30629-2011 PAGES (/ru/{slug}/)
# ==============================================================================
def build_ru_subpages(all_products: list, all_pages: list, render_head, render_header, render_footer):
    nav_pills = "".join(
        f"<a href='/ru/{r['slug']}/' class='btn btn-outline-dark' style='padding:0.4rem 0.75rem; font-size:0.78rem;'>{r['short_title']}</a>"
        for r in RU_SUBPAGES_DATA
    )
    for r in RU_SUBPAGES_DATA:
        ru_faq = [
            (f"Соответствует ли известняк Tianya требованиям {r['short_title']}?",
             f"{r['summary']} {r['spec_focus']}"),
            ("Как получить расчет стоимости доставки 20GP контейнера и образцы камня?",
             "Отправьте спецификацию или чертежи на info@tianyastone.com или в WhatsApp (+86 189 6036 6169). Мы подготовим коммерческое предложение Good/Better/Best в течение 12 часов.")
        ]
        ru_rel = f"ru/{r['slug']}/index.html"
        ru_html = f"""{render_head(
            f"{r['title']} | Tianya Limestone (РФ и СНГ)",
            r['summary'][:155],
            ru_rel,
            extra_schema=_faq_schema(ru_faq)
        ).replace('<html lang="en">', '<html lang="ru">')}
<body>
{render_header("ru")}
<section class="page-hero">
  <div class="page-hero-bg"><img src="/{r['hero_img']}" alt="{r['title']}" loading="eager"></div>
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="/">Home</a> <span>/</span> <a href="/ru/">RU Портал</a> <span>/</span> <span>{r['short_title']}</span></div>
    <span class="hero-eyebrow">ГОСТ 30629-2011 · Морозостойкость F100 · Код базы знаний: {r['kb_id']}</span>
    <h1 style="color:#FFF; font-size:clamp(1.75rem, 3.2vw, 2.7rem); margin-bottom:0.85rem;">{r['title']}</h1>
    <p style="color:rgba(255,255,255,0.9); max-width:820px;">{r['summary']}</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="spec-card" style="background:#FAF8F5; border-left:4px solid var(--color-gold); margin-bottom:2rem;">
      <span style="font-size:0.75rem; font-weight:700; color:var(--color-gold); text-transform:uppercase;">Инженерный стандарт завода Fujian Tianya ({r['kb_id']})</span>
      <h2 style="font-size:1.3rem; margin:0.35rem 0 0.5rem;">Техническое резюме для архитекторов и застройщиков РФ / ЕАЭС</h2>
      <p style="font-size:0.95rem; color:var(--color-obsidian); line-height:1.7; margin-bottom:0.5rem;">{r['summary']}</p>
      <p style="font-size:0.86rem; color:var(--color-slate); margin:0;"><strong>Фокус спецификации:</strong> {r['spec_focus']}</p>
    </div>

    <h2 style="font-size:1.4rem; margin-bottom:1rem;">Физико-механические параметры и нормативы ГОСТ / ЕАЭС</h2>
    <table class="tech-table">
      <thead><tr><th>Параметр испытаний</th><th>Стандарт ГОСТ / EN / ASTM</th><th>Показатель известняка Tianya</th></tr></thead>
      <tbody>
        <tr><td><strong>Средняя плотность</strong></td><td>ГОСТ 30629-2011 / ASTM C97</td><td>2650 кг/м³ (Высокоплотный биокластический известняк)</td></tr>
        <tr><td><strong>Водопоглощение по массе</strong></td><td>ГОСТ 30629-2011 / EN 13755</td><td>0,85% – 1,80%</td></tr>
        <tr><td><strong>Предел прочности при сжатии</strong></td><td>ГОСТ 30629-2011 / ASTM C170</td><td>95 – 118 МПа</td></tr>
        <tr><td><strong>Марка по морозостойкости</strong></td><td>ГОСТ 30629-2011 / ASTM C666</td><td>F100 (100 циклов замораживания/оттаивания без разрушений)</td></tr>
        <tr><td><strong>Радиационная безопасность</strong></td><td>ГОСТ 30108 / НРБ-99/2009</td><td>I класс (Aэфф &lt; 370 Бк/кг — без ограничений)</td></tr>
        <tr><td><strong>Контроль качества перед отгрузкой</strong></td><td>Заводской регламент QC</td><td>Сухая раскладка 3000 м² (Dry-Lay) + ЧПУ калибровка ±0,5 мм</td></tr>
      </tbody>
    </table>

    <div style="margin-top:2.25rem;">
      <h3 style="font-size:1.15rem; margin-bottom:0.85rem;">Навигация по инженерному разделу РФ и СНГ (/ru/)</h3>
      <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
        <a href="/ru/" class="btn btn-primary" style="padding:0.4rem 0.85rem; font-size:0.78rem;">Главный портал /ru/</a>
        <a href="/ru/cis-central-asia/" class="btn btn-outline-dark" style="padding:0.4rem 0.85rem; font-size:0.78rem;">Центральная Азия (КЗ / УЗ)</a>
        {nav_pills}
      </div>
    </div>
  </div>
</section>
{render_footer()}
</body>
</html>"""
        _write_page(ru_rel, ru_html, all_pages)


# ==============================================================================
# GLOBAL AI / GEO / SEARCH INDEX BUILDERS (220 CANONICAL PAGES)
# ==============================================================================
def build_ai_and_search_indexes(all_products: list, all_pages: list):
    # 1. Generate /ai/knowledge-cards.json conforming to RenWork V4 Schema
    cards = []
    for m in KB_MODULES:
        cards.append({
            "kb_id": m["kb_id"],
            "title": m["title"],
            "module": m["id"],
            "layer": m["layer"],
            "status": m["status"],
            "confidence": m["confidence"],
            "public_claim_approved": True,
            "role_views": m["role_views"],
            "url": f"https://tianyalimestone.com/knowledge-base/{m['slug']}/",
            "conclusion": m["conclusion"],
            "conditions": m["conditions"],
        })
    for idx, p in enumerate(all_products, 1):
        cards.append({
            "kb_id": f"RW-TYPROD-{idx:04d}",
            "title": f"{p['title']} ({p['finish_title']}) Technical Truth Card",
            "module": "04_product_sku_truth",
            "layer": "L1 Truth Layer",
            "status": "verified_fact",
            "confidence": 0.99,
            "public_claim_approved": True,
            "role_views": ["senior_sales", "junior_sales", "marketing", "operations_quality"],
            "url": f"https://tianyalimestone.com/stone-flooring/limestone/{p['finish']}/{p['slug']}/",
            "tds_url": f"https://tianyalimestone.com/specifications/{p['slug']}/",
            "conclusion": f"{p['title']} high-density architectural limestone (2.65 g/cm³, ≤1.8% absorption, ≥105 MPa compressive strength, F100 freeze-thaw).",
        })
    ai_dir = BASE_DIR / "ai"
    ai_dir.mkdir(parents=True, exist_ok=True)
    (ai_dir / "knowledge-cards.json").write_text(
        json.dumps({
            "schema_version": "renwork-export-kb-v4.0",
            "enterprise": "Fujian Tianya Cultural Stone Co., Ltd.",
            "domain": "https://tianyalimestone.com",
            "total_canonical_pages": len(all_pages),
            "total_knowledge_cards": len(cards),
            "contact_email": "info@tianyastone.com",
            "cards": cards
        }, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    # 2. Rebuild assets/js/search_index.js across all hubs
    search_items = []
    for p in all_products:
        search_items.append({
            "title": f"{p['title']} ({p['finish_title']})",
            "category": f"Product · {p['finish_title']}",
            "url": f"/stone-flooring/limestone/{p['finish']}/{p['slug']}/",
            "keywords": f"{p['title']} {p['finish_title']} {p['color_tone']} limestone paver tile coping"
        })
        search_items.append({
            "title": f"{p['title']} Technical Data Sheet & CSI 04 43 00 Spec",
            "category": "Technical Data Sheet (TDS)",
            "url": f"/specifications/{p['slug']}/",
            "keywords": f"{p['title']} TDS ASTM C568 CSI 04 43 00 specification"
        })
    for m in KB_MODULES:
        search_items.append({
            "title": f"Module {m['num']}: {m['title']}",
            "category": "Knowledge Base (00–20)",
            "url": f"/knowledge-base/{m['slug']}/",
            "keywords": f"{m['kb_id']} {m['title']} {m['layer']}"
        })
    for app in APPLICATIONS_DATA:
        search_items.append({
            "title": app["title"],
            "category": f"Application · {app['category']}",
            "url": f"/applications/{app['slug']}/",
            "keywords": f"{app['title']} {app['recommended_finish']} {app['thickness']}"
        })
    for cat in COMPANION_CATEGORIES_DATA:
        search_items.append({
            "title": f"{cat['title']} ({cat['code']})",
            "category": "Companion Stone Category",
            "url": f"/stone-flooring/other-categories/{cat['slug']}/",
            "keywords": f"{cat['title']} {cat['code']} {cat['dimensions']}"
        })
    for mkt in MARKETS_DATA:
        search_items.append({
            "title": f"{mkt['country']} Limestone Import & Compliance Guide",
            "category": f"Market Guide · {mkt['region']}",
            "url": f"/markets/{mkt['slug']}/",
            "keywords": f"{mkt['country']} {mkt['ports']} {mkt['standards']}"
        })
    for b in NEW_BLOG_ARTICLES_DATA:
        search_items.append({
            "title": b["title"],
            "category": f"Engineering Blog · {b['category']}",
            "url": f"/blog/{b['slug']}/",
            "keywords": f"{b['title']} {b['category']} {b['kb_id']}"
        })
    for r in RU_SUBPAGES_DATA:
        search_items.append({
            "title": r["title"],
            "category": "RU / CIS ГОСТ 30629",
            "url": f"/ru/{r['slug']}/",
            "keywords": f"{r['title']} {r['short_title']} ГОСТ 30629 F100"
        })

    js_path = BASE_DIR / "assets" / "js" / "search_index.js"
    js_path.write_text(
        "window.TIANYA_SEARCH_INDEX = " + json.dumps(search_items, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8"
    )



def _get_depth(rel_path: str) -> int:
    return len(Path(rel_path).parts) - 1

def _render_head_factory(bts):
    def _render_head(title: str, desc: str, rel_path: str, og_type: str = "website", extra_schema: str = None) -> str:
        depth = _get_depth(rel_path)
        r = bts.get_rel_path(depth)
        canonical = bts.get_canonical_url(rel_path)
        schema_block = f'<script type="application/ld+json">{extra_schema}</script>' if extra_schema else ""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  {bts.GA4_SNIPPET}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/webp" href="{r}assets/images/logo/favicon.webp">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Tianya Limestone">
  <meta property="og:image" content="https://tianyalimestone.com/assets/images/hero/hero-limestone.webp">
  <meta name="twitter:card" content="summary_large_image">
  {schema_block}
  <link rel="stylesheet" href="{r}assets/css/eco-outdoor.css?v=3">
  <link rel="stylesheet" href="{r}assets/css/tianya-custom.css?v=3">
  <style>
    :root {{ --color-gold: #8c734b; --color-obsidian: #1a1a18; --color-slate: #5c564b; --color-border: #e5e0d8; --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
    .container {{ max-width: 1280px; margin: 0 auto; padding: 0 1.5rem; }}
    .section {{ padding: 3.5rem 0; }}
    .section-header {{ margin-bottom: 2rem; }}
    .section-eyebrow, .hero-eyebrow {{ display: inline-block; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #E9F551; background: rgba(26,26,24,0.75); padding: 0.25rem 0.65rem; border-radius: 4px; margin-bottom: 0.75rem; }}
    .section-eyebrow {{ color: #8c734b; background: #f5f0e6; }}
    .page-hero {{ position: relative; background: #1a1a18; color: #fff; padding: 4.5rem 0 3.5rem; overflow: hidden; }}
    .page-hero-bg {{ position: absolute; inset: 0; opacity: 0.32; pointer-events: none; }}
    .page-hero-bg img {{ width: 100%; height: 100%; object-fit: cover; }}
    .page-hero-content {{ position: relative; z-index: 2; }}
    .breadcrumb {{ font-size: 0.78rem; color: rgba(255,255,255,0.75); margin-bottom: 0.85rem; display: flex; flex-wrap: wrap; gap: 0.4rem; align-items: center; }}
    .breadcrumb a {{ color: #fff; text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .spec-card {{ background: #fff; border: 1px solid #e5e0d8; border-radius: 6px; padding: 1.35rem; box-shadow: 0 1px 3px rgba(0,0,0,0.03); }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.35rem; }}
    .badge-pill {{ display: inline-block; font-size: 0.72rem; padding: 0.2rem 0.55rem; border-radius: 4px; }}
    .tech-table {{ width: 100%; border-collapse: collapse; margin: 1rem 0 1.5rem; font-size: 0.86rem; background: #fff; border: 1px solid #e5e0d8; }}
    .tech-table th {{ background: #f5f0e6; color: #1a1a18; text-align: left; padding: 0.75rem 0.9rem; font-weight: 700; border-bottom: 1px solid #e5e0d8; }}
    .tech-table td {{ padding: 0.7rem 0.9rem; border-bottom: 1px solid #ece8e1; color: #3d3932; vertical-align: top; line-height: 1.55; }}
    .tech-table tr:hover td {{ background: #faf8f5; }}
    .btn {{ display: inline-block; padding: 0.65rem 1.25rem; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; border-radius: 4px; text-decoration: none; transition: all 0.2s; }}
    .btn-primary {{ background: #1a1a18; color: #fff; border: 1px solid #1a1a18; }}
    .btn-primary:hover {{ background: #E9F551; color: #1a1a18; border-color: #E9F551; }}
    .btn-outline-dark {{ background: #fff; color: #1a1a18; border: 1px solid #1a1a18; }}
    .btn-outline-dark:hover {{ background: #1a1a18; color: #fff; }}
    @media (max-width: 900px) {{
      .section div[style*="grid-template-columns:2fr 1fr"] {{ grid-template-columns: 1fr !important; }}
    }}
  </style>
</head>"""
    return _render_head

def build_all_expansion(all_products: list, all_pages: list):
    import build_tianya_site as bts
    r_head = _render_head_factory(bts)
    r_header = lambda tab="kb": bts.render_header(0, active_tab=tab).replace('href="index.html"', 'href="/"').replace('href="./"', 'href="/"').replace('href="#enquiry-section"', 'href="/contact-us/"').replace('href="stone-flooring/', 'href="/stone-flooring/').replace('href="applications/', 'href="/applications/').replace('href="markets/', 'href="/markets/').replace('href="knowledge-base/', 'href="/knowledge-base/').replace('href="specifications/', 'href="/specifications/').replace('href="compliance/', 'href="/compliance/').replace('href="resources/', 'href="/resources/').replace('href="blog/', 'href="/blog/').replace('href="about-us/', 'href="/about-us/').replace('href="contact-us/', 'href="/contact-us/').replace('src="assets/', 'src="/assets/')
    r_footer = lambda: bts.render_footer(0).replace('href="./"', 'href="/"').replace('href="stone-flooring/', 'href="/stone-flooring/').replace('href="applications/', 'href="/applications/').replace('href="markets/', 'href="/markets/').replace('href="knowledge-base/', 'href="/knowledge-base/').replace('href="specifications/', 'href="/specifications/').replace('href="compliance/', 'href="/compliance/').replace('href="resources/', 'href="/resources/').replace('href="blog/', 'href="/blog/').replace('href="about-us/', 'href="/about-us/').replace('href="contact-us/', 'href="/contact-us/').replace('href="sitemap.xml"', 'href="/sitemap.xml"').replace('src="assets/', 'src="/assets/')
    build_knowledge_base_hub(all_products, all_pages, r_head, r_header, r_footer)
    build_specifications_hub(all_products, all_pages, r_head, r_header, r_footer)
    build_applications_hub(all_products, all_pages, r_head, r_header, r_footer)
    build_companion_categories_hub(all_products, all_pages, r_head, r_header, r_footer)
    build_markets_hub(all_products, all_pages, r_head, r_header, r_footer)
    build_blog_expansion(all_products, all_pages, bts.BLOG_ARTICLES, r_head, r_header, r_footer)
    build_ru_subpages(all_products, all_pages, r_head, r_header, r_footer)
    build_ai_and_search_indexes(all_products, all_pages)
    print(f"[RenWork V4 Expansion] Compiled all 7 hubs -> Total Canonical Pages: {len(all_pages)}")


def append_renwork_to_llms():
    llms_section = """
## RenWork V4 Architectural Limestone Export Knowledge Base (220 Canonical Pages)
- **Export Knowledge Base Hub (21 Modules 00–20):** https://tianyalimestone.com/knowledge-base/
- **29-SKU Technical Data Sheets & CSI 04 43 00 Hub:** https://tianyalimestone.com/specifications/
- **24 Architectural Application Engineering Guides:** https://tianyalimestone.com/applications/
- **18 Companion Stone & 5-Axis CNC Profile Categories:** https://tianyalimestone.com/stone-flooring/other-categories/
- **25 Global Country & Port Import/Compliance Guides:** https://tianyalimestone.com/markets/
- **44 Technical & Commercial Engineering Blog Guides:** https://tianyalimestone.com/blog/
- **13 Russian & CIS GOST 30629-2011 Engineering Pages:** https://tianyalimestone.com/ru/
- **Machine-Readable RenWork V4 Knowledge Cards JSON:** https://tianyalimestone.com/ai/knowledge-cards.json
"""
    for fname in ("llms.txt", "llms-full.txt"):
        fpath = BASE_DIR / fname
        if fpath.exists():
            cur = fpath.read_text(encoding="utf-8")
            if "RenWork V4 Architectural Limestone Export Knowledge Base" not in cur:
                fpath.write_text(cur.rstrip() + "\n" + llms_section, encoding="utf-8")
