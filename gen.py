
import json

TAG_DATA = {
    "original":       {"label": "Original Structure",       "css": "tag-green",  "desc": "Original construction from the dynasty period, still standing."},
    "site_later":     {"label": "Original Site, Later Building", "css": "tag-yellow", "desc": "Original location, but the current structure was rebuilt in a later period."},
    "archaeological": {"label": "Archaeological Site",       "css": "tag-orange","desc": "Excavated ruins only. No standing original structure. Artifacts are in museums."},
    "modern_rebuild": {"label": "Modern Reconstruction",     "css": "tag-red",    "desc": "Built in recent decades. A theme park or tourist reconstruction, not a historical structure."}
}

SITES = [
    {"image":"images/foguang.webp", "id":"foguang","dynasty":"tang","tag":"original","name":"Foguang Temple East Hall","zh":"Foguang Si Dong Dadian","pinyin":"Foguang Si Dong Dadian","year":857,"city":"Xinzhou","province":"Shanxi","country":"CN","why":"Largest Tang wooden structure still standing. Liang Sicheng found it in 1937 while searching for surviving Tang buildings. Japanese scholars had claimed none existed in China. It proved Tang timber-frame architecture was real.","honest":"4 hr drive from Taiyuan on mountain road. No public transit. Nearest town Doucun has basic guesthouses.","admission":"40 CNY","duration":"2 hrs min","basis":"1961 NPU","related":["nanchan"],"section":"tang"},
    {"image":"images/nanchan.webp", "id":"nanchan","dynasty":"tang","tag":"original","name":"Nanchan Temple","zh":"Nanchan Si","pinyin":"Nanchan Si","year":782,"city":"Xinzhou","province":"Shanxi","country":"CN","why":"Oldest surviving wooden building in China, dated 782. A modest three-bay hall that escaped the 845 Buddhist persecution by being too small and remote to matter.","honest":"Even more remote than Foguang. Combine both in one trip. No public transit.","admission":"20 CNY","duration":"1.5 hrs","basis":"1961 NPU","related":["foguang"],"section":"tang"},
    {"image":"images/dayanta.webp", "id":"dayanta","dynasty":"tang","tag":"site_later","name":"Big Wild Goose Pagoda","zh":"Dayan Ta","pinyin":"Dayan Ta","year":652,"city":"Xi'an","province":"Shaanxi","country":"CN","why":"Built 652 under Xuanzang to house sutras from India. Current structure is Ming dynasty but follows Tang form on original Tang foundation. One of few tangible Tang landmarks in Xi'an.","honest":"This is a Ming dynasty rebuild on a Tang foundation. It is NOT a Tang structure. Interior is modern.","admission":"50 CNY","duration":"1-2 hrs","basis":"1961 NPU","related":[],"section":"tang"},
    {"image":"images/mogao.webp", "id":"mogao","dynasty":"tang","tag":"original","name":"Mogao Caves (Tang Caves)","zh":"Mogao Ku","pinyin":"Mogao Ku","year":618,"city":"Dunhuang","province":"Gansu","country":"CN","why":"200+ Tang-period caves with original wall paintings and sculptures. Largest surviving body of Tang pictorial art. Cave 45 has the best-preserved Tang sculpture grouping.","honest":"Guided tours only, strictly timed. No photos inside. Book weeks ahead.","admission":"238 CNY","duration":"3-4 hrs","basis":"1987 UNESCO","related":[],"section":"tang"},
    {"image":"images/famen.webp", "id":"famen","dynasty":"tang","tag":"archaeological","name":"Famen Temple Museum","zh":"Famen Si","pinyin":"Famen Si","year":874,"city":"Baoji","province":"Shaanxi","country":"CN","why":"1987 discovery of an intact Tang underground palace sealed in 874. Contained Buddha finger-bone relic plus 2,499 items of Tang gold, silver, glass, and textiles. Greatest Tang archaeological find.","honest":"The above-ground temple is modern. Only the underground crypt and museum collection are Tang.","admission":"120 CNY","duration":"2-3 hrs","basis":"State Council protected site","related":[],"section":"tang"},
    {"image":"images/daming.webp", "id":"daming","dynasty":"tang","tag":"archaeological","name":"Daming Palace National Heritage Park","zh":"Daming Gong","pinyin":"Daming Gong","year":634,"city":"Xi'an","province":"Shaanxi","country":"CN","why":"Main Tang imperial palace, larger than the Forbidden City. Today: foundations exposed, museum on site. Understanding Tang scale requires seeing this.","honest":"Almost nothing above ground. You walk across buried foundations in a large park. The reconstructed gate is modern.","admission":"60 CNY","duration":"2-3 hrs","basis":"National Archaeological Park","related":[],"section":"tang"},
    {"image":"images/datangbuye.webp", "id":"datangbuye","dynasty":"tang","tag":"modern_rebuild","name":"Great Tang All Day Mall","zh":"Datang Buyecheng","pinyin":"Datang Buyecheng","year":2010,"city":"Xi'an","province":"Shaanxi","country":"CN","why":"Popular night-time tourist street with Tang-style lighting and performances. Lively after dark.","honest":"2010 theme park. Nothing is old. Popular for photos; no interest for serious history seekers.","admission":"Free","duration":"1-2 hrs eve","basis":"N-A (modern construction)","related":[],"section":"tang"},
    {"image":"images/baoguo.webp", "id":"baoguo","dynasty":"song","tag":"original","name":"Baoguo Temple Main Hall","zh":"Baoguo Si Dadian","pinyin":"Baoguo Si Dadian","year":1013,"city":"Ningbo","province":"Zhejiang","country":"CN","why":"Oldest wooden structure in southern China, built 1013. Masterpiece of Song timber framing that predates the official Song building manual (Yingzao Fashi, 1103).","honest":"Only the Main Hall is Song. Other temple halls are later additions.","admission":"20 CNY","duration":"1-2 hrs","basis":"1961 NPU","related":[],"section":"song"},
    {"image":"images/huqiu.webp", "id":"huqiu","dynasty":"song","tag":"original","name":"Tiger Hill Pagoda","zh":"Huqiu Ta","pinyin":"Huqiu Ta","year":961,"city":"Suzhou","province":"Jiangsu","country":"CN","why":"Famous 3-degree lean predates Pisa by 200 years. Original brick pagoda with visible traces of original color. One of the most atmospheric Song sites.","honest":"Cannot enter the pagoda. The lean is charming but a structural issue.","admission":"60 CNY","duration":"2-3 hrs","basis":"1961 NPU","related":[],"section":"song"},
    {"image":"images/kaifengtieta.webp", "id":"kaifengtieta","dynasty":"song","tag":"original","name":"Kaifeng Iron Pagoda","zh":"Kaifeng Tieta","pinyin":"Kaifeng Tieta","year":1049,"city":"Kaifeng","province":"Henan","country":"CN","why":"Brown-glazed brick pagoda that survived floods, wars, and the Yellow River shifting course. Only Song structure above ground in Kaifeng.","honest":"The rest of Song Kaifeng is buried 8 meters under Yellow River silt. Only this pagoda remains visible.","admission":"40 CNY","duration":"1-2 hrs","basis":"1961 NPU","related":[],"section":"song"},
    {"image":"images/jinci.webp", "id":"jinci","dynasty":"song","tag":"original","name":"Jinci Temple Hall of Holy Mother","zh":"Jinci Shengmudian","pinyin":"Jinci Shengmudian","year":1032,"city":"Taiyuan","province":"Shanxi","country":"CN","why":"Earliest surviving major Song timber hall. Intricate wood-carved dragons wrap around the front columns.","honest":"Complex has many later additions. Focus on the main hall only.","admission":"80 CNY","duration":"2-3 hrs","basis":"1961 NPU","related":[],"section":"song"},
    {"image":"images/longxing.webp", "id":"longxing","dynasty":"song","tag":"original","name":"Longxing Temple","zh":"Longxing Si","pinyin":"Longxing Si","year":971,"city":"Zhengding","province":"Hebei","country":"CN","why":"Four original Song buildings plus a 21.3m bronze Guanyin statue cast in 971 - the tallest surviving Song bronze sculpture.","honest":"Zhengding is off the tourist circuit. 3-hr drive from Beijing or accessible via Shijiazhuang HSR.","admission":"50 CNY","duration":"2-3 hrs","basis":"1961 NPU","related":[],"section":"song"},
    {"image":"images/qingmingheyuan.webp", "id":"qingmingheyuan","dynasty":"song","tag":"modern_rebuild","name":"Qingming Riverside Landscape Garden","zh":"Qingming Shanghe Yuan","pinyin":"Qingming Shanghe Yuan","year":1998,"city":"Kaifeng","province":"Henan","country":"CN","why":"1998 theme park recreating scenes from the famous Song painting Along the River During the Qingming Festival. Performances and reconstructed Song streets.","honest":"Zero historical fabric. A theme park. Useful for families and understanding Song street life at human scale.","admission":"120 CNY","duration":"3-4 hrs","basis":"N-A (modern construction)","related":[],"section":"song"},
]

