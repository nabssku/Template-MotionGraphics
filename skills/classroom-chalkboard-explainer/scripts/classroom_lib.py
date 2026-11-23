#!/usr/bin/env python3
"""Unified classroom stage & animation helpers matching galeri-mograph-papan.mp4."""
import os, math, re

W, H = 720, 1280
DARK = "#3A2418"
Y, P, B, Wt = "#F2D45C", "#F29AB0", "#8FD0F0", "#FFFFFF"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "compositions")
os.makedirs(OUT, exist_ok=True)

# Unified chalkboard interior coordinates in wide-stage space (720x1280):
# Board outer frame: x=116..534 (cx=325, w=418), y=140..616 (cy=378, h=476)
# Slate interior:    x=130..520 (cx=325, w=390), y=154..600 (cy=377, h=446)
BX, BY, BW, BH = 130, 154, 390, 446
BCX, BCY = 325, 377

# Camera presets (scale, focus_x, focus_y):
CAM_WIDE = (1.0, 360, 640)
CAM_BOARD = (1.66, 325, 412)       # exact board close-up matching f_28.0.png
CAM_CLOCK = (2.8, 325, 130)        # intro zoom on wall clock
CAM_RIGHT_MED = (1.32, 428, 535)   # board + teacher + right students (sheet_1, sheet_17)
CAM_TEACHER = (1.66, 515, 445)     # pan right to teacher beside board (f_36.2.png, sheet_4)
CAM_BOY_MID = (2.35, 324, 920)     # center boy 10 fingers close-up (sheet_3)
CAM_GIRL = (2.35, 135, 935)        # left girl close-up (sheet_9)

FONTS_CSS = """
    @font-face { font-family:'Caveat Brush'; src:url('assets/fonts/caveat-brush.ttf'); font-weight:400; }
    @font-face { font-family:'Fredoka'; src:url('assets/fonts/fredoka.ttf'); font-weight:400 700; }
"""


def defs(p):
    return f'''
<defs>
  <pattern id="{p}-batik" width="24" height="24" patternUnits="userSpaceOnUse">
    <rect width="24" height="24" fill="#7D421A"/>
    <ellipse cx="12" cy="6" rx="4.2" ry="6.2" fill="#E8B870" opacity="0.92"/>
    <ellipse cx="12" cy="18" rx="4.2" ry="6.2" fill="#E8B870" opacity="0.92"/>
    <ellipse cx="6" cy="12" rx="6.2" ry="4.2" fill="#E8B870" opacity="0.92"/>
    <ellipse cx="18" cy="12" rx="6.2" ry="4.2" fill="#E8B870" opacity="0.92"/>
    <circle cx="12" cy="12" r="4.8" fill="#7D421A"/>
    <circle cx="12" cy="12" r="2.2" fill="#F2CC86"/>
    <circle cx="0" cy="0" r="2.6" fill="#5D2E10"/><circle cx="24" cy="0" r="2.6" fill="#5D2E10"/>
    <circle cx="0" cy="24" r="2.6" fill="#5D2E10"/><circle cx="24" cy="24" r="2.6" fill="#5D2E10"/>
  </pattern>
  <pattern id="{p}-hatchY" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
    <rect width="8" height="8" fill="#F2D45C" fill-opacity="0.14"/>
    <rect width="3.5" height="8" fill="#F2D45C" fill-opacity="0.88"/>
  </pattern>
  <pattern id="{p}-hatchP" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
    <rect width="8" height="8" fill="#F29AB0" fill-opacity="0.14"/>
    <rect width="3.5" height="8" fill="#F29AB0" fill-opacity="0.88"/>
  </pattern>
  <pattern id="{p}-hatchB" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
    <rect width="7" height="7" fill="#8FD0F0" fill-opacity="0.14"/>
    <rect width="3" height="7" fill="#8FD0F0" fill-opacity="0.85"/>
  </pattern>
  <filter id="{p}-chalk" x="-6%" y="-6%" width="112%" height="112%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="7" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="1.9" result="d"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 5 -1.4" result="mask"/>
    <feComposite in="d" in2="mask" operator="in"/>
  </filter>
  <clipPath id="{p}-board-clip"><rect x="{BX}" y="{BY}" width="{BW}" height="{BH}"/></clipPath>
</defs>'''


def bunting():
    # Two curved garlands left (0..265) and right (385..730), arching gently around the wall clock at x=325
    out = []
    for x0, x1, dip in [(-14, 264, 18), (386, 734, 20)]:
        span = x1 - x0
        out.append(f'<path d="M{x0} 0 Q{(x0+x1)/2:.0f} {dip*2:.0f} {x1} 0" stroke="#7A5B42" stroke-width="2.2" fill="none"/>')
        n = 0
        x = x0
        step = 26
        while x < x1 - 6:
            xm = x + step / 2
            t1 = max(0, min(1, (x - x0) / span))
            t2 = max(0, min(1, (x + step - x0) / span))
            y1 = 4 * dip * t1 * (1 - t1)
            y2 = 4 * dip * t2 * (1 - t2)
            ym = (y1 + y2) / 2
            col = "#C81E2B" if n % 2 == 0 else "#FFFFFF"
            out.append(f'<polygon points="{x:.1f},{y1:.1f} {x+step-2:.1f},{y2:.1f} {xm:.1f},{ym+36:.1f}" fill="{col}" stroke="{DARK}" stroke-width="2.2" stroke-linejoin="round"/>')
            x += step
            n += 1
    return "\n".join(out)


