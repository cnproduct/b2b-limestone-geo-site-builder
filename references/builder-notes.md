# 构建器实战笔记

`build_tianya_site.py` 是全站唯一真相源。以下是在 1→6 优化中沉淀的可复用模式。

## depth 分支 SEO 头
`generate_home_page(all_products, depth)` 同时渲染首页（`depth=0`）和 `/stone-flooring/limestone/` 分类页（`depth=2`）。两者曾共用同一 title/description/H1：
```python
if depth == 2:
    title = "Limestone Flooring Collection: 29 Pavers, Tiles & Pool Coping | Tianya Limestone"
    description = "Browse all 29 quarry-direct ..."
    hero_h1 = "Limestone Pavers, Tiles<br>& Pool Coping"
    hero_eyebrow = "Natural Limestone · Tianya Stone"
else:
    hero_h1 = "Quarry-Direct Limestone<br>Pavers, Tiles & Pool Coping"
    hero_eyebrow = "Stone with soul."   # 品牌语保留为副标题
```
OG 标签与 JSON-LD `WebPage` 共用同一变量，自动保持一致。改后 `curl` 两个 URL 对 diff `<title>` / description / `<h1>`。

## 新增页面类型三步
1. 写 `generate_<thing>()`：按 head（含 GA4、OG、JSON-LD）→ breadcrumb → main → footer 的结构；`depth` 决定资源相对路径。
2. `build_all()` 里 `os.makedirs` + 写 `index.html` + 把相对 URL 追加进 `all_pages`（sitemap/llms 自动收录）。
3. 桌面导航加链接并配 `active_tab`（参考 `/blog/` 的 `active_tab='blog'`）。

## Sitemap 图片条目
`generate_sitemap_and_robots(all_pages, all_products)`：
- `<urlset>` 加 `xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"`
- 29 个产品页各 2 条 `<image:image>`（`images[]` 的 scene + swatch，绝对地址、去掉 `?v=`、标题做 HTML 转义）
- 发布后校验 XML 可解析、抽查图片 200
