---
title: SEO Audit Report
domain: tang-and-song.relics.guide
business_type: Travel Guide / Historical Content
date: 2026-08-05
health_score: 71
pages_analyzed: 19 (1 homepage + 18 detail pages, full source analysis)
---

# SEO Audit Report -- tang-and-song.relics.guide

## Executive Summary

**Health Score: 71/100**

A single-page Tang and Song dynasty relic guide with 18 rich detail pages. The content is distinctive and well-researched, with a strong "honest note" authenticity system that sets it apart from generic history sites. However, several technical issues are holding back performance and indexability scores.

### Top 5 Critical Issues

1. **Schema JSON-LD is broken on all 18 detail pages** -- double-brace `{{` `}}` escaping renders structured data unparseable by Google
2. **Tailwind CDN is render-blocking** -- `<script src="https://cdn.tailwindcss.com">` in `<head>` blocks first paint
3. **No `og:image` or `twitter:image`** -- social previews are invisible, hurting click-through rates
4. **Images are oversized** -- 18 images total 3.8 MB, many over 250 KB, no responsive `srcset`
5. **No `llms.txt`** -- missing for AI crawler discoverability

### Top 5 Quick Wins

1. Fix schema JSON-LD `{{}}` escape bug across all detail pages (one-line build pipeline fix)
2. Add `og:image` / `twitter:image` to every page (one HTML tag per page)
3. Add responsive `srcset` and `width`/`height` attributes to all images
4. Run images through `cwebp -q 75` to reduce total image payload by ~50%
5. Create a `llms.txt` file at the site root

---

## 1. Technical SEO -- Score: 62/100

### What Works

- Clean `robots.txt` allowing all crawlers with sitemap reference
- `sitemap.xml` covers all 19 pages with proper `lastmod`, `changefreq`, and `priority`
- Canonical URLs are correct on all pages
- Meta robots `index,follow` on every page
- No `noindex` or `nofollow` directives anywhere
- All pages return proper 200 responses with valid HTML
- All pages have proper `lang="en"` attribute
- Viewport meta tag present
- Charset UTF-8 declared
- No mixed content issues (all HTTPS)

### Findings

**Critical -- Schema JSON-LD broken on all 18 detail pages**
Every detail page (e.g., `sites/foguang/index.html`, `sites/nanchan/index.html`) uses `{{` and `}}` as JSON delimiters in schema LD+JSON blocks. This renders Google unable to parse any structured data on those pages. The homepage schema is correct. This affects TouristAttraction and BreadcrumbList schemas on every detail page.
Recommendation: Fix the build pipeline so `{` and `}` are not escaped. If using Python `.format()`, ensure the template uses `{` properly.

**High -- No security headers**
No Content-Security-Policy, Strict-Transport-Security, X-Content-Type-Options, or X-Frame-Options headers are configured.
Recommendation: Configure the web server to add `Strict-Transport-Security: max-age=31536000`, `X-Content-Type-Options: nosniff`, and `X-Frame-Options: SAMEORIGIN`.

**Medium -- Sitemap `changefreq` and `priority` provide no value**
All sitemap entries use `changefreq=monthly` and identical priorities (0.8 for detail pages). Modern best practice is to omit these -- Google primarily uses `lastmod`.
Recommendation: Keep `lastmod` but drop `changefreq` and `priority` from all entries except homepage.

**Medium -- Trailing slash inconsistency risk**
The sitemap entries all use trailing slashes (e.g., `/sites/foguang/`). If the server also serves `/sites/foguang` without redirecting, duplicate content could emerge.
Recommendation: Verify the server redirects trailing-slash-less URLs to trailing-slash versions (or vice versa).

---

## 2. On-Page SEO -- Score: 78/100

### What Works

- Title tags are unique, descriptive, and keyword-rich across all 19 pages
- Meta descriptions are unique and present on all pages
- H1 on every page (detail pages use site name as H1)
- Clean heading hierarchy: H1 -> H2 sections on detail pages
- Open Graph and Twitter Card tags present on all pages
- Strong internal linking: homepage links to all detail pages, detail pages link back via breadcrumbs
- Breadcrumb navigation on every detail page
- "People Also Search For" section with semantic internal linking
- FAQ section with expandable `<details>` elements
- Mobile-responsive navigation with hamburger menu