def classroom(p):
    # Clock ticks around (325, 84) r=37
    cticks = []
    for k in range(12):
        a = math.radians(k * 30)
        r1 = 26 if k % 3 == 0 else 29
        r2 = 34
        sw = 2.6 if k % 3 == 0 else 1.7
        cticks.append(f'<line x1="{325+r1*math.sin(a):.1f}" y1="{84-r1*math.cos(a):.1f}" x2="{325+r2*math.sin(a):.1f}" y2="{84-r2*math.cos(a):.1f}" stroke="{DARK}" stroke-width="{sw}" stroke-linecap="round"/>')
    planks = "".join(f'<line x1="0" y1="{y}" x2="720" y2="{y}" stroke="#B67E46" stroke-width="2.5" opacity="0.72"/>' for y in range(848, 1280, 68))
    return f'''
<!-- Wall, wainscoting & wooden floor -->
<rect x="-120" y="-120" width="960" height="824" fill="#F3E4CA"/>
<rect x="-120" y="704" width="960" height="76" fill="#DFC9A3"/>
<rect x="-120" y="702" width="960" height="7" fill="#CEB68E"/>
<rect x="-120" y="780" width="960" height="620" fill="#CF965C"/>
<line x1="-120" y1="780" x2="840" y2="780" stroke="{DARK}" stroke-width="3.2"/>
<g>{planks}</g>

<!-- Bunting -->
{bunting()}

<!-- School bell (top left) -->
<g id="{p}-bell">
  <rect x="12" y="106" width="12" height="10" rx="2" fill="#8A5530" stroke="{DARK}" stroke-width="2.5"/>
  <circle cx="18" cy="158" r="6" fill="#D49A3A" stroke="{DARK}" stroke-width="2.5"/>
  <path d="M-8 154 C-6 126 4 116 18 116 C32 116 42 126 44 154 L48 156 L-12 156 Z" fill="#F2D25B" stroke="{DARK}" stroke-width="2.8" stroke-linejoin="round"/>
  <g id="{p}-bell-ring" opacity="0">
    <path d="M54 128 Q62 138 54 148" fill="none" stroke="{DARK}" stroke-width="2.8" stroke-linecap="round"/>
    <path d="M64 122 Q74 138 64 154" fill="none" stroke="{DARK}" stroke-width="2.8" stroke-linecap="round"/>
  </g>
</g>

<!-- Window (left wall) -->
<g id="{p}-win">
  <rect x="-8" y="214" width="78" height="238" fill="#FFFFFF" stroke="{DARK}" stroke-width="3"/>
  <rect x="-2" y="220" width="66" height="226" fill="#8DCBF0" stroke="{DARK}" stroke-width="2"/>
  <path d="M-2 292 Q14 274 30 282 Q44 276 54 290 L54 296 L-2 296 Z" fill="#FFFFFF" opacity="0.92"/>
  <circle cx="-2" cy="426" r="34" fill="#60A84E" stroke="{DARK}" stroke-width="2.6"/>
  <circle cx="50" cy="448" r="34" fill="#60A84E" stroke="{DARK}" stroke-width="2.6"/>
  <rect x="16" y="218" width="6" height="230" fill="#FFFFFF"/>
  <rect x="-4" y="324" width="70" height="6" fill="#FFFFFF"/>
  <rect x="-10" y="446" width="84" height="9" rx="2" fill="#FFFFFF" stroke="{DARK}" stroke-width="2.5"/>
</g>

<!-- Wall clock centered at (325, 84) -->
<g id="{p}-clock-gold" opacity="0">
  {"".join(f'<line x1="{325+48*math.sin(math.radians(a)):.1f}" y1="{84-48*math.cos(math.radians(a)):.1f}" x2="{325+64*math.sin(math.radians(a)):.1f}" y2="{84-64*math.cos(math.radians(a)):.1f}" stroke="#E6A92E" stroke-width="5" stroke-linecap="round"/>' for a in range(0, 360, 30))}
  <circle cx="325" cy="84" r="49" fill="none" stroke="#F2D25B" stroke-width="7"/>
</g>
<g id="{p}-clock">
  <circle cx="325" cy="84" r="43" fill="#FFFFFF" stroke="#C81E2B" stroke-width="8"/>
  <circle cx="325" cy="84" r="46" fill="none" stroke="{DARK}" stroke-width="2.6"/>
  <circle cx="325" cy="84" r="38" fill="none" stroke="{DARK}" stroke-width="1.6"/>
  {"".join(cticks)}
  <line x1="325" y1="84" x2="325" y2="62" stroke="{DARK}" stroke-width="4" stroke-linecap="round" transform="rotate(-62 325 84)"/>
  <line x1="325" y1="84" x2="325" y2="56" stroke="{DARK}" stroke-width="3.2" stroke-linecap="round" transform="rotate(62 325 84)"/>
  <g id="{p}-sh"><line x1="325" y1="93" x2="325" y2="52" stroke="#C81E2B" stroke-width="2" stroke-linecap="round"/></g>
  <circle cx="325" cy="84" r="3.4" fill="{DARK}"/>
</g>

<!-- Chalkboard centered at x=325 -->
<g id="{p}-board">
  <rect x="116" y="140" width="418" height="476" rx="4" fill="#9A6035" stroke="{DARK}" stroke-width="3.2"/>
  <rect x="{BX}" y="{BY}" width="{BW}" height="{BH}" fill="#2D6C50" stroke="{DARK}" stroke-width="2.4"/>
  <!-- Diagonal chalk glare -->
  <polygon points="310,154 388,154 228,600 156,600" fill="#FFFFFF" opacity="0.06"/>
  <polygon points="418,154 456,154 296,600 260,600" fill="#FFFFFF" opacity="0.055"/>
  <!-- Chalk tray -->
  <rect x="108" y="608" width="434" height="14" rx="3" fill="#A66A3E" stroke="{DARK}" stroke-width="2.8"/>
  <rect x="160" y="602" width="18" height="6" rx="2.5" fill="#FFFFFF" stroke="{DARK}" stroke-width="1.6"/>
  <rect x="184" y="602" width="18" height="6" rx="2.5" fill="{Y}" stroke="{DARK}" stroke-width="1.6"/>
  <rect x="204" y="602" width="18" height="6" rx="2.5" fill="{P}" stroke="{DARK}" stroke-width="1.6"/>
  <rect x="224" y="602" width="18" height="6" rx="2.5" fill="{B}" stroke="{DARK}" stroke-width="1.6"/>
  <!-- Resting eraser on tray -->
  <g id="{p}-tray-er">
    <rect x="420" y="591" width="66" height="18" rx="4" fill="#7D756D" stroke="{DARK}" stroke-width="2.4"/>
    <rect x="420" y="587" width="66" height="13" rx="4" fill="#A66A3E" stroke="{DARK}" stroke-width="2.4"/>
  </g>
</g>

<!-- Teacher desk centered at x=325 -->
<g id="{p}-tdesk">
  <rect x="196" y="702" width="258" height="116" fill="#D6A064" stroke="{DARK}" stroke-width="2.8"/>
  <rect x="188" y="688" width="274" height="16" rx="3" fill="#E4B074" stroke="{DARK}" stroke-width="2.8"/>
  <rect x="276" y="734" width="96" height="28" rx="2" fill="#E4B074" stroke="{DARK}" stroke-width="2.4"/>
  <!-- 3 stacked books -->
  <rect x="224" y="672" width="68" height="16" rx="2" fill="#2F7A4D" stroke="{DARK}" stroke-width="2.2"/>
  <rect x="227" y="657" width="62" height="15" rx="2" fill="#C81E2B" stroke="{DARK}" stroke-width="2.2"/>
  <rect x="226" y="643" width="64" height="14" rx="2" fill="{Y}" stroke="{DARK}" stroke-width="2.2"/>
  <!-- Apple -->
  <circle cx="348" cy="674" r="14" fill="#C81E2B" stroke="{DARK}" stroke-width="2.2"/>
  <path d="M348 660 Q351 653 356 652" fill="none" stroke="{DARK}" stroke-width="2.4" stroke-linecap="round"/>
  <!-- Pencil cup -->
  <line x1="392" y1="654" x2="389" y2="632" stroke="{Y}" stroke-width="5" stroke-linecap="round"/>
  <line x1="402" y1="654" x2="406" y2="634" stroke="#C81E2B" stroke-width="5" stroke-linecap="round"/>
  <rect x="384" y="652" width="25" height="36" rx="2" fill="#8DCBF0" stroke="{DARK}" stroke-width="2.2"/>
</g>'''


