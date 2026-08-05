# -*- coding: utf-8 -*-
import os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs('sites', exist_ok=True)
with open('gen.py','r',encoding='utf-8') as f:
    code = f.read()
ns = {'json':json}
exec(code[:code.find('\ndef tag_badge')], ns)
SITES = ns['SITES']; TAG_DATA = ns['TAG_DATA']; FLAG = ns['FLAG']
FLAG_EMOJI = {'CN':'&#x1f1e8;&#x1f1f3;','JP':'&#x1f1ef;&#x1f1f5;'}
DYN = {'tang':'Tang Dynasty','song':'Song Dynasty'}
GFONTS = 'https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&amp;family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400;1,500&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap'
CSS = 'html{scroll-behavior:smooth;scroll-padding-top:80px}h1,h2,h3,h4,.display{font-family:DM Serif Display,Georgia,serif}body{font-family:IBM Plex Sans,system-ui,sans-serif}.tag-dot{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:6px}.tag-green{background:#166534}.tag-yellow{background:#ca8a04}.tag-orange{background:#ea580c}.tag-red{background:#dc2626}.nav-link{position:relative}.nav-link::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:#b91c1c;transition:width .2s}.nav-link:hover::after{width:100%}'
print(f'Loaded {len(SITES)} sites, ready to generate')
