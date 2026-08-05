#!/usr/bin/env python3
"""Write the complete enhanced index.html from gen.py data."""
import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("gen.py", "r", encoding="utf-8") as f:
    gen_code = f.read()
data_part = gen_code[:gen_code.find(chr(10)+"def tag_badge")]
ns = {}
exec(data_part, ns)
SITES, TAG_DATA, FAQ = ns["SITES"], ns["TAG_DATA"], list(ns["FAQ"])
MUSEUMS, ROUTES, FLAG = ns["MUSEUMS"], ns["ROUTES"], ns["FLAG"]
FAQ.extend([
    ("What is the oldest wooden building in China?","Nanchan Temple in Shanxi, dated 782 (Tang Dynasty). It survived the great Buddhist persecution of 845 because it was too remote and insignificant to target."),
    ("Can I visit Foguang Temple without a guide?","Yes, but it is difficult. The temple is 4 hours from Taiyuan on mountain roads. No public transit. You need a private driver (~600-800 CNY/day from Taiyuan). Combine with Nanchan Temple in one day. No English signage."),
    ("What should I know about visiting Mogao Caves?","Book Standard Visit (8 caves, 238 CNY) 2-3 weeks ahead via WeChat mini-program. Strictly timed tours. No photos inside. Best months: April-May and September-October."),
    ("Are there any Tang dynasty artifacts still in Xi'an?","Very few in situ. Shaanxi History Museum has the best Tang collection. Daming Palace has foundations only. Big Wild Goose Pagoda is a Ming rebuild. For original Tang, go to Shanxi or Dunhuang."),
    ("Is the Forbidden City from the Tang or Song dynasty?","Neither. Built 1406-1420 during Ming Dynasty. Tang used Daming Palace in Xi'an. Song never used Beijing as capital."),
])


def tag_badge(k):
    t = TAG_DATA[k]
    return f'<span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded text-xs font-medium bg-{t["css"]}-bg text-{t["css"]}"><span class="tag-dot {t["css"]}"></span>{t["label"]}</span>'

def site_card(s):
    t, flg = TAG_DATA[s["tag"]], FLAG.get(s.get("country",""),"")
    img_path = s.get("image", "")
    if img_path:
        img_html = f'<img src="{img_path}" alt="{s["name"]}" class="w-full aspect-[4/3] object-cover border-b border-rule" loading="lazy">'
    else:
        img_html = f'<div class="image-slot w-full aspect-[4/3] bg-stone/[0.04] flex flex-col items-center justify-center gap-1.5 border-b border-rule"><svg class="w-8 h-8 text-stone/20" fill="none" stroke="currentColor" stroke-width="1" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg><span class="text-[11px] text-stone/25 font-mono uppercase tracking-wide">{s["name"]}</span></div>'
    return f"""<article class="site-card overflow-hidden">
{img_html}
<div class="p-5 md:p-6">
<div class="flex items-start justify-between gap-3 mb-3"><div>{tag_badge(s["tag"])}</div><span class="text-xs text-stone font-mono">{flg}</span></div>
<h3 class="display text-xl mb-1">{s["name"]}</h3>
<p class="text-sm text-stone mb-3">{s["zh"]} &middot; {s["pinyin"]}</p>
<div class="flex flex-wrap gap-4 text-sm text-ink mb-4"><span><strong>Built:</strong> {s["year"]}</span><span><strong>Location:</strong> {s["city"]}, {s["province"]}</span></div>
<p class="text-sm text-ink leading-relaxed mb-3"><strong>Why go:</strong> {s["why"]}</p>
<div class="flex flex-wrap gap-4 text-sm text-ink mb-3"><span><strong>Admission:</strong> {s["admission"]}</span><span><strong>Time:</strong> {s["duration"]}</span></div>
<p class="text-sm text-stone border-l-2 border-vermillion pl-3 italic">Honest note: {s["honest"]}</p>
<p class="text-xs text-stone mt-3 font-mono">Basis: {s["basis"]}</p>
<div class="mt-4 pt-3 border-t border-rule"><a href="sites/{s["id"]}/" class="inline-flex items-center gap-1 text-sm text-vermillion font-medium hover:text-accent-hover transition">View Details <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a></div>
</div></article>"""