def teacher(p):
    # Teacher stands cleanly to the right of the chalkboard at cx=632!
    # Right shoulder (viewer's left) at (566, 488)
    return f'''
<g id="{p}-teacher">
  <!-- Shoes -->
  <ellipse cx="607" cy="788" rx="25" ry="10" fill="#2B211B"/>
  <ellipse cx="655" cy="788" rx="25" ry="10" fill="#2B211B"/>
  <!-- Pants -->
  <rect x="595" y="640" width="31" height="146" fill="#45505E" stroke="{DARK}" stroke-width="2.8"/>
  <rect x="634" y="640" width="31" height="146" fill="#45505E" stroke="{DARK}" stroke-width="2.8"/>

  <!-- Left arm (viewer's right): resting/waving vs raised in shock -->
  <g id="{p}-t-larm-rest">
    <path d="M694 484 L732 524 L710 584" fill="none" stroke="{DARK}" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M694 484 L732 524 L710 584" fill="none" stroke="url(#{p}-batik)" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="708" cy="588" r="11" fill="#E7B080" stroke="{DARK}" stroke-width="2.6"/>
  </g>
  <g id="{p}-t-larm-up" opacity="0">
    <path d="M694 484 L728 456 L706 402" fill="none" stroke="{DARK}" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M694 484 L728 456 L706 402" fill="none" stroke="url(#{p}-batik)" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="703" cy="396" r="12" fill="#E7B080" stroke="{DARK}" stroke-width="2.6"/>
  </g>

  <!-- Batik shirt body -->
  <rect x="564" y="470" width="134" height="174" rx="14" fill="url(#{p}-batik)" stroke="{DARK}" stroke-width="2.8"/>
  <!-- Neck & Collar -->
  <rect x="617" y="450" width="28" height="26" rx="8" fill="#E7B080" stroke="{DARK}" stroke-width="2.6"/>
  <polygon points="604,470 631,494 658,470 644,466 631,480 618,466" fill="#8A4B22" stroke="{DARK}" stroke-width="2.4" stroke-linejoin="round"/>
  <circle cx="631" cy="522" r="3.4" fill="#FFFFFF" stroke="{DARK}" stroke-width="1.5"/>
  <circle cx="631" cy="560" r="3.4" fill="#FFFFFF" stroke="{DARK}" stroke-width="1.5"/>
  <circle cx="631" cy="598" r="3.4" fill="#FFFFFF" stroke="{DARK}" stroke-width="1.5"/>

  <!-- Head -->
  <g id="{p}-thead">
    <circle cx="582" cy="414" r="9" fill="#E7B080" stroke="{DARK}" stroke-width="2.6"/>
    <circle cx="682" cy="414" r="9" fill="#E7B080" stroke="{DARK}" stroke-width="2.6"/>
    <ellipse cx="632" cy="408" rx="48" ry="46" fill="#E7B080" stroke="{DARK}" stroke-width="2.8"/>
    <!-- Hair -->
    <path d="M584 402 C583 356 608 352 632 352 C658 352 681 362 680 402 C670 384 648 378 630 378 C610 378 594 388 584 402 Z" fill="#2E1E16" stroke="{DARK}" stroke-width="2.4"/>
    <!-- Blush -->
    <ellipse cx="601" cy="426" rx="9" ry="5.5" fill="#F29AB0" opacity="0.55"/>
    <ellipse cx="663" cy="426" rx="9" ry="5.5" fill="#F29AB0" opacity="0.55"/>
    <!-- Eyebrows -->
    <path d="M602 390 Q611 384 620 390" fill="none" stroke="#2E1E16" stroke-width="2.4" stroke-linecap="round"/>
    <path d="M644 390 Q653 384 662 390" fill="none" stroke="#2E1E16" stroke-width="2.4" stroke-linecap="round"/>
    <!-- Eyes (warm, normal size) -->
    <circle cx="611" cy="410" r="4.4" fill="#2E1E16"/><circle cx="612.5" cy="408.5" r="1.4" fill="#FFFFFF"/>
    <circle cx="653" cy="410" r="4.4" fill="#2E1E16"/><circle cx="654.5" cy="408.5" r="1.4" fill="#FFFFFF"/>
    <!-- Clear round glasses (NO white fog!) -->
    <circle cx="611" cy="410" r="15.5" fill="none" stroke="#2E1E16" stroke-width="2.8"/>
    <circle cx="653" cy="410" r="15.5" fill="none" stroke="#2E1E16" stroke-width="2.8"/>
    <line x1="626.5" y1="410" x2="637.5" y2="410" stroke="#2E1E16" stroke-width="2.8"/>
    <line x1="585" y1="408" x2="595.5" y2="410" stroke="#2E1E16" stroke-width="2.4"/>
    <line x1="668.5" y1="410" x2="679" y2="408" stroke="#2E1E16" stroke-width="2.4"/>
    <!-- Nose & moustache -->
    <path d="M631 416 Q635 421 631 424" fill="none" stroke="#B67C52" stroke-width="2" stroke-linecap="round"/>
    <path d="M616 430 Q632 422 648 430 Q632 436 616 430 Z" fill="#2E1E16"/>
    <!-- Mouths: happy open smile (m1), talking/O (m2), closed smile (m3) -->
    <g id="{p}-t-m1">
      <path d="M620 434 Q632 434 644 434 Q642 448 632 448 Q622 448 620 434 Z" fill="#8A2B26" stroke="{DARK}" stroke-width="2"/>
      <ellipse cx="632" cy="444" rx="6" ry="3" fill="#D65A54"/>
    </g>
    <g id="{p}-t-m2" opacity="0">
      <ellipse cx="632" cy="440" rx="7.5" ry="9" fill="#8A2B26" stroke="{DARK}" stroke-width="2"/>
      <ellipse cx="632" cy="445" rx="4.5" ry="3" fill="#D65A54"/>
    </g>
    <path id="{p}-t-m3" d="M622 438 Q632 444 642 438" fill="none" stroke="{DARK}" stroke-width="2.6" stroke-linecap="round" opacity="0"/>
  </g>

  <!-- Right arm (viewer's left) resting with vertical pointer stick on floor -->
  <g id="{p}-t-rarm-rest">
    <line x1="556" y1="620" x2="564" y2="792" stroke="{DARK}" stroke-width="10" stroke-linecap="round"/>
    <line x1="556" y1="620" x2="564" y2="792" stroke="#D7AE74" stroke-width="5.5" stroke-linecap="round"/>
    <circle cx="564" cy="792" r="3.5" fill="#C81E2B"/>
    <path d="M566 484 L554 548 L556 614" fill="none" stroke="{DARK}" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M566 484 L554 548 L556 614" fill="none" stroke="url(#{p}-batik)" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="556" cy="616" r="11.5" fill="#E7B080" stroke="{DARK}" stroke-width="2.6"/>
  </g>

  <!-- Active pointing arm + pointer stick (pivots cleanly from hand/shoulder to point at board!) -->
  <g id="{p}-t-rarm-point" opacity="0">
    <!-- Arm from shoulder (566,488) reaching left to hand at (520,510) and stick pointing straight left along -X -->
    <g id="{p}-tarm">
      <line x1="335" y1="488" x2="516" y2="488" stroke="{DARK}" stroke-width="9.5" stroke-linecap="round"/>
      <line x1="335" y1="488" x2="516" y2="488" stroke="#D7AE74" stroke-width="5" stroke-linecap="round"/>
      <circle cx="335" cy="488" r="3.8" fill="#C81E2B"/>
      <path d="M566 488 L544 516 L516 488" fill="none" stroke="{DARK}" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M566 488 L544 516 L516 488" fill="none" stroke="url(#{p}-batik)" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="516" cy="488" r="11.5" fill="#E7B080" stroke="{DARK}" stroke-width="2.6"/>
    </g>
  </g>
</g>'''


