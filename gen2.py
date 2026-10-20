"""Generate deep detail pages from deep_data.py"""
import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))

exec(open("deep_data.py","r",encoding="utf-8").read())

# Load site data from gen.py
import json as _json
with open("gen.py","r",encoding="utf-8") as f:
    code = f.read()
ns = {"json":_json}
exec(code[:code.find("\ndef tag_badge")], ns)
SITES = ns["SITES"]; TAG_DATA = ns["TAG_DATA"]; FLAG = ns["FLAG"]
FLAG_EMOJI = {"CN":"&#x1f1e8;&#x1f1f3;","JP":"&#x1f1ef;&#x1f1f5;"}
DYN = {"tang":"Tang Dynasty","song":"Song Dynasty"}
# intrinsic pixel size of images/<id>.webp, measured locally with ffmpeg
IMG_DIMS = {"baoguo":[1200,801],"daming":[1200,800],"datangbuye":[1200,436],"dayanta":[1200,1600],"famen":[1200,731],"foguang":[1200,900],"huqiu":[1200,1857],"jinci":[1200,900],"kaifengtieta":[1200,800],"longxing":[1200,900],"mogao":[1024,731],"nanchan":[1200,900],"qingmingheyuan":[1200,882]}
GFONTS = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&amp;family=Noto+Serif+SC:wght@500;700&amp;family=Noto+Sans+SC:wght@300;400;500&amp;family=IBM+Plex+Sans:wght@300;400;500;600&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap"
CSS = "html{scroll-behavior:smooth;scroll-padding-top:80px}h1,h2,h3,h4,.display{font-family:'Cormorant Garamond','Noto Serif SC',Georgia,serif}body{font-family:'IBM Plex Sans','Noto Sans SC',system-ui,sans-serif}.tag-dot{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:6px}.tag-green{background:#166534}.tag-yellow{background:#ca8a04}.tag-orange{background:#ea580c}.tag-red{background:#dc2626}.nav-link{position:relative}.nav-link::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:#b91c1c;transition:width .2s}.nav-link:hover::after{width:100%}"

for site in SITES:
    sid = site["id"]
    ext = DEEP.get(sid)
    if not ext:
        print(f"  WARNING: no deep data for {sid}")
        continue
    t = TAG_DATA[site["tag"]]
    label = t["label"]; css = t["css"]
    flg = FLAG.get(site.get("country",""),"")
    flag_e = FLAG_EMOJI.get(site.get("country",""),"")
    dynasty = DYN.get(site.get("dynasty","tang"),"Tang Dynasty")
    sec = site.get("section","tang")
    sec_anchor = {"tang":"tang-sites","song":"song-sites"}.get(sec,"tang-sites")
    url = f"https://www.tang-and-song-dynasty.com/sites/{sid}/"
    w, h = IMG_DIMS.get(sid, [1200, 900])
    rel_ids = list(site.get("related") or [])
    for other in SITES:
        if len(rel_ids) >= 4: break
        if other["id"] == sid or other["id"] in rel_ids: continue
        if other.get("province") == site.get("province") or other.get("dynasty") == site.get("dynasty"): rel_ids.append(other["id"])
    rel_map = {s["id"]: s for s in SITES}
    rel_html = "".join(f'<a href="/sites/{rid}/" class="flex items-center justify-between gap-3 px-4 py-3 border border-rule rounded hover:border-vermillion transition"><span class="text-sm font-medium text-ink">{rel_map[rid]["name"]}</span><span class="text-xs text-stone font-mono whitespace-nowrap">{rel_map[rid]["year"]} \u00b7 {rel_map[rid]["province"]}</span></a>' for rid in rel_ids[:4] if rid in rel_map)
    meta_desc = f"{site['name']} in {site['city']} ({dynasty}, {site['year']}). {label}. Getting there, seasons, where to stay, and honest tips for visitors."

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YZGSK745YV"></script>
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('js',new Date());gtag('config','G-YZGSK745YV');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{site['name']} ({site['year']}) | {dynasty} Guide</title>
<meta name="description" content="{meta_desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{site['name']} — Complete {dynasty} Travel Guide">
<meta property="og:description" content="{meta_desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{site['name']} — {dynasty} Travel Guide">
<meta name="twitter:description" content="{meta_desc}">
<meta property="og:image" content="https://www.tang-and-song-dynasty.com/images/{sid}.webp">
<meta property="og:image:width" content="{w}">
<meta property="og:image:height" content="{h}">
<meta name="twitter:image" content="https://www.tang-and-song-dynasty.com/images/{sid}.webp">
<link rel="stylesheet" href="/tailwind.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{GFONTS}" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"TouristAttraction","name":"{site['name']}","description":"{meta_desc[:300]}","address":{{"@type":"PostalAddress","addressLocality":"{site['city']}","addressRegion":"{site['province']}","addressCountry":"{site.get('country','CN')}"}}}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Tang and Song Dynasty Guide","item":"https://www.tang-and-song-dynasty.com"}},{{"@type":"ListItem","position":2,"name":"{site['name']}","item":"{url}"}}]}}</script>
</head>
<body class="bg-paper text-ink antialiased">
<header class="sticky top-0 z-50 bg-paper/95 backdrop-blur-sm border-b border-rule">
  <div class="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
    <a href="/" class="text-lg font-semibold tracking-tight display text-ink">&larr; Relics Guide</a>
    <nav class="hidden md:flex items-center gap-5 text-sm text-stone">
      <a href="/" class="nav-link hover:text-ink transition-colors">Home</a>
      <a href="/#tang-sites" class="nav-link hover:text-ink transition-colors">Tang Sites</a>
      <a href="/#song-sites" class="nav-link hover:text-ink transition-colors">Song Sites</a>
      <a href="/#routes" class="nav-link hover:text-ink transition-colors">Routes</a>
    </nav>
  </div>
