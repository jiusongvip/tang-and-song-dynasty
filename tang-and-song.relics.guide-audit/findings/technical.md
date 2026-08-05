# Technical SEO Findings

## robots.txt
Status: PASS
Clean configuration. Allows all crawlers with sitemap reference.
Path: /robots.txt

## sitemap.xml
Status: PASS with notes
19 URLs total (1 homepage + 18 detail pages). Proper XML format with lastmod dates.
Notes: All entries use changefreq=monthly and priority 0.8 (detail pages). These are unnecessary -- Google primarily uses lastmod.

## Canonical URLs
Status: PASS
Homepage: https://tang-and-song.relics.guide/
Detail pages: https://tang-and-song.relics.guide/sites/{id}/
All canonical URLs are correct and self-referential.

## Meta Robots
Status: PASS
All pages use <meta name="robots" content="index, follow">. No conflicts with robots.txt.

## Schema JSON-LD (Detail Pages)
Status: FAIL -- CRITICAL
All 18 detail pages use {{ and }} as JSON delimiters in schema LD+JSON blocks.
Affected schemas: TouristAttraction, BreadcrumbList on every detail page.
Google Rich Results Test will fail on these pages.
Homepage schema is unaffected and correct.

## Security Headers
Status: FAIL -- HIGH
No CSP, HSTS, X-Content-Type-Options, or X-Frame-Options headers configured.
Recommendation: Add via server config (Nginx/Cloudflare).

## Trailing Slash Consistency
Status: UNVERIFIED
Sitemap uses trailing slashes for all URLs. Server redirect behavior unknown.
If both /sites/foguang and /sites/foguang/ serve content, duplicate pages emerge.
