# Performance Findings

## Render-Blocking Resources
Status: FAIL -- 2 render-blocking resources

1. cdn.tailwindcss.com (JS) -- loaded synchronously in head
2. fonts.googleapis.com (CSS) -- external font stylesheet

Impact: First Contentful Paint delayed by 1-3 seconds on slow connections.

## Image Optimization
Status: FAIL -- oversized, not responsive

Total image payload: ~3.8 MB across 18 images
Format: WebP (good)
Responsive: No srcset (poor)
Size range: 119 KB (kaifengtieta) to 286 KB (baoguo)
Target: All images should be under 150 KB for primary, with 400w/800w/1200w variants.

## CSS Delivery
Status: MIXED

Inline critical CSS -- good for FCP
Google Fonts external -- adds latency
Duplicate inline CSS across 18 detail pages -- minor code smell
No external stylesheet to cache -- both good and bad (fast first load, no caching benefit)

## JavaScript
Status: GOOD

No heavy frameworks
No third-party scripts
No analytics (privacy-positive, but no performance data)
Tailwind CDN is the only JS (renders utility classes dynamically)

## Layout Stability
Status: NEEDS WORK

Images lack width/height attributes -- will cause CLS
Tailwind CSS renders dynamically after JS execution -- may cause layout shifts
Recommend: static CSS + explicit image dimensions
