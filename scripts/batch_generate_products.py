#!/usr/bin/env python3
"""
Tianya Limestone - Codex-IMG Batch Product Image Generator & WebP Converter
Reads data/products_mapping.json and generates high-res swatches (1:1) and architectural scenes (1536x1024)
Converts raw PNGs to high-performance WebP (quality 85) for fast global B2B loading.
"""

import os
import sys
import json
import time
import subprocess
import argparse
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent
MAPPING_FILE = BASE_DIR / 'data' / 'products_mapping.json'
OUT_DIR = BASE_DIR / 'assets' / 'images' / 'products'

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
    parser = argparse.ArgumentParser(description="Batch generate limestone product images using codex-img")
    parser.add_argument("--finish", choices=["antique", "lightly_distressed", "sandblasted_brushed", "sandblasted", "tumbled", "all"], default="all")
    parser.add_argument("--slug", help="Generate for a specific product new_slug")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of items to generate (0 for unlimited)")
    parser.add_argument("--keep-png", action="store_true", help="Keep large raw PNG files")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(MAPPING_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    items_to_process = []
    for finish_cat, prods in data.items():
        if args.finish != "all" and args.finish != finish_cat:
            continue
        for p in prods:
            if args.slug and p["new_slug"] != args.slug:
                continue
            items_to_process.append((finish_cat, p))

    if args.limit > 0:
        items_to_process = items_to_process[:args.limit]

    total = len(items_to_process)
    print(f"=== Starting batch generation for {total} products ===")

    success_count = 0
    for idx, (finish_cat, p) in enumerate(items_to_process, 1):
        slug = p["new_slug"]
        title = p["new_title"]
        print(f"\n[{idx}/{total}] Processing {finish_cat} / {title} ({slug}):")

        # 1. Swatch image (1:1 1024x1024)
        swatch_png = OUT_DIR / f"{slug}_swatch.png"
        swatch_webp = OUT_DIR / f"{slug}_swatch.webp"

        if swatch_webp.exists() and swatch_webp.stat().st_size > 5000:
            print(f"  ⚡ Swatch webp already exists ({swatch_webp.name}), skipping.")
        else:
            if not swatch_png.exists() or swatch_png.stat().st_size == 0:
                ok = run_codex_generate(p["swatch_prompt"], "1024x1024", f"{slug}_swatch", OUT_DIR)
                if not ok:
                    print(f"  ⚠️ Skipping swatch for {slug} due to generation failure.")
                time.sleep(2)
            if swatch_png.exists():
                convert_to_webp(swatch_png, swatch_webp)
                if not args.keep_png:
                    try:
                        swatch_png.unlink()
                    except Exception:
                        pass

        # 2. Scene image (1536x1024)
        scene_png = OUT_DIR / f"{slug}_scene.png"
        scene_webp = OUT_DIR / f"{slug}_scene.webp"

        if scene_webp.exists() and scene_webp.stat().st_size > 5000:
            print(f"  ⚡ Scene webp already exists ({scene_webp.name}), skipping.")
        else:
            if not scene_png.exists() or scene_png.stat().st_size == 0:
                ok = run_codex_generate(p["scene_prompt"], "1536x1024", f"{slug}_scene", OUT_DIR)
                if not ok:
                    print(f"  ⚠️ Skipping scene for {slug} due to generation failure.")
                time.sleep(2)
            if scene_png.exists():
                convert_to_webp(scene_png, scene_webp)
                if not args.keep_png:
                    try:
                        scene_png.unlink()
                    except Exception:
                        pass

        success_count += 1
        time.sleep(1)

    print(f"\n🎉 Finished batch generation! {success_count}/{total} products processed successfully.")

if __name__ == "__main__":
    main()
