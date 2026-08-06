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
        img_html = f'<img src="{img_path}" alt="{s["name"]}" width="800" height="600" class="w-full aspect-[4/3] object-cover border-b border-rule" loading="lazy">'
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

def gen_sites_section(sec_key, id_str, title, kicker):
    cards = "".join(site_card(s) for s in SITES if s["section"] == sec_key)
    k = f'<p class="kicker flex items-center gap-3 text-gold text-[11px] font-mono uppercase mb-4"><span class="inline-block h-px w-8 bg-gold"></span>{kicker}</p>'
    return f'<section id="{id_str}" class="py-16 md:py-24 px-4 max-w-7xl mx-auto">{k}<h2 class="display text-3xl md:text-[3.4rem] mb-8">{title}</h2><div class="grid grid-cols-1 lg:grid-cols-2 gap-6">{cards}</div></section>'


TAG_IMG = {"original":"images/tag-original.webp","site_later":"images/tag-site-later.webp","archaeological":"images/tag-archaeological.webp","modern_rebuild":"images/tag-modern-rebuild.webp"}
tag_items = "".join(f'<div class="border border-rule rounded overflow-hidden bg-surface flex flex-col"><img src="{TAG_IMG[k]}" alt="{v["label"]} illustration" width="1000" height="1415" class="w-full h-40 object-contain bg-stone/[0.04] border-b border-rule" loading="lazy"><div class="p-5 flex-1"><div class="flex items-center gap-2 mb-2"><span class="tag-dot {v["css"]}"></span><h3 class="display text-lg">{v["label"]}</h3></div><p class="text-sm text-stone leading-relaxed">{v["desc"]}</p></div></div>' for k,v in TAG_DATA.items())
faq_items = "".join(f'<details class="faq border-b border-rule py-4"><summary class="flex items-center justify-between text-ink font-medium cursor-pointer display text-lg">{q}<svg class="w-5 h-5 text-stone flex-shrink-0 ml-3" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></summary><p class="mt-3 text-stone leading-relaxed max-w-3xl">{a}</p></details>' for q,a in FAQ)

sites_json = json.dumps(SITES, ensure_ascii=False)
tags_json = json.dumps(TAG_DATA, ensure_ascii=False)

