#!/usr/bin/env python3
"""Locked reusable visual templates (captions, index, notebook, hands, board pictograms)
for the classroom-chalkboard-explainer skill. Keep styling constants identical to classroom_lib.py."""
import os, re, math
from classroom_lib import OUT, W, H, DARK, Y, P, B, Wt, FONTS_CSS, line

# Locked chalk hand outline for board diagrams
CHALK_HAND = (
    'M184 480 L176 346 C175 326 196 324 198 344 L203 398 '
    'L204 316 C205 296 226 296 228 316 L231 392 '
    'L235 306 C237 286 258 288 259 308 L260 392 '
    'L266 322 C269 304 288 308 287 328 L280 412 '
    'C294 388 312 394 310 418 C308 446 284 468 272 486 L270 500'
)


def sun_svg(cx, cy, r=26):
    rays = "".join(
        f'<line x1="{cx+(r+6)*math.sin(math.radians(a)):.1f}" y1="{cy-(r+6)*math.cos(math.radians(a)):.1f}" '
        f'x2="{cx+(r+16)*math.sin(math.radians(a)):.1f}" y2="{cy-(r+16)*math.cos(math.radians(a)):.1f}" '
        f'stroke="{Y}" stroke-width="3.2" stroke-linecap="round"/>'
        for a in range(0, 360, 30)
    )
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{Y}" stroke-width="3.6"/>{rays}'


def moon_svg(cx, cy):
    return (
        f'<path d="M{cx+14} {cy-24} A26 26 0 1 0 {cx+14} {cy+24} '
        f'A20 20 0 1 1 {cx+14} {cy-24} Z" fill="none" stroke="{B}" stroke-width="3.4" stroke-linejoin="round"/>'
    )


def star_svg(x, y, col=Wt, r=10.5):
    pts = " ".join(
        f"{x + (r if k%2==0 else r*0.44)*math.sin(math.radians(k*36)):.1f},"
        f"{y - (r if k%2==0 else r*0.44)*math.cos(math.radians(k*36)):.1f}"
        for k in range(10)
    )
    return f'<polygon points="{pts}" fill="none" stroke="{col}" stroke-width="2.4" stroke-linejoin="round"/>'


def brick_pyr(x0, x1, yb, yt, elem_id):
    xm = (x0 + x1) / 2
    segs = [f"M{x0} {yb} L{xm:.0f} {yt} L{x1} {yb} Z", f"M{xm:.0f} {yt} L{xm+10:.0f} {yb}"]
    for frac in (0.33, 0.66):
        yy = yb - (yb - yt) * frac
        lx = x0 + (xm - x0) * frac
        rx = x1 - (x1 - xm) * frac
        segs.append(f"M{lx:.0f} {yy:.0f} L{rx:.0f} {yy:.0f}")
    return line(elem_id, " ".join(segs), Wt, 2.8)


def build_captions(caps, climax_html=None, climax_start=None, climax_dur=1.1, out_dir=None):
    """Build locked TikTok/Reels-style caption pill layer (compositions/caps.html).
    Each entry in caps: (start_sec, end_sec, "plain [highlighted] text").
    """
    out_dir = out_dir or OUT
    divs, js = [], []
    for i, (a, b, txt) in enumerate(caps):
        html = re.sub(r"\[(.+?)\]", r"<em>\1</em>", txt)
        divs.append(
            f'<div id="cp{i}" class="cap clip" data-start="{a}" data-duration="{b-a:.3f}">'
            f'<span class="pill">{html}</span></div>'
        )
        js.append(
            f'tl.fromTo("#cp{i}",{{opacity:0,y:8,scale:0.94}},{{opacity:1,y:0,scale:1,duration:0.09,ease:"back.out(2)"}},{a});'
        )
    if climax_html and climax_start is not None:
        divs.append(
            f'<div id="capbig" class="clip" data-start="{climax_start}" data-duration="{climax_dur}">{climax_html}</div>'
        )
        js.append(
            f'tl.fromTo("#capbig",{{opacity:0,scale:0.55}},{{opacity:1,scale:1,duration:0.28,ease:"back.out(2.2)"}},{climax_start});'
        )
    html = f'''<template>
  <style>
    {FONTS_CSS}
    #root {{ position:absolute; inset:0; }}
    .cap {{ position:absolute; left:0; right:0; top:1042px; text-align:center; opacity:0; }}
    .cap .pill {{ display:inline-block; padding:8px 24px 10px; border-radius:18px; background:#1F1812;
      font-family:'Fredoka'; font-weight:700; font-size:35px; line-height:1.1; color:#FFFFFF; letter-spacing:0.01em; }}
    .cap em, #capbig em {{ font-style:normal; color:#F2D45C; }}
    #capbig {{ position:absolute; left:0; right:0; top:780px; text-align:center; opacity:0;
      font-family:'Fredoka'; font-weight:700; font-size:66px; line-height:1; white-space:nowrap;
      color:#FFFFFF; -webkit-text-stroke:12px #2B1C14; paint-order:stroke fill; }}
  </style>
  <div id="root" data-composition-id="caps" data-width="{W}" data-height="{H}">
    {"".join(divs)}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join(js)}
    window.__timelines["caps"] = tl;
  </script>
</template>
'''
    open(os.path.join(out_dir, "caps.html"), "w").write(html)