MUSEUMS = [
    {"name":"Shaanxi History Museum","city":"Xi'an","country":"CN","why":"Richest Tang gold, silver, mural collection anywhere. Free but book 3+ days ahead on WeChat."},
    {"name":"Palace Museum","city":"Beijing","country":"CN","why":"Original Song painting Qingming Shanghe Tu and imperial ceramics. Book 7 days ahead."},
    {"name":"National Palace Museum","city":"Taipei","country":"TW","why":"Largest Song ceramics outside mainland. 21 Ru ware pieces - finest in the world."},
    {"name":"British Museum (Room 33)","city":"London","country":"GB","why":"Admonitions Scroll (Tang copy) and Tang-Song ceramics. Free. Scroll displayed 6 weeks/year."},
]

ROUTES = [
    {"image":"", "id":"tang-trail","name":"Tang Heritage Trail: Xi'an to Dunhuang","days":"8-10 days","cities":"Xi'an, Taiyuan, Xinzhou, Dunhuang","stops":"Dayanta, Famen Temple, Shaanxi History Museum, Jinci, Foguang, Nanchan, Mogao Caves","transport":"Fly into Xi'an (XIY). High-speed rail Xi'an-Taiyuan (3.5 hrs). Rent car+driver for Xinzhou mountain leg (Foguang/Nanchan: 4 hrs from Taiyuan, last stretch mountain road). Fly Taiyuan-Dunhuang or train via Lanzhou. Dunhuang: fly out or return to Xi'an.","note":"The Shanxi mountain temples (Foguang, Nanchan) are hardest to reach but most rewarding. No public transit to either temple. Hire a private driver from Taiyuan (~600-800 CNY/day). Combine both temples in one day trip. Road is paved but winding."},
    {"image":"", "id":"song-trail","name":"Song Heritage Trail: Kaifeng to Ningbo","days":"10-14 days","cities":"Kaifeng, Zhengding, Taiyuan, Suzhou, Hangzhou, Ningbo","stops":"Iron Pagoda, Longxing Temple, Jinci, Tiger Hill, Liuhe Pagoda, Baoguo Temple","transport":"Fly into Zhengzhou (CGO) for Kaifeng. High-speed rail Kaifeng-Shijiazhuang (2 hrs). Bus/taxi to Zhengding (30 min). Train to Taiyuan (1.5 hrs by HSR). Fly or HSR Taiyuan-Shanghai then train to Suzhou (30 min). HSR Suzhou-Hangzhou (1 hr). HSR Hangzhou-Ningbo (1 hr). Fly out from Ningbo (NGB) or Shanghai (PVG).","note":"Kaifeng stretch is sparse: most Song Kaifeng is buried under 8m of Yellow River silt. Only the Iron Pagoda is visible. Focus your time on Jiangnan (Suzhou-Hangzhou-Ningbo). All Jiangnan sites are accessible by public transit or short taxi rides."},
]