def hand_5f(cx, cy, skin, flip=1):
    # Cute little open 5-finger raised cartoon hand centered at (cx, cy)
    f = flip
    return (f'<g transform="translate({cx} {cy}) scale({f} 1)">'
            f'<circle cx="0" cy="0" r="11" fill="{skin}" stroke="{DARK}" stroke-width="2.4"/>'
            f'<circle cx="-9" cy="-10" r="3.8" fill="{skin}" stroke="{DARK}" stroke-width="1.8"/>'
            f'<circle cx="-3.5" cy="-13" r="3.8" fill="{skin}" stroke="{DARK}" stroke-width="1.8"/>'
            f'<circle cx="3" cy="-13" r="3.8" fill="{skin}" stroke="{DARK}" stroke-width="1.8"/>'
            f'<circle cx="9" cy="-10" r="3.8" fill="{skin}" stroke="{DARK}" stroke-width="1.8"/>'
            f'<circle cx="12" cy="-2" r="3.6" fill="{skin}" stroke="{DARK}" stroke-width="1.8"/>'
            f'</g>')


def student(p, i, cx, cy_off, skin, kind):
    # kind: "girl", "boy_mid", "boy_right"
    hy = 928 + cy_off  # head center y
    sy = 988 + cy_off  # shoulders top y
    hair_back, hair_front = "", ""
    if kind == "girl":
        hair_back = (f'<path d="M-74 {hy+8} C-76 {hy-64} -44 {hy-82} 0 {hy-82} C44 {hy-82} 76 {hy-64} 74 {hy+8} '
                     f'C74 {hy+44} 58 {hy+52} 36 {hy+46} L-36 {hy+46} C-58 {hy+52} -74 {hy+44} -74 {hy+8} Z" fill="#2E1E16" stroke="{DARK}" stroke-width="2.8"/>')
        hair_front = (f'<path d="M-64 {hy-4} C-54 {hy-46} -24 {hy-56} 0 {hy-56} C26 {hy-56} 54 {hy-42} 64 {hy-4} '
                      f'C44 {hy-32} 22 {hy-36} 0 {hy-36} C-22 {hy-36} -46 {hy-32} -64 {hy-4} Z" fill="#2E1E16"/>'
                      # Cute red ribbon bow on top right
                      f'<g transform="translate(49 {hy-42}) rotate(20)">'
                      f'<polygon points="-12,-6 0,0 -12,6" fill="#C81E2B" stroke="{DARK}" stroke-width="1.8"/>'
                      f'<polygon points="12,-6 0,0 12,6" fill="#C81E2B" stroke="{DARK}" stroke-width="1.8"/>'
                      f'<circle cx="0" cy="0" r="3.5" fill="#E63946" stroke="{DARK}" stroke-width="1.6"/></g>')
    elif kind == "boy_mid":
        hair_front = (f'<path d="M-62 {hy-2} C-64 {hy-56} -30 {hy-66} 0 {hy-66} C30 {hy-66} 64 {hy-56} 62 {hy-2} '
                      f'L48 {hy-26} L34 {hy-10} L18 {hy-30} L0 {hy-12} L-18 {hy-30} L-36 {hy-10} L-48 {hy-26} Z" fill="#2E1E16" stroke="{DARK}" stroke-width="2.4" stroke-linejoin="round"/>')
    else:
        hair_front = (f'<path d="M-60 {hy-4} C-60 {hy-54} -28 {hy-62} 0 {hy-62} C28 {hy-62} 60 {hy-54} 60 {hy-4} '
                      f'C42 {hy-34} 22 {hy-40} 0 {hy-40} C-22 {hy-40} -42 {hy-34} -60 {hy-4} Z" fill="#2E1E16" stroke="{DARK}" stroke-width="2.4"/>'
                      f'<path d="M6 {hy-61} Q16 {hy-76} 28 {hy-70}" fill="none" stroke="#2E1E16" stroke-width="3.6" stroke-linecap="round"/>')

    # Single raised arm (for asking a question / pointing up)
    arm_up_r = (f'<g id="{p}-st{i}-armR" opacity="0">'
                f'<path d="M54 {sy+32} L82 {sy-16} L76 {sy-82}" fill="none" stroke="{DARK}" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<path d="M54 {sy+32} L82 {sy-16} L76 {sy-82}" fill="none" stroke="#FFFFFF" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<path d="M79 {sy-48} L76 {sy-82}" fill="none" stroke="{skin}" stroke-width="18" stroke-linecap="round"/>'
                f'<circle cx="76" cy="{sy-90}" r="12" fill="{skin}" stroke="{DARK}" stroke-width="2.6"/></g>')
    # Both cheering arms up (with 5-finger hands!)
    cheer = (f'<g id="{p}-st{i}-cheer" opacity="0">'
             f'<path d="M-54 {sy+36} L-82 {sy-24} L-96 {sy-120}" fill="none" stroke="{DARK}" stroke-width="25" stroke-linecap="round" stroke-linejoin="round"/>'
             f'<path d="M-54 {sy+36} L-82 {sy-24} L-96 {sy-120}" fill="none" stroke="{skin}" stroke-width="19" stroke-linecap="round" stroke-linejoin="round"/>'
             f'<path d="M-54 {sy+36} L-78 {sy-14}" fill="none" stroke="#FFFFFF" stroke-width="20" stroke-linecap="round"/>'
             f'{hand_5f(-97, sy-134, skin, 1)}'
             f'<path d="M54 {sy+36} L82 {sy-24} L96 {sy-120}" fill="none" stroke="{DARK}" stroke-width="25" stroke-linecap="round" stroke-linejoin="round"/>'
             f'<path d="M54 {sy+36} L82 {sy-24} L96 {sy-120}" fill="none" stroke="{skin}" stroke-width="19" stroke-linecap="round" stroke-linejoin="round"/>'
             f'<path d="M54 {sy+36} L78 {sy-14}" fill="none" stroke="#FFFFFF" stroke-width="20" stroke-linecap="round"/>'
             f'{hand_5f(97, sy-134, skin, -1)}'
             f'</g>')

    return f'''
<g id="{p}-st{i}" transform="translate({cx} 0)">
  {arm_up_r}
  {cheer}
  <!-- Resting body + arms -->
  <g id="{p}-st{i}-arms-rest">
    <path d="M-58 {sy+20} L-84 {sy+68} L-52 {sy+86}" fill="none" stroke="{DARK}" stroke-width="25" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M-58 {sy+20} L-84 {sy+68} L-52 {sy+86}" fill="none" stroke="#FFFFFF" stroke-width="19" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M58 {sy+20} L84 {sy+68} L52 {sy+86}" fill="none" stroke="{DARK}" stroke-width="25" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M58 {sy+20} L84 {sy+68} L52 {sy+86}" fill="none" stroke="#FFFFFF" stroke-width="19" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="-48" cy="{sy+88}" r="11" fill="{skin}" stroke="{DARK}" stroke-width="2.4"/>
    <circle cx="48" cy="{sy+88}" r="11" fill="{skin}" stroke="{DARK}" stroke-width="2.4"/>
  </g>
  <!-- Shirt torso + collar + red SD tie -->
  <path d="M-64 {sy+100} L-56 {sy+18} Q-44 {sy} -18 {sy} L18 {sy} Q44 {sy} 56 {sy+18} L64 {sy+100} Z" fill="#FFFFFF" stroke="{DARK}" stroke-width="2.8" stroke-linejoin="round"/>
  <rect x="20" y="{sy+48}" width="20" height="20" rx="2" fill="none" stroke="#D8D2CA" stroke-width="2"/>
  <polygon points="-24,{sy} -4,{sy+22} 0,{sy+8}" fill="#FFFFFF" stroke="{DARK}" stroke-width="2.4" stroke-linejoin="round"/>
  <polygon points="24,{sy} 4,{sy+22} 0,{sy+8}" fill="#FFFFFF" stroke="{DARK}" stroke-width="2.4" stroke-linejoin="round"/>
  <polygon points="-7,{sy+12} 7,{sy+12} 10,{sy+72} 0,{sy+86} -10,{sy+72}" fill="#C81E2B" stroke="{DARK}" stroke-width="2.2" stroke-linejoin="round"/>

  <!-- Head -->
  {hair_back}
  <circle cx="-62" cy="{hy+6}" r="10" fill="{skin}" stroke="{DARK}" stroke-width="2.6"/>
  <circle cx="62" cy="{hy+6}" r="10" fill="{skin}" stroke="{DARK}" stroke-width="2.6"/>
  <ellipse cx="0" cy="{hy}" rx="60" ry="54" fill="{skin}" stroke="{DARK}" stroke-width="2.8"/>
  {hair_front}
  <!-- Rosy cheeks -->
  <circle cx="-38" cy="{hy+18}" r="9.5" fill="#F29AB0" opacity="0.6"/>
  <circle cx="38" cy="{hy+18}" r="9.5" fill="#F29AB0" opacity="0.6"/>
  <!-- Eyebrows -->
  <path d="M-32 {hy-16} Q-22 {hy-22} -12 {hy-16}" fill="none" stroke="{DARK}" stroke-width="2.4" stroke-linecap="round"/>
  <path d="M12 {hy-16} Q22 {hy-22} 32 {hy-16}" fill="none" stroke="{DARK}" stroke-width="2.4" stroke-linecap="round"/>
  <!-- Normal eyes -->
  <g id="{p}-st{i}-en">
    <ellipse cx="-22" cy="{hy+2}" rx="6" ry="7.5" fill="#2E1E16"/><circle cx="-19.5" cy="{hy-1}" r="2.3" fill="#FFFFFF"/>
    <ellipse cx="22" cy="{hy+2}" rx="6" ry="7.5" fill="#2E1E16"/><circle cx="24.5" cy="{hy-1}" r="2.3" fill="#FFFFFF"/>
  </g>
  <!-- Laughing crescent eyes -->
  <g id="{p}-st{i}-el" opacity="0">
    <path d="M-32 {hy+5} Q-22 {hy-9} -12 {hy+5}" fill="none" stroke="#2E1E16" stroke-width="3.6" stroke-linecap="round"/>
    <path d="M12 {hy+5} Q22 {hy-9} 32 {hy+5}" fill="none" stroke="#2E1E16" stroke-width="3.6" stroke-linecap="round"/>
  </g>
  <!-- Mouths: smile (m1), surprised O (m2), big happy D-laugh (m3) -->
  <path id="{p}-st{i}-m1" d="M-12 {hy+24} Q0 {hy+34} 12 {hy+24}" fill="none" stroke="{DARK}" stroke-width="3.2" stroke-linecap="round"/>
  <ellipse id="{p}-st{i}-m2" cx="0" cy="{hy+28}" rx="8.5" ry="11" fill="#8A2B26" stroke="{DARK}" stroke-width="2.4" opacity="0"/>
  <g id="{p}-st{i}-m3" opacity="0">
    <path d="M-14 {hy+22} L14 {hy+22} Q12 {hy+42} 0 {hy+42} Q-12 {hy+42} -14 {hy+22} Z" fill="#8A2B26" stroke="{DARK}" stroke-width="2.4" stroke-linejoin="round"/>
    <ellipse cx="0" cy="{hy+37}" rx="7.5" ry="3.8" fill="#E0645E"/>
  </g>
</g>'''


