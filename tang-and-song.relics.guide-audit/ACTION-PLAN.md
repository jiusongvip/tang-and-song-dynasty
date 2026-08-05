# Action Plan -- tang-and-song.relics.guide

## Phase 1: Critical Fixes (Week 1)

These issues block indexability or significantly degrade search performance. Fix immediately.

### 1.1 Fix schema JSON-LD on all detail pages

**Severity:** Critical  
**Effort:** Low (1-2 hours)  
**Files:** 18 detail pages under `sites/*/index.html`, build pipeline  

The `{{` and `}}` double-brace escaping makes every schema block invalid JSON-LD. Google Rich Results Test will fail on all 18 detail pages.

**Fix:**
1. Inspect the detail page generation script (currently `gen_detail_pages.py` is incomplete)
2. Ensure schema JSON uses single braces `{` and `}`
3. Rebuild all 18 detail pages
4. Validate with [Google Rich Results Test](https://search.google.com/test/rich-results)

### 1.2 Add og:image to all pages

**Severity:** High  
**Effort:** Low (1 hour)  
**Files:** 19 HTML files  

**Fix:**
- Add to homepage `<head>`: `<meta property="og:image" content="https://tang-and-song.relics.guide/images/foguang.webp">`
- Add to each detail page: `<meta property="og:image" content="https://tang-and-song.relics.guide/images/{id}.webp">`
- Add width/height: `<meta property="og:image:width" content="1200">` and `height` matching aspect ratio
- Add `twitter:image` matching tags

### 1.3 Remove Tailwind CDN, build locally

**Severity:** Critical (Performance)  
**Effort:** Medium (2-3 hours)  
**Files:** All HTML files, build pipeline  

**Fix:**
1. Install Tailwind CLI: `pnpm add -D tailwindcss`
2. Create `tailwind.config.js` with existing color/font config
3. Build: `npx tailwindcss -i ./src/input.css -o ./dist/tailwind.css --minify`
4. Replace `<script src="https://cdn.tailwindcss.com">` with `<link rel="stylesheet" href="/dist/tailwind.css">`
5. Remove inline `tailwind.config` script from all pages

---

## Phase 2: High-Impact Improvements (Weeks 2-3)

These changes have measurable impact on search visibility and user experience. Fix within 2 weeks.

### 2.1 Optimize images and add responsive srcset

**Severity:** High  
**Effort:** Medium (3-4 hours)  
**Files:** `images/` directory, all HTML files  

**Fix:**
1. Recompress all images: `for f in images/*.webp; do cwebp -q 75 "$f" -o "$f"; done`
2. Generate responsive variants: 400w, 800w, 1200w per image
3. Update `<img>` tags to use `srcset` and `sizes`
4. Add `width` and `height` attributes to prevent CLS

Estimated image payload reduction: 40-50% (3.8 MB -> ~2.0 MB)

### 2.2 Create llms.txt

**Severity:** High (AI Search)  
**Effort:** Low (30 minutes)  
**Files:** New file `llms.txt`  

**Fix:** Create `/llms.txt` at site root with page listing and descriptions. See recommendation in audit report Section 7.

### 2.3 Add security headers

**Severity:** High  
**Effort:** Low (30 minutes, server config)  
**Files:** Server config (Nginx/Cloudflare)  

**Fix:**
- `Strict-Transport-Security: max-age=31536000; includeSubDomains`
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: SAMEORIGIN`
- `Referrer-Policy: strict-origin-when-cross-origin`

### 2.4 Compress and externalize shared CSS

**Severity:** Medium  
**Effort:** Low (1 hour)  
**Files:** All HTML files  

**Fix:**
1. Extract shared inline `<style>` blocks from all detail pages
2. Create `shared.css` with long cache headers
3. Link via `<link rel="stylesheet">` on all detail pages

---

## Phase 3: Content and Authority (Month 2)

These changes strengthen E-E-A-T signals and content depth. Address within 4 weeks.

### 3.1 Add About and Contact pages

**Severity:** Medium  
**Effort:** Low (1-2 hours)  
**Files:** New `about/index.html`, `contact/index.html`  

**Fix:**
- Create `/about/` with organization story, editorial standards, authenticity methodology
- Create `/contact/` with email or contact form
- Add to navigation and sitemap

### 3.2 Add Organization schema

**Severity:** Medium  
**Effort:** Low (30 minutes)  
**Files:** `index.html`  

**Fix:** Add Organization + WebSite schema to homepage head:
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Relics Guide",
  "url": "https://tang-and-song.relics.guide/"
}
```

### 3.3 Expand thin "Why Visit" sections

**Severity:** Low  
**Effort:** Low (1 hour)  
**Files:** `deep_data.py`, detail pages  

**Fix:** Expand "Why Visit" for Japan sites and theme parks to 3-4 unique sentences. Ensure no text is duplicated from homepage cards.

### 3.4 Add hero images to detail pages

**Severity:** Low  
**Effort:** Low (1-2 hours)  
**Files:** All 18 detail pages  

**Fix:** Add an `<img>` element in the header section above the H1, using the existing site image with `loading="eager"` (above-fold).

---

## Phase 4: Monitoring and Iteration (Ongoing)

### 4.1 Add analytics

**Severity:** Low  
**Effort:** Low (1 hour)  
**Files:** All HTML files  

**Fix:** Add Cloudflare Web Analytics or Plausible script to track:
- Organic search traffic
- AI crawler referral traffic
- Page-level engagement

### 4.2 Monitor Google Search Console

Set up GSC property for `tang-and-song.relics.guide` to track:
- Indexation status
- Search queries and impressions
- Core Web Vitals
- Rich result appearance

### 4.3 Sitemap optimization

- Remove `changefreq` and `priority` from all entries
- Verify trailing slash redirects are consistent
- Submit updated sitemap to Google Search Console

### 4.4 Performance monitoring

After Tailwind local build and image optimization:
- Run Lighthouse on homepage and 3 detail pages
- Target: LCP < 2.5s, CLS < 0.1, TBT < 200ms
- Monitor CDN-cached CSS and image hit rates

---

## Implementation Summary

| Phase | Items | Effort | Impact |
|---|---|---|---|
| Phase 1: Critical Fixes | 3 items | 4-6 hours | Fixes broken schema, unblocks social sharing, fixes render-blocking |
| Phase 2: High-Impact | 4 items | 4.5-5.5 hours | Image optimization, AI readiness, security, CSS dedup |
| Phase 3: Content & Authority | 4 items | 3.5-5.5 hours | E-E-A-T signals, content depth, visual polish |
| Phase 4: Monitoring | 4 items | 2-3 hours | Analytics, GSC, ongoing optimization |
| **Total** | **15 items** | **14-20 hours** | |

Estimated health score improvement: **71 -> 85+**