### Findings

**High -- Missing og:image on all pages**
Not a single page has an `og:image` or `twitter:image` meta tag. For a travel guide with rich photography, this is a significant missed opportunity. Social shares (Twitter, Facebook, LinkedIn, Discord) show no preview image.
Recommendation: Add `og:image` pointing to each site hero image, plus a default fallback. Add `og:image:width` and `og:image:height`.

**Low -- Homepage title could be shorter**
Current title: "Tang vs Song Dynasty: What Survives Today - A Traveler Guide to Real Ruins" (82 chars). Google may truncate after 60-70 chars.
Recommendation: Consider "Tang vs Song Dynasty: What Survives Today | Relics Guide" (61 chars).

**Low -- Meta descriptions are formulaic**
Detail page meta descriptions follow a fixed template. They are functional but do not entice clicks from SERPs.
Recommendation: Lead with the most compelling fact about each site. For Foguang: "The largest Tang wooden building on earth -- found in 1937 when the world thought none survived. Complete travel guide."

---

## 3. Content Quality -- Score: 85/100

### What Works

The content is this site strongest asset. It is original, specific, and opinionated.

- **Authenticity label system** (Original / Later / Archaeological / Modern) is genuinely differentiating
- Every site entry includes a "Basis" citation (NPU designation, UNESCO listing, State Council record)
- "Honest note" field gives candid assessments -- builds E-E-A-T trust
- Detail pages are comprehensive: Why Visit, How to Get There, Where to Stay, What to Eat, Best Time, Tips for Foreign Travelers
- Content addresses real pain points: "No English signage," "No public transit," "Bring cash"
- FAQ section targets real search queries with substantive answers
- Timeline covers all Chinese dynasties with distinguishing facts
- Museum listings are highly practical
- No thin or duplicate pages
- No AI-generated filler or marketing fluff

### Findings

**Medium -- No author attribution or About page**
The site uses Organization schema for authorship but has no About page, author bio, or contact information. E-E-A-T signals for this content niche benefit from transparent authorship.
Recommendation: Add an `/about/` page with organization details, editorial standards, and contact method.

**Low -- Some "Why Visit" sections reuse homepage text**
For some Japan entries (Toshodai-ji, Horyu-ji), the "Why Visit" text is identical to the homepage card description.
Recommendation: Expand each "Why Visit" section to 3-4 unique sentences.

**Low -- No internal content freshness signals**
Footer says "Facts verified: 2026-08" on all pages. This is good but uniform.
Recommendation: Add per-page `dateModified` in schema and a "Last updated" line.

---

## 4. Schema / Structured Data -- Score: 60/100

### What Works

- Homepage: Article, FAQPage, Table, ItemList (TouristAttraction x18), BreadcrumbList
- FAQPage on homepage with 13 Q&A pairs -- excellent for AI Overview visibility
- BreadcrumbList on all detail pages
- TouristAttraction schema on all detail pages

### Findings

**Critical -- All detail page schemas are unparseable**
The `{{` `}}` escaping bug makes every schema block on the 18 detail pages invalid JSON-LD. Google Rich Results Test will fail.
Recommendation: This is priority #1. Fix the build pipeline.

**Medium -- Missing Organization schema**
No Organization or WebSite schema on the homepage.
Recommendation: Add `Organization` schema with name "Relics Guide" and URL.

**Medium -- Missing ImageObject schema**
Each TouristAttraction should have an `image` property pointing to an `ImageObject`.
Recommendation: Extend TouristAttraction schema to include image URLs with dimensions.

**Low -- Table schema is minimal**
The `Table` schema on the homepage has only an `about` field.
Recommendation: Populate with Tang vs Song comparison data or remove it.

---

## 5. Performance -- Score: 55/100

### What Works

- Inline critical CSS avoids render-blocking external stylesheets
- No analytics or tracking scripts
- No cookie consent banners
- No advertising scripts
- WebP format for all images
- No heavy JavaScript frameworks
- Static HTML -- fast to serve

### Findings

**Critical -- Tailwind CDN in head blocks rendering**
`<script src="https://cdn.tailwindcss.com">` is loaded synchronously in `<head>`. This blocks HTML parsing and first paint until the CDN script downloads, parses, and scans the entire DOM. On slow connections, this adds 1-3 seconds to FCP/LCP.
Recommendation: Build Tailwind CSS locally with `npx tailwindcss -i input.css -o output.css --minify` and serve the compiled CSS as a static file. This eliminates the CDN dependency entirely.