def students(p):
    out = [
        student(p, 0, 90, 0, "#F1C39B", "girl"),
        student(p, 1, 324, 18, "#E8B287", "boy_mid"),
        student(p, 2, 562, 0, "#C98E63", "boy_right"),
    ]
    # 3 foreground desks (center desk slightly lower with red book on top, matching f_98.5.png!)
    desks = (
        f'<g id="{p}-sdesks">'
        # Left desk
        f'<rect x="-12" y="1096" width="208" height="210" fill="#D59E63" stroke="{DARK}" stroke-width="2.8"/>'
        f'<rect x="-16" y="1078" width="222" height="19" rx="3" fill="#E4B074" stroke="{DARK}" stroke-width="2.8"/>'
        f'<line x1="0" y1="1150" x2="176" y2="1150" stroke="#B67E46" stroke-width="3"/>'
        # Right desk
        f'<rect x="454" y="1096" width="222" height="210" fill="#D59E63" stroke="{DARK}" stroke-width="2.8"/>'
        f'<rect x="444" y="1078" width="236" height="19" rx="3" fill="#E4B074" stroke="{DARK}" stroke-width="2.8"/>'
        f'<line x1="472" y1="1150" x2="656" y2="1150" stroke="#B67E46" stroke-width="3"/>'
        # Center desk (slightly lower)
        f'<rect x="212" y="1116" width="226" height="200" fill="#D59E63" stroke="{DARK}" stroke-width="2.8"/>'
        f'<rect x="204" y="1098" width="242" height="19" rx="3" fill="#E4B074" stroke="{DARK}" stroke-width="2.8"/>'
        f'<rect x="276" y="1088" width="96" height="10" rx="2" fill="#C81E2B" stroke="{DARK}" stroke-width="2"/>'
        f'<line x1="226" y1="1170" x2="424" y2="1170" stroke="#B67E46" stroke-width="3"/>'
        f'</g>'
    )
    return "\n".join(out) + desks


