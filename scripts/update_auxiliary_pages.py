#!/usr/bin/env python3
"""
Tianya Limestone - Auxiliary Pages Redesign Script
Replaces the 5 auxiliary page generators in build_tianya_site.py with publication-grade,
architecturally styled implementations featuring rich WebP imagery, responsive layouts,
technical spec tables, and interactive B2B conversion funnels.
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BUILD_SCRIPT = BASE_DIR / "build_tianya_site.py"

NEW_GENERATORS_CODE = '''def generate_other_categories_page(all_products):
    depth = 2
    r = get_rel_path(depth)
    rel_file = "stone-flooring/other-categories/index.html"
    canonical = get_canonical_url(rel_file)

    title = "Companion Architectural Stone & Thin Veneer Collections | Tianya Limestone"
    description = "Explore companion architectural natural stone and thin cladding collections manufactured by Fujian Tianya Cultural Stone Co., Ltd. Ultra-thin flexible stone veneer, MCM panels, natural ledger stone, travertine, and sandstone. Available for mixed container consolidation."

    cat_cards = []
    for cat in OTHER_CATEGORIES:
        cat_cards.append(f\'\'\'
          <div id="{cat[\'id\']}" class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 py-12 border-b border-primary-10 items-center">
            <div class="lg:col-span-5">
              <div class="aspect-[4/3] w-full bg-primary-10 overflow-hidden relative border border-primary-10 shadow-sm group">
                <img src="{r}{cat[\'image\']}" alt="{cat[\'title\']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" width="600" height="450">
                <div class="absolute top-3 left-3 bg-[#251700]/80 backdrop-blur-sm text-white text-[11px] font-semibold px-2.5 py-1 tracking-wider uppercase">
                  {cat[\'thickness\']}
                </div>
              </div>
            </div>
            <div class="lg:col-span-7 space-y-4">
              <div class="flex items-center gap-3">
                <span class="text-[11px] uppercase font-semibold text-primary-40 tracking-wider">Companion Product Line</span>
                <span class="text-xs bg-[#E9F551] text-black px-2.5 py-0.5 font-semibold rounded-sm">Weight: {cat[\'weight\']}</span>
              </div>
              <h2 class="text-3xl font-heading font-medium text-primary-100">{cat[\'title\']}</h2>
              <p class="text-sm text-primary-80 leading-relaxed font-copy">
                {cat[\'desc\']}
              </p>
              <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 text-xs p-4 bg-primary-2 border border-primary-10 font-copy">
                <div>
                  <span class="text-primary-40 block text-[11px] uppercase">Thickness Range</span>
                  <strong class="text-primary-100 font-semibold">{cat[\'thickness\']}</strong>
                </div>
                <div>
                  <span class="text-primary-40 block text-[11px] uppercase">Unit Weight</span>
                  <strong class="text-primary-100 font-semibold">{cat[\'weight\']}</strong>
                </div>
                <div>
                  <span class="text-primary-40 block text-[11px] uppercase">Fabrication Base</span>
                  <strong class="text-primary-100 font-semibold">Shuitou, Fujian</strong>
                </div>
              </div>
              <div class="pt-2 flex flex-wrap gap-4 items-center">
                <a href="{COMPANY_INFO[\'sister_domain\']}" target="_blank" rel="noopener" class="text-xs font-semibold text-primary-100 hover:text-black inline-flex items-center gap-1.5 hover:underline">
                  <span>View Full Technical Specs on tystoneveneer.com</span>
                  <svg width="12" height="12" viewBox="0 0 16 16" fill="none"><path d="M5 3H13V11M13 3L3 13" stroke="currentColor" stroke-width="1.5"/></svg>
                </a>
                <a href="{r}contact-us/index.html" class="px-5 py-2.5 bg-primary-100 text-white text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-[#E9F551] hover:text-black transition-colors">
                  Inquire / Order Samples
                </a>
              </div>
            </div>
          </div>
        \'\'\')

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "name": title,
                "description": description,
                "inLanguage": "en",
                "url": canonical
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{COMPANY_INFO[\'domain\']}/"},
                    {"@type": "ListItem", "position": 2, "name": "Flooring", "item": f"{COMPANY_INFO[\'domain\']}/stone-flooring/limestone/"},
                    {"@type": "ListItem", "position": 3, "name": "Other Categories", "item": canonical}
                ]
            }
        ]
    }

    html = f\'\'\'<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/webp" href="{r}assets/images/logo/favicon.webp">

  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Tianya Limestone">
  <meta property="og:image" content="{COMPANY_INFO[\'domain\']}/assets/images/categories/mixed_container_loading.webp">
  <meta name="twitter:card" content="summary_large_image">

  <script type="application/ld+json">
{json.dumps(schema_data, indent=2)}
  </script>

  <link rel="stylesheet" href="{r}assets/css/eco-outdoor.css?v=3">
  <link rel="stylesheet" href="{r}assets/css/tianya-custom.css?v=3">
</head>
<body class="bg-white">
  {render_header(depth, active_tab=\'other\')}

  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6">
    <!-- Breadcrumb -->
    <nav class="flex items-center gap-2 text-xs text-primary-70 mb-6 font-copy" aria-label="Breadcrumbs">
      <a href="{r}index.html" class="hover:underline text-primary-40">Flooring</a>
      <span>/</span>
      <span class="font-medium text-primary-100">Other Categories</span>
    </nav>

    <!-- Visible Meta Description Matching Schema Rule -->
    <div class="sr-only">
      <p>{description}</p>
    </div>

    <!-- Editorial Hero Section -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 pb-12 border-b border-primary-10 items-center">
      <div class="lg:col-span-6 space-y-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-primary-2 border border-primary-10 text-[11px] font-semibold uppercase tracking-wider text-primary-70">
          <span>Beyond Limestone</span>
          <span>•</span>
          <span>Comprehensive Stonecraft Portfolio</span>
        </div>
        <h1 class="text-4xl lg:text-5xl font-heading font-medium text-primary-100 leading-tight">
          Companion Architectural Stone & Thin Claddings
        </h1>
        <p class="text-base text-primary-80 leading-relaxed font-copy">
          While Tianya Limestone focuses on dense architectural limestone flooring, pool copings, and modular paving, our Shuitou manufacturing headquarters produces an expansive range of architectural natural stone lines. Engineered to the same demanding export tolerances, these collections can be consolidated seamlessly into mixed export containers.
        </p>
        <div class="pt-2 flex flex-wrap gap-4">
          <a href="#mixed-consolidation" class="px-5 py-2.5 bg-primary-100 text-white text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-[#E9F551] hover:text-black transition-colors">
            Mixed Container Consolidation
          </a>
          <a href="{COMPANY_INFO[\'sister_domain\']}" target="_blank" rel="noopener" class="px-5 py-2.5 border border-primary-100 text-primary-100 text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-primary-100 hover:text-white transition-colors inline-flex items-center gap-1.5">
            <span>Visit tystoneveneer.com</span>
            <svg width="12" height="12" viewBox="0 0 16 16" fill="none"><path d="M5 3H13V11M13 3L3 13" stroke="currentColor" stroke-width="1.5"/></svg>
          </a>
        </div>
      </div>
      <div class="lg:col-span-6">
        <div class="aspect-[16/10] overflow-hidden rounded-sm border border-primary-10 shadow-sm relative group">
          <img src="{r}assets/images/categories/mixed_container_loading.webp" alt="Mixed Container Consolidation Diagram for Export" class="w-full h-full object-cover" width="800" height="500">
          <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent p-4 text-white text-xs">
            <span class="font-semibold block text-sm">Container Weight & Volume Optimization</span>
            <span class="text-white/80 text-[11px]">Heavy limestone flooring on floor + ultra-thin flexible veneers above maximize ocean freight economics.</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Mixed Container Freight Strategy Feature -->
    <section id="mixed-consolidation" class="my-14 bg-accent-limestone p-8 lg:p-12 border border-primary-10">
      <div class="max-w-3xl mb-8">
        <span class="text-xs uppercase font-semibold text-primary-70 tracking-wider block mb-1">The B2B Freight Advantage</span>
        <h2 class="text-2xl lg:text-3xl font-heading font-medium text-primary-100 mb-3">Maximize Ocean Shipping ROI via Mixed Container Consolidation</h2>
        <p class="text-xs text-primary-80 leading-relaxed font-copy">
          Natural stone flooring is inherently heavy. A standard 20GP export container reaches its 27,000 kg weight payload with approximately 380–420 m² of 30mm limestone pavers, leaving over 50% of the container\'s cubic volume empty. By consolidating dense limestone flooring together with ultra-light flexible stone veneers or MCM panels, distributors achieve 100% capacity utilization.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-white p-6 border border-primary-10">
          <span class="font-brand text-2xl font-bold text-primary-100 block mb-1">100% Utilization</span>
          <h3 class="font-heading text-base font-medium text-primary-100 mb-2">Weight + Cube Harmony</h3>
          <p class="text-xs text-primary-70 leading-relaxed font-copy">
            Place 350 m² of heavy limestone on the container deck, then pack up to 800 m² of ultra-thin flexible stone veneer (1.5 kg/m²) in the remaining vertical space.
          </p>
        </div>

        <div class="bg-white p-6 border border-primary-10">
          <span class="font-brand text-2xl font-bold text-primary-100 block mb-1">Up to 38%</span>
          <h3 class="font-heading text-base font-medium text-primary-100 mb-2">Ocean Freight Reduction</h3>
          <p class="text-xs text-primary-70 leading-relaxed font-copy">
            Amortize fixed ocean freight, port handling charges, and customs clearance fees over nearly 3x the square meter volume, dramatically lowering landed costs.
          </p>
        </div>

        <div class="bg-white p-6 border border-primary-10">
          <span class="font-brand text-2xl font-bold text-primary-100 block mb-1">1 Supplier</span>
          <h3 class="font-heading text-base font-medium text-primary-100 mb-2">Coordinated Logistics</h3>
          <p class="text-xs text-primary-70 leading-relaxed font-copy">
            A single Bill of Lading, synchronized production schedules in Shuitou, and dedicated inspection photos before crate sealing at Xiamen Seaport.
          </p>
        </div>
      </div>
    </section>

    <!-- Companion Product Lines List -->
    <div class="my-10">
      <div class="border-b border-primary-10 pb-4 mb-6">
        <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider">Product Catalog</span>
        <h2 class="text-2xl font-heading font-medium text-primary-100">Manufactured Companion Stone Lines</h2>
      </div>
      { \'\'.join(cat_cards) }
    </div>

    <!-- Sourcing Assistance RFQ Box -->
    <div class="bg-primary-2 border border-primary-10 p-8 lg:p-12 my-14">
      <div class="max-w-2xl mx-auto text-center space-y-4">
        <span class="text-xs uppercase font-semibold text-primary-70 tracking-wider">Direct Manufacturer Specification</span>
        <h3 class="font-heading text-2xl lg:text-3xl font-medium text-primary-100">Need Custom Mixed Container Quotations?</h3>
        <p class="text-xs text-primary-80 leading-relaxed font-copy">
          Our Shuitou export desk provides full container packing plans, weight distribution calculations, and express swatch boxes for limestone flooring, flexible veneer, and ledger stone.
        </p>
        <div class="pt-2">
          <a href="{r}contact-us/index.html" class="px-6 py-3 bg-primary-100 text-white font-semibold text-xs uppercase tracking-wider rounded-sm hover:bg-[#E9F551] hover:text-black transition-colors inline-block">
            Speak With An Export Consolidation Specialist →
          </a>
        </div>
      </div>
    </div>
  </main>

  {render_footer(depth)}
  <script src="{r}assets/js/search_index.js"></script>
  <script src="{r}assets/js/main.js"></script>
</body>
</html>
\'\'\'
    return html

def generate_about_page():
    depth = 1
    r = get_rel_path(depth)
    rel_file = "about-us/index.html"
    canonical = get_canonical_url(rel_file)

    title = "About Us - Quarry Concession & Stonecraft Since 2000 | Tianya Limestone"
    description = "Established in 2000 in Shuitou Town, Fujian Tianya Cultural Stone Co., Ltd. is an integrated quarry concessionaire and manufacturer of architectural natural stone, high-density limestone flooring, and thin stone cladding."

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "name": title,
                "description": description,
                "inLanguage": "en",
                "url": canonical
            },
            {
                "@type": "Organization",
                "name": COMPANY_INFO["name"],
                "alternateName": COMPANY_INFO["chinese_name"],
                "url": COMPANY_INFO["domain"],
                "logo": f"{COMPANY_INFO[\'domain\']}/assets/images/logo/tianya-logo.webp",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": COMPANY_INFO["address"],
                    "addressLocality": "Quanzhou",
                    "addressRegion": "Fujian",
                    "postalCode": "362342",
                    "addressCountry": "CN"
                },
                "contactPoint": {
                    "@type": "ContactPoint",
                    "telephone": COMPANY_INFO["phone"],
                    "contactType": "sales",
                    "email": COMPANY_INFO["sales_email"]
                }
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{COMPANY_INFO[\'domain\']}/"},
                    {"@type": "ListItem", "position": 2, "name": "About Tianya", "item": canonical}
                ]
            }
        ]
    }

    html = f\'\'\'<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/webp" href="{r}assets/images/logo/favicon.webp">

  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Tianya Limestone">
  <meta property="og:image" content="{COMPANY_INFO[\'domain\']}/assets/images/about/about_hero_quarry.webp">
  <meta name="twitter:card" content="summary_large_image">

  <script type="application/ld+json">
{json.dumps(schema_data, indent=2)}
  </script>

  <link rel="stylesheet" href="{r}assets/css/eco-outdoor.css?v=3">
  <link rel="stylesheet" href="{r}assets/css/tianya-custom.css?v=3">
</head>
<body class="bg-white">
  {render_header(depth, active_tab=\'about\')}

  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6">
    <nav class="flex items-center gap-2 text-xs text-primary-70 mb-6 font-copy" aria-label="Breadcrumbs">
      <a href="{r}index.html" class="hover:underline text-primary-40">Home</a>
      <span>/</span>
      <span class="font-medium text-primary-100">About Tianya</span>
    </nav>

    <!-- Visible Meta Description Matching Schema Rule -->
    <div class="sr-only">
      <p>{description}</p>
    </div>

    <!-- Editorial Split Hero Section -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 pb-12 border-b border-primary-10 items-center">
      <div class="lg:col-span-5 space-y-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-primary-2 border border-primary-10 text-[11px] font-semibold uppercase tracking-wider text-primary-70">
          <span>Est. May 2000</span>
          <span>•</span>
          <span>Shuitou, Fujian, China</span>
        </div>
        <h1 class="text-4xl lg:text-5xl font-heading font-medium text-primary-100 leading-tight">
          Architectural Stonecraft & Quarry Concession
        </h1>
        <span class="text-xs uppercase tracking-wider text-primary-40 font-semibold block">24+ Years of Master Fabrication in the World Stone Capital</span>
        <p class="text-base text-primary-80 leading-relaxed font-copy">
          Established in May 2000, <strong>Fujian Tianya Cultural Stone Co., Ltd.</strong> (福建天涯文化石有限公司) is an integrated quarry concessionaire and manufacturer of architectural natural stone, high-density limestone flooring, and thin stone cladding headquartered in Shuitou Town, Nan\'an City, Quanzhou, Fujian Province, China — universally recognized as the <em>World Stone Capital</em>.
        </p>
        <p class="text-xs text-primary-70 leading-relaxed font-copy">
          Over two decades of precision fabrication and quarry extraction have shaped Tianya into an international stone supplier exporting to more than 50 countries, including Australia, New Zealand, the United States, Canada, Europe, and the Middle East.
        </p>
        <div class="pt-2 flex flex-wrap gap-4">
          <a href="{r}stone-flooring/limestone/index.html" class="px-5 py-2.5 bg-primary-100 text-white text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-[#E9F551] hover:text-black transition-colors">
            Explore Limestone Collections
          </a>
          <a href="{r}contact-us/index.html" class="px-5 py-2.5 border border-primary-100 text-primary-100 text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-primary-100 hover:text-white transition-colors">
            Schedule Factory Inspection
          </a>
        </div>
      </div>
      <div class="lg:col-span-7">
        <div class="aspect-[16/10] overflow-hidden rounded-sm border border-primary-10 shadow-sm relative group">
          <img src="{r}assets/images/about/about_hero_quarry.webp" alt="Tianya Limestone Quarry Bench in Fujian Mountains" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" width="800" height="500">
          <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent p-4 text-white text-xs">
            <span class="font-semibold block text-sm">Tianya Concession Reserve No. 2 — Deep-bed high-density limestone extraction</span>
            <span class="text-white/80 text-[11px]">Precision diamond wire saws slicing monolithic raw blocks for structural flooring slabs.</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Core Factory Pillars (4-Card Metric Grid) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 my-14">
      <div class="metric-card">
        <span class="font-brand text-3xl font-bold text-primary-100 block mb-2">50,000+ m²</span>
        <h3 class="font-heading text-lg font-medium text-primary-100 mb-2">Monthly Quarry Output</h3>
        <p class="text-xs text-primary-70 leading-relaxed font-copy">
          Operating across 3 dedicated quarry concessions with multi-blade gang saws, automated slab calibrators, and tumbling barrels for dependable commercial volumes.
        </p>
      </div>

      <div class="metric-card">
        <span class="font-brand text-3xl font-bold text-primary-100 block mb-2">ASTM & CE</span>
        <h3 class="font-heading text-lg font-medium text-primary-100 mb-2">Third-Party Lab Tested</h3>
        <p class="text-xs text-primary-70 leading-relaxed font-copy">
          Every batch conforms to ASTM C97 (&lt;0.22% water absorption), ASTM C170 (>120 MPa compressive strength), ASTM C666 freeze-thaw cycles, and EN 1341 / EN 1469 CE benchmarks.
        </p>
      </div>

      <div class="metric-card">
        <span class="font-brand text-3xl font-bold text-primary-100 block mb-2">28 km</span>
        <h3 class="font-heading text-lg font-medium text-primary-100 mb-2">Proximity to Xiamen Port</h3>
        <p class="text-xs text-primary-70 leading-relaxed font-copy">
          Strategically located 28 km from Xiamen Deep-Water Container Terminal, offering rapid 15–20 day production turnaround and streamlined ocean shipping to global ports.
        </p>
      </div>

      <div class="metric-card">
        <span class="font-brand text-3xl font-bold text-primary-100 block mb-2">100% Direct</span>
        <h3 class="font-heading text-lg font-medium text-primary-100 mb-2">Quarry Provenance</h3>
        <p class="text-xs text-primary-70 leading-relaxed font-copy">
          Direct block selection at the extraction face ensures unbroken vein harmonization, zero intermediate trading markups, and project-specific color grading.
        </p>
      </div>
    </div>

    <!-- Section 2: Master Stonemasonry Craftsmanship -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center py-12 border-t border-primary-10">
      <div class="lg:col-span-6">
        <div class="aspect-[4/3] overflow-hidden rounded-sm border border-primary-10 shadow-sm relative group">
          <img src="{r}assets/images/about/craftsman_stonemason.webp" alt="Master Stonemason Hand-Finishing Limestone Edge" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" width="700" height="525">
          <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent p-4 text-white text-xs">
            <span class="font-semibold block">Artisanal Hand-Dressing</span>
            <span class="text-white/80 text-[11px]">Senior stonemason inspecting the hand-chiseled tumbled edge of an antique limestone paver.</span>
          </div>
        </div>
      </div>
      <div class="lg:col-span-6 space-y-4">
        <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider block">Artisanal Heritage Meets Modern Precision</span>
        <h2 class="text-3xl lg:text-4xl font-heading font-medium text-primary-100 leading-tight">
          Hand-Dressed Edges & Bespoke Architectural Detailing
        </h2>
        <p class="text-xs text-primary-80 leading-relaxed font-copy">
          While computer-controlled diamond saws achieve sub-millimeter caliber precision, the authentic tactile spirit of historical natural stone surfaces relies on the practiced eye and seasoned hands of our master stonemasons.
        </p>
        <p class="text-xs text-primary-80 leading-relaxed font-copy">
          From hand-chiseled tumbled borders that recreate centuries of organic foot-wear to custom rebated drop-down pool copings with 50mm–100mm seamless solid stone aprons, every bespoke architectural piece is individually inspected and detailed.
        </p>
        <ul class="text-xs text-primary-70 space-y-2 font-copy pt-1">
          <li class="flex items-center gap-2">
            <span class="text-primary-100 font-bold">✓</span> Hand-chiseled, tumbled, and rumbler-aged edge patinas
          </li>
          <li class="flex items-center gap-2">
            <span class="text-primary-100 font-bold">✓</span> Monolithic drop-down pool copings and custom step nosings
          </li>
          <li class="flex items-center gap-2">
            <span class="text-primary-100 font-bold">✓</span> Precision Roman modular sets with mathematically repeatable 1.16 m² bundles
          </li>
          <li class="flex items-center gap-2">
            <span class="text-primary-100 font-bold">✓</span> Full bay dry-lay color blending prior to export crating
          </li>
        </ul>
      </div>
    </div>

    <!-- Section 3: Shuitou Automated Fabrication Facility -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center py-12 border-t border-primary-10">
      <div class="lg:col-span-6 order-2 lg:order-1 space-y-4">
        <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider block">Industrial Scale & Technology</span>
        <h2 class="text-3xl lg:text-4xl font-heading font-medium text-primary-100 leading-tight">
          High-Precision CNC Fabrication & Closed-Loop Sustainability
        </h2>
        <p class="text-xs text-primary-80 leading-relaxed font-copy">
          Tianya\'s 35,000 m² covered fabrication complex in Shuitou Town combines raw heavy-quarry processing with cutting-edge stone finishing technology. Our facility operates 8 high-speed multi-blade diamond gang saws, 4 five-axis CNC bridge saws, automated slab calibrators, and high-capacity tumbling drums.
        </p>
        <p class="text-xs text-primary-80 leading-relaxed font-copy">
          Committed to responsible stone stewardship, our facility operates a state-of-the-art closed-loop water treatment system that purifies and recycles 95% of industrial processing water, generating zero sludge effluent and meeting the highest global environmental benchmarks.
        </p>
        <div class="grid grid-cols-2 gap-3 pt-2 text-xs font-copy">
          <div class="p-3 bg-primary-2 border border-primary-10">
            <strong class="text-primary-100 block mb-0.5">±1.0 mm Caliber</strong>
            <span class="text-primary-70">Computerized slab calibration ensures uniform bedding thickness.</span>
          </div>
          <div class="p-3 bg-primary-2 border border-primary-10">
            <strong class="text-primary-100 block mb-0.5">95% Water Recycled</strong>
            <span class="text-primary-70">Closed-loop filtration with multi-stage flocculation and zero waste.</span>
          </div>
        </div>
      </div>
      <div class="lg:col-span-6 order-1 lg:order-2">
        <div class="aspect-[4/3] overflow-hidden rounded-sm border border-primary-10 shadow-sm relative group">
          <img src="{r}assets/images/about/factory_fabrication.webp" alt="Automated Bridge Saws in Tianya Shuitou Factory" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" width="700" height="525">
          <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent p-4 text-white text-xs">
            <span class="font-semibold block">Automated High-Speed Fabrication</span>
            <span class="text-white/80 text-[11px]">Computer-controlled multi-blade bridge saws cutting dense limestone slabs with cooling water spray.</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Section 4: Packaging & Global Seaport Logistics -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center py-12 border-t border-primary-10">
      <div class="lg:col-span-6">
        <div class="aspect-[4/3] overflow-hidden rounded-sm border border-primary-10 shadow-sm relative group">
          <img src="{r}assets/images/about/export_crates_logistics.webp" alt="Solid Timber Export Crates with ISPM-15 Stamp" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" width="700" height="525">
          <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent p-4 text-white text-xs">
            <span class="font-semibold block">Heavy-Duty Export Packaging</span>
            <span class="text-white/80 text-[11px]">ISPM-15 heat-treated fumigated crates with EPE foam interleaves and heavy steel strapping.</span>
          </div>
        </div>
      </div>
      <div class="lg:col-span-6 space-y-4">
        <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider block">Zero-Breakage Delivery Guarantee</span>
        <h2 class="text-3xl lg:text-4xl font-heading font-medium text-primary-100 leading-tight">
          Heavy-Duty Timber Crating & Xiamen Seaport Drayage
        </h2>
        <p class="text-xs text-primary-80 leading-relaxed font-copy">
          International ocean freight demands packaging that withstands rough sea voyages, container shunting, and multiple forklift handlings. Every crate produced by Tianya is constructed from kiln-dried solid pine timber compliant with international ISPM 15 fumigation standards.
        </p>
        <p class="text-xs text-primary-80 leading-relaxed font-copy">
          Tiles and pavers are stacked vertically with high-density EPE foam interleaves between every piece. Crates are sealed with waterproof heat-shrink wrap and banded with high-tensile steel straps with corner edge protectors.
        </p>
        <ul class="text-xs text-primary-70 space-y-2 font-copy pt-1">
          <li class="flex items-center gap-2">
            <span class="text-primary-100 font-bold">✓</span> Certified ISPM 15 heat treatment stamps on all 4 crate facets
          </li>
          <li class="flex items-center gap-2">
            <span class="text-primary-100 font-bold">✓</span> Moisture barrier plastic heat-shrink wrapping prevents ocean salt spray efflorescence
          </li>
          <li class="flex items-center gap-2">
            <span class="text-primary-100 font-bold">✓</span> Heavy-duty dunnage airbags and timber cross-bracing inside containers
          </li>
          <li class="flex items-center gap-2">
            <span class="text-primary-100 font-bold">✓</span> Direct 28 km drayage to Xiamen Deep-Water Seaport for priority vessel loading
          </li>
        </ul>
      </div>
    </div>

    <!-- Section 5: Company Milestones (Timeline) -->
    <section class="py-14 border-t border-primary-10">
      <div class="max-w-3xl mb-10">
        <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider block mb-1">Our Journey</span>
        <h2 class="text-3xl font-heading font-medium text-primary-100">Twenty-Four Years of Continuous Evolution</h2>
      </div>

      <div class="timeline-track space-y-8">
        <div class="timeline-node">
          <span class="text-xs font-semibold text-primary-40 uppercase tracking-wider block mb-1">May 2000</span>
          <h3 class="font-heading text-lg font-medium text-primary-100 mb-1">Company Founded in Shuitou Town</h3>
          <p class="text-xs text-primary-70 leading-relaxed font-copy">
            Tianya Cultural Stone established its initial quarry concession and traditional masonry workshop in Shuitou, supplying handcrafted architectural stone to regional projects.
          </p>
        </div>

        <div class="timeline-node">
          <span class="text-xs font-semibold text-primary-40 uppercase tracking-wider block mb-1">October 2008</span>
          <h3 class="font-heading text-lg font-medium text-primary-100 mb-1">Industrial Hydraulic Gang Saw Expansion</h3>
          <p class="text-xs text-primary-70 leading-relaxed font-copy">
            Commissioned the first covered automated processing plant with hydraulic gang saws and automatic slab polishing lines, scaling monthly capacity past 20,000 m².
          </p>
        </div>

        <div class="timeline-node">
          <span class="text-xs font-semibold text-primary-40 uppercase tracking-wider block mb-1">March 2014</span>
          <h3 class="font-heading text-lg font-medium text-primary-100 mb-1">Global Architectural Specification Partnerships</h3>
          <p class="text-xs text-primary-70 leading-relaxed font-copy">
            Signed long-term supply partnerships with leading architectural stone distributors in Australia, the United Kingdom, and the United States for certified limestone paving.
          </p>
        </div>

        <div class="timeline-node">
          <span class="text-xs font-semibold text-primary-40 uppercase tracking-wider block mb-1">August 2019</span>
          <h3 class="font-heading text-lg font-medium text-primary-100 mb-1">CNC Profiling & 95% Water Recycling Transformation</h3>
          <p class="text-xs text-primary-70 leading-relaxed font-copy">
            Modernized the fabrication center with 5-axis CNC waterjets, rumbler tumbling drums, and a multi-stage closed-loop water treatment facility recovering 95% of industrial water.
          </p>
        </div>

        <div class="timeline-node">
          <span class="text-xs font-semibold text-primary-40 uppercase tracking-wider block mb-1">2024 – Present</span>
          <h3 class="font-heading text-lg font-medium text-primary-100 mb-1">Digital B2B Architectural Platform Launch</h3>
          <p class="text-xs text-primary-70 leading-relaxed font-copy">
            Launched the unified B2B platform with 29 curated limestone collections, dual architectural naming, digital CAD/BIM downloads, and express air courier sample logistics.
          </p>
        </div>
      </div>
    </section>

    <!-- Technical Facility Details & Contact Card -->
    <div class="bg-primary-2 border border-primary-10 p-8 lg:p-12 my-12">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <div>
          <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider block mb-2">Facility Credentials</span>
          <h2 class="text-3xl font-heading font-medium text-primary-100 mb-4">Shuitou Automated Fabrication Center</h2>
          <p class="text-xs text-primary-80 leading-relaxed font-copy mb-4">
            Whether crafting interlocking Roman modular paving sets or custom drop-down pool copings with 50mm rebated aprons, every piece meets millimeter tolerances.
          </p>
          <ul class="text-xs text-primary-70 space-y-2 font-copy">
            <li>✓ ISO 9001:2015 Quality Management System Certification</li>
            <li>✓ Fumigated ISPM 15 Heavy-Duty Timber Export Crates</li>
            <li>✓ Full Traceability from Raw Quarry Block to Finished Pallet</li>
            <li>✓ Dedicated Logistics Fleet for 28km Xiamen Port Container Drayage</li>
          </ul>
        </div>
        <div class="bg-white p-6 border border-primary-10 space-y-3 text-xs">
          <h4 class="font-heading text-base font-semibold text-primary-100">Factory Coordinates & Direct Contacts</h4>
          <p><strong>Legal Entity:</strong> {COMPANY_INFO[\'name\']} ({COMPANY_INFO[\'chinese_name\']})</p>
          <p><strong>Factory Address:</strong> {COMPANY_INFO[\'address\']}</p>
          <p><strong>GPS Coordinates:</strong> {COMPANY_INFO[\'coordinates\']}</p>
          <p><strong>Direct Inquiries:</strong> <a href="mailto:{COMPANY_INFO[\'email\']}" class="text-primary-100 underline font-semibold">{COMPANY_INFO[\'email\']}</a></p>
          <p><strong>Sales Hotline:</strong> <a href="tel:{COMPANY_INFO[\'phone\']}" class="text-primary-100 underline font-semibold">{COMPANY_INFO[\'phone\']}</a></p>
          <p><strong>Main Stone Portal:</strong> <a href="{COMPANY_INFO[\'sister_domain\']}" target="_blank" rel="noopener" class="text-primary-100 underline font-semibold">tystoneveneer.com</a></p>
        </div>
      </div>
    </div>
  </main>

  {render_footer(depth)}
  <script src="{r}assets/js/search_index.js"></script>
  <script src="{r}assets/js/main.js"></script>
</body>
</html>
\'\'\'
    return html

def generate_compliance_page():
    depth = 1
    r = get_rel_path(depth)
    rel_file = "compliance/index.html"
    canonical = get_canonical_url(rel_file)

    title = "ASTM & European CE Technical Compliance Hub | Tianya Limestone"
    description = "Exhaustive technical compliance data, physical property test reports, and ASTM / CE standard benchmarks for Tianya architectural limestone pavers and flooring. ASTM C97, ASTM C170, ASTM C880, ASTM C666, EN 1341."

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "name": title,
                "description": description,
                "inLanguage": "en",
                "url": canonical
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{COMPANY_INFO[\'domain\']}/"},
                    {"@type": "ListItem", "position": 2, "name": "ASTM & CE Compliance", "item": canonical}
                ]
            }
        ]
    }

    html = f\'\'\'<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/webp" href="{r}assets/images/logo/favicon.webp">

  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Tianya Limestone">
  <meta property="og:image" content="{COMPANY_INFO[\'domain\']}/assets/images/compliance/lab_testing.webp">
  <meta name="twitter:card" content="summary_large_image">

  <script type="application/ld+json">
{json.dumps(schema_data, indent=2)}
  </script>

  <link rel="stylesheet" href="{r}assets/css/eco-outdoor.css?v=3">
  <link rel="stylesheet" href="{r}assets/css/tianya-custom.css?v=3">
</head>
<body class="bg-white">
  {render_header(depth, active_tab=\'compliance\')}

  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6">
    <nav class="flex items-center gap-2 text-xs text-primary-70 mb-6 font-copy" aria-label="Breadcrumbs">
      <a href="{r}index.html" class="hover:underline text-primary-40">Home</a>
      <span>/</span>
      <span class="font-medium text-primary-100">ASTM & CE Compliance</span>
    </nav>

    <!-- Visible Meta Description Matching Schema Rule -->
    <div class="sr-only">
      <p>{description}</p>
    </div>

    <!-- Editorial Hero Section -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 pb-12 border-b border-primary-10 items-center">
      <div class="lg:col-span-5 space-y-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-primary-2 border border-primary-10 text-[11px] font-semibold uppercase tracking-wider text-primary-70">
          <span>Engineering Compliance</span>
          <span>•</span>
          <span>ASTM & CE Accredited Testing</span>
        </div>
        <h1 class="text-4xl lg:text-5xl font-heading font-medium text-primary-100 leading-tight">
          Physical & Mechanical Testing Hub
        </h1>
        <span class="text-xs uppercase tracking-wider text-primary-40 font-semibold block">Independent Laboratory Certifications & Benchmark Matrix</span>
        <p class="text-base text-primary-80 leading-relaxed font-copy">
          Architectural specification of natural stone requires unassailable engineering proof. Tianya Limestone is subjected to exhaustive laboratory physical testing under American ASTM and European EN harmonized stone standards, validating low water absorption, exceptional compressive strength, and high slip safety.
        </p>
        <div class="pt-2 flex flex-wrap gap-4">
          <a href="#test-matrix" class="px-5 py-2.5 bg-primary-100 text-white text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-[#E9F551] hover:text-black transition-colors">
            View Technical Data Matrix
          </a>
          <a href="#download-certs" class="px-5 py-2.5 border border-primary-100 text-primary-100 text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-primary-100 hover:text-white transition-colors">
            Download Lab Reports
          </a>
        </div>
      </div>
      <div class="lg:col-span-7">
        <div class="aspect-[16/10] overflow-hidden rounded-sm border border-primary-10 shadow-sm relative group">
          <img src="{r}assets/images/compliance/lab_testing.webp" alt="Materials Engineering Hydraulic Compressive Strength Testing" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" width="800" height="500">
          <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent p-4 text-white text-xs">
            <span class="font-semibold block">Materials Engineering Laboratory</span>
            <span class="text-white/80 text-[11px]">Hydraulic compressive testing apparatus crushing cylindrical core specimens of high-density limestone.</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Core Standards (4 Badges) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 my-14">
      <div class="cert-card">
        <div class="qc-step-badge">CE</div>
        <div>
          <h3 class="font-heading text-base font-semibold text-primary-100">CE Marking (EN 1341)</h3>
          <p class="text-xs text-primary-70 mt-1 font-copy">Full Declaration of Performance (DoP) for external paving and internal cladding in EU member states.</p>
        </div>
      </div>

      <div class="cert-card">
        <div class="qc-step-badge">ASTM</div>
        <div>
          <h3 class="font-heading text-base font-semibold text-primary-100">ASTM C97 / C170</h3>
          <p class="text-xs text-primary-70 mt-1 font-copy">Compressive strength 128.5 MPa, exceeding ASTM commercial limestone requirements by over 130%.</p>
        </div>
      </div>

      <div class="cert-card">
        <div class="qc-step-badge">P5</div>
        <div>
          <h3 class="font-heading text-base font-semibold text-primary-100">AS 4586 Slip Safety</h3>
          <p class="text-xs text-primary-70 mt-1 font-copy">Wet Pendulum test ratings P4 to P5 (R11 to R12 equivalent), certified for commercial concourses and pool surrounds.</p>
        </div>
      </div>

      <div class="cert-card">
        <div class="qc-step-badge">A1</div>
        <div>
          <h3 class="font-heading text-base font-semibold text-primary-100">Reaction to Fire Class A1</h3>
          <p class="text-xs text-primary-70 mt-1 font-copy">EN 13501-1 and ASTM E84 Class A compliant. 100% non-combustible natural mineral with zero flame spread.</p>
        </div>
      </div>
    </div>

    <!-- Testing Matrix Table Section -->
    <section id="test-matrix" class="my-14">
      <div class="border-b border-primary-10 pb-4 mb-6">
        <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider">Technical Data Sheet (TDS)</span>
        <h2 class="text-3xl font-heading font-medium text-primary-100">Physical & Mechanical Properties Matrix</h2>
        <p class="text-xs text-primary-70 mt-1">Certified laboratory test results performed on Tianya dense architectural limestone specimens.</p>
      </div>

      <div class="overflow-x-auto border border-primary-10 bg-white shadow-sm">
        <table class="spec-table">
          <thead>
            <tr>
              <th>Physical Property</th>
              <th>Testing Standard</th>
              <th>Tianya Limestone Specification</th>
              <th>Commercial Standard Requirement</th>
              <th>Compliance Verdict</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="font-semibold text-primary-100">Water Absorption</td>
              <td class="font-mono text-xs text-primary-70">ASTM C97 / EN 13755</td>
              <td class="font-semibold text-black">0.18% – 0.22%</td>
              <td class="text-xs text-primary-70">&le; 3.0% (ASTM Class III)</td>
              <td><span class="text-xs font-semibold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded">✓ Exceeds ASTM Standard</span></td>
            </tr>
            <tr>
              <td class="font-semibold text-primary-100">Bulk Specific Gravity (Density)</td>
              <td class="font-mono text-xs text-primary-70">ASTM C97 / EN 1936</td>
              <td class="font-semibold text-black">2.65 – 2.70 g/cm³</td>
              <td class="text-xs text-primary-70">&ge; 2.56 g/cm³</td>
              <td><span class="text-xs font-semibold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded">✓ High-Density Crystalline</span></td>
            </tr>
            <tr>
              <td class="font-semibold text-primary-100">Compressive Strength (Dry)</td>
              <td class="font-mono text-xs text-primary-70">ASTM C170 / EN 1926</td>
              <td class="font-semibold text-black">128.5 MPa</td>
              <td class="text-xs text-primary-70">&ge; 55.0 MPa</td>
              <td><span class="text-xs font-semibold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded">✓ +133% Above Minimum</span></td>
            </tr>
            <tr>
              <td class="font-semibold text-primary-100">Compressive Strength (Wet)</td>
              <td class="font-mono text-xs text-primary-70">ASTM C170 / EN 1926</td>
              <td class="font-semibold text-black">115.0 MPa</td>
              <td class="text-xs text-primary-70">&ge; 50.0 MPa</td>
              <td><span class="text-xs font-semibold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded">✓ High Wet Bearing</span></td>
            </tr>
            <tr>
              <td class="font-semibold text-primary-100">Flexural / Bending Strength</td>
              <td class="font-mono text-xs text-primary-70">ASTM C880 / EN 12372</td>
              <td class="font-semibold text-black">18.4 – 24.2 MPa</td>
              <td class="text-xs text-primary-70">&ge; 6.9 MPa</td>
              <td><span class="text-xs font-semibold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded">✓ Commercial Paving Grade</span></td>
            </tr>
            <tr>
              <td class="font-semibold text-primary-100">Freeze-Thaw Resistance</td>
              <td class="font-mono text-xs text-primary-70">ASTM C666 / EN 12371</td>
              <td class="font-semibold text-black">100 Cycles (0% Cleavage / Spalling)</td>
              <td class="text-xs text-primary-70">&le; 1.0% mass loss</td>
              <td><span class="text-xs font-semibold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded">✓ Alpine & Winter Proof</span></td>
            </tr>
            <tr>
              <td class="font-semibold text-primary-100">Slip Resistance (Wet Pendulum)</td>
              <td class="font-mono text-xs text-primary-70">AS 4586 / ASTM C1028</td>
              <td class="font-semibold text-black">P4 to P5 (R11 to R12)</td>
              <td class="text-xs text-primary-70">&ge; P3 for wet pedestrian areas</td>
              <td><span class="text-xs font-semibold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded">✓ Pool Deck & Civic Approved</span></td>
            </tr>
            <tr>
              <td class="font-semibold text-primary-100">Reaction to Fire</td>
              <td class="font-mono text-xs text-primary-70">EN 13501-1 / ASTM E84</td>
              <td class="font-semibold text-black">Class A1 / Flame Spread 0</td>
              <td class="text-xs text-primary-70">Non-combustible</td>
              <td><span class="text-xs font-semibold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded">✓ 100% Non-Combustible</span></td>
            </tr>
            <tr>
              <td class="font-semibold text-primary-100">Deep Abrasion Resistance</td>
              <td class="font-mono text-xs text-primary-70">EN 14157 / ASTM C1353</td>
              <td class="font-semibold text-black">18.2 mm Groove Length</td>
              <td class="text-xs text-primary-70">&le; 25.0 mm for intensive use</td>
              <td><span class="text-xs font-semibold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded">✓ Heavy Traffic Rated</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- Six-Gate Quality Assurance Protocol -->
    <section class="my-16 border-t border-primary-10 pt-12">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-5">
          <div class="aspect-[4/3] overflow-hidden rounded-sm border border-primary-10 shadow-sm relative group">
            <img src="{r}assets/images/compliance/quality_inspection.webp" alt="Quality Control Inspector Measuring Limestone Caliber" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" width="600" height="450">
            <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent p-4 text-white text-xs">
              <span class="font-semibold block">Precision Thickness Calibration</span>
              <span class="text-white/80 text-[11px]">Digital vernier micrometer measurement ensuring strict &plusmn;1.0mm caliber tolerance.</span>
            </div>
          </div>
        </div>

        <div class="lg:col-span-7 space-y-4">
          <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider block">Quality Management System</span>
          <h2 class="text-3xl font-heading font-medium text-primary-100">Six-Gate Quality Assurance Protocol</h2>
          <p class="text-xs text-primary-80 leading-relaxed font-copy">
            Every cubic meter of natural limestone processed at our Shuitou facility passes through six mandatory quality gates before export shipping authorization:
          </p>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
            <div class="p-3 bg-primary-2 border border-primary-10">
              <div class="flex items-center gap-2 mb-1">
                <span class="text-xs font-bold text-primary-100 bg-[#E9F551] px-1.5 py-0.5 rounded-sm">01</span>
                <strong class="text-xs text-primary-100">Geological Soundness Scan</strong>
              </div>
              <p class="text-[11px] text-primary-70 font-copy">Ultrasonic scanning of extracted raw blocks to confirm dense crystalline matrix and zero fissure voids.</p>
            </div>

            <div class="p-3 bg-primary-2 border border-primary-10">
              <div class="flex items-center gap-2 mb-1">
                <span class="text-xs font-bold text-primary-100 bg-[#E9F551] px-1.5 py-0.5 rounded-sm">02</span>
                <strong class="text-xs text-primary-100">Precision Slicing (&plusmn;1mm)</strong>
              </div>
              <p class="text-[11px] text-primary-70 font-copy">Automated multi-blade diamond gang saws with laser guides ensuring squareness and thickness calibration.</p>
            </div>

            <div class="p-3 bg-primary-2 border border-primary-10">
              <div class="flex items-center gap-2 mb-1">
                <span class="text-xs font-bold text-primary-100 bg-[#E9F551] px-1.5 py-0.5 rounded-sm">03</span>
                <strong class="text-xs text-primary-100">Tactile Finish Uniformity</strong>
              </div>
              <p class="text-[11px] text-primary-70 font-copy">Verification of tumbling edge depth, antique brushing consistency, and sandblasted slip traction.</p>
            </div>

            <div class="p-3 bg-primary-2 border border-primary-10">
              <div class="flex items-center gap-2 mb-1">
                <span class="text-xs font-bold text-primary-100 bg-[#E9F551] px-1.5 py-0.5 rounded-sm">04</span>
                <strong class="text-xs text-primary-100">Bay Dry-Lay Tone Blending</strong>
              </div>
              <p class="text-[11px] text-primary-70 font-copy">Full-bay mock-up dry lay to blend natural vein rhythms and ensure smooth tonal gradation across batches.</p>
            </div>

            <div class="p-3 bg-primary-2 border border-primary-10">
              <div class="flex items-center gap-2 mb-1">
                <span class="text-xs font-bold text-primary-100 bg-[#E9F551] px-1.5 py-0.5 rounded-sm">05</span>
                <strong class="text-xs text-primary-100">ISPM 15 Export Crating</strong>
              </div>
              <p class="text-[11px] text-primary-70 font-copy">Kiln-dried fumigated solid timber crates, high-density foam interleaves, and heavy steel banding.</p>
            </div>

            <div class="p-3 bg-primary-2 border border-primary-10">
              <div class="flex items-center gap-2 mb-1">
                <span class="text-xs font-bold text-primary-100 bg-[#E9F551] px-1.5 py-0.5 rounded-sm">06</span>
                <strong class="text-xs text-primary-100">Pre-Shipment Photo Pack</strong>
              </div>
              <p class="text-[11px] text-primary-70 font-copy">High-resolution photographic dossier of finished crates and container stuffing sent before dispatch.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Download Testing Certificates -->
    <section id="download-certs" class="my-14">
      <div class="border-b border-primary-10 pb-4 mb-6">
        <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider">Document Downloads</span>
        <h2 class="text-2xl font-heading font-medium text-primary-100">Official Testing Reports & Declarations</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="resource-card">
          <div>
            <span class="text-[10px] uppercase font-semibold text-primary-40 tracking-wider block mb-1">PDF / 2.4 MB</span>
            <h3 class="font-heading text-lg font-medium text-primary-100 mb-2">ASTM C97 & C170 Comprehensive Lab Dossier</h3>
            <p class="text-xs text-primary-70 leading-relaxed font-copy">Complete physical engineering test reports including water absorption, specific gravity, compressive strength, and flexural strength data.</p>
          </div>
          <div class="mt-6 pt-4 border-t border-primary-10">
            <a href="{COMPANY_INFO[\'sister_domain\']}/docs/3_engineering_whitepapers_and_case_studies.md" target="_blank" rel="noopener" class="text-xs font-semibold text-primary-100 hover:text-black inline-flex items-center gap-1.5">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              <span>Download ASTM Dossier</span>
            </a>
          </div>
        </div>

        <div class="resource-card">
          <div>
            <span class="text-[10px] uppercase font-semibold text-primary-40 tracking-wider block mb-1">PDF / 1.6 MB</span>
            <h3 class="font-heading text-lg font-medium text-primary-100 mb-2">European CE Declaration of Performance (DoP)</h3>
            <p class="text-xs text-primary-70 leading-relaxed font-copy">Official CE marking certification compliant with EN 1341 (External Natural Stone Paving) and EN 1469 (Slabs for Cladding).</p>
          </div>
          <div class="mt-6 pt-4 border-t border-primary-10">
            <a href="{COMPANY_INFO[\'sister_domain\']}/docs/3_engineering_whitepapers_and_case_studies.md" target="_blank" rel="noopener" class="text-xs font-semibold text-primary-100 hover:text-black inline-flex items-center gap-1.5">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              <span>Download CE Certificate</span>
            </a>
          </div>
        </div>

        <div class="resource-card">
          <div>
            <span class="text-[10px] uppercase font-semibold text-primary-40 tracking-wider block mb-1">PDF / 890 KB</span>
            <h3 class="font-heading text-lg font-medium text-primary-100 mb-2">AS 4586 Wet Pendulum Slip Test Certificate</h3>
            <p class="text-xs text-primary-70 leading-relaxed font-copy">Certified British Pendulum Test ratings (P4 and P5) across honed, tumbled, sandblasted, and flamed limestone surfaces.</p>
          </div>
          <div class="mt-6 pt-4 border-t border-primary-10">
            <a href="{COMPANY_INFO[\'sister_domain\']}/docs/3_engineering_whitepapers_and_case_studies.md" target="_blank" rel="noopener" class="text-xs font-semibold text-primary-100 hover:text-black inline-flex items-center gap-1.5">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              <span>Download Slip Report</span>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Project Specific Lab Testing Inquiry -->
    <div class="bg-primary-2 border border-primary-10 p-8 lg:p-10 my-10 flex flex-col md:flex-row items-center justify-between gap-6">
      <div>
        <h3 class="font-heading text-xl font-medium text-primary-100">Need Project-Specific Laboratory Test Reports or CSI Specifications?</h3>
        <p class="text-xs text-primary-70 mt-1 font-copy">We provide project batch certificates of analysis (CoA), LEED contribution documentation, and customized CSI Section 04 42 00 3-part specifications.</p>
      </div>
      <a href="mailto:{COMPANY_INFO[\'sales_email\']}?subject=Request%20ASTM%20Batch%20Test%20Reports" class="px-5 py-2.5 bg-primary-100 text-white text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-[#E9F551] hover:text-black transition-colors flex-shrink-0">
        Email Engineering Desk →
      </a>
    </div>
  </main>

  {render_footer(depth)}
  <script src="{r}assets/js/search_index.js"></script>
  <script src="{r}assets/js/main.js"></script>
</body>
</html>
\'\'\'
    return html

def generate_resources_page():
    depth = 1
    r = get_rel_path(depth)
    rel_file = "resources/index.html"
    canonical = get_canonical_url(rel_file)

    title = "Architectural Technical Resources & CAD/BIM Downloads | Tianya Limestone"
    description = "Download technical drawings, modular pattern schedules, sub-base preparation guidelines, ASTM compliance reports, and CAD hatch files for Tianya Limestone pavers."

    resources_list = [
        {"title": "Roman Modular Pattern CAD Schematics & Layout Schedule", "type": "PDF & DWG / 2.4 MB", "desc": "Complete dimensional schematics for Roman modular 4-size laying patterns (1.16 m² repeatable sets), perimeter terminations, and corner details."},
        {"title": "Sub-Base Preparation & Paving Adhesive Guidelines", "type": "PDF / 3.1 MB", "desc": "Mortar bed mix ratios, concrete slab preparation, movement expansion joint placements, and pool coping installation details."},
        {"title": "Drop-Down Rebated Pool Coping & Step Tread Details", "type": "DWG & PDF / 1.9 MB", "desc": "Vector architectural details for monolithic drop-face copings (30mm, 50mm, 80mm aprons), pencil-round edges, and concealed skimmer lids."},
        {"title": "ASTM C97 & C170 Comprehensive Engineering Testing Dossier", "type": "PDF / 1.2 MB", "desc": "Certified compressive, flexural, density and water absorption laboratory reports from accredited independent testing bodies."},
        {"title": "Natural Stone Flooring & Paving Maintenance Manual", "type": "PDF / 1.8 MB", "desc": "Step-by-step penetrating sealer selection, routine pH-neutral cleaning protocols, and stain removal procedures for outdoor and indoor limestone."},
        {"title": "10-Year Commercial & Residential Manufacturer Warranty", "type": "PDF / 850 KB", "desc": "Official manufacturer warranty terms against structural delamination, crumbling, and freeze-thaw failure under normal architectural use."}
    ]

    res_cards = []
    for item in resources_list:
        res_cards.append(f\'\'\'
          <div class="resource-card">
            <div>
              <span class="text-[10px] uppercase font-semibold text-primary-40 tracking-wider block mb-1">{item[\'type\']}</span>
              <h3 class="font-heading text-lg font-medium text-primary-100 mb-2">{item[\'title\']}</h3>
              <p class="text-xs text-primary-70 leading-relaxed font-copy">{item[\'desc\']}</p>
            </div>
            <div class="mt-6 pt-4 border-t border-primary-10">
              <a href="{COMPANY_INFO[\'sister_domain\']}/docs/3_engineering_whitepapers_and_case_studies.md" target="_blank" rel="noopener" class="text-xs font-semibold text-primary-100 hover:text-black inline-flex items-center gap-1.5">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                <span>Download Specification File</span>
              </a>
            </div>
          </div>
        \'\'\')

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "name": title,
                "description": description,
                "inLanguage": "en",
                "url": canonical
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{COMPANY_INFO[\'domain\']}/"},
                    {"@type": "ListItem", "position": 2, "name": "Resources", "item": canonical}
                ]
            }
        ]
    }

    html = f\'\'\'<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/webp" href="{r}assets/images/logo/favicon.webp">

  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Tianya Limestone">
  <meta property="og:image" content="{COMPANY_INFO[\'domain\']}/assets/images/resources/cad_blueprints.webp">
  <meta name="twitter:card" content="summary_large_image">

  <script type="application/ld+json">
{json.dumps(schema_data, indent=2)}
  </script>

  <link rel="stylesheet" href="{r}assets/css/eco-outdoor.css?v=3">
  <link rel="stylesheet" href="{r}assets/css/tianya-custom.css?v=3">
</head>
<body class="bg-white">
  {render_header(depth, active_tab=\'resources\')}

  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6">
    <nav class="flex items-center gap-2 text-xs text-primary-70 mb-6 font-copy" aria-label="Breadcrumbs">
      <a href="{r}index.html" class="hover:underline text-primary-40">Home</a>
      <span>/</span>
      <span class="font-medium text-primary-100">Resources & CAD</span>
    </nav>

    <!-- Visible Meta Description Matching Schema Rule -->
    <div class="sr-only">
      <p>{description}</p>
    </div>

    <!-- Editorial Hero Section -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 pb-12 border-b border-primary-10 items-center">
      <div class="lg:col-span-5 space-y-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-primary-2 border border-primary-10 text-[11px] font-semibold uppercase tracking-wider text-primary-70">
          <span>Architectural Documentation</span>
          <span>•</span>
          <span>CAD, BIM & Specifications</span>
        </div>
        <h1 class="text-4xl lg:text-5xl font-heading font-medium text-primary-100 leading-tight">
          Technical Resources & CAD/BIM Downloads
        </h1>
        <span class="text-xs uppercase tracking-wider text-primary-40 font-semibold block">Streamline Specification from Concept Drafting to Site Construction</span>
        <p class="text-base text-primary-80 leading-relaxed font-copy">
          Access authoritative technical drawings, modular pattern schedules, sub-base preparation guidelines, and CAD/BIM resources curated to facilitate seamless specification from preliminary concept through final site construction.
        </p>
        <div class="pt-2 flex flex-wrap gap-4">
          <a href="#master-bundle" class="px-5 py-2.5 bg-primary-100 text-white text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-[#E9F551] hover:text-black transition-colors">
            Download 2026 Architect Pack
          </a>
          <a href="#laying-patterns" class="px-5 py-2.5 border border-primary-100 text-primary-100 text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-primary-100 hover:text-white transition-colors">
            Modular Laying Schedules
          </a>
        </div>
      </div>
      <div class="lg:col-span-7">
        <div class="aspect-[16/10] overflow-hidden rounded-sm border border-primary-10 shadow-sm relative group">
          <img src="{r}assets/images/resources/cad_blueprints.webp" alt="Architectural CAD Blueprints and Limestone Material Swatches" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" width="800" height="500">
          <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent p-4 text-white text-xs">
            <span class="font-semibold block">Architectural Studio Flatlay</span>
            <span class="text-white/80 text-[11px]">Technical floor plan schematics, scale drafting instruments, and calibrated limestone swatches.</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Featured Master Download Hero Box -->
    <section id="master-bundle" class="my-14 bg-primary-100 text-white p-8 lg:p-12 rounded-sm shadow-md">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <div class="lg:col-span-8 space-y-3">
          <div class="inline-flex items-center gap-2 px-2.5 py-0.5 bg-[#E9F551] text-black text-[11px] font-bold uppercase tracking-wider rounded-sm">
            Complete Specifier Bundle
          </div>
          <h2 class="text-2xl lg:text-3xl font-heading font-medium text-white">2026 Master Architect Specification Pack</h2>
          <p class="text-xs text-white/80 leading-relaxed font-copy">
            A unified 18.5 MB compressed package containing all 29 product technical data sheets (TDS), French Roman modular pattern CAD blocks (.DWG and .DXF), AutoCAD .PAT hatch patterns, ASTM C97/C170 lab test dossiers, and CSI MasterFormat Section 04 42 00 3-part guide specifications.
          </p>
          <div class="flex flex-wrap gap-4 text-xs text-white/70 pt-2 font-mono">
            <span>✓ 29 Product TDS (PDF)</span>
            <span>✓ 2D/3D CAD Blocks (DWG)</span>
            <span>✓ AutoCAD Hatch Patterns (.PAT)</span>
            <span>✓ CSI Section 04 42 00 (DOCX)</span>
          </div>
        </div>
        <div class="lg:col-span-4 text-center lg:text-right">
          <a href="{COMPANY_INFO[\'sister_domain\']}/docs/3_engineering_whitepapers_and_case_studies.md" target="_blank" rel="noopener" class="px-6 py-3.5 bg-[#E9F551] text-black font-semibold text-xs uppercase tracking-wider rounded-sm hover:bg-white transition-colors inline-block shadow">
            Download Complete Pack (18.5 MB) →
          </a>
        </div>
      </div>
    </section>

    <!-- Modular Laying Patterns Feature Section -->
    <section id="laying-patterns" class="my-14 border-t border-primary-10 pt-12">
      <div class="border-b border-primary-10 pb-4 mb-8">
        <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider">Modular Geometry</span>
        <h2 class="text-3xl font-heading font-medium text-primary-100">Roman Modular 4-Size Laying Pattern Schedule</h2>
        <p class="text-xs text-primary-70 mt-1">Mathematical ratio for repeatable 1.16 m² (12.48 sq ft) paving bundles with interlocking organic joint rhythm.</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-6">
          <div class="aspect-[4/3] overflow-hidden rounded-sm border border-primary-10 shadow-sm relative group">
            <img src="{r}assets/images/resources/modular_pattern_diagram.webp" alt="Roman Modular Stone Paving Pattern Layout Diagram" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" width="700" height="525">
            <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent p-4 text-white text-xs">
              <span class="font-semibold block">French Roman Modular Diagram</span>
              <span class="text-white/80 text-[11px]">Interlocking non-linear layout utilizing four coordinated rectangular and square sizes.</span>
            </div>
          </div>
        </div>

        <div class="lg:col-span-6 space-y-4">
          <div class="border border-primary-10 bg-white p-5 space-y-3 font-copy text-xs">
            <h4 class="font-heading text-base font-semibold text-primary-100">Repeat Module Schedule (1.16 m² per bundle)</h4>
            <table class="w-full text-xs">
              <thead>
                <tr class="border-b border-primary-10 text-primary-40 text-left">
                  <th class="py-2">Tile Format</th>
                  <th class="py-2">Dimensions (mm)</th>
                  <th class="py-2">Quantity / Bundle</th>
                  <th class="py-2">Area Share</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-primary-10">
                <tr>
                  <td class="py-2 font-semibold text-primary-100">Size A (Large Rect.)</td>
                  <td class="py-2 font-mono">600 &times; 400 mm</td>
                  <td class="py-2">1 piece</td>
                  <td class="py-2">20.7%</td>
                </tr>
                <tr>
                  <td class="py-2 font-semibold text-primary-100">Size B (Square)</td>
                  <td class="py-2 font-mono">400 &times; 400 mm</td>
                  <td class="py-2">2 pieces</td>
                  <td class="py-2">27.6%</td>
                </tr>
                <tr>
                  <td class="py-2 font-semibold text-primary-100">Size C (Small Rect.)</td>
                  <td class="py-2 font-mono">400 &times; 200 mm</td>
                  <td class="py-2">1 piece</td>
                  <td class="py-2">6.9%</td>
                </tr>
                <tr>
                  <td class="py-2 font-semibold text-primary-100">Size D (Accent Sq.)</td>
                  <td class="py-2 font-mono">200 &times; 200 mm</td>
                  <td class="py-2">2 pieces</td>
                  <td class="py-2">6.9%</td>
                </tr>
              </tbody>
            </table>
            <p class="text-[11px] text-primary-70 pt-2 border-t border-primary-10">
              * Recommended grout joint: 3mm to 5mm using flexible polymer-modified exterior paving grout.
            </p>
          </div>

          <div class="grid grid-cols-2 gap-3 text-xs font-copy">
            <div class="p-3 bg-primary-2 border border-primary-10">
              <strong class="text-primary-100 block mb-0.5">Stretcher Bond Options</strong>
              <span class="text-primary-70">Single-format running bond in 600&times;300, 800&times;400, or 900&times;600mm.</span>
            </div>
            <div class="p-3 bg-primary-2 border border-primary-10">
              <strong class="text-primary-100 block mb-0.5">Custom Sizing Support</strong>
              <span class="text-primary-70">Computerized bridge saws slice to any project architectural dimensions.</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Curated Resource Cards Grid -->
    <section class="my-14 border-t border-primary-10 pt-12">
      <div class="border-b border-primary-10 pb-4 mb-6">
        <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider">Document Library</span>
        <h2 class="text-2xl font-heading font-medium text-primary-100">Engineering Guides & Specifications</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        { \'\'.join(res_cards) }
      </div>
    </section>

    <!-- Sub-Base Engineering Comparison Box -->
    <div class="bg-primary-2 border border-primary-10 p-8 lg:p-12 my-14">
      <div class="max-w-3xl mb-8">
        <span class="text-xs uppercase font-semibold text-primary-70 tracking-wider block mb-1">Installation Engineering</span>
        <h3 class="font-heading text-2xl font-medium text-primary-100">Sub-Base Preparation: Rigid vs Flexible Foundations</h3>
        <p class="text-xs text-primary-80 leading-relaxed font-copy">
          Correct sub-base specification is critical to ensure long-term structural integrity and prevent differential settlement cracking.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="bg-white p-6 border border-primary-10 space-y-3 font-copy text-xs">
          <div class="inline-block bg-primary-100 text-white font-semibold text-[11px] px-2 py-0.5 uppercase tracking-wider rounded-sm">
            Rigid Installation (Recommended)
          </div>
          <h4 class="font-heading text-base font-semibold text-primary-100">Mortar Bed Over Reinforced Concrete Slab</h4>
          <p class="text-primary-70 leading-relaxed">
            Essential for vehicular driveways, commercial concourses, and swimming pool copings. Minimum 100mm reinforced concrete slab cured for 28 days.
          </p>
          <ul class="text-primary-70 space-y-1">
            <li>• C2S1 / C2S2 polymer-modified exterior tile adhesive</li>
            <li>• 100% full contact bed coverage (no dot-and-dab voids)</li>
            <li>• Perimeter expansion joints every 4.0 to 5.0 meters</li>
          </ul>
        </div>

        <div class="bg-white p-6 border border-primary-10 space-y-3 font-copy text-xs">
          <div class="inline-block bg-primary-10 text-primary-100 font-semibold text-[11px] px-2 py-0.5 uppercase tracking-wider rounded-sm">
            Flexible Installation
          </div>
          <h4 class="font-heading text-base font-semibold text-primary-100">Compacted Crushed Rock & Bedding Sand</h4>
          <p class="text-primary-70 leading-relaxed">
            Permeable solution for residential pedestrian garden pathways and courtyards with free-draining sandy sub-soils.
          </p>
          <ul class="text-primary-70 space-y-1">
            <li>• 100mm–150mm heavily compacted roadbase aggregate</li>
            <li>• 25mm–30mm washed coarse bedding sand layer</li>
            <li>• Polymeric jointing sand between paver joints</li>
          </ul>
        </div>
      </div>
    </div>
  </main>

  {render_footer(depth)}
  <script src="{r}assets/js/search_index.js"></script>
  <script src="{r}assets/js/main.js"></script>
</body>
</html>
\'\'\'
    return html

def generate_contact_page():
    depth = 1
    r = get_rel_path(depth)
    rel_file = "contact-us/index.html"
    canonical = get_canonical_url(rel_file)

    title = "Contact Factory Sales & Request Samples | Tianya Limestone"
    description = "Contact Fujian Tianya Cultural Stone Co., Ltd. for quarry-direct limestone pricing, express sample box shipping, and FOB/CIF container quotes. 28km from Xiamen Port."

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "name": title,
                "description": description,
                "inLanguage": "en",
                "url": canonical
            },
            {
                "@type": "Organization",
                "name": COMPANY_INFO["name"],
                "alternateName": COMPANY_INFO["chinese_name"],
                "url": COMPANY_INFO["domain"],
                "logo": f"{COMPANY_INFO[\'domain\']}/assets/images/logo/tianya-logo.webp",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": COMPANY_INFO["address"],
                    "addressLocality": "Quanzhou",
                    "addressRegion": "Fujian",
                    "postalCode": "362342",
                    "addressCountry": "CN"
                },
                "contactPoint": [
                    {
                        "@type": "ContactPoint",
                        "telephone": COMPANY_INFO["phone"],
                        "contactType": "sales",
                        "email": COMPANY_INFO["sales_email"]
                    },
                    {
                        "@type": "ContactPoint",
                        "telephone": COMPANY_INFO["phone_alt"],
                        "contactType": "customer service"
                    }
                ]
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{COMPANY_INFO[\'domain\']}/"},
                    {"@type": "ListItem", "position": 2, "name": "Contact Us", "item": canonical}
                ]
            }
        ]
    }

    html = f\'\'\'<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/webp" href="{r}assets/images/logo/favicon.webp">

  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Tianya Limestone">
  <meta property="og:image" content="{COMPANY_INFO[\'domain\']}/assets/images/contact/sample_kit_box.webp">
  <meta name="twitter:card" content="summary_large_image">

  <script type="application/ld+json">
{json.dumps(schema_data, indent=2)}
  </script>

  <link rel="stylesheet" href="{r}assets/css/eco-outdoor.css?v=3">
  <link rel="stylesheet" href="{r}assets/css/tianya-custom.css?v=3">
</head>
<body class="bg-white">
  {render_header(depth, active_tab=\'contact\')}

  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6">
    <nav class="flex items-center gap-2 text-xs text-primary-70 mb-6 font-copy" aria-label="Breadcrumbs">
      <a href="{r}index.html" class="hover:underline text-primary-40">Home</a>
      <span>/</span>
      <span class="font-medium text-primary-100">Contact Us</span>
    </nav>

    <!-- Visible Meta Description Matching Schema Rule -->
    <div class="sr-only">
      <p>{description}</p>
    </div>

    <!-- Editorial Hero Section -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 pb-12 border-b border-primary-10 items-center">
      <div class="lg:col-span-5 space-y-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 bg-primary-2 border border-primary-10 text-[11px] font-semibold uppercase tracking-wider text-primary-70">
          <span>Factory Direct Sourcing</span>
          <span>•</span>
          <span>Shuitou HQ Export Desk</span>
        </div>
        <h1 class="text-4xl lg:text-5xl font-heading font-medium text-primary-100 leading-tight">
          Direct Quarry Sourcing & Express Sample Logistics
        </h1>
        <span class="text-xs uppercase tracking-wider text-primary-40 font-semibold block">Connect Directly with Our Bilingual Stone Engineering Team</span>
        <p class="text-base text-primary-80 leading-relaxed font-copy">
          Whether you require physical sample kits delivered to your architecture studio, FOB Xiamen container quotes, CIF ocean schedules to your local port, or custom-dimensioned pool copings, our export team is at your disposal.
        </p>
        <div class="pt-2 flex flex-wrap gap-4">
          <a href="#sample-box-section" class="px-5 py-2.5 bg-primary-100 text-white text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-[#E9F551] hover:text-black transition-colors">
            Order Curated Sample Kit
          </a>
          <a href="#rfq-form" class="px-5 py-2.5 border border-primary-100 text-primary-100 text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-primary-100 hover:text-white transition-colors">
            Submit Specification RFQ
          </a>
        </div>
      </div>
      <div class="lg:col-span-7">
        <div class="aspect-[16/10] overflow-hidden rounded-sm border border-primary-10 shadow-sm relative group">
          <img src="{r}assets/images/contact/sample_kit_box.webp" alt="Curated Bespoke Architectural Limestone Sample Presentation Box" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" width="800" height="500">
          <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent p-4 text-white text-xs">
            <span class="font-semibold block">Architectural Presentation Sample Box</span>
            <span class="text-white/80 text-[11px]">Matte-black timber presentation box containing 100x100mm limestone swatches with laser-engraved finish labels.</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Sample Box Showcase Feature -->
    <section id="sample-box-section" class="my-14 bg-accent-limestone p-8 lg:p-12 border border-primary-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <div class="lg:col-span-8 space-y-3">
          <span class="text-xs uppercase font-semibold text-primary-70 tracking-wider block">Express Material Examination</span>
          <h2 class="text-2xl lg:text-3xl font-heading font-medium text-primary-100">Order a Curated Architectural Sample Kit</h2>
          <p class="text-xs text-primary-80 leading-relaxed font-copy">
            Digital photography cannot replace the tactile sensation of natural stone under fingertips. We provide complimentary curated presentation boxes containing calibrated 100&times;100mm limestone swatches showcasing our five signature finishes: <em>Antique, Tumbled, Sandblasted, Brushed, and Flamed</em>.
          </p>
          <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 pt-2 text-xs font-copy">
            <div>
              <strong class="text-primary-100 block">3–5 Business Days</strong>
              <span class="text-primary-70">DHL / FedEx Express global air courier.</span>
            </div>
            <div>
              <strong class="text-primary-100 block">Complete Engineering TDS</strong>
              <span class="text-primary-70">Physical ASTM test summary included.</span>
            </div>
            <div>
              <strong class="text-primary-100 block">Zero Cost for Specifiers</strong>
              <span class="text-primary-70">Complimentary for architects & builders.</span>
            </div>
          </div>
        </div>
        <div class="lg:col-span-4 text-center lg:text-right">
          <a href="#rfq-form" class="px-6 py-3.5 bg-primary-100 text-white font-semibold text-xs uppercase tracking-wider rounded-sm hover:bg-[#E9F551] hover:text-black transition-colors inline-block shadow">
            Request Free Sample Box →
          </a>
        </div>
      </div>
    </section>

    <!-- Main Contact & RFQ Columns -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 my-14 items-start">
      <!-- Info Left -->
      <div class="lg:col-span-5 space-y-6">
        <div class="bg-primary-2 border border-primary-10 p-6 space-y-4 text-xs font-copy rounded-sm">
          <h3 class="font-heading text-lg font-medium text-primary-100">Quarry & Manufacturing HQ</h3>
          <p><strong>Legal Entity:</strong> {COMPANY_INFO[\'name\']} ({COMPANY_INFO[\'chinese_name\']})</p>
          <p><strong>Factory Address:</strong> {COMPANY_INFO[\'address\']}</p>
          <p><strong>GPS Coordinates:</strong> {COMPANY_INFO[\'coordinates\']}</p>
          <p><strong>Nearest Seaport:</strong> {COMPANY_INFO[\'port\']}</p>
        </div>

        <div class="bg-primary-2 border border-primary-10 p-6 space-y-4 text-xs font-copy rounded-sm">
          <h3 class="font-heading text-lg font-medium text-primary-100">Direct Communication Channels</h3>
          <p><strong>Direct Inquiries Email:</strong> <a href="mailto:{COMPANY_INFO[\'email\']}" class="text-primary-100 font-semibold underline">{COMPANY_INFO[\'email\']}</a></p>
          <p><strong>Sales Hotline:</strong> <a href="tel:{COMPANY_INFO[\'phone\']}" class="text-primary-100 font-semibold underline">{COMPANY_INFO[\'phone\']}</a></p>
          <p><strong>WhatsApp / Mobile:</strong> <a href="tel:{COMPANY_INFO[\'phone_alt\']}" class="text-primary-100 font-semibold underline">{COMPANY_INFO[\'phone_alt\']}</a></p>
          <p><strong>Main Stone Website:</strong> <a href="{COMPANY_INFO[\'sister_domain\']}" target="_blank" rel="noopener" class="text-primary-100 font-semibold underline">tystoneveneer.com</a></p>
        </div>

        <!-- Logistics Corridor Card -->
        <div class="bg-white border border-primary-10 p-6 space-y-4 text-xs font-copy rounded-sm shadow-sm">
          <div class="aspect-[16/9] w-full overflow-hidden rounded-sm border border-primary-10 mb-2">
            <img src="{r}assets/images/contact/xiamen_port_logistics.webp" alt="Xiamen International Container Port Logistics Hub" class="w-full h-full object-cover" loading="lazy" width="500" height="280">
          </div>
          <h4 class="font-heading text-base font-semibold text-primary-100">Global Shipping & Transit Times</h4>
          <p class="text-primary-70 leading-relaxed">
            Located just 28 km from Xiamen Deep-Water Seaport with weekly direct ocean container liner departures:
          </p>
          <div class="space-y-1.5 pt-1">
            <div class="flex justify-between items-center py-1 border-b border-primary-10">
              <span class="font-semibold text-primary-100">Australia (Sydney/Melb/Bris)</span>
              <span class="transit-badge">12 – 16 Days</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-primary-10">
              <span class="font-semibold text-primary-100">USA West Coast (Long Beach/LA)</span>
              <span class="transit-badge">15 – 18 Days</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-primary-10">
              <span class="font-semibold text-primary-100">USA East Coast (Savannah/NY)</span>
              <span class="transit-badge">28 – 32 Days</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-primary-10">
              <span class="font-semibold text-primary-100">Western Europe (Rotterdam/Hamburg)</span>
              <span class="transit-badge">24 – 28 Days</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-primary-10">
              <span class="font-semibold text-primary-100">Middle East (Dubai / Jebel Ali)</span>
              <span class="transit-badge">14 – 18 Days</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Form Right -->
      <div id="rfq-form" class="lg:col-span-7 bg-white p-6 sm:p-8 lg:p-10 border border-primary-10 shadow-sm rounded-sm">
        <div class="border-b border-primary-10 pb-4 mb-6">
          <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider">Fast Turnaround RFQ Desk</span>
          <h3 class="font-heading text-2xl font-medium text-primary-100 mb-1">Direct Factory Specification & RFQ</h3>
          <p class="text-xs text-primary-70 font-copy">Complete the form below to receive FOB/CIF pricing, packing lists, freight schedules, and complimentary sample swatches.</p>
        </div>

        { render_progressive_rfq_form("General Contact Inquiry", "contact_page_form") }
      </div>
    </div>
  </main>

  {render_footer(depth)}
  <script src="{r}assets/js/search_index.js"></script>
  <script src="{r}assets/js/main.js"></script>
</body>
</html>
\'\'\'
    return html
'''

def main():
    with open(BUILD_SCRIPT, "r", encoding="utf-8") as f:
        content = f.read()

    # Find start and end of the 5 generators block
    start_token = "def generate_other_categories_page(all_products):"
    end_token = "def generate_sitemap_and_robots(all_pages):"

    start_idx = content.find(start_token)
    if start_idx == -1:
        print("❌ Could not find start token in build_tianya_site.py")
        sys.exit(1)

    end_idx = content.find(end_token)
    if end_idx == -1:
        print("❌ Could not find end token in build_tianya_site.py")
        sys.exit(1)

    new_content = content[:start_idx] + NEW_GENERATORS_CODE + "\n" + content[end_idx:]

    with open(BUILD_SCRIPT, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✅ Successfully updated build_tianya_site.py with new auxiliary page generators!")

if __name__ == "__main__":
    main()
