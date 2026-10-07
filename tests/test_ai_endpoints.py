#!/usr/bin/env python3
"""
Test suite for Tianya Limestone AI & GEO endpoints.
Validates machine-readable API contracts, sitemaps, robots.txt, and LLM text specs.
"""
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


def test_ai_json_endpoints():
    ai_dir = BASE_DIR / "ai"
    assert ai_dir.is_dir(), "ai/ directory must exist"

    # 1. summary.json
    summary_file = ai_dir / "summary.json"
    assert summary_file.is_file(), "summary.json must exist"
    with open(summary_file, "r", encoding="utf-8") as f:
        summary = json.load(f)
    assert summary["entity"]["brand_name"] == "Tianya Limestone"
    assert "coordinates" in summary["entity"]
    assert summary["entity"]["coordinates"]["latitude"] == 24.6931
    assert "physical_properties" in summary
    assert "ASTM C97" in summary["physical_properties"]["water_absorption"]
    assert "ASTM C170" in summary["physical_properties"]["compressive_strength_dry"]

    # 2. faq.json
    faq_file = ai_dir / "faq.json"
    assert faq_file.is_file(), "faq.json must exist"
    with open(faq_file, "r", encoding="utf-8") as f:
        faq = json.load(f)
    assert isinstance(faq, list)
    assert len(faq) >= 8
    for item in faq:
        assert "question" in item and "answer" in item

    # 3. vendor-comparison.json
    comp_file = ai_dir / "vendor-comparison.json"
    assert comp_file.is_file(), "vendor-comparison.json must exist"
    with open(comp_file, "r", encoding="utf-8") as f:
        comp = json.load(f)
    assert "vendors" in comp
    assert len(comp["vendors"]) >= 4

    # 4. products.json
    prod_file = ai_dir / "products.json"
    assert prod_file.is_file(), "products.json must exist"
    with open(prod_file, "r", encoding="utf-8") as f:
        prods = json.load(f)
    assert isinstance(prods, list)
    assert len(prods) == 29, f"Expected 29 products, got {len(prods)}"
    for p in prods:
        assert "trade_title" in p
        assert "finish_type" in p
        assert "canonical_url" in p
        assert "slip_rating" in p

    print("PASS: /ai/ JSON endpoints format and schema assertions verified.")


def test_crawlers_and_llms():
    # robots.txt
    robots_file = BASE_DIR / "robots.txt"
    assert robots_file.is_file()
    robots_text = robots_file.read_text(encoding="utf-8")
    assert "User-agent: GPTBot" in robots_text
    assert "User-agent: ClaudeBot" in robots_text
    assert "User-agent: PerplexityBot" in robots_text
    assert "Sitemap: https://tianyalimestone.com/sitemap.xml" in robots_text
    assert "# llms.txt: https://tianyalimestone.com/llms.txt" in robots_text
    assert "# llms-full.txt: https://tianyalimestone.com/llms-full.txt" in robots_text

    # llms.txt
    llms_file = BASE_DIR / "llms.txt"
    assert llms_file.is_file()
    llms_text = llms_file.read_text(encoding="utf-8")
    assert "Tianya Limestone" in llms_text
    assert "29 Limestone Collections Catalog" in llms_text
    assert "Machine-Readable AI Knowledge API Endpoints" in llms_text

    # llms-full.txt
    llms_full_file = BASE_DIR / "llms-full.txt"
    assert llms_full_file.is_file()
    llms_full_text = llms_full_file.read_text(encoding="utf-8")
    assert "Comprehensive Engineering Specification" in llms_full_text
    assert "ASTM C170" in llms_full_text
    assert "French Pattern" in llms_full_text
    assert len(llms_full_text) > 5000

    # sitemap.xml
    sitemap_file = BASE_DIR / "sitemap.xml"
    assert sitemap_file.is_file()
    sitemap_text = sitemap_file.read_text(encoding="utf-8")
    assert "<loc>https://tianyalimestone.com/</loc>" in sitemap_text
    assert "<image:loc>" in sitemap_text
    assert "<priority>1.0</priority>" in sitemap_text

    print("PASS: robots.txt, llms.txt, llms-full.txt, and sitemap.xml verified.")


def test_homepage_schema():
    index_file = BASE_DIR / "index.html"
    assert index_file.is_file()
    index_text = index_file.read_text(encoding="utf-8")
    assert "ItemList" in index_text
    assert "Tianya Natural Limestone Collections" in index_text
    assert "knowsAbout" in index_text
    assert "Fujian Tianya Cultural Stone Co., Ltd." in index_text
    assert "GeoCoordinates" in index_text

    print("PASS: Homepage rich Schema.org JSON-LD verified.")


def main():
    test_ai_json_endpoints()
    test_crawlers_and_llms()
    test_homepage_schema()
    print("\n🎉 ALL AI & GEO TESTS PASSED 100%!")


if __name__ == "__main__":
    main()