def build_notebook_scene(cid, start, end, header_lines, strokes, circle_spec=None, out_dir=None):
    """Build locked tilted ruled notebook scene with animated cartoon hand holding a yellow pencil.
    header_lines: list of (text, y) pre-written at top of page.
    strokes: list of (text, x, y, size, color, global_t0, duration, clip_width).
    circle_spec: optional (cx, cy, rx, ry, color, global_t0, duration) drawn around answer.
    """
    out_dir = out_dir or OUT
    o = start
    t = lambda g: round(max(0.0, g - o), 3)
    wood_lines = "".join(
        f'<line x1="0" y1="{y}" x2="720" y2="{y+(6 if (y//110)%2 else -5)}" stroke="#D6A262" stroke-width="3.5"/>'
        for y in range(60, 1280, 110)
    )
    bg = f'<rect width="720" height="1280" fill="#E8B879"/>{wood_lines}'
    rules = "".join(f'<line x1="42" y1="{y}" x2="674" y2="{y}" stroke="#A9D2EE" stroke-width="2.2"/>' for y in range(195, 1105, 45))
    holes = "".join(f'<circle cx="78" cy="{y}" r="14" fill="#E6B472" stroke="{DARK}" stroke-width="3.8"/>' for y in (306, 628, 950))
    headers = "".join(
        f'<text x="186" y="{hy}" font-family="Caveat Brush" font-size="56" fill="#3B424D">{ht}</text>'
        for ht, hy in header_lines
    )
    paper = (
        f'<g transform="rotate(-1.2 360 618)">'
        f'<rect x="48" y="114" width="632" height="1014" rx="8" fill="{DARK}" opacity="0.85"/>'
        f'<rect x="42" y="108" width="632" height="1014" rx="8" fill="#FAF8F0" stroke="{DARK}" stroke-width="5"/>'
        f'{rules}<line x1="138" y1="110" x2="138" y2="1120" stroke="#F0A0B2" stroke-width="3.2"/>{holes}{headers}'
    )
    items, clips, js = [], [], []
    pts = [(start, 620, 820)]
    for k, (txt, x, y, sz, col, t0, d, w) in enumerate(strokes):
        clips.append(f'<clipPath id="{cid}-c{k}"><rect id="{cid}-cr{k}" x="{x-8}" y="{y-sz*1.1:.0f}" width="0" height="{sz*1.4:.0f}"/></clipPath>')
        items.append(f'<g clip-path="url(#{cid}-c{k})"><text x="{x}" y="{y}" font-family="Caveat Brush" font-size="{sz}" fill="{col}">{txt}</text></g>')
        js.append(f'tl.fromTo("#{cid}-cr{k}",{{attr:{{width:0}}}},{{attr:{{width:{w}}},duration:{d},ease:"none"}},{t(t0)});')
        pts.append((t0, x + 6, y - 18))
        pts.append((t0 + d, x + min(w, len(txt) * sz * 0.52), y - 18))
    circ = ""
    if circle_spec:
        cx, cy, rx, ry, ccol, ct0, cd = circle_spec
        circ = (
            f'<ellipse id="{cid}-ring" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{ccol}" '
            f'stroke-width="6.5" stroke-linecap="round" pathLength="1" stroke-dasharray="1 1.2" '
            f'stroke-dashoffset="1.1" transform="rotate(-4 {cx} {cy})"/>'
        )
        js.append(f'tl.fromTo("#{cid}-ring",{{attr:{{"stroke-dashoffset":1.1}}}},{{attr:{{"stroke-dashoffset":0}},duration:{cd},ease:"power1.inOut"}},{t(ct0)});')
        pts.append((ct0, cx - rx + 10, cy))
        pts.append((ct0 + cd * 0.5, cx, cy - ry))
        pts.append((ct0 + cd, cx + rx, cy + 12))
    pts.append((end - 0.02, 560, 760))

    pen = (
        f'<g id="{cid}-penhand">'
        f'<g transform="rotate(42)">'
        f'<rect x="34" y="-42" width="520" height="92" rx="46" fill="#FFFFFF" stroke="{DARK}" stroke-width="5.5"/>'
        f'<rect x="26" y="-26" width="108" height="60" rx="30" fill="#E3B188"/>'
        f'</g>'
        f'<g transform="rotate(-24)">'
        f'<polygon points="0,0 24,-9 24,9" fill="#F2D9B1" stroke="{DARK}" stroke-width="3.5" stroke-linejoin="round"/>'
        f'<polygon points="0,0 10,-4 10,4" fill="#3B424D"/>'
        f'<rect x="24" y="-9" width="96" height="18" fill="#F2D25B" stroke="{DARK}" stroke-width="3.5"/>'
        f'<rect x="120" y="-9" width="16" height="18" rx="3" fill="#F29AB0" stroke="{DARK}" stroke-width="3.5"/>'
        f'</g>'
        f'<circle cx="42" cy="18" r="34" fill="#E3B188" stroke="{DARK}" stroke-width="4.5"/>'
        f'<circle cx="24" cy="4" r="14" fill="#E3B188" stroke="{DARK}" stroke-width="4"/>'
        f'<path d="M26 28 Q46 42 64 26" fill="none" stroke="{DARK}" stroke-width="3.5" stroke-linecap="round"/>'
        f'</g>'
    )
    js.append(f'tl.set("#{cid}-penhand",{{x:{pts[0][1]:.0f},y:{pts[0][2]:.0f}}},0);')
    for k in range(1, len(pts)):
        t_prev = pts[k - 1][0]
        t_cur, x, y = pts[k]
        if t_cur <= t_prev + 0.02:
            continue
        dur = max(0.03, round(t_cur - t_prev - 0.01, 3))
        js.append(f'tl.to("#{cid}-penhand",{{x:{x:.0f},y:{y:.0f},duration:{dur},ease:"power1.inOut"}},{t(t_prev)});')

    html = f'''<template>
  <style>
    {FONTS_CSS}
    #root {{ position:absolute; inset:0; overflow:hidden; background:#E8B879; }}
    #root svg {{ position:absolute; inset:0; width:100%; height:100%; }}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H}">
    <svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
      <defs>{"".join(clips)}</defs>
      {bg}{paper}{"".join(items)}{circ}</g>{pen}
    </svg>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join(js)}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
'''
    open(os.path.join(out_dir, f"{cid}.html"), "w").write(html)


def build_index(scenes_order, total_duration, fps=30, audio_src=None, out_path="index.html"):
    """Build locked root composition index.html (720x1280, graphics + captions + optional audio)."""
    hosts = "\n".join(
        f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" '
        f'data-start="{a}" data-duration="{b-a:.3f}" data-track-index="1" data-track-kind="graphics" '
        f'data-width="{W}" data-height="{H}"></div>'
        for cid, a, b in scenes_order
    )
    audio_tag = (
        f'\n      <audio id="orig-audio" src="{audio_src}" data-start="0" data-duration="{total_duration}"></audio>'
        if audio_src else ""
    )
    html = f'''<!doctype html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      html, body {{ margin:0; width:{W}px; height:{H}px; overflow:hidden; background:#F3E4CA; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total_duration}" data-width="{W}" data-height="{H}" data-fps="{fps}">
{hosts}
      <div id="caps" data-composition-id="caps" data-composition-src="compositions/caps.html" data-start="0" data-duration="{total_duration}" data-track-index="2" data-track-kind="captions" data-width="{W}" data-height="{H}"></div>{audio_tag}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
'''
    open(out_path, "w").write(html)
