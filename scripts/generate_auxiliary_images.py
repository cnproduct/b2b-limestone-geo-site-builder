#!/usr/bin/env python3
"""
Tianya Limestone - Generate Editorial & Architectural Assets for Auxiliary Pages
Uses codex-img to generate high-end architectural photography and converts to WebP.
"""

import os
import sys
import subprocess
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS = [
    {
        "name": "about_hero_quarry",
        "dir": BASE_DIR / "assets" / "images" / "about",
        "size": "1536x1024",
        "prompt": "Cinematic architectural photography of an expansive limestone open-cast quarry in Fujian mountains, monumental stepped quarry walls cut with precision diamond wire saws, massive cubic blocks of beige and grey limestone neatly staged on quarry ground, bright morning sunlight casting crisp architectural shadows, misty mountains in background, high-end architectural documentary aesthetic, 8k resolution, photorealistic."
    },
    {
        "name": "craftsman_stonemason",
        "dir": BASE_DIR / "assets" / "images" / "about",
        "size": "1536x1024",
        "prompt": "High-end editorial documentary portrait of a skilled senior stonemason in a natural stone workshop, wearing protective apron and gloves, carefully inspecting the hand-chiseled tumbled edge of a large warm beige limestone paver, fine stone dust, warm natural side lighting streaming through factory window, authentic artisanal craftsmanship, Hasselblad medium format camera style."
    },
    {
        "name": "factory_fabrication",
        "dir": BASE_DIR / "assets" / "images" / "about",
        "size": "1536x1024",
        "prompt": "Modern high-tech natural stone fabrication facility interior, large multi-blade bridge saws cutting dense limestone slabs with cooling water spray, automated roller conveyor systems, immaculate organized industrial hall, stacks of cut-to-size limestone pavers with precision millimeter edges, architectural industrial photography, high shutter speed capturing water droplets."
    },
    {
        "name": "export_crates_logistics",
        "dir": BASE_DIR / "assets" / "images" / "about",
        "size": "1536x1024",
        "prompt": "High-end industrial logistics photography of solid timber export crates filled with vertically stacked limestone pavers, ISPM-15 heat-treatment stamps visible on fumigated wood, heavy-duty steel strapping and plastic corner protectors, factory shipping staging yard with forklift in background under clean daylight, international freight ready."
    },
    {
        "name": "lab_testing",
        "dir": BASE_DIR / "assets" / "images" / "compliance",
        "size": "1536x1024",
        "prompt": "Modern materials engineering laboratory, close-up of a hydraulic compressive strength testing apparatus crushing a cylindrical limestone core specimen, digital pressure gauge displays, calipers, micrometer, testing certificates and lab notebook on clean stainless steel workbench, professional ISO accredited testing environment, sharp focus."
    },
    {
        "name": "quality_inspection",
        "dir": BASE_DIR / "assets" / "images" / "compliance",
        "size": "1536x1024",
        "prompt": "Professional quality control inspector in safety vest using a digital vernier caliper to measure the exact thickness and edge squareness of a honed limestone tile, checklist clipboard nearby, brightly lit stone quality assurance station in a modern factory, technical precision."
    },
    {
        "name": "cad_blueprints",
        "dir": BASE_DIR / "assets" / "images" / "resources",
        "size": "1536x1024",
        "prompt": "Top-down architectural drafting studio flatlay, detailed architectural CAD blueprints and floor plan schematics for luxury residence stone paving layout, several 100x100mm natural limestone sample swatches in beige, grey and antique finishes resting on the drawings, architect metal scale ruler, technical pen, clean minimal aesthetic."
    },
    {
        "name": "modular_pattern_diagram",
        "dir": BASE_DIR / "assets" / "images" / "resources",
        "size": "1536x1024",
        "prompt": "Crisp clean architectural graphic render of a French Roman modular stone paving pattern laid out seamlessly, four interlocking rectangular and square sizes (600x400, 400x400, 400x200, 200x200mm) in subtle neutral limestone tones, 3mm grout joints, modern landscape design presentation sheet."
    },
    {
        "name": "sample_kit_box",
        "dir": BASE_DIR / "assets" / "images" / "contact",
        "size": "1536x1024",
        "prompt": "Luxury bespoke matte-black wooden architectural sample presentation box open on a clean oak design table, containing neatly arranged 100x100mm cut stone swatch samples of limestone in various finishes (tumbled, brushed, antique, sandblasted) with discrete laser-etched metal labels, embossed Tianya Limestone logo on inside lid, high-end B2B sample package."
    },
    {
        "name": "xiamen_port_logistics",
        "dir": BASE_DIR / "assets" / "images" / "contact",
        "size": "1536x1024",
        "prompt": "Aerial commercial photography of Xiamen international deep-water container terminal port, modern blue gantry cranes loading shipping containers onto an ocean container vessel, calm blue sea, sunny clear day, vibrant logistics and global maritime freight hub."
    },
    {
        "name": "mixed_container_loading",
        "dir": BASE_DIR / "assets" / "images" / "categories",
        "size": "1536x1024",
        "prompt": "Clean 3D architectural diagram and cutaway illustration of a standard 20ft ocean freight shipping container efficiently packed with mixed stone products: bottom layer packed with heavy timber crates of natural limestone pavers, top and side space organized with lightweight ultra-thin stone veneer crates and ledger stone boxes, clear volume and weight optimization layout, professional logistics infographic."
    }
]

def run_codex_generate(prompt, size, name, out_dir):
    cmd = [
        "codex-img", "generate", prompt,
        "--size", size,
        "--out", str(out_dir),
        "--name", name
    ]
    print(f"  → Running codex-img for {name} ({size})...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  ❌ Error generating {name}: {res.stderr or res.stdout}")
        return False
    return True

def convert_to_webp(png_path, webp_path, quality=85):
    try:
        with Image.open(png_path) as im:
            im.save(webp_path, "WEBP", quality=quality)
        png_mb = os.path.getsize(png_path) / 1024 / 1024
        webp_kb = os.path.getsize(webp_path) / 1024
        print(f"  ✅ Converted {webp_path.name} ({png_mb:.2f}MB → {webp_kb:.1f}KB)")
        return True
    except Exception as e:
        print(f"  ❌ WebP conversion error: {e}")
        return False

def main():
    print(f"Generating {len(ASSETS)} editorial and technical assets for auxiliary pages...")
    for idx, item in enumerate(ASSETS, 1):
        item["dir"].mkdir(parents=True, exist_ok=True)
        webp_path = item["dir"] / f"{item['name']}.webp"
        png_path = item["dir"] / f"{item['name']}.png"

        if webp_path.exists():
            print(f"[{idx}/{len(ASSETS)}] ⏩ Already exists: {webp_path.name}")
            continue

        print(f"[{idx}/{len(ASSETS)}] 🎨 Generating {item['name']}...")
        success = run_codex_generate(item["prompt"], item["size"], item["name"], item["dir"])
        if success and png_path.exists():
            convert_to_webp(png_path, webp_path)
            # Remove large png to save space
            png_path.unlink()
        else:
            print(f"  ⚠️ Skipping conversion for {item['name']}")

    print("\nAsset generation complete!")

if __name__ == "__main__":
    main()