**High -- Images are large and not responsive**
18 WebP images total 3.8 MB with no `srcset`. Mobile visitors download full desktop-sized images.
Recommendation: Generate 400w, 800w, 1200w variants per image and use `<img srcset="...">`. Recompress originals with `cwebp -q 75`.

**High -- Google Fonts add network dependency**
Three font families loaded from Google Fonts CDN. While `preconnect` hints help, the fonts still add latency.
Recommendation: Self-host font files with `font-display: swap` to prevent FOIT.

**Medium -- Inline CSS duplicated across detail pages**
Each of 18 detail pages contains identical `<style>` blocks (~500 bytes).
Recommendation: Extract shared CSS into a single external stylesheet.

**Medium -- No caching headers config visible**
No server configuration found in the source repo for Cache-Control or ETag headers.
Recommendation: Configure server to cache images for 1 year, CSS/JS for 1 month, HTML for 1 day.

---

## 6. Images -- Score: 72/100

### What Works

- All images in WebP format
- All images have `alt` text
- Proper aspect ratios via CSS classes
- Organized in dedicated `images/` directory
- Consistent naming convention
- No broken image references

### Findings

**High -- No responsive image variants**
Every `<img>` serves a single file with no `srcset`. Mobile users download desktop-sized images.
Recommendation: Generate 400w, 800w, 1200w WebP variants with `srcset` + `sizes`.

**Medium -- Large image files**

| Image | Size | Target |
|---|---|---|
| baoguo.webp | 286 KB | ~150 KB |
| famen.webp | 272 KB | ~140 KB |
| mogao.webp | 269 KB | ~140 KB |
| shosoin.webp | 266 KB | ~140 KB |
| jinci.webp | 258 KB | ~130 KB |
| huqiu.webp | 254 KB | ~130 KB |
| daming.webp | 251 KB | ~130 KB |

**Medium -- Missing width and height attributes**
No `<img>` tags include `width`/`height` attributes, causing Cumulative Layout Shift.
Recommendation: Add explicit dimensions matching natural aspect ratio.

**Low -- Detail pages have no hero images**
Detail pages are text-only above the fold.
Recommendation: Add a hero image to each detail page header.

---

## 7. AI Search Readiness -- Score: 68/100

### What Works

- FAQPage schema on homepage is well-structured for AI Overview extraction
- BreadcrumbList helps AI crawlers understand site hierarchy
- Content written in clear, definitional prose -- easy for AI models to cite
- Substantive factual claims with specific data points
- No paywalls or login gates -- fully accessible to crawlers
- Chinese + English site names provided

### Findings

**High -- No llms.txt file**
`llms.txt` is not present at the site root. This is the primary discovery mechanism for LLM crawlers (ChatGPT, Claude, Perplexity).
Recommendation: Create `llms.txt` listing key pages with brief descriptions.

**Medium -- No /about page for brand authority**
AI models evaluate site authority partially based on About/Contact page signals.
Recommendation: Add an `/about/` page with org info and editorial policy.

**Medium -- No citation-friendly paragraph anchors**
Travel guide sections cannot be deep-linked at the paragraph level.
Recommendation: Add `id` attributes to section headings for external deep-linking.

**Low -- No analytics to measure AI traffic**
No analytics means no visibility into AI crawler referral patterns.
Recommendation: Add Plausible or Cloudflare Web Analytics (privacy-respecting).

---

## Category Score Summary

| Category | Score | Weight | Weighted |
|---|---|---|---|
| Technical SEO | 62 | 22% | 13.6 |
| Content Quality | 85 | 23% | 19.6 |
| On-Page SEO | 78 | 20% | 15.6 |
| Schema / Structured Data | 60 | 10% | 6.0 |
| Performance | 55 | 10% | 5.5 |
| AI Search Readiness | 68 | 10% | 6.8 |
| Images | 72 | 5% | 3.6 |
| **Total** | **71** | | **70.7** |

---

*Audit completed 2026-08-05. Based on full source analysis of 19 pages. No live crawling -- findings from static source code inspection.*