def gen_sites_section(sec_key, id_str, title):
    cards = "".join(site_card(s) for s in SITES if s["section"] == sec_key)
    return f'<section id="{id_str}" class="py-16 md:py-24 px-4 max-w-7xl mx-auto"><h2 class="display text-3xl md:text-4xl mb-8">{title}</h2><div class="grid grid-cols-1 lg:grid-cols-2 gap-5">{cards}</div></section>'


jp_cards = "".join(site_card(s) for s in SITES if s["section"] == "japan")
tag_items = "".join(f'<div class="border border-rule rounded p-5 bg-surface"><div class="flex items-center gap-2 mb-2"><span class="tag-dot {v["css"]}"></span><h3 class="display text-lg">{v["label"]}</h3></div><p class="text-sm text-stone leading-relaxed">{v["desc"]}</p></div>' for v in TAG_DATA.values())
faq_items = "".join(f'<details class="faq border-b border-rule py-4"><summary class="flex items-center justify-between text-ink font-medium cursor-pointer display text-lg">{q}<svg class="w-5 h-5 text-stone flex-shrink-0 ml-3" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></summary><p class="mt-3 text-stone leading-relaxed max-w-3xl">{a}</p></details>' for q,a in FAQ)

sites_json = json.dumps(SITES, ensure_ascii=False)
tags_json = json.dumps(TAG_DATA, ensure_ascii=False)

GFONTS = "https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&amp;family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400;1,500&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap"
CSS = (
    "  html { scroll-behavior: smooth; scroll-padding-top: 80px; }\n"
    "  h1,h2,h3,h4,.display { font-family: 'DM Serif Display',Georgia,serif; }\n"
    "  body { font-family: 'IBM Plex Sans',system-ui,sans-serif; }\n"
    "  .tag-dot { display: inline-block; width: 12px; height: 12px; border-radius: 50%; margin-right: 6px; }\n"
    "  .tag-green { background: #166534; } .tag-yellow { background: #ca8a04; }\n"
    "  .tag-orange { background: #ea580c; } .tag-red { background: #dc2626; }\n"
    "  .site-card { border:1px solid #e7e5e4; border-radius:4px; background:#fff; transition: box-shadow .2s, border-color .2s; }\n"
    "  .site-card:hover { border-color:#b91c1c; box-shadow:0 2px 12px rgb(185 28 28/.08); }\n"
    "  .nav-link { position:relative; }\n"
    "  .nav-link::after { content:''; position:absolute; bottom:-4px; left:0; width:0; height:2px; background:#b91c1c; transition:width .2s; }\n"
    "  .nav-link:hover::after { width:100%; }\n"
    "  .comp-table th { font-weight:600; text-align:left; padding:10px 16px; border-bottom:2px solid #e7e5e4; }\n"
    "  .comp-table td { padding:10px 16px; border-bottom:1px solid #e7e5e4; vertical-align:top; }\n"
    "  .comp-table tr:hover td { background:#fafaf7; }\n"
    "  .faq summary::-webkit-details-marker { display:none; }\n"
    "  .faq summary { list-style:none; cursor:pointer; }\n"
    "  .chk-res { display:none; } .chk-res.on { display:block; }\n"
    "  .image-slot { transition: background-color .2s; }\n"
    "  .site-card:hover .image-slot { background-color: rgb(28 25 23 / .06); }\n"
    "  @media print { header,footer,#checker,#newsletter,#related { display:none; } body { font-size:11pt; } h2 { page-break-before:always; } }\n"
)

