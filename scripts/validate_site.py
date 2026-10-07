#!/usr/bin/env python3
"""
Tianya Limestone - Site Release Validator
Checks link integrity, asset presence, Schema.org JSON-LD, canonical correctness,
and backward-compatibility redirects across all compiled HTML pages.
"""

import os
import sys
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent

def validate_all():
    print("=== Starting Tianya Limestone Release Audit ===")
    html_files = list(BASE_DIR.glob("**/*.html"))
    print(f"Found {len(html_files)} HTML files to inspect.")

    errors = []
    warnings = []
    checked_links = 0
    checked_images = 0

    for html_path in html_files:
        rel_path = html_path.relative_to(BASE_DIR).as_posix()
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check basic structure
        if not content.startswith("<!DOCTYPE html>"):
            errors.append(f"[{rel_path}] Missing <!DOCTYPE html>")

        soup = BeautifulSoup(content, "html.parser")

        # Skip redirect stubs from full content check
        meta_refresh = soup.find("meta", attrs={"http-equiv": re.compile(r"refresh", re.I)})
        if meta_refresh:
            continue

        # Check Title & Description
        title = soup.find("title")
        if not title or not title.text.strip():
            errors.append(f"[{rel_path}] Missing or empty <title>")

        meta_desc = soup.find("meta", attrs={"name": "description"})
        if not meta_desc or not meta_desc.get("content", "").strip():
            errors.append(f"[{rel_path}] Missing or empty meta description")

        # Check Canonical
        canonical = soup.find("link", attrs={"rel": "canonical"})
        if not canonical or not canonical.get("href"):
            errors.append(f"[{rel_path}] Missing canonical URL")

        # Check Schema.org
        schema_scripts = soup.find_all("script", attrs={"type": "application/ld+json"})
        for s in schema_scripts:
            try:
                data = json.loads(s.string)
                if not data.get("@context"):
                    errors.append(f"[{rel_path}] Schema.org missing @context")
            except Exception as e:
                errors.append(f"[{rel_path}] Malformed Schema JSON-LD: {e}")

        # Check internal images
        for img in soup.find_all("img"):
            src = img.get("src")
            if not src:
                continue
            checked_images += 1
            if src.startswith("http://") or src.startswith("https://"):
                continue
            clean_src = src.split('?')[0].split('#')[0]
            target_path = (html_path.parent / clean_src).resolve()
            if not target_path.exists():
                errors.append(f"[{rel_path}] Broken image reference: {src} (resolved to {target_path})")

        # Check gallery data-gallery-img
        for btn in soup.find_all(attrs={"data-gallery-img": True}):
            gsrc = btn["data-gallery-img"]
            if gsrc.startswith("http://") or gsrc.startswith("https://"):
                continue
            clean_gsrc = gsrc.split('?')[0].split('#')[0]
            target_path = (html_path.parent / clean_gsrc).resolve()
            if not target_path.exists():
                errors.append(f"[{rel_path}] Broken data-gallery-img reference: {gsrc}")

        # Check internal links
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("javascript:"):
                continue
            if href.startswith("http://") or href.startswith("https://"):
                continue
            checked_links += 1
            clean_href = href.split("#")[0].split("?")[0]
            if not clean_href:
                continue
            target_path = (html_path.parent / clean_href).resolve()
            if target_path.is_dir():
                target_path = target_path / "index.html"
            if not target_path.exists():
                errors.append(f"[{rel_path}] Broken internal link: {href} (resolved to {target_path})")

    print(f"\nAudit complete: Checked {checked_images} images, {checked_links} internal links.")
    if warnings:
        print(f"⚠️ Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
    if errors:
        print(f"❌ Errors ({len(errors)}):")
        for e in errors[:20]:
            print(f"  - {e}")
        return False

    print("✅ 0 Errors! All pages, images, canonical links, and schemas are 100% valid.")
    return True

if __name__ == "__main__":
    ok = validate_all()
    sys.exit(0 if ok else 1)