def cloud_path(cx, cy, rx, ry):
    # Cute fluffy cartoon thought cloud centered at (cx, cy) with approx radius (rx, ry)
    pts = [
        (-0.85, 0.25), (-0.98, -0.15), (-0.72, -0.58), (-0.30, -0.82),
        (0.22, -0.85), (0.68, -0.62), (0.98, -0.18), (0.88, 0.30),
        (0.55, 0.70), (0.05, 0.82), (-0.48, 0.72),
    ]
    d = f"M {cx + pts[0][0]*rx:.1f} {cy + pts[0][1]*ry:.1f} "
    n = len(pts)
    for k in range(n):
        x1, y1 = cx + pts[k][0] * rx, cy + pts[k][1] * ry
        x2, y2 = cx + pts[(k + 1) % n][0] * rx, cy + pts[(k + 1) % n][1] * ry
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        vx, vy = mx - cx, my - cy
        d += f"Q {mx + vx*0.36:.1f} {my + vy*0.36:.1f} {x2:.1f} {y2:.1f} "
    return d + "Z"


def ell(i, cx, cy, rx, ry, col, sw=4, rot=0):
    return (f'<ellipse id="{i}" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{col}" '
            f'stroke-width="{sw}" stroke-linecap="round" pathLength="1" stroke-dasharray="1 1.2" '
            f'stroke-dashoffset="1.1" transform="rotate({rot} {cx} {cy})"/>')


def line(i, d, col, sw=4):
    return (f'<path id="{i}" d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round" pathLength="1" stroke-dasharray="1 1.2" stroke-dashoffset="1.1"/>')


def T(c, col):
    return f'<tspan fill="{col}">{c}</tspan>'