FAQ = [
    ("What is the main difference between Tang and Song dynasties?","Tang (618-907) was a cosmopolitan military empire based in Chang'an. Song (960-1279) was an inward-looking commercial society based in Kaifeng then Hangzhou. Tang conquered; Song traded. Tang was bigger; Song was more innovative (paper money, gunpowder, compass, movable type)."),
    ("How many Tang dynasty wooden buildings still exist?","Only 4 Tang wooden buildings survive in China: Nanchan Temple (782), Foguang East Hall (857), Tiantai Hermitage, and Guangrenwang Temple (831). All in Shanxi province."),
    ("Why are there so few Tang buildings left?","Timber burns. The An Lushan Rebellion (755-763), Huang Chao Rebellion (874-884), Buddhist persecution of 845, and repeated dynastic wars destroyed most Tang structures."),
    ("Is Tang Paradise in Xi'an original?","No. Built after 2000. It is a theme park. For real Tang Xi'an sites: Big Wild Goose Pagoda (Ming rebuild on Tang foundation) and the Shaanxi History Museum."),
    ("Where can I see the best Tang architecture?","In China: Foguang Temple and Nanchan Temple (both in Shanxi). Foguang East Hall is the largest Tang wooden structure still standing."),
    ("Is Qingming Riverside Garden worth visiting?","Only with family. It is a 1998 theme park with zero historical fabric. For real Song structures: Baoguo Temple (1013, Ningbo) or Iron Pagoda (1049, Kaifeng)."),
    ("How long should I plan for a Tang-Song trip?","Minimum 2 weeks for both trails. 8-10 days for Tang alone. 10-14 days for Song alone."),
    ("Are sites accessible without Chinese language skills?","Mixed. Xi'an and Hangzhou have good infrastructure. Shanxi mountain temples (Foguang, Nanchan) have almost no English signage and limited transit. Hire a guide or join a specialized tour."),
]
FLAG = {"CN":"cn","JP":"jp","TW":"tw","GB":"gb"}