art = json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Tang vs Song Dynasty: What Survives Today - A Traveler's Guide","description":"Compare Tang and Song dynasties and find surviving ruins you can visit. Honest authenticity labels on every site.","datePublished":"2026-08-05","dateModified":"2026-08-05","author":{"@type":"Organization","name":"Relics Guide"},"publisher":{"@type":"Organization","name":"Relics Guide"}}, ensure_ascii=False)
faqs_schema = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}, ensure_ascii=False)
tbl = json.dumps({"@context":"https://schema.org","@type":"Table","about":"Tang vs Song Dynasty Comparison"})
tas = json.dumps({"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"TouristAttraction","name":s["name"],"description":s["why"],"address":{"@type":"PostalAddress","addressLocality":s["city"],"addressRegion":s["province"],"addressCountry":s["country"]}} for s in SITES]}, ensure_ascii=False)
bc = '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Tang and Song Dynasty Guide","item":"https://tang-and-song-dynasty.com/"}]}'

head = (
    '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    '<title>Tang vs Song Dynasty: What Survives Today</title>\n'
    '<meta name="description" content="Compare Tang and Song dynasties: what you can still see today. An honest guide to surviving architecture with authenticity labels on every site.">\n'
    '<meta name="robots" content="index, follow">\n'
    '<link rel="canonical" href="https://tang-and-song-dynasty.com/">\n'
    '<meta property="og:title" content="Tang vs Song Dynasty: What Survives Today - Real Ruins Guide">\n'
    '<meta property="og:description" content="Compare Tang and Song dynasties: what they achieved, how they fell, and what you can still visit today.">\n'
    '<meta property="og:type" content="website">\n'
    '<meta name="twitter:card" content="summary_large_image">\n'
    '<meta name="twitter:title" content="Tang vs Song Dynasty: What Survives Today">\n'
    '<meta name="twitter:description" content="Honest labels on every site. Best Tang architecture is in Japan.">\n'
    '<script src="https://cdn.tailwindcss.com"></script>\n'
    '<script>\ntailwind.config = {\n  theme: {\n    extend: {\n'
    "      colors: {\n        ink: '#1a1714', stone: '#57534e', paper: '#fafaf7', surface: '#ffffff',\n"
    "        vermillion: '#b91c1c', 'accent-hover': '#991b1b', rule: '#e7e5e4',\n"
    "        'tag-green': '#166534', 'tag-green-bg': '#dcfce7',\n"
    "        'tag-yellow': '#92400e', 'tag-yellow-bg': '#fef3c7',\n"
    "        'tag-orange': '#9a3412', 'tag-orange-bg': '#ffedd5',\n"
    "        'tag-red': '#991b1b', 'tag-red-bg': '#fee2e2',\n      },\n"
    "      fontFamily: {\n        display: ['\"DM Serif Display\"','Georgia','serif'],\n"
    "        body: ['\"IBM Plex Sans\"','system-ui','sans-serif'],\n"
    "        mono: ['IBM Plex Mono','monospace'],\n      },\n    }\n  }\n}\n</script>\n"
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="' + GFONTS + '" rel="stylesheet">\n'
    '<style>' + CSS + '</style>\n'
    '<script type="application/ld+json">' + art + '</script>\n'
    '<script type="application/ld+json">' + faqs_schema + '</script>\n'
    '<script type="application/ld+json">' + tbl + '</script>\n'
    '<script type="application/ld+json">' + tas + '</script>\n'
    '<script type="application/ld+json">' + bc + '</script>\n'
    '</head>\n<body class="bg-paper text-ink antialiased">\n'
)

nav_html = """<header class="sticky top-0 z-50 bg-paper/95 backdrop-blur-sm border-b border-rule">
  <div class="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
    <a href="#hero" class="text-lg font-semibold tracking-tight display text-ink">Relics Guide</a>
    <nav class="hidden lg:flex items-center gap-3 text-sm text-stone">
      <a href="#quick-answer" class="nav-link hover:text-ink transition-colors">Answer</a>
      <a href="#tang-vs-song" class="nav-link hover:text-ink transition-colors">Compare</a>
      <a href="#for-travelers" class="nav-link hover:text-ink transition-colors">Travel</a>
      <a href="#authenticity" class="nav-link hover:text-ink transition-colors">Labels</a>
      <a href="#tang-sites" class="nav-link hover:text-ink transition-colors">Tang</a>
      <a href="#song-sites" class="nav-link hover:text-ink transition-colors">Song</a>
      <a href="#japan" class="nav-link hover:text-ink transition-colors">Japan</a>
      <a href="#authentic-vs-rebuilt" class="nav-link hover:text-ink transition-colors">Real v Fake</a>
      <a href="#routes" class="nav-link hover:text-ink transition-colors">Routes</a>
      <a href="#museums" class="nav-link hover:text-ink transition-colors">Museums</a>
      <a href="#timeline" class="nav-link hover:text-ink transition-colors">Timeline</a>
      <a href="#checker" class="nav-link hover:text-ink transition-colors">Checker</a>
      <a href="#faq" class="nav-link hover:text-ink transition-colors">FAQ</a>
    </nav>
    <button class="lg:hidden text-stone p-2" onclick="document.getElementById('mn').classList.toggle('hidden')" aria-label="Menu">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
    </button>
  </div>
  <div id="mn" class="hidden lg:hidden border-t border-rule bg-paper px-4 py-3 grid grid-cols-2 gap-1 text-sm text-stone">
    <a href="#quick-answer" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Quick Answer</a>
    <a href="#tang-vs-song" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Compare</a>
    <a href="#for-travelers" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Travel</a>
    <a href="#authenticity" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Labels</a>
    <a href="#tang-sites" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Tang Sites</a>
    <a href="#song-sites" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Song Sites</a>
    <a href="#japan" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Japan</a>
    <a href="#routes" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Routes</a>
    <a href="#museums" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Museums</a>
    <a href="#authentic-vs-rebuilt" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Real vs Rebuilt</a>
    <a href="#timeline" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Timeline</a>
    <a href="#checker" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Checker</a>
    <a href="#faq" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">FAQ</a>
  </div>
</header>"""

hero = """<section id="hero" class="min-h-[75dvh] flex items-center px-4 max-w-7xl mx-auto pt-20 pb-16">
  <div class="max-w-3xl">
    <p class="text-xs text-stone font-mono uppercase tracking-wide mb-4">Travel Guide &mdash; Facts verified 2026-08</p>
    <h1 class="display text-4xl md:text-6xl tracking-tight leading-tight mb-5">Tang vs Song Dynasty:<br>What Survives Today</h1>
    <p class="text-stone text-lg md:text-xl max-w-2xl leading-relaxed mb-3">
      The Tang left <strong class="text-ink">4 wooden buildings</strong> in China. The Song, fewer than 30. And the best Tang architecture is <strong class="text-ink">in Nara, Japan</strong> &mdash; not China.
    </p>
    <p class="text-stone text-sm max-w-2xl leading-relaxed mb-8">
      Every site carries an honesty label. Green = original. Red = theme park. No other English-language guide does this.
    </p>
    <div class="flex flex-wrap gap-3">
      <a href="#quick-answer" class="px-6 py-2.5 bg-vermillion text-white text-sm font-medium rounded hover:bg-accent-hover transition inline-block">Tang vs Song: Quick Answer</a>
      <a href="#for-travelers" class="px-6 py-2.5 border border-rule text-ink text-sm font-medium rounded hover:border-vermillion transition inline-block">I&rsquo;m Planning a Trip</a>
      <a href="#japan" class="px-6 py-2.5 border border-rule text-ink text-sm font-medium rounded hover:border-vermillion transition inline-block">Best Tang in Japan</a>
      <a href="#checker" class="px-6 py-2.5 border border-rule text-ink text-sm font-medium rounded hover:border-vermillion transition inline-block">Authenticity Checker</a>
    </div>
  </div>
</section>"""

footer = """<footer class="border-t border-rule py-12 px-4 max-w-7xl mx-auto text-center text-sm text-stone">
  <p>Facts verified: 2026-08. All site classifications based on public heritage records: NPU designations, UNESCO listings, and State Council protected sites.</p>
  <p class="mt-1">No trackers. No cookies. No ads. Just honest information about what survives.</p>
</footer>"""

# Assemble all sections
full = head + nav_html + hero
full += open("sections/quick_answer.html", encoding="utf-8").read()
full += open("sections/comparison_table.html", encoding="utf-8").read()
full += open("sections/travel_transition.html", encoding="utf-8").read()
full += open("sections/tag_system.html", encoding="utf-8").read().replace("__TAG_ITEMS__", tag_items)
full += gen_sites_section("tang", "tang-sites", "Tang Dynasty: Where to See What Survives")
full += gen_sites_section("song", "song-sites", "Song Dynasty: Where to See What Survives")
full += open("sections/japan_header.html", encoding="utf-8").read()
full += '<div class="grid grid-cols-1 md:grid-cols-2 gap-5">' + jp_cards + '</div></section>'
full += open("sections/authentic_vs_rebuilt.html", encoding="utf-8").read()
full += open("sections/routes.html", encoding="utf-8").read()
full += open("sections/museums.html", encoding="utf-8").read()
full += open("sections/timeline.html", encoding="utf-8").read()
full += open("sections/related.html", encoding="utf-8").read()
full += open("sections/checker_base.html", encoding="utf-8").read().replace("__SITES_JSON__", sites_json).replace("__TAGS_JSON__", tags_json)
full += open("sections/newsletter.html", encoding="utf-8").read()
full += open("sections/faq_header.html", encoding="utf-8").read().replace("__FAQ_ITEMS__", faq_items)
full += "\n" + footer + "\n</body>\n</html>\n"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full)
print(f"index.html written: {len(full):,} bytes")