class Scene:
    def __init__(self, p, start, end):
        self.p, self.start, self.end = p, start, end
        self.off = start
        self.dur = end - start
        self.board = []        # SVG inside chalkboard (clipped to slate, chalk-filtered)
        self.board_free = []   # SVG above chalkboard (NOT clipped to slate — e.g. overflowing 33,3333!)
        self.extra_svg = []    # overlays on top of teacher/students (bubbles, HA!, etc.)
        self.defs_extra = []
        self.js = []
        self.clipn = 0
        self.er_n = 0

    def lt(self, t):
        return round(max(0.0, t - self.off), 4)

    def text(self, content, x, y, size, t0, d, fill="#FFFFFF", anchor="middle", family="Caveat Brush", tid=None, plain_len=None, rot=0, free=False, stroke="", sw=0):
        p = self.p
        self.clipn += 1
        n = self.clipn
        L = plain_len or len(re.sub(r"<[^>]+>", "", content))
        est = L * size * 0.56 + 40
        left = x - est / 2 if anchor == "middle" else x - 12
        tid = tid or f"{p}-t{n}"
        self.defs_extra.append(f'<clipPath id="{p}-c{n}"><rect id="{p}-cr{n}" x="{left:.0f}" y="{y-size*1.15:.0f}" width="0" height="{size*1.65:.0f}"/></clipPath>')
        tr = f' transform="rotate({rot} {x} {y})"' if rot else ""
        st = f' stroke="{stroke}" stroke-width="{sw}" paint-order="stroke" stroke-linejoin="round"' if stroke else ""
        el = f'<g clip-path="url(#{p}-c{n})"{tr}><text id="{tid}" x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{st}>{content}</text></g>'
        (self.board_free if free else self.board).append(el)
        self.js.append(f'tl.fromTo("#{p}-cr{n}",{{attr:{{width:0}}}},{{attr:{{width:{est:.0f}}},duration:{d},ease:"none"}},{self.lt(t0)});')
        return tid

    def draw(self, svg, t0, d, ease="power1.inOut", free=False):
        (self.board_free if free else self.board).append(svg)
        i = re.search(r'id="([^"]+)"', svg).group(1)
        self.js.append(f'tl.fromTo("#{i}",{{attr:{{"stroke-dashoffset":1.1}}}},{{attr:{{"stroke-dashoffset":0}},duration:{d},ease:"{ease}"}},{self.lt(t0)});')
        return i

    def pop(self, gid, svg, t0, cx, cy, d=0.28, frm=0.4, ease="back.out(2)", free=False):
        (self.board_free if free else self.board).append(f'<g id="{gid}" opacity="0">{svg}</g>')
        self.js.append(f'tl.fromTo("#{gid}",{{opacity:0,scale:{frm},svgOrigin:"{cx} {cy}"}},{{opacity:1,scale:1,svgOrigin:"{cx} {cy}",duration:{d},ease:"{ease}"}},{self.lt(t0)});')

    def stamp(self, gid, label, cx, cy, w, h, col, t0, rot=-8, size=34):
        svg = (f'<g transform="rotate({rot} {cx} {cy})">'
               f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="4" fill="none" stroke="{col}" stroke-width="3.6"/>'
               f'<rect x="{cx-w/2+4}" y="{cy-h/2+4}" width="{w-8}" height="{h-8}" rx="2" fill="none" stroke="{col}" stroke-width="1.4" opacity="0.7"/>'
               f'<text x="{cx}" y="{cy+size*0.33:.1f}" font-family="Caveat Brush" font-size="{size}" fill="{col}" text-anchor="middle">{label}</text></g>')
        self.pop(gid, svg, t0, cx, cy, 0.24, 1.9, "back.out(2.2)")

    def cam(self, t, preset_or_tuple, d=0.0, ease="power2.inOut"):
        s, cx, cy = preset_or_tuple
        x, y = (360 - cx) * s, (640 - cy) * s
        lt = self.lt(t)
        if d <= 0:
            self.js.append(f'tl.set("#{self.p}-cam",{{scale:{s},x:{x:.1f},y:{y:.1f},transformOrigin:"360px 640px"}},{lt});')
        else:
            self.js.append(f'tl.to("#{self.p}-cam",{{scale:{s},x:{x:.1f},y:{y:.1f},transformOrigin:"360px 640px",duration:{d},ease:"{ease}"}},{lt});')

    def pointer_mode(self, t, active=True):
        lt = self.lt(t)
        a, b = (0, 1) if active else (1, 0)
        self.js.append(f'tl.set("#{self.p}-t-rarm-rest",{{opacity:{a}}},{lt}).set("#{self.p}-t-rarm-point",{{opacity:{b}}},{lt});')

    def point_at(self, t, bx, by, d=0.35):
        """Aim teacher's pointer stick tip cleanly at board point (bx, by)."""
        # Shoulder pivot at (566, 488), resting stick tip at (335, 488) -> length 231 along -X
        dx = 566 - bx
        dy = 488 - by
        ang = math.degrees(math.atan2(dy, dx))
        # Clamp subtle translation so tip reaches closer or farther spots naturally
        dist = math.hypot(dx, dy)
        shift_x = max(-90, min(35, 231 - dist)) * math.cos(math.radians(ang))
        shift_y = max(-45, min(55, 231 - dist)) * math.sin(math.radians(ang))
        lt = self.lt(t)
        if d <= 0:
            self.js.append(f'tl.set("#{self.p}-tarm",{{rotation:{ang:.1f},x:{-shift_x:.1f},y:{-shift_y:.1f},svgOrigin:"566 488"}},{lt});')
        else:
            self.js.append(f'tl.to("#{self.p}-tarm",{{rotation:{ang:.1f},x:{-shift_x:.1f},y:{-shift_y:.1f},svgOrigin:"566 488",duration:{d},ease:"power2.inOut"}},{lt});')

    def teacher_talk(self, t0, t1, step=0.22):
        p = self.p
        t = t0
        while t < t1 - 0.04:
            a, b = self.lt(t), self.lt(min(t + step * 0.55, t1))
            self.js.append(f'tl.set("#{p}-t-m1",{{opacity:0}},{a}).set("#{p}-t-m2",{{opacity:1}},{a}).set("#{p}-t-m1",{{opacity:1}},{b}).set("#{p}-t-m2",{{opacity:0}},{b});')
            t += step

    def teacher_shock(self, t0, t1):
        p = self.p
        a, b = self.lt(t0), self.lt(t1)
        self.js.append(f'tl.set("#{p}-t-m1",{{opacity:0}},{a}).set("#{p}-t-m2",{{opacity:1}},{a}).set("#{p}-t-m1",{{opacity:1}},{b}).set("#{p}-t-m2",{{opacity:0}},{b});')
        self.js.append(f'tl.set("#{p}-t-larm-rest",{{opacity:0}},{a}).set("#{p}-t-larm-up",{{opacity:1}},{a}).set("#{p}-t-larm-rest",{{opacity:1}},{b}).set("#{p}-t-larm-up",{{opacity:0}},{b});')

    def eraser_wipe(self, t0, dur=0.75, hide_ids=None):
        """Sweeps eraser horizontally back-and-forth down the chalkboard leaving fading streaks."""
        p = self.p
        self.er_n += 1
        k = self.er_n
        streaks = "".join(
            f'<rect class="{p}-stk{k}" x="{BX+10+(j%2)*14}" y="{BY+16+j*54}" width="{BW-38-(j*23)%50}" height="28" rx="14" fill="#529674" opacity="0"/>'
            for j in range(8))
        dots = "".join(
            f'<circle class="{p}-stk{k}" cx="{BX+35+(j*61)%330}" cy="{BY+40+(j*83)%370}" r="2.5" fill="#B5E0C8" opacity="0"/>'
            for j in range(10))
        self.board.append(f'<g id="{p}-stkg{k}">{streaks}{dots}</g>')
        er = (f'<g id="{p}-er{k}" opacity="0">'
              f'<rect x="{BX+18}" y="{BY+10}" width="24" height="68" rx="5" fill="#7D756D" stroke="{DARK}" stroke-width="2.6"/>'
              f'<rect x="{BX+22}" y="{BY+10}" width="18" height="68" rx="4" fill="#A66A3E" stroke="{DARK}" stroke-width="2.6"/></g>')
        self.board_free.append(er)
        lt = self.lt(t0)
        d1 = round(dur / 4, 3)
        self.js.append(f'tl.set("#{p}-tray-er",{{opacity:0}},{lt}).set("#{p}-er{k}",{{opacity:1,x:320,y:0,rotation:4}},{lt});')
        self.js.append(f'tl.to("#{p}-er{k}",{{x:10,y:90,rotation:-6,duration:{d1},ease:"power1.inOut"}},{lt});')
        self.js.append(f'tl.to("#{p}-er{k}",{{x:330,y:190,rotation:6,duration:{d1},ease:"power1.inOut"}},{round(lt+d1,3)});')
        self.js.append(f'tl.to("#{p}-er{k}",{{x:20,y:295,rotation:-5,duration:{d1},ease:"power1.inOut"}},{round(lt+2*d1,3)});')
        self.js.append(f'tl.to("#{p}-er{k}",{{x:310,y:370,rotation:4,duration:{d1},ease:"power1.inOut"}},{round(lt+3*d1,3)});')
        self.js.append(f'tl.set("#{p}-er{k}",{{opacity:0}},{round(lt+dur,3)}).set("#{p}-tray-er",{{opacity:1}},{round(lt+dur,3)});')
        self.js.append(f'tl.fromTo("#{p}-stkg{k} .{p}-stk{k}",{{opacity:0}},{{opacity:0.52,duration:0.18,stagger:0.04}},{lt});')
        self.js.append(f'tl.to("#{p}-stkg{k} .{p}-stk{k}",{{opacity:0,duration:0.55,stagger:0.04,ease:"power1.out"}},{round(lt+dur*0.55,3)});')
        if hide_ids:
            sel = ",".join(f"#{i}" for i in hide_ids)
            self.js.append(f'tl.set("{sel}",{{opacity:0}},{round(lt+dur*0.45,3)});')

    def cloud_bubble(self, t0, t1, lines, cx, cy, tail_to, rx=98, ry=46, size=24):
        p = self.p
        bid = f"{p}-bub{len(self.extra_svg)}"
        tx_, ty_ = tail_to
        c1x, c1y = cx + (tx_ - cx) * 0.78, cy + (ty_ - cy) * 0.78
        c2x, c2y = cx + (tx_ - cx) * 0.54, cy + (ty_ - cy) * 0.56
        # Reveal text lines smoothly inside the bubble
        t_el = []
        t_js = []
        for k, (txt, col, delay) in enumerate(lines):
            yy = cy + 6 + (k - (len(lines) - 1) / 2) * (size * 1.12)
            cid = f"{bid}-c{k}"
            self.defs_extra.append(f'<clipPath id="{cid}"><rect id="{cid}r" x="{cx-rx:.0f}" y="{yy-size:.0f}" width="0" height="{size*1.5:.0f}"/></clipPath>')
            t_el.append(f'<g clip-path="url(#{cid})"><text x="{cx}" y="{yy:.0f}" font-family="Caveat Brush" font-size="{size}" fill="{col}" text-anchor="middle">{txt}</text></g>')
            t_js.append(f'tl.fromTo("#{cid}r",{{attr:{{width:0}}}},{{attr:{{width:{rx*2:.0f}}},duration:0.42,ease:"none"}},{self.lt(t0+delay)});')
        svg = (f'<g id="{bid}" opacity="0">'
               f'<circle cx="{c1x:.0f}" cy="{c1y:.0f}" r="6" fill="#FFFFFF" stroke="{DARK}" stroke-width="2.6"/>'
               f'<circle cx="{c2x:.0f}" cy="{c2y:.0f}" r="10" fill="#FFFFFF" stroke="{DARK}" stroke-width="2.6"/>'
               f'<path d="{cloud_path(cx, cy, rx, ry)}" fill="#FFFFFF" stroke="{DARK}" stroke-width="3.2" stroke-linejoin="round"/>'
               f'{"".join(t_el)}</g>')
        self.extra_svg.append(svg)
        self.js.append(f'tl.fromTo("#{bid}",{{opacity:0,scale:0.35,svgOrigin:"{tx_} {ty_}"}},{{opacity:1,scale:1,svgOrigin:"{tx_} {ty_}",duration:0.35,ease:"back.out(2)"}},{self.lt(t0)});')
        self.js.extend(t_js)
        self.js.append(f'tl.set("#{bid}",{{opacity:0}},{self.lt(t1)});')

    def student_arm_r(self, i, t0):
        lt = self.lt(t0)
        self.js.append(f'tl.fromTo("#{self.p}-st{i}-armR",{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.28,ease:"back.out(2)"}},{lt});')

    def student_mouth(self, i, mode, t0):
        # mode: 1=smile, 2=O, 3=laugh
        lt = self.lt(t0)
        for m in (1, 2, 3):
            self.js.append(f'tl.set("#{self.p}-st{i}-m{m}",{{opacity:{1 if m==mode else 0}}},{lt});')

    def student_cheer(self, i, t0, bounce_reps=5):
        p = self.p
        lt = self.lt(t0)
        self.js.append(f'tl.set("#{p}-st{i}-arms-rest",{{opacity:0}},{lt});')
        self.js.append(f'tl.fromTo("#{p}-st{i}-cheer",{{opacity:0,y:36}},{{opacity:1,y:0,duration:0.28,ease:"back.out(2)"}},{lt});')
        self.student_mouth(i, 3, t0)
        if bounce_reps > 0:
            self.js.append(f'tl.fromTo("#{p}-st{i}",{{y:0}},{{y:-12,duration:0.16,yoyo:true,repeat:{bounce_reps},ease:"power1.inOut"}},{round(lt+0.25,3)});')

    def students_laugh(self, t0, t1):
        p = self.p
        a, b = self.lt(t0), self.lt(t1)
        reps = max(1, int((t1 - t0) / 0.16) - 1)
        for i in range(3):
            self.js.append(f'tl.set("#{p}-st{i}-en",{{opacity:0}},{a}).set("#{p}-st{i}-el",{{opacity:1}},{a})'
                           f'.set("#{p}-st{i}-en",{{opacity:1}},{b}).set("#{p}-st{i}-el",{{opacity:0}},{b});')
            self.student_mouth(i, 3, t0)
            self.student_mouth(i, 1, t1)
            self.js.append(f'tl.fromTo("#{p}-st{i}",{{y:0}},{{y:-9,duration:0.15,yoyo:true,repeat:{reps},ease:"power1.inOut"}},{round(a+0.04*i,3)});')
        # Floating HA! labels
        spots = [(70, 836, -12), (222, 850, 8), (434, 838, -8), (602, 846, 10)]
        ha_svg = "".join(f'<text x="{x}" y="{y}" transform="rotate({r} {x} {y})" font-family="Fredoka" font-weight="700" font-size="28" fill="#FFFFFF" stroke="{DARK}" stroke-width="5.5" paint-order="stroke" font-style="italic">HA!</text>' for x, y, r in spots)
        self.extra_svg.append(f'<g id="{p}-ha" opacity="0">{ha_svg}</g>')
        self.js.append(f'tl.set("#{p}-ha",{{opacity:1}},{a}).set("#{p}-ha",{{opacity:0}},{b});')
        self.js.append(f'tl.fromTo("#{p}-ha",{{y:5}},{{y:-5,duration:0.16,yoyo:true,repeat:{reps},ease:"none"}},{a});')

    def gold_clock(self, t0):
        lt = self.lt(t0)
        self.js.append(f'tl.fromTo("#{self.p}-clock-gold",{{opacity:0,scale:0.65,svgOrigin:"325 84"}},{{opacity:1,scale:1,svgOrigin:"325 84",duration:0.38,ease:"back.out(2)"}},{lt});')

    def ring_bell(self, t0):
        lt = self.lt(t0)
        self.js.append(f'tl.set("#{self.p}-bell-ring",{{opacity:1}},{lt});')
        self.js.append(f'tl.fromTo("#{self.p}-bell",{{rotation:-10,svgOrigin:"18 112"}},{{rotation:10,svgOrigin:"18 112",duration:0.12,yoyo:true,repeat:7,ease:"sine.inOut"}},{lt});')

    def build(self):
        p = self.p
        sec = "".join(f'tl.set("#{p}-sh",{{rotation:{6*(k+int(self.start))},svgOrigin:"325 84"}},{k});' for k in range(int(self.dur) + 1))
        html = f'''<template>
  <style>
    {FONTS_CSS}
    #root {{ position:absolute; inset:0; overflow:hidden; background:#F3E4CA; }}
    #{p}-cam {{ position:absolute; inset:0; }}
    #{p}-cam svg {{ position:absolute; inset:0; width:100%; height:100%; }}
  </style>
  <div id="root" data-composition-id="{p}" data-width="{W}" data-height="{H}">
    <div id="{p}-cam">
      <svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
        {defs(p)}
        <defs>{"".join(self.defs_extra)}</defs>
        {classroom(p)}
        <g id="{p}-chalk" clip-path="url(#{p}-board-clip)" filter="url(#{p}-chalk)">
          {"".join(self.board)}
        </g>
        <g id="{p}-chalk-free">
          {"".join(self.board_free)}
        </g>
        {students(p)}
        {teacher(p)}
        {"".join(self.extra_svg)}
      </svg>
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {sec}
    {chr(10).join(self.js)}
    window.__timelines["{p}"] = tl;
  </script>
</template>
'''
        open(os.path.join(OUT, f"{p}.html"), "w").write(html)