GFONTS = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&amp;family=Noto+Serif+SC:wght@500;700&amp;family=Noto+Sans+SC:wght@300;400;500&amp;family=IBM+Plex+Sans:wght@300;400;500;600&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap"
CSS = (
    "  html { scroll-behavior: smooth; scroll-padding-top: 84px; }\n"
    "  .display, h1,h2,h3,h4 { font-family: 'Cormorant Garamond','Noto Serif SC',Georgia,'Songti SC','STSong',serif; font-kerning: normal; letter-spacing:-.01em; }\n"
    "  body { font-family: 'IBM Plex Sans','Noto Sans SC',system-ui,sans-serif; }\n"
    "  ::selection { background:#a01e14; color:#fdf8ef; }\n"
    "  .tag-dot { display: inline-block; width: 11px; height: 11px; border-radius: 50%; margin-right: 6px; box-shadow: inset 0 0 0 1px rgb(0 0 0/.06); }\n"
    "  .tag-green { background: #3e7d52; } .tag-yellow { background: #caa43b; }\n"
    "  .tag-orange { background: #c97b3d; } .tag-red { background: #b03a2f; }\n"
    "  .site-card { border:1px solid #e2d7c8; border-radius:2px; background:#fffdf8; transition: box-shadow .6s cubic-bezier(.16,1,.3,1), border-color .6s; box-shadow: 0 1px 2px rgb(26 21 16/.04); }\n"
    "  .site-card:hover { border-color:#b03a2f; box-shadow:0 18px 34px -20px rgb(26 16 12/.4); }\n"
    "  .site-card img { transition: transform .8s cubic-bezier(.16,1,.3,1); filter:saturate(.92); }\n"
    "  .site-card:hover img { transform: scale(1.035); filter:saturate(1); }\n"
    "  .site-card h3 { transition: color .4s; }\n"
    "  .site-card:hover h3 { color:#a01e14; }\n"
    "  .nav-link { position:relative; }\n"
    "  .nav-link::after { content:''; position:absolute; bottom:-4px; left:0; width:0; height:1px; background:#a01e14; transition:width .4s cubic-bezier(.16,1,.3,1); }\n"
    "  .nav-link:hover::after { width:100%; }\n"
    "  .btn { transition: background-color .4s ease, border-color .4s ease, transform .5s cubic-bezier(.16,1,.3,1), box-shadow .5s; }\n"
    "  .btn:hover { transform: translateY(-1px); box-shadow: 0 14px 28px -16px rgb(23 16 12/.4); }\n"
    "  .kicker { letter-spacing:.3em; text-transform:uppercase; }\n"
    "  h2.display { position:relative; padding-bottom:.8rem; }\n"
    "  h2.display::after { content:''; position:absolute; left:2px; bottom:0; height:2px; width:64px; background:linear-gradient(90deg,#a01e14,#c8a45c); }\n"
    "  .reveal { opacity:0; transform: translateY(30px); transition: opacity .9s cubic-bezier(.16,1,.3,1), transform .9s cubic-bezier(.16,1,.3,1); }\n"
    "  .reveal.in { opacity:1; transform:none; }\n"
    "  .vert { writing-mode:vertical-rl; text-orientation:upright; letter-spacing:.32em; }\n"
    "  .seal { display:inline-grid; place-items:center; width:2rem; height:2rem; background:#a01e14; color:#fdf8ef; font-size:1rem; line-height:1; border-radius:1px; box-shadow: 0 2px 6px rgb(160 30 20/.35); }\n"
    "  .seal.raise:hover { background:#8a1810; transform:translateY(-1px); }\n"
    "  .watermark { pointer-events:none; user-select:none; }\n"
    "  #hero:has(.cta-trigger:hover) .hero-fog { opacity: 0.16; transition: opacity 0.9s cubic-bezier(.16,1,.3,1); }\n"
    "  @media (prefers-reduced-motion: reduce){ .reveal{opacity:1; transform:none; transition:none; } .site-card img, .btn, .nav-link::after { transition:none; } html{scroll-behavior:auto;} }\n"
    "  .comp-table th { font-weight:600; text-align:left; padding:12px 18px; border-bottom:1px solid #e8dcc9; color:#7a6f60; letter-spacing:.02em; font-size:.8rem; text-transform:uppercase; }\n"
    "  .comp-table td { padding:12px 18px; border-bottom:1px solid #efe6d8; vertical-align:top; }\n"
    "  .comp-table tr:hover td { background:#faf4e9; }\n"
    "  .faq summary::-webkit-details-marker { display:none; }\n"
    "  .faq summary { list-style:none; cursor:pointer; }\n"
    "  .chk-res { display:none; } .chk-res.on { display:block; }\n"
    "  .image-slot { transition: background-color .4s; }\n"
    "  .site-card:hover .image-slot { background-color: rgb(26 21 18/.08); }\n"
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
    '<meta name="twitter:description" content="Honest labels on every site. What really survives from Tang and Song China — and how to travel to it.">\n'
    '<meta property="og:image" content="https://tang-and-song-dynasty.com/images/hero.webp">\n'
    '<meta property="og:image:width" content="1200">\n'
    '<meta property="og:image:height" content="800">\n'
    '<meta name="twitter:image" content="https://tang-and-song-dynasty.com/images/hero.webp">\n'
    '<link rel="stylesheet" href="/dist/tailwind.css">\n'
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

nav_html = """<header class="sticky top-0 z-50 bg-paper/90 backdrop-blur-md border-b border-rule">
  <div class="max-w-7xl mx-auto px-4 h-[4.5rem] flex items-center justify-between">
    <a href="#hero" class="flex items-center gap-3 display text-lg tracking-tight text-ink group">
      <span class="seal group-hover:scale-105 transition-transform" aria-hidden="true">真</span>
      <span class="font-normal leading-none">Relics&nbsp;Guide</span>
      <span class="hidden sm:inline text-[10px] font-sans font-medium tracking-[.3em] uppercase text-gold">唐宋 · 遗存</span>
    </a>
    <nav class="hidden lg:flex items-center gap-4 text-[13px] tracking-wide text-stone">
      <a href="#quick-answer" class="nav-link hover:text-ink transition-colors">Answer</a>
      <a href="#tang-vs-song" class="nav-link hover:text-ink transition-colors">Compare</a>
      <a href="#for-travelers" class="nav-link hover:text-ink transition-colors">Travel</a>
      <a href="#tang-sites" class="nav-link hover:text-ink transition-colors">Tang</a>
      <a href="#song-sites" class="nav-link hover:text-ink transition-colors">Song</a>
      <a href="#routes" class="nav-link hover:text-ink transition-colors">Routes</a>
      <a href="#museums" class="nav-link hover:text-ink transition-colors">Museums</a>
      <a href="#timeline" class="nav-link hover:text-ink transition-colors">Timeline</a>
      <a href="#faq" class="nav-link hover:text-ink transition-colors">FAQ</a>
    </nav>
    <div class="flex items-center gap-2">
      <span class="hidden md:inline text-[10px] font-mono uppercase tracking-[.2em] text-gold">Est. Reviews 2026</span>
      <button class="lg:hidden text-stone p-2" onclick="document.getElementById('mn').classList.toggle('hidden')" aria-label="Menu">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
      </button>
    </div>
  </div>
  <div id="mn" class="hidden lg:hidden border-t border-rule bg-paper px-4 py-3 grid grid-cols-2 gap-1 text-sm text-stone">
    <a href="#quick-answer" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Quick Answer</a>
    <a href="#tang-vs-song" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Compare</a>
    <a href="#for-travelers" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Travel</a>
    <a href="#tang-sites" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Tang Sites</a>
    <a href="#song-sites" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Song Sites</a>
    <a href="#routes" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Routes</a>
    <a href="#museums" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Museums</a>
    <a href="#timeline" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">Timeline</a>
    <a href="#faq" class="py-1.5" onclick="this.parentElement.classList.add('hidden')">FAQ</a>
  </div>
</header>"""

hero = """<section id="hero" class="relative overflow-hidden">
  <img src="images/hero.webp" alt="Mogao Caves at Dunhuang, Gansu &mdash; the greatest surviving body of Tang-dynasty art" class="absolute inset-0 w-full h-full object-cover object-center" fetchpriority="high" decoding="async">
  <div class="hero-fog absolute inset-0 bg-paper/45" aria-hidden="true"></div>
  <div class="hero-fog absolute inset-0" aria-hidden="true" style="background:linear-gradient(180deg,rgba(245,239,230,.88) 0%,rgba(245,239,230,.52) 40%,rgba(245,239,230,.94) 100%);"></div>
  <span aria-hidden="true" class="watermark absolute font-display text-[38vw] md:text-[24vw] leading-none text-ink/[0.05] top-1/2 -translate-y-1/2 -right-[6vw] select-none whitespace-nowrap">唐&ensp;宋</span>
  <div class="relative max-w-7xl mx-auto px-4 sm:px-6 min-h-[82dvh] flex items-center gap-12 md:gap-16 pt-36 pb-20">
    <div aria-hidden="true" class="vert shrink-0 hidden lg:flex text-stone/55 text-sm tracking-[.45em] leading-loose pr-8 self-stretch items-center border-r border-rule">
      <span>行至山河 · 见唐所遗 · 观宋之雅</span>
    </div>
    <div class="max-w-3xl">
      <p class="flex items-center gap-3 text-stone text-[11px] font-mono uppercase tracking-[.25em] mb-7">
        <span class="inline-block h-px w-10 bg-gold"></span>
        <span>中国旅行指南</span><span class="text-gold">/</span><span>China Travel &middot; Verified 2026</span>
      </p>
      <h1 class="display text-[2.6rem] md:text-6xl lg:text-[4.4rem] leading-[1.02] tracking-tight text-ink mb-7">
        The Tang and the Song,<br/><span class="italic text-gold">and what survives</span> today
      </h1>
      <p class="text-stone text-lg md:text-xl leading-relaxed max-w-xl mb-3">
        China keeps <strong class="text-ink font-medium">four wooden buildings</strong> from the Tang, and fewer than thirty from the Song. The surviving relics cluster along three routes: <strong class="text-ink font-medium">Shanxi&rsquo;s mountain temples, Xi&rsquo;an&rsquo;s imperial core, and Dunhuang&rsquo;s cave art</strong>.
      </p>
      <p class="text-stone/80 text-sm leading-relaxed max-w-xl mb-9">
        Every site carries an honesty label &mdash; <span class="text-gold font-medium">gold, original</span>; <span class="text-vermillion font-medium">cinnabar, rebuilt</span>. Built for travelers who want the real thing, not a theme park.
      </p>
      <div class="flex flex-wrap gap-3.5">
        <a href="#quick-answer" class="cta-trigger btn inline-flex items-center gap-2 px-7 py-3.5 bg-vermillion text-paper text-sm font-medium rounded-sm hover:bg-accent-hover">
          Tang vs Song: Quick Answer
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
        <a href="#tang-sites" class="btn inline-flex items-center gap-2 px-7 py-3.5 border border-rule text-ink text-sm font-medium rounded-sm hover:border-vermillion">Where to go</a>
        <a href="#routes" class="btn inline-flex items-center gap-2 px-7 py-3.5 border border-rule text-ink text-sm font-medium rounded-sm hover:border-vermillion">China Travel Routes</a>
      </div>
    </div>
  </div>
</section>"""

footer = """<footer class="border-t border-rule py-14 px-4 max-w-7xl mx-auto">
  <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
    <div class="flex items-center gap-3 display text-ink">
      <span class="seal" aria-hidden="true">真</span>
      <span class="font-normal">Relics Guide</span>
    </div>
    <p class="text-sm text-stone leading-relaxed max-w-xl">
      Facts verified 2026-08. Classifications follow public heritage records: national protected sites, UNESCO listings and State Council designations.
    </p>
  </div>
  <div class="mt-8 pt-6 border-t border-rule flex flex-wrap items-center justify-between gap-3 text-xs text-stone/80">
    <span>No trackers. No cookies. No ads &mdash; honest information about what survives.</span>
    <span class="font-mono uppercase tracking-[.2em] text-gold">唐 宋 &middot; 遗 存 &middot; 真</span>
  </div>
  <div class="mt-4 text-[11px] leading-relaxed text-stone/60 max-w-3xl">
    Photographs are real site imagery sourced from <a class="underline underline-offset-2 hover:text-ink" href="https://commons.wikimedia.org/wiki/Category:Mogao_Caves" rel="noopener">Wikimedia Commons</a> under CC BY / CC BY-SA licences &mdash; no AI-generated imagery. Individual author and licence details appear on each image&rsquo;s Commons file page.
  </div>
</footer>"""

reveal_js = """<script>
(function () {
  if (!('IntersectionObserver' in window)) return;
  var sections = document.querySelectorAll('section');
  sections.forEach(function (s) { s.classList.add('reveal'); });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.06, rootMargin: '0px 0px -8% 0px' });
  sections.forEach(function (s) { io.observe(s); });
})();
</script>"""

# Assemble all sections
full = head + nav_html + hero
full += open("sections/quick_answer.html", encoding="utf-8").read()
full += open("sections/comparison_table.html", encoding="utf-8").read()
full += open("sections/travel_transition.html", encoding="utf-8").read()
full += open("sections/tag_system.html", encoding="utf-8").read().replace("__TAG_ITEMS__", tag_items)
full += gen_sites_section("tang", "tang-sites", "Tang Dynasty: Where to See What Survives", "Era I &mdash; The Tang · 唐 遗存")
full += gen_sites_section("song", "song-sites", "Song Dynasty: Where to See What Survives", "Era II &mdash; The Song · 宋 遗存")
full += open("sections/routes.html", encoding="utf-8").read()
full += open("sections/museums.html", encoding="utf-8").read()
full += open("sections/timeline.html", encoding="utf-8").read()
full += open("sections/related.html", encoding="utf-8").read()
full += open("sections/checker_base.html", encoding="utf-8").read().replace("__SITES_JSON__", sites_json).replace("__TAGS_JSON__", tags_json)
full += open("sections/newsletter.html", encoding="utf-8").read()
full += open("sections/faq_header.html", encoding="utf-8").read().replace("__FAQ_ITEMS__", faq_items)
full += "\n" + footer + "\n" + reveal_js + "\n</body>\n</html>\n"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full)
print(f"index.html written: {len(full):,} bytes")