</header>
<section class="pt-20 pb-12 px-4 max-w-4xl mx-auto">
  <p class="text-xs text-stone font-mono uppercase tracking-wide mb-4"><a href="/" class="hover:text-vermillion transition">Relics Guide</a> &rsaquo; <a href="/#{sec_anchor}" class="hover:text-vermillion transition">{dynasty} Sites</a> &rsaquo; {site['name']}</p>
  <div class="flex items-start justify-between gap-4 mb-3">
    <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded text-xs font-medium bg-{css}-bg text-{css}"><span class="tag-dot {css}"></span>{label}</span>
    <span class="text-xs text-stone font-mono">{flag_e} {flg}</span>
  </div>
  <h1 class="display text-3xl md:text-5xl tracking-tight leading-tight mb-3">{site['name']}</h1>
  <p class="text-stone mb-2">{site['pinyin']}</p>
  <div class="flex flex-wrap gap-x-6 gap-y-2 text-sm text-ink mt-4 mb-6">
    <span><strong>Built:</strong> {site['year']}</span>
    <span><strong>Dynasty:</strong> {dynasty}</span>
    <span><strong>Location:</strong> {site['city']}, {site['province']}</span>
    <span><strong>Admission:</strong> {site['admission']}</span>
    <span><strong>Time needed:</strong> {site['duration']}</span>
  </div>
  <figure class="mb-5"><div class="aspect-[4/3] overflow-hidden border border-rule bg-stone/[0.04]"><img src="/images/{sid}.webp" alt="{site['name']}, {site['city']} ({site['year']}) — {label}" width="{w}" height="{h}" fetchpriority="high" decoding="async" class="w-full h-full object-cover"></div><figcaption class="text-xs text-stone mt-2 font-mono">{site['name']} \u00b7 {site['city']}, {site['province']}</figcaption></figure>
  <p class="text-sm text-stone border-l-2 border-vermillion pl-3 italic mb-4">Honest note: {site['honest']}</p>
  <p class="text-xs text-stone font-mono">Basis: {site['basis']} — click <a href="/#authenticity" class="text-vermillion underline underline-offset-2">Authenticity Labels</a> to understand our classification system.</p>
</section>
<section class="py-8 px-4 max-w-4xl mx-auto">
  <h2 class="display text-2xl md:text-3xl mb-4">Why Visit</h2>
  <div class="text-stone leading-relaxed text-lg">{site['why']}</div>
</section>
<section class="py-8 px-4 max-w-4xl mx-auto">
  <h2 class="display text-2xl md:text-3xl mb-4">How to Get There</h2>
  <div class="text-stone leading-relaxed space-y-3">{ext['t']}</div>
</section>
<section class="py-8 px-4 max-w-4xl mx-auto">
  <h2 class="display text-2xl md:text-3xl mb-4">Where to Stay</h2>
  <div class="text-stone leading-relaxed space-y-3">{ext['s']}</div>
</section>
<section class="py-8 px-4 max-w-4xl mx-auto">
  <h2 class="display text-2xl md:text-3xl mb-4">What to Eat</h2>
  <div class="text-stone leading-relaxed space-y-3">{ext['f']}</div>
</section>
<section class="py-8 px-4 max-w-4xl mx-auto">
  <h2 class="display text-2xl md:text-3xl mb-4">Best Time to Visit</h2>
  <div class="text-stone leading-relaxed space-y-3">{ext['se']}</div>
</section>
<section class="py-8 px-4 max-w-4xl mx-auto">
  <h2 class="display text-2xl md:text-3xl mb-4">Tips for Foreign Travelers</h2>
  <div class="text-stone leading-relaxed space-y-3">{ext['ti']}</div>
</section>
<section class="py-8 px-4 max-w-4xl mx-auto">
  <h2 class="display text-2xl md:text-3xl mb-4">Pair it with another site</h2>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">{rel_html}</div>
</section>
<section class="py-12 px-4 max-w-4xl mx-auto border-t border-rule">
  <div class="flex flex-wrap gap-3">
    <a href="/#{sec_anchor}" class="px-5 py-2 border border-rule text-ink text-sm font-medium rounded hover:border-vermillion transition">Back to {dynasty} Sites</a>
    <a href="/#routes" class="px-5 py-2 border border-rule text-ink text-sm font-medium rounded hover:border-vermillion transition">See Trip Routes</a>
    <a href="/" class="px-5 py-2 bg-vermillion text-white text-sm font-medium rounded hover:bg-accent-hover transition">Back to Guide Home</a>
  </div>
</section>
<footer class="border-t border-rule py-12 px-4 max-w-7xl mx-auto text-center text-sm text-stone">
  <p>Facts verified: 2026-08. All site classifications based on public heritage records: NPU designations, UNESCO listings, and State Council protected sites.</p>
  <p class="mt-1">No ads, no accounts, no email collection. Traffic is counted only as anonymous aggregate page views by Google Analytics.</p>
</footer>
</body>
</html>"""
    d = os.path.join("sites", sid)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d,"index.html"),"w",encoding="utf-8") as f:
        f.write(html)
    sz = len(html)
    print(f"  Generated: {sid}/index.html ({sz} bytes)")

print(f"\nGenerated {len([s for s in SITES if s['id'] in DEEP])} deep detail pages.")
