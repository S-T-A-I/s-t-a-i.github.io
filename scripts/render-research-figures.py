"""Draw the landing-page research diagrams as light and dark SVGs.

Usage: python3 scripts/render-research-figures.py static/img/research
The palette uses four site colours: ink, muted grey, orange and the logo purple.
"""
import os, sys
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
PAL = {
  'light': dict(ink='#38343F', mut='#B8B1C2', acc='#C2521C', sec='#A6249D'),
  'dark':  dict(ink='#D9D3E2', mut='#5C5468', acc='#FFA45C', sec='#D46BCB'),
}
HEAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 160" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="3">'
FIGS = {
'ai-safety': '''
<rect x="20" y="30" width="80" height="100" rx="8" stroke="{ink}"/>
<path d="M34 50h52M34 65h44M34 95h48M34 110h38" stroke="{mut}"/>
<path d="M34 80h52" stroke="{acc}" stroke-width="3.5"/>
<path d="M130 46v22M130 92v22" stroke="{sec}"/>
<circle cx="130" cy="20" r="7" stroke="{sec}"/>
<path d="M118 38c2-7 7-10 12-10s10 3 12 10" stroke="{sec}"/>
<path d="M96 80h56M146 74l7 6-7 6" stroke="{acc}" stroke-width="3.5"/>
<rect x="160" y="50" width="60" height="60" rx="8" stroke="{ink}"/>
<path d="M172 80h36" stroke="{acc}" stroke-width="3.5"/>''',
'agents': '''
<circle cx="36" cy="58" r="16" stroke="{ink}"/>
<circle cx="92" cy="58" r="16" stroke="{ink}"/>
<circle cx="148" cy="58" r="16" stroke="{acc}" stroke-width="3.5"/>
<circle cx="204" cy="58" r="16" stroke="{ink}"/>
<path d="M52 58h18M65 53l5 5-5 5M108 58h18M121 53l5 5-5 5M164 58h18M177 53l5 5-5 5" stroke="{ink}"/>
<circle cx="36" cy="58" r="4" fill="{ink}" stroke="none"/>
<circle cx="92" cy="58" r="4" fill="{ink}" stroke="none"/>
<circle cx="204" cy="58" r="4" fill="{ink}" stroke="none"/>
<path d="M142 52l12 12M154 52l-12 12" stroke="{acc}" stroke-width="3.5"/>
<path d="M36 74v40M92 74v40M204 74v40M24 114h192" stroke="{mut}" stroke-dasharray="4 6"/>
<path d="M148 74v28" stroke="{sec}"/>
<circle cx="148" cy="114" r="11" stroke="{sec}"/>
<path d="M156 122l9 9" stroke="{sec}"/>''',
'memory': '''
<rect x="18" y="52" width="56" height="56" rx="10" stroke="{ink}"/>
<circle cx="34" cy="68" r="3" fill="{ink}" stroke="none"/><circle cx="46" cy="68" r="3" fill="{ink}" stroke="none"/><circle cx="58" cy="68" r="3" fill="{ink}" stroke="none"/>
<circle cx="34" cy="80" r="3" fill="{ink}" stroke="none"/><circle cx="46" cy="80" r="3" fill="{ink}" stroke="none"/><circle cx="58" cy="80" r="3" fill="{ink}" stroke="none"/>
<circle cx="34" cy="92" r="3" fill="{ink}" stroke="none"/><circle cx="46" cy="92" r="3" fill="{ink}" stroke="none"/><circle cx="58" cy="92" r="3" fill="{ink}" stroke="none"/>
<path d="M80 80h24M86 74l-6 6 6 6M98 74l6 6-6 6" stroke="{ink}"/>
<rect x="110" y="44" width="66" height="24" rx="6" stroke="{acc}" stroke-width="3.5"/>
<path d="M120 56h46" stroke="{acc}" stroke-width="3.5"/>
<rect x="110" y="76" width="66" height="24" rx="6" stroke="{ink}"/>
<path d="M120 88h38" stroke="{mut}"/>
<rect x="110" y="108" width="66" height="24" rx="6" stroke="{ink}"/>
<path d="M120 120h42" stroke="{mut}"/>
<circle cx="214" cy="30" r="7" stroke="{sec}"/>
<path d="M202 48c2-7 7-10 12-10s10 3 12 10" stroke="{sec}"/>
<path d="M214 56c0 4-10 0-30 0M190 50l-6 6 6 6" stroke="{sec}"/>''',
'retrieval': '''
<rect x="18" y="22" width="72" height="52" rx="6" stroke="{ink}"/>
<path d="M30 38h48M30 62h36" stroke="{mut}"/>
<path d="M30 50h48" stroke="{acc}" stroke-width="3.5"/>
<rect x="18" y="88" width="72" height="50" rx="6" stroke="{ink}"/>
<path d="M26 128l18-18 12 11 10-9 16 16" stroke="{sec}"/>
<circle cx="72" cy="101" r="4" stroke="{sec}"/>
<rect x="150" y="50" width="72" height="60" rx="6" stroke="{ink}"/>
<path d="M162 68h48M162 92h32" stroke="{mut}"/>
<path d="M162 80h48" stroke="{acc}" stroke-width="3.5"/>
<path d="M90 50c30 0 32 30 60 30" stroke="{acc}" stroke-width="3.5"/>
<path d="M90 113c30 0 32-21 60-21" stroke="{sec}" stroke-dasharray="5 6"/>''',
}
for name, body in FIGS.items():
    for mode, pal in PAL.items():
        open(f'{out}/{name}-{mode}.svg', 'w').write(HEAD + body.format(**pal) + '\n</svg>\n')
print(sorted(os.listdir(out)))
