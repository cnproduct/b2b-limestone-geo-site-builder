#!/usr/bin/env python3
"""
Tianya Limestone - Visual Capture of Redesigned Auxiliary Pages
Takes high-res desktop (1440x900) and mobile (390x844) screenshots using Playwright.
"""

import os
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_DIR = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = BASE_DIR / "evidence"
EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

PAGES = [
    {"name": "about", "file": BASE_DIR / "about-us" / "index.html"},
    {"name": "compliance", "file": BASE_DIR / "compliance" / "index.html"},
    {"name": "resources", "file": BASE_DIR / "resources" / "index.html"},
    {"name": "contact", "file": BASE_DIR / "contact-us" / "index.html"},
    {"name": "other_categories", "file": BASE_DIR / "stone-flooring" / "other-categories" / "index.html"}
]

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # 1. Desktop captures
        desktop_context = browser.new_context(viewport={"width": 1440, "height": 900})
        desktop_page = desktop_context.new_page()

        for item in PAGES:
            url = f"file://{item['file']}"
            print(f"📸 Capturing Desktop: {item['name']}...")
            desktop_page.goto(url)
            desktop_page.wait_for_load_state("networkidle")
            time.sleep(0.5)

            # Full page screenshot
            out_file = EVIDENCE_DIR / f"redesign_{item['name']}_desktop.png"
            desktop_page.screenshot(path=str(out_file), full_page=True)
            print(f"  ✅ Saved {out_file.name}")

        desktop_context.close()

        # 2. Mobile captures (iPhone 14 Pro emulation)
        mobile_context = browser.new_context(
            viewport={"width": 390, "height": 844},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
        )
        mobile_page = mobile_context.new_page()

        for item in PAGES:
            url = f"file://{item['file']}"
            print(f"📱 Capturing Mobile: {item['name']}...")
            mobile_page.goto(url)
            mobile_page.wait_for_load_state("networkidle")
            time.sleep(0.5)

            out_file = EVIDENCE_DIR / f"redesign_{item['name']}_mobile.png"
            mobile_page.screenshot(path=str(out_file), full_page=True)
            print(f"  ✅ Saved {out_file.name}")

        mobile_context.close()
        browser.close()

    print("\nVisual audit screenshots successfully captured in evidence/!")

if __name__ == "__main__":
    main()