def tag_badge(tag_key):
    t = TAG_DATA[tag_key]
    return '<span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded text-xs font-medium bg-{0}-bg text-{0}"><span class="tag-dot {0}"></span>{1}</span>'.format(t["css"], t["label"])

def site_card(s):
    t = TAG_DATA[s["tag"]]
    img = s.get("image","")
    h = '<article class="site-card overflow-hidden">'
    if img:
        h += '<img src="' + img + '" alt="' + s["name"] + '" class="w-full aspect-[16/9] object-cover" loading="lazy">'
    else:
        h += '<div class="image-slot w-full aspect-[4/3] bg-stone/[0.04] flex flex-col items-center justify-center gap-1.5 border-b border-rule">'
        h += '<svg class="w-8 h-8 text-stone/20" fill="none" stroke="currentColor" stroke-width="1" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg>'
        h += '<span class="text-[11px] text-stone/25 font-mono uppercase tracking-wide">' + s["name"] + '</span>'
        h += '</div>'
    h += '<div class="p-5 md:p-6">'
    h += '<div class="flex items-start justify-between gap-3 mb-3"><div>'
    h += tag_badge(s["tag"]) + '</div>'
    h += '<span class="text-xs text-stone font-mono">{0}</span></div>'.format(FLAG.get(s.get("country",""),""))
    h += '<h3 class="display text-xl mb-1">{0}</h3>'.format(s["name"])
    name_line = s["zh"] if s["zh"] == s["pinyin"] else '{0} &middot; {1}'.format(s["zh"], s["pinyin"])
    h += '<p class="text-sm text-stone mb-3">{0}</p>'.format(name_line)
    h += '<div class="flex flex-wrap gap-4 text-sm text-ink mb-4"><span><strong>Built:</strong> {0}</span><span><strong>Location:</strong> {1}, {2}</span></div>'.format(s["year"], s["city"], s["province"])
    h += '<p class="text-sm text-ink leading-relaxed mb-3"><strong>Why go:</strong> {0}</p>'.format(s["why"])
    h += '<div class="flex flex-wrap gap-4 text-sm text-ink mb-3"><span><strong>Admission:</strong> {0}</span><span><strong>Time:</strong> {1}</span></div>'.format(s["admission"], s["duration"])
    h += '<p class="text-sm text-stone border-l-2 border-vermillion pl-3 italic">Honest note: {0}</p>'.format(s["honest"])
    h += '<p class="text-xs text-stone mt-3 font-mono">Basis: {0}</p>'.format(s["basis"])
    h += '<div class="mt-4 pt-3 border-t border-rule"><a href="sites/{0}/" class="inline-flex items-center gap-1 text-sm text-vermillion font-medium hover:text-accent-hover transition">View Details <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a></div>'.format(s["id"])
    h += '</div></article>'
    return h
