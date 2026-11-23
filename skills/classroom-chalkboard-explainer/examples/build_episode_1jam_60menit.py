#!/usr/bin/env python3
"""Builds the full 99s manual replica of galeri-mograph-papan.mp4."""
import os, re, math
from classroom_lib import (
    Scene, OUT, W, H, DARK, Y, P, B, Wt, BX, BY, BW, BH, BCX, BCY,
    CAM_WIDE, CAM_BOARD, CAM_CLOCK, CAM_RIGHT_MED, CAM_TEACHER, CAM_BOY_MID, CAM_GIRL,
    FONTS_CSS, ell, line, T
)

SCENES = []

# =========================================================================
# B1: 0.0 - 4.95  (Clock intro -> 1 jam = 60 menit -> kenapa nggak 100?)
# =========================================================================
s = Scene("b1", 0.0, 4.95); SCENES.append(s)
s.cam(0.0, CAM_CLOCK)
s.cam(0.55, CAM_BOARD, 0.55, "power2.out")
s.cam(2.25, (1.16, 435, 625), 0.45)  # smooth zoom out to board + teacher + 2 right students
s.cam(4.25, CAM_BOARD, 0.35)

s.pointer_mode(0.0, False)
s.pointer_mode(1.0, True)
s.point_at(1.0, 210, 228, 0.0)
s.point_at(1.1, 455, 228, 1.15)
s.point_at(2.3, 470, 228, 0.2)
s.pointer_mode(2.55, False)

s.text(f'1 jam = {T("60", Y)} menit', BCX, 232, 46, 1.0, 1.15, plain_len=16)
s.draw(ell("b1-c1", 347, 220, 41, 27, Y, 3.6, -4), 2.15, 0.32)
s.draw(line("b1-u1", "M172 254 Q325 264 476 252", Y, 3.6), 2.32, 0.35)

s.text("kenapa nggak", BCX, 342, 32, 2.55, 0.65, fill=B, plain_len=12)
s.text(f'{T("100", P)} {T("?", P)}', BCX, 442, 86, 3.15, 0.65, plain_len=5)
s.draw(ell("b1-c2", 308, 418, 86, 46, P, 4.2, -3), 3.7, 0.35)
s.text("biar gampang?", BCX, 526, 34, 3.85, 0.7, plain_len=13)

s.teacher_talk(1.0, 2.3); s.teacher_talk(2.6, 4.6)
s.student_arm_r(2, 2.55)
s.student_mouth(2, 2, 2.55)
s.cloud_bubble(2.55, 4.45, [("KENAPA NGGAK", DARK, 0.25), ("100 ?", "#C81E2B", 0.55)], 462, 796, (540, 872), 96, 44, 24)

# =========================================================================
# B2: 4.95 - 11.4  (Eraser -> Rivers Efrat & Tigris -> ZAMAN KUNO -> MESOPOTAMIA)
# =========================================================================
s = Scene("b2", 4.95, 11.4); SCENES.append(s)
s.cam(4.95, CAM_BOARD)
s.cam(7.5, (1.72, 330, 418), 3.6, "none")
s.eraser_wipe(4.95, 0.65)
s.pointer_mode(4.95, False)
s.pointer_mode(7.4, True)
s.point_at(7.4, 340, 255, 0.0)
s.point_at(8.2, 415, 255, 0.8)
s.point_at(9.3, 305, 445, 0.6)
s.point_at(10.0, 390, 560, 0.6)

# Mountains + two rivers + Persian Gulf delta
s.draw(line("b2-m1", "M162 280 L182 262 L198 278 L216 260 L236 280", Wt, 3), 5.1, 0.35)
s.draw(line("b2-m2", "M274 280 L292 262 L310 278 L328 262 L346 280", Wt, 3), 5.2, 0.35)
s.draw(line("b2-r1", "M186 284 Q202 365 288 446 T 426 566", B, 4.2), 5.25, 0.7)
s.draw(line("b2-r2", "M296 284 Q314 360 364 432 T 442 562", B, 4.2), 5.45, 0.65)
s.pop("b2-delta", f'<path d="M406 588 Q434 542 478 548 Q506 558 514 588 Z" fill="url(#b2-hatchB)" stroke="{B}" stroke-width="3"/>', 5.85, 456, 566, 0.3, 0.85)
s.text("Efrat", 168, 452, 26, 6.0, 0.5, fill=B, anchor="start", plain_len=5)
s.text("Tigris", 412, 354, 26, 6.2, 0.5, fill=B, anchor="start", plain_len=6)
s.text("ZAMAN KUNO", BCX, 214, 46, 6.3, 0.85, plain_len=10)
s.text("± 4.000 tahun lalu", BCX, 262, 27, 8.0, 1.0, fill=Y, plain_len=18)
s.text("MESOPOTAMIA", 306, 568, 36, 9.6, 0.9, fill=Y, plain_len=11)
s.draw(line("b2-ar", "M342 536 Q344 484 366 446 M366 446 L352 454 M366 446 L372 462", Y, 3), 10.1, 0.45)
s.text("antara sungai", 414, 462, 20, 10.3, 0.5, fill=Y, plain_len=13)
s.teacher_talk(5.1, 11.1)

# =========================================================================
# B3: 11.4 - 17.9  (Sumeria -> Babilonia clay tablet -> center boy 10 jari)
# =========================================================================
s = Scene("b3", 11.4, 17.9); SCENES.append(s)
s.cam(11.4, CAM_BOARD)
s.cam(15.8, CAM_BOY_MID, 0.45)        # smooth pan DOWN to center boy!
s.cam(17.0, CAM_BOARD, 0.45)          # smooth pan UP back to board!
s.eraser_wipe(11.4, 0.6)

s.pointer_mode(11.4, True)
s.point_at(11.7, 275, 290, 0.0)
s.point_at(12.2, 290, 215, 0.45)
s.point_at(13.0, 445, 215, 0.65)
s.point_at(14.0, 390, 360, 0.6)
s.point_at(15.1, 385, 515, 0.5)
s.pointer_mode(15.8, False)

# Clay tablet square + Sumeria -> Babilonia
s.draw(f'<rect id="b3-tab" x="252" y="274" width="146" height="162" fill="none" stroke="{Y}" stroke-width="3.8" stroke-linejoin="round" pathLength="1" stroke-dasharray="1 1.2" stroke-dashoffset="1.1"/>', 11.65, 0.55)
s.text("SUMERIA", 148, 216, 34, 11.9, 0.65, anchor="start", plain_len=7)
s.draw(line("b3-ar", "M294 204 L344 204 M344 204 L331 195 M344 204 L331 213", Y, 3.2), 12.5, 0.35)
s.text("BABILONIA", 352, 216, 34, 12.85, 0.75, anchor="start", plain_len=9)

# 4 rows of cuneiform strokes inside tablet
cunei = ["◀▼▼  ◀◀▼", "▼▼▼  ◀▼▼▼▼", "◀◀◀▼  ◀▼", "▼ ◀▼▼  ◀◀"]
for k, row in enumerate(cunei):
    s.text(row, BCX, 312 + k * 32, 18, 13.45 + k * 0.32, 0.3, family="Fredoka", plain_len=12)
s.text("tablet tanah liat", BCX, 458, 19, 14.65, 0.45, fill=Y, plain_len=17)
s.text("basis", 222, 524, 52, 15.0, 0.45, anchor="start", plain_len=5)
s.text(T("60", Y), 388, 524, 54, 15.4, 0.35, plain_len=2)
s.draw(ell("b3-c60", 388, 506, 40, 28, Y, 3.6, -5), 15.65, 0.3)
s.text("bukan 10", BCX, 572, 32, 17.1, 0.45, fill=P, plain_len=8)
s.eraser_wipe(17.35, 0.55)

# Center boy raises BOTH hands with 10 spread fingers + smiling + cloud bubble "10 jari = basis 10"
s.student_cheer(1, 15.85, bounce_reps=0)
s.cloud_bubble(15.9, 17.25, [("10 jari", DARK, 0.1), ("= basis 10", "#C81E2B", 0.4)], 324, 790, (324, 874), 88, 42, 24)
s.teacher_talk(11.8, 15.7)

# =========================================================================
# B4: 17.9 - 31.6  (Kenapa 60? Gampang dibagi! 10 circled divisors + quotients)
# =========================================================================
s = Scene("b4", 17.9, 31.6); SCENES.append(s)
s.cam(17.9, CAM_BOARD)
s.cam(19.2, CAM_TEACHER, 0.5)     # pan right to show teacher beside 60?
s.cam(21.25, CAM_BOARD, 0.5)      # pan back to board for divisor chips

s.pointer_mode(17.9, True)
s.point_at(17.9, 330, 245, 0.0)
s.pointer_mode(19.2, False)
s.pointer_mode(21.7, True)
s.point_at(21.7, 174, 360, 0.0)

s.text("kenapa", 162, 224, 24, 18.0, 0.5, fill=B, anchor="start", plain_len=6)
s.text(T("60", Y), 312, 260, 96, 18.4, 0.65, plain_len=2)
s.text(T("?", P), 416, 256, 76, 19.0, 0.25, plain_len=1)
s.text("gampang dibagi!", BCX, 316, 36, 19.9, 0.95, plain_len=15)
s.draw(line("b4-u", "M204 330 Q325 339 446 329", Y, 3.4), 20.85, 0.35)

xs = [174, 249, 325, 401, 476]
row1 = [("÷2", 22.1), ("÷3", 22.8), ("÷4", 23.6), ("÷5", 24.4), ("÷6", 25.1)]
row2 = [("÷10", 26.0), ("÷12", 26.7), ("÷15", 27.4), ("÷20", 28.4), ("÷30", 29.2)]
for k, (lab, tt) in enumerate(row1):
    s.pop(f"b4-c1{k}", f'<ellipse cx="{xs[k]}" cy="382" rx="34" ry="25" fill="none" stroke="{Y}" stroke-width="3.5"/><text x="{xs[k]}" y="393" font-family="Caveat Brush" font-size="30" fill="#FFFFFF" text-anchor="middle">{lab}</text>', tt, xs[k], 382)
    s.point_at(tt - 0.15, xs[k], 396, 0.35)
for k, (lab, tt) in enumerate(row2):
    s.pop(f"b4-c2{k}", f'<ellipse cx="{xs[k]}" cy="472" rx="34" ry="25" fill="none" stroke="{Y}" stroke-width="3.5"/><text x="{xs[k]}" y="483" font-family="Caveat Brush" font-size="28" fill="#FFFFFF" text-anchor="middle">{lab}</text>', tt, xs[k], 472)
    s.point_at(tt - 0.15, xs[k], 488, 0.35)

for k, v in enumerate(["30", "20", "15", "12", "10"]):
    s.text(v, xs[k], 426, 22, 30.0 + k * 0.08, 0.18, fill=Y, plain_len=2)
for k, v in enumerate(["6", "5", "4", "3", "2"]):
    s.text(v, xs[k], 516, 22, 30.35 + k * 0.08, 0.18, fill=Y, plain_len=1)
s.text("semua bulat ✓", BCX, 564, 30, 30.65, 0.6, fill=Y, plain_len=13)
s.point_at(30.6, 425, 560, 0.4)
s.teacher_talk(18.0, 31.3)

# =========================================================================
# B5: 31.6 - 38.5  (100 / 3 = 33,3333333... overflows wall + teacher shocked + HA!)
# =========================================================================
s = Scene("b5", 31.6, 38.5); SCENES.append(s)
s.cam(31.6, CAM_BOARD)
s.cam(35.3, CAM_TEACHER, 1.5, "power1.inOut")  # tracks the overflowing 33333 across the wall!
s.cam(37.2, CAM_WIDE, 0.4)                     # smooth zoom out to laughing class!
s.eraser_wipe(31.6, 0.55)

s.pointer_mode(31.6, True)
s.point_at(32.1, 210, 250, 0.0)
s.point_at(32.2, 390, 250, 1.4)
s.pointer_mode(34.3, False)

s.text("100 ÷ 3 =", 170, 250, 56, 32.1, 1.45, anchor="start", plain_len=9)
# ICONIC GAG: 33,33333... written in board_free with dark outline so it sails cleanly across the cream wall over the teacher's head!
s.text("33,333333333333333333333333333", 156, 336, 48, 34.0, 3.3, anchor="start", plain_len=31, free=True, stroke=DARK, sw=7)
s.text("nggak abis-abis!", BCX, 424, 32, 37.35, 0.7, fill=P, plain_len=16)
s.draw(line("b5-u", "M212 438 Q325 446 438 436", P, 3), 37.95, 0.3)

s.teacher_talk(32.0, 35.3)
s.teacher_shock(35.4, 38.45)
s.students_laugh(37.3, 38.45)

# =========================================================================
# B6: 38.5 - 46.0  (60 menit clock slices 1/2=30, 1/3=20, RAPI! stamp -> wide)
# =========================================================================
s = Scene("b6", 38.5, 46.0); SCENES.append(s)
s.cam(38.5, CAM_WIDE)
s.cam(38.55, CAM_BOARD, 0.45)
s.cam(44.85, CAM_WIDE, 0.55)
s.eraser_wipe(38.55, 0.55)

s.pointer_mode(38.5, False)
s.pointer_mode(40.3, True)
s.point_at(40.3, 380, 355, 0.0)
s.point_at(40.8, 370, 498, 0.8)
s.point_at(42.5, 290, 320, 0.4)
s.point_at(43.0, 370, 540, 0.8)
s.pointer_mode(44.7, False)

cx, cy, r = BCX, 346, 102
s.text("60 menit", BCX, 206, 36, 38.85, 0.5, plain_len=8)
s.draw(f'<circle id="b6-face" cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#FFFFFF" stroke-width="3.8" pathLength="1" stroke-dasharray="1 1.2" stroke-dashoffset="1.1"/>', 39.0, 0.65)
ticks = "".join(f'<line x1="{cx+(r-10)*math.sin(math.radians(a)):.1f}" y1="{cy-(r-10)*math.cos(math.radians(a)):.1f}" x2="{cx+(r-1)*math.sin(math.radians(a)):.1f}" y2="{cy-(r-1)*math.cos(math.radians(a)):.1f}" stroke="#FFFFFF" stroke-width="2.4"/>' for a in range(0, 360, 30))
nums = "".join(f'<text x="{x}" y="{y}" font-family="Caveat Brush" font-size="22" fill="#FFFFFF" text-anchor="middle">{n}</text>' for n, x, y in [(12, cx, cy - r + 26), (3, cx + r - 20, cy + 7), (6, cx, cy + r - 10), (9, cx - r + 20, cy + 7)])
s.pop("b6-tk", ticks + nums, 39.65, cx, cy, 0.25, 0.94)
s.pop("b6-half", f'<path d="M{cx} {cy} L{cx} {cy-r} A{r} {r} 0 0 1 {cx} {cy+r} Z" fill="url(#b6-hatchY)" stroke="{Y}" stroke-width="2.6"/><text x="{cx+42}" y="{cy+10}" font-family="Caveat Brush" font-size="34" fill="#FFFFFF" text-anchor="middle">1/2</text>', 40.35, cx + 44, cy, 0.4, 0.9)
s.text(f'{T("1/2 jam", Y)} = 30 menit', BCX, 498, 30, 40.7, 1.0, plain_len=18)
s.pop("b6-third", f'<path d="M{cx} {cy} L{cx} {cy-r} A{r} {r} 0 0 0 {cx-r*math.sin(math.radians(120)):.1f} {cy-r*math.cos(math.radians(120)):.1f} Z" fill="url(#b6-hatchP)" stroke="{P}" stroke-width="2.6"/><text x="{cx-44}" y="{cy-22}" font-family="Caveat Brush" font-size="34" fill="#FFFFFF" text-anchor="middle">1/3</text>', 42.5, cx - 44, cy - 26, 0.4, 0.9)
s.text(f'{T("1/3 jam", P)} = 20 menit', BCX, 540, 30, 42.9, 1.0, plain_len=18)
s.stamp("b6-rapi", "RAPI!", 456, 204, 102, 42, Y, 44.35, -7, 32)
s.teacher_talk(38.9, 45.2)

# =========================================================================
# B7: 46.0 - 49.0  (Teori Jari tease in wide shot -> smooth zoom to girl with "!")
# =========================================================================
s = Scene("b7", 46.0, 49.0); SCENES.append(s)
s.cam(46.0, CAM_WIDE)
s.cam(47.45, CAM_GIRL, 0.45)
s.eraser_wipe(46.0, 0.5)
s.pointer_mode(46.0, False)

# Clean rounded chalk hand outline on board
CHALK_HAND = (
    'M184 480 L176 346 C175 326 196 324 198 344 L203 398 '
    'L204 316 C205 296 226 296 228 316 L231 392 '
    'L235 306 C237 286 258 288 259 308 L260 392 '
    'L266 322 C269 304 288 308 287 328 L280 412 '
    'C294 388 312 394 310 418 C308 446 284 468 272 486 L270 500'
)
s.draw(line("b7-hand", CHALK_HAND, Wt, 3.6), 46.2, 0.8)
s.text("TEORI JARI", BCX, 212, 34, 46.6, 0.75, plain_len=10)
s.teacher_talk(46.1, 47.6)

# Girl raises her right hand, surprised O -> happy smile, white "!" pops right beside her raised hand!
s.student_arm_r(0, 47.6)
s.student_mouth(0, 2, 47.6)
s.student_mouth(0, 1, 48.55)
s.extra_svg.append(
    f'<g id="b7-ex" opacity="0" transform="rotate(-10 158 836)">'
    f'<text x="158" y="852" font-family="Fredoka" font-weight="700" font-size="48" fill="#FFFFFF" stroke="{DARK}" stroke-width="7" paint-order="stroke" text-anchor="middle">!</text></g>'
)
s.js.append('tl.fromTo("#b7-ex",{opacity:0,scale:0.3,svgOrigin:"158 836"},{opacity:1,scale:1,svgOrigin:"158 836",duration:0.25,ease:"back.out(2.6)"},1.9);')

# =========================================================================
# HANDS: 49.0 - 59.92  (Chunky full-width hands: thumb counting 1..12 + folding 5x12!)
# =========================================================================
def build_hands():
    o = 49.0
    t = lambda g: round(g - o, 3)
    SKIN = "#EEC19A"
    SHADE = "#D69E76"
    wood_lines = "".join(f'<line x1="-100" y1="{y}" x2="1540" y2="{y + (6 if (y//110)%2 else -5)}" stroke="#D6A262" stroke-width="3.5"/>' for y in range(60, 1280, 110))
    bg = f'<rect x="-100" y="0" width="1640" height="1280" fill="#E8B879"/>{wood_lines}'

    # ---- HAND 1 (centered at x=360, huge chunky hand matching f_52.5.png!) ----
    # 4 upright fingers left-to-right: pinky(x=162), ring(x=264), middle(x=366), index(x=468), width=92
    fspecs = [
        # (idx, x, top_y, bot_y, num_start)
        (0, 162, 412, 650, 10),  # pinky (leftmost) -> 10, 11, 12
        (1, 264, 352, 636, 7),   # ring -> 7, 8, 9
        (2, 366, 316, 632, 4),   # middle -> 4, 5, 6
        (3, 468, 364, 646, 1),   # index (rightmost) -> 1, 2, 3
    ]
    h1_fingers = []
    h1_highlights = []
    h1_dots = []
    dot_pos = {}
    for fi, x, top, bot, n0 in fspecs:
        cx = x + 46
        h = bot - top
        seg = h / 3.1
        h1_fingers.append(f'<rect x="{x}" y="{top}" width="92" height="{h+60}" rx="46" fill="{SKIN}" stroke="{DARK}" stroke-width="6"/>')
        h1_highlights.append(f'<rect id="h1-hl{fi}" x="{x+7}" y="{top+10}" width="78" height="{seg*3-8:.0f}" rx="36" fill="#F4DC66" opacity="0"/>')
        for k in (1, 2):
            yy = top + seg * k + 6
            h1_fingers.append(f'<path d="M{x+16} {yy:.0f} Q{cx} {yy-8:.0f} {x+76} {yy:.0f}" fill="none" stroke="{DARK}" stroke-width="4.5" stroke-linecap="round"/>')
        for k in range(3):
            num = n0 + k
            cy = top + seg * (k + 0.5) + 4
            dot_pos[num] = (cx, cy)
            h1_dots.append(
                f'<g id="h1-n{num}" opacity="0">'
                f'<circle cx="{cx}" cy="{cy:.0f}" r="20" fill="#FFFFFF" stroke="{DARK}" stroke-width="3.8"/>'
                f'<text x="{cx}" y="{cy+7:.0f}" font-family="Fredoka" font-weight="700" font-size="22" fill="{DARK}" text-anchor="middle">{num}</text></g>'
            )

    h1_palm = (
        f'<path d="M162 630 L162 965 Q162 1030 220 1030 L500 1030 Q554 1030 562 955 L568 636 L162 630 Z" fill="{SKIN}" stroke="{DARK}" stroke-width="6" stroke-linejoin="round"/>'
        f'<rect x="168" y="616" width="388" height="70" fill="{SKIN}"/>'
        f'<path d="M224 756 Q340 712 456 720 M214 842 Q325 820 434 868 M418 930 Q432 975 438 1005" fill="none" stroke="{SHADE}" stroke-width="5" stroke-linecap="round"/>'
    )
    h1_thumb_open = (
        f'<g id="h1-th-open">'
        f'<path d="M518 896 C590 855 640 770 644 650 C646 588 572 574 554 630 L516 746" fill="{SKIN}" stroke="{DARK}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
        f'</g>'
    )
    # Rounded jointed pointing thumb rooted smoothly inside right palm edge (532, 741)
    h1_thumb_ptr = (
        f'<g id="h1-th-ptr" opacity="0">'
        f'<rect x="306" y="706" width="254" height="70" rx="35" fill="{SKIN}" stroke="{DARK}" stroke-width="6"/>'
        f'<path d="M350 722 Q360 741 350 760" fill="none" stroke="{SHADE}" stroke-width="4" stroke-linecap="round"/>'
        f'</g>'
    )

    sleeve = lambda dx: (
        f'<g transform="translate({dx} 0)">'
        f'<rect x="132" y="1008" width="456" height="290" rx="22" fill="#FFFFFF" stroke="{DARK}" stroke-width="6"/>'
        f'<rect x="132" y="1008" width="456" height="72" rx="20" fill="#E3E3E3" stroke="{DARK}" stroke-width="6"/>'
        f'<rect x="224" y="1028" width="272" height="14" rx="4" fill="{DARK}"/>'
        f'</g>'
    )

    jempol = (
        f'<g id="h1-ring" opacity="0"><circle cx="514" cy="520" r="54" fill="none" stroke="{Y}" stroke-width="7"/></g>'
        f'<g id="h1-jem" opacity="0" transform="rotate(-8 565 566)">'
        f'<rect x="492" y="540" width="146" height="48" rx="24" fill="{B}" stroke="{DARK}" stroke-width="4.5"/>'
        f'<text x="565" y="573" font-family="Fredoka" font-weight="700" font-size="26" fill="{DARK}" text-anchor="middle">JEMPOL</text></g>'
    )

    hand1 = f'<g id="hand1">{"".join(h1_fingers)}{"".join(h1_highlights)}{h1_palm}{"".join(h1_dots)}{h1_thumb_open}{h1_thumb_ptr}{jempol}{sleeve(0)}</g>'

    # ---- HAND 2 (placed at x + 760 so camera pans cleanly from Hand 1 to Hand 2!) ----
    # Left palm (mirrored): thumb on LEFT, index(184), middle(286), ring(388), pinky(490)
    h2_specs = [
        # fold order: pinky(0) -> ring(1) -> middle(2) -> index(3)
        (3, 184, 364, 646),  # index (leftmost finger)
        (2, 286, 316, 632),  # middle
        (1, 388, 352, 636),  # ring
        (0, 490, 412, 650),  # pinky (rightmost finger -> folds FIRST!)
    ]
    h2_open, h2_fold = [], []
    for k, x, top, bot in h2_specs:
        cx = x + 46
        h = bot - top
        seg = h / 3.1
        h2_open.append(
            f'<g id="h2-fo{k}">'
            f'<rect x="{x}" y="{top}" width="92" height="{h+60}" rx="46" fill="{SKIN}" stroke="{DARK}" stroke-width="6"/>'
            f'<path d="M{x+16} {top+seg+6:.0f} Q{cx} {top+seg-2:.0f} {x+76} {top+seg+6:.0f}" fill="none" stroke="{DARK}" stroke-width="4.5" stroke-linecap="round"/>'
            f'<path d="M{x+16} {top+seg*2+6:.0f} Q{cx} {top+seg*2-2:.0f} {x+76} {top+seg*2+6:.0f}" fill="none" stroke="{DARK}" stroke-width="4.5" stroke-linecap="round"/>'
            f'</g>'
        )
        fy = 478 + (28 if k == 0 else (8 if k == 1 else (0 if k == 2 else 12)))
        h2_fold.append(
            f'<g id="h2-ff{k}" opacity="0">'
            f'<path d="M{x} {fy+128} L{x} {fy+44} A46 44 0 0 1 {x+92} {fy+44} L{x+92} {fy+128}" fill="{SKIN}" stroke="{DARK}" stroke-width="6" stroke-linecap="round"/>'
            f'<ellipse cx="{cx}" cy="{fy+68}" rx="37" ry="44" fill="{SHADE}"/>'
            f'<rect x="{cx-33}" y="{fy-14}" width="66" height="40" rx="18" fill="{Y}" stroke="{DARK}" stroke-width="4.5"/>'
            f'<text x="{cx}" y="{fy+15}" font-family="Fredoka" font-weight="700" font-size="26" fill="{DARK}" text-anchor="middle">12</text></g>'
        )
    h2_palm = (
        f'<path d="M162 630 L168 955 Q176 1030 230 1030 L510 1030 Q568 1030 568 965 L568 625 L162 630 Z" fill="{SKIN}" stroke="{DARK}" stroke-width="6" stroke-linejoin="round"/>'
        f'<rect x="174" y="616" width="388" height="70" fill="{SKIN}"/>'
        f'<path d="M268 720 Q384 712 500 756 M290 868 Q400 820 510 842 M296 930 Q282 975 276 1005" fill="none" stroke="{SHADE}" stroke-width="5" stroke-linecap="round"/>'
    )
    h2_th_open = (
        f'<g id="h2-tho">'
        f'<path d="M206 896 C134 855 84 770 80 650 C78 588 152 574 170 630 L208 746" fill="{SKIN}" stroke="{DARK}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
        f'</g>'
    )
    h2_th_fold = (
        f'<g id="h2-thf" opacity="0">'
        f'<path d="M174 878 C156 806 208 720 278 730 C350 740 388 810 342 848 C302 878 242 848 214 824" fill="{SKIN}" stroke="{DARK}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<rect x="176" y="704" width="66" height="40" rx="18" fill="{Y}" stroke="{DARK}" stroke-width="4.5"/>'
        f'<text x="209" y="733" font-family="Fredoka" font-weight="700" font-size="26" fill="{DARK}" text-anchor="middle">12</text></g>'
    )
    hand2 = f'<g id="hand2" transform="translate(760 0)">{"".join(h2_open)}{h2_palm}{"".join(h2_fold)}{h2_th_open}{h2_th_fold}{sleeve(0)}</g>'

    def top_pill(pid, x, y, txt, fill, w, sz=38):
        return (f'<g id="{pid}" opacity="0"><rect x="{x-w/2}" y="{y-32}" width="{w}" height="64" rx="32" fill="{fill}" stroke="{DARK}" stroke-width="5"/>'
                f'<text x="{x}" y="{y+13}" font-family="Fredoka" font-weight="700" font-size="{sz}" fill="{DARK}" text-anchor="middle">{txt}</text></g>')

    pills = (
        top_pill("p3r", 514, 310, "3 RUAS", Y, 178, 30)
        + top_pill("p4j", 360, 200, "4 JARI", "#FFFFFF", 206, 36)
        + top_pill("p12", 360, 200, "12 RUAS", Y, 254, 40)
        + top_pill("px12", 360, 200, "× 12 ?", "#FFFFFF", 214, 38)
        + top_pill("p5j", 360, 200, "5 JARI", Y, 224, 40)
    )

    js = []
    # Hand 1 enters cleanly
    js.append('tl.fromTo("#hpan",{x:0,y:40},{x:0,y:0,duration:0.35,ease:"back.out(1.6)"},0);')
    # Helper to aim articulated thumb tip at phalanx n (1..12)
    def aim_thumb(tt, num, dur=0.18):
        tx_, ty_ = dot_pos[num]
        dx, dy = 532 - tx_, 741 - ty_
        ang = math.degrees(math.atan2(dy, dx))
        dist = math.hypot(dx, dy)
        sx = max(0.55, min(1.38, dist / 210.0))
        js.append(f'tl.to("#h1-th-ptr",{{rotation:{ang:.1f},scaleX:{sx:.2f},svgOrigin:"532 741",duration:{dur},ease:"power2.inOut"}},{t(tt)});')

    # Switch to active pointing thumb at 49.55
    js.append(f'tl.set("#h1-th-open",{{opacity:0}},{t(49.55)}).set("#h1-th-ptr",{{opacity:1}},{t(49.55)});')
    # Index finger: 1, 2, 3
    js.append(f'tl.to("#h1-hl3",{{opacity:0.95,duration:0.2}},{t(49.6)});')
    seq = [
        (1, 49.6), (2, 50.0), (3, 50.45),
        (4, 51.55), (5, 51.78), (6, 52.0),
        (7, 52.25), (8, 52.48), (9, 52.7),
        (10, 52.95), (11, 53.18), (12, 53.4),
    ]
    for num, tt in seq:
        aim_thumb(tt, num, 0.16)
        js.append(f'tl.fromTo("#h1-n{num}",{{opacity:0,scale:0.4,svgOrigin:"{dot_pos[num][0]} {dot_pos[num][1]:.0f}"}},{{opacity:1,scale:1,svgOrigin:"{dot_pos[num][0]} {dot_pos[num][1]:.0f}",duration:0.16,ease:"back.out(2.2)"}},{t(tt+0.04)});')
    js.append(f'tl.to("#h1-hl2",{{opacity:0.95,duration:0.2}},{t(51.5)});')
    js.append(f'tl.to("#h1-hl1",{{opacity:0.95,duration:0.2}},{t(52.2)});')
    js.append(f'tl.to("#h1-hl0",{{opacity:0.95,duration:0.2}},{t(52.9)});')

    # Release thumb back open at 53.75
    js.append(f'tl.set("#h1-th-ptr",{{opacity:0}},{t(53.75)}).set("#h1-th-open",{{opacity:1}},{t(53.75)});')

    # Top pills lifecycle
    def show_pill(pid, t0, t1, cx, cy):
        js.append(f'tl.fromTo("#{pid}",{{opacity:0,scale:0.55,svgOrigin:"{cx} {cy}"}},{{opacity:1,scale:1,svgOrigin:"{cx} {cy}",duration:0.24,ease:"back.out(2)"}},{t(t0)});')
        if t1:
            js.append(f'tl.set("#{pid}",{{opacity:0}},{t(t1)});')

    show_pill("p3r", 50.55, 51.35, 514, 310)
    show_pill("p4j", 51.4, 53.45, 360, 200)
    show_pill("p12", 53.45, 55.4, 360, 200)
    js.append(f'tl.fromTo("#h1-ring",{{opacity:0,scale:0.6,svgOrigin:"514 520"}},{{opacity:1,scale:1,svgOrigin:"514 520",duration:0.22}},{t(54.45)});')
    js.append(f'tl.fromTo("#h1-jem",{{opacity:0,scale:0.4,svgOrigin:"565 566"}},{{opacity:1,scale:1,svgOrigin:"565 566",duration:0.24,ease:"back.out(2.2)"}},{t(54.8)});')

    # Smooth pan across from Hand 1 to Hand 2! (55.4 -> 55.9)
    js.append(f'tl.to("#hpan",{{x:-760,duration:0.48,ease:"power2.inOut"}},{t(55.4)});')

    # Hand 2 folds fingers ONE BY ONE: pinky(0) -> ring(1) -> middle(2) -> index(3) -> thumb!
    show_pill("px12", 56.9, 58.95, 360, 200)
    for k, tt in [(0, 56.35), (1, 56.95), (2, 57.55), (3, 58.15)]:
        js.append(f'tl.set("#h2-fo{k}",{{opacity:0}},{t(tt)}).fromTo("#h2-ff{k}",{{opacity:0,y:-36}},{{opacity:1,y:0,duration:0.22,ease:"back.out(2)"}},{t(tt)});')
    js.append(f'tl.set("#h2-tho",{{opacity:0}},{t(58.7)}).fromTo("#h2-thf",{{opacity:0,x:-30}},{{opacity:1,x:0,duration:0.24,ease:"back.out(2)"}},{t(58.7)});')
    show_pill("p5j", 58.95, None, 360, 200)
    js.append(f'tl.to("#hand2",{{y:-46,duration:0.35,ease:"back.out(1.8)"}},{t(59.3)});')

    html = f'''<template>
  <style>
    {FONTS_CSS}
    #root {{ position:absolute; inset:0; overflow:hidden; background:#E8B879; }}
    #root svg {{ position:absolute; inset:0; width:100%; height:100%; }}
  </style>
  <div id="root" data-composition-id="hands" data-width="{W}" data-height="{H}">
    <svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
      <g id="hpan">{bg}{hand1}{hand2}</g>
      {pills}
    </svg>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join(js)}
    window.__timelines["hands"] = tl;
  </script>
</template>
'''
    open(os.path.join(OUT, "hands.html"), "w").write(html)


# =========================================================================
# B8: 59.92 - 66.3  (Teori Jari 12 ruas x 5 jari = 60 -> TEORI stamp -> wide)
# =========================================================================
s = Scene("b8", 59.92, 66.3); SCENES.append(s)
s.cam(59.92, CAM_BOARD)
s.cam(64.25, CAM_WIDE, 0.5)

s.pointer_mode(59.92, True)
s.point_at(60.0, 415, 260, 0.0)
s.point_at(61.0, 420, 326, 0.5)
s.point_at(62.0, 420, 416, 0.5)
s.point_at(63.6, 445, 515, 0.45)
s.pointer_mode(64.35, False)

# Static hand + title already on board
s.board.append(
    f'<text x="{BCX}" y="206" font-family="Caveat Brush" font-size="34" fill="#FFFFFF" text-anchor="middle">TEORI JARI</text>'
    f'<path d="{CHALK_HAND}" fill="none" stroke="#FFFFFF" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<g stroke="{Y}" stroke-width="2.6"><line x1="178" y1="362" x2="198" y2="362"/><line x1="180" y1="384" x2="200" y2="384"/>'
    f'<line x1="205" y1="340" x2="227" y2="340"/><line x1="206" y1="366" x2="228" y2="366"/>'
    f'<line x1="236" y1="332" x2="258" y2="332"/><line x1="237" y1="360" x2="258" y2="360"/>'
    f'<line x1="264" y1="348" x2="285" y2="348"/><line x1="262" y1="374" x2="283" y2="374"/></g>'
    f'<text x="176" y="544" font-family="Caveat Brush" font-size="22" fill="{B}">12 ruas?</text>'
)
s.text(f'{T("12", Y)} <tspan font-size="22" fill="#FFFFFF">ruas</tspan>', 424, 266, 48, 60.0, 0.7, plain_len=8)
s.text(f'× 5 <tspan font-size="22">jari</tspan>', 424, 336, 44, 60.95, 0.75, plain_len=9)
s.draw(line("b8-u", "M358 358 L492 358", Wt, 3.4), 61.6, 0.25)
s.text(T("60", Y), 424, 428, 72, 61.85, 0.5, plain_len=2)
s.draw(ell("b8-c", 425, 404, 52, 38, Y, 3.8, -5), 62.3, 0.35)
s.stamp("b8-stamp", "TEORI", 436, 512, 110, 42, P, 63.65, -7, 32)
s.text("belum ada bukti pasti", 252, 574, 20, 64.65, 0.85, fill=P, plain_len=21)
s.teacher_talk(60.0, 66.0)

# =========================================================================
# B9: 66.3 - 77.4  (Sehari 24 jam? -> eraser -> Mesir Kuno pyramids + 12 stars)
# =========================================================================
s = Scene("b9", 66.3, 77.4); SCENES.append(s)
s.cam(66.3, CAM_WIDE)
s.cam(69.0, CAM_BOARD, 0.5)
s.eraser_wipe(66.3, 0.5)

s.pointer_mode(66.3, False)
s.pointer_mode(67.8, True)
s.point_at(67.8, 330, 310, 0.0)
s.point_at(70.2, 325, 535, 0.5)
s.point_at(71.6, 226, 370, 0.45)
s.point_at(73.1, 418, 370, 0.45)
s.point_at(75.0, 396, 355, 0.35)
s.point_at(76.2, 476, 395, 1.0)

def sun_svg(cx, cy, r):
    rays = "".join(
        f'<line x1="{cx+(r+6)*math.sin(math.radians(a)):.1f}" y1="{cy-(r+6)*math.cos(math.radians(a)):.1f}" '
        f'x2="{cx+(r+16)*math.sin(math.radians(a)):.1f}" y2="{cy-(r+16)*math.cos(math.radians(a)):.1f}" '
        f'stroke="{Y}" stroke-width="3.2" stroke-linecap="round"/>'
        for a in range(0, 360, 30)
    )
    # SOLID circle (NOT hidden with stroke-dashoffset!) so sun circle ALWAYS renders cleanly!
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{Y}" stroke-width="3.6"/>{rays}'

def moon_svg(cx, cy):
    return f'<path d="M{cx+14} {cy-24} A26 26 0 1 0 {cx+14} {cy+24} A20 20 0 1 1 {cx+14} {cy-24} Z" fill="none" stroke="{B}" stroke-width="3.4" stroke-linejoin="round"/>'

# Beat A (66.8 - 69.7): SEHARI = 24 JAM? + sun/moon
t_ids = []
s.pop("b9-sun1", sun_svg(230, 466, 24), 66.85, 230, 466)
s.pop("b9-moon1", moon_svg(424, 462), 67.05, 424, 462)
t_ids.append(s.text("siang", 230, 540, 24, 67.2, 0.4, plain_len=5))
t_ids.append(s.text("malam", 424, 540, 24, 67.35, 0.4, fill=B, plain_len=5))
t_ids.append(s.text("SEHARI =", BCX, 246, 38, 67.7, 0.55, plain_len=8))
t_ids.append(s.text(T("24 JAM?", Y), BCX, 342, 72, 68.1, 0.85, plain_len=7))
s.cloud_bubble(68.05, 69.35, [("24 JAM?", DARK, 0.25)], 324, 800, (324, 874), 78, 34, 24)

# Real eraser wipe clears Beat A cleanly at 69.5!
s.eraser_wipe(69.5, 0.65, hide_ids=["b9-sun1", "b9-moon1"] + t_ids)

# Beat B (70.1 - 77.4): MESIR KUNO + 3 brick-lined pyramids + sun/moon + 12 stars
def brick_pyr(x0, x1, yb, yt, i):
    xm = (x0 + x1) / 2
    segs = [f"M{x0} {yb} L{xm:.0f} {yt} L{x1} {yb} Z", f"M{xm:.0f} {yt} L{xm+10:.0f} {yb}"]
    for frac in (0.33, 0.66):
        yy = yb - (yb - yt) * frac
        lx = x0 + (xm - x0) * frac
        rx = x1 - (x1 - xm) * frac
        segs.append(f"M{lx:.0f} {yy:.0f} L{rx:.0f} {yy:.0f}")
    return line(i, " ".join(segs), Wt, 2.8)

s.draw(brick_pyr(182, 268, 574, 514, "b9-p1"), 70.05, 0.35)
s.draw(brick_pyr(258, 396, 574, 474, "b9-p2"), 70.25, 0.45)
s.draw(brick_pyr(386, 466, 574, 520, "b9-p3"), 70.5, 0.35)
s.draw(line("b9-gr", "M154 576 L496 576", Y, 3.2), 70.8, 0.3)

s.text("MESIR KUNO", BCX, 210, 42, 70.25, 1.0, plain_len=10)
s.draw(line("b9-div", "M325 248 L325 470", Wt, 2.6), 71.55, 0.35)
s.pop("b9-sun2", sun_svg(226, 326, 26), 71.65, 226, 326)
s.text("SIANG", 226, 404, 24, 71.95, 0.4, plain_len=5)
s.text(T("12", Y), 226, 448, 38, 72.35, 0.35, plain_len=2)

s.pop("b9-moon2", moon_svg(424, 286), 72.95, 424, 286)
s.text("MALAM", 424, 420, 24, 73.45, 0.4, fill=B, plain_len=5)
s.text(T("12", Y), 424, 460, 38, 73.95, 0.35, plain_len=2)

def star(x, y, col, r=10.5):
    pts = " ".join(
        f"{x + (r if k%2==0 else r*0.44)*math.sin(math.radians(k*36)):.1f},{y - (r if k%2==0 else r*0.44)*math.cos(math.radians(k*36)):.1f}"
        for k in range(10)
    )
    return f'<polygon points="{pts}" fill="none" stroke="{col}" stroke-width="2.4" stroke-linejoin="round"/>'

# Clean 4x3 constellation grid above MALAM 12 (never colliding with moon or text!)
star_spots = [
    (356, 324, Wt), (396, 326, Y), (446, 324, Wt), (484, 328, Y),
    (362, 356, Y), (402, 358, Wt), (442, 356, Wt), (482, 358, Wt),
    (366, 388, Wt), (406, 388, Y), (448, 388, Wt), (486, 388, Y),
]
for k, (sx, sy, sc) in enumerate(star_spots):
    s.pop(f"b9-star{k}", star(sx, sy, sc), 74.85 + k * 0.19, sx, sy, 0.2, 0.25)
s.teacher_talk(66.8, 77.1)

# =========================================================================
# NOTE: 77.4 - 80.8  (Ruled notebook: pencil hand writing 12 + 12 = 24 + red circle!)
# =========================================================================
def build_note():
    o = 77.4
    t = lambda g: round(g - o, 3)
    wood_lines = "".join(f'<line x1="0" y1="{y}" x2="720" y2="{y+(6 if (y//110)%2 else -5)}" stroke="#D6A262" stroke-width="3.5"/>' for y in range(60, 1280, 110))
    bg = f'<rect width="720" height="1280" fill="#E8B879"/>{wood_lines}'
    rules = "".join(f'<line x1="42" y1="{y}" x2="674" y2="{y}" stroke="#A9D2EE" stroke-width="2.2"/>' for y in range(195, 1105, 45))
    holes = "".join(f'<circle cx="78" cy="{y}" r="14" fill="#E6B472" stroke="{DARK}" stroke-width="3.8"/>' for y in (306, 628, 950))
    paper = (
        f'<g transform="rotate(-1.2 360 618)">'
        f'<rect x="48" y="114" width="632" height="1014" rx="8" fill="{DARK}" opacity="0.85"/>'
        f'<rect x="42" y="108" width="632" height="1014" rx="8" fill="#FAF8F0" stroke="{DARK}" stroke-width="5"/>'
        f'{rules}<line x1="138" y1="110" x2="138" y2="1120" stroke="#F0A0B2" stroke-width="3.2"/>{holes}'
        f'<text x="186" y="276" font-family="Caveat Brush" font-size="56" fill="#3B424D">siang = 12 jam</text>'
        f'<text x="186" y="346" font-family="Caveat Brush" font-size="56" fill="#3B424D">malam = 12 jam</text>'
    )
    items, clips, js = [], [], []
    # (text, x, y, size, color, t0, d, width)
    strokes = [
        ("12", 162, 560, 112, "#3B424D", 77.75, 0.45, 130),
        ("+", 340, 560, 112, "#3B424D", 78.25, 0.25, 90),
        ("12", 464, 560, 112, "#3B424D", 78.55, 0.45, 130),
        ("=", 232, 718, 112, "#D62436", 79.15, 0.30, 90),
        ("24", 358, 718, 112, "#D62436", 79.50, 0.50, 145),
    ]
    for k, (txt, x, y, sz, col, t0, d, w) in enumerate(strokes):
        clips.append(f'<clipPath id="nc{k}"><rect id="ncr{k}" x="{x-8}" y="{y-sz*1.1:.0f}" width="0" height="{sz*1.4:.0f}"/></clipPath>')
        items.append(f'<g clip-path="url(#nc{k})"><text x="{x}" y="{y}" font-family="Caveat Brush" font-size="{sz}" fill="{col}">{txt}</text></g>')
        js.append(f'tl.fromTo("#ncr{k}",{{attr:{{width:0}}}},{{attr:{{width:{w}}},duration:{d},ease:"none"}},{t(t0)});')
    circ = f'<ellipse id="nring" cx="424" cy="686" rx="92" ry="56" fill="none" stroke="#D62436" stroke-width="6.5" stroke-linecap="round" pathLength="1" stroke-dasharray="1 1.2" stroke-dashoffset="1.1" transform="rotate(-4 424 686)"/>'
    js.append(f'tl.fromTo("#nring",{{attr:{{"stroke-dashoffset":1.1}}}},{{attr:{{"stroke-dashoffset":0}},duration:0.45,ease:"power1.inOut"}},{t(80.1)});')

    # Cute cartoon hand holding yellow pencil, TIP aligned exactly at (0, 0)!
    pen = (
        f'<g id="penhand">'
        f'<g transform="rotate(42)">'
        f'<rect x="34" y="-42" width="520" height="92" rx="46" fill="#FFFFFF" stroke="{DARK}" stroke-width="5.5"/>'
        f'<rect x="26" y="-26" width="108" height="60" rx="30" fill="#E3B188"/>'
        f'</g>'
        # Yellow pencil body pointing from tip (0,0) up-right to (120, -54)
        f'<g transform="rotate(-24)">'
        f'<polygon points="0,0 24,-9 24,9" fill="#F2D9B1" stroke="{DARK}" stroke-width="3.5" stroke-linejoin="round"/>'
        f'<polygon points="0,0 10,-4 10,4" fill="#3B424D"/>'
        f'<rect x="24" y="-9" width="96" height="18" fill="#F2D25B" stroke="{DARK}" stroke-width="3.5"/>'
        f'<rect x="120" y="-9" width="16" height="18" rx="3" fill="#F29AB0" stroke="{DARK}" stroke-width="3.5"/>'
        f'</g>'
        # Rounded cartoon fist/fingers gripping the pencil cleanly near (34, 14)
        f'<circle cx="42" cy="18" r="34" fill="#E3B188" stroke="{DARK}" stroke-width="4.5"/>'
        f'<circle cx="24" cy="4" r="14" fill="#E3B188" stroke="{DARK}" stroke-width="4"/>'
        f'<path d="M26 28 Q46 42 64 26" fill="none" stroke="{DARK}" stroke-width="3.5" stroke-linecap="round"/>'
        f'</g>'
    )
    # Strictly non-overlapping sequential path for #penhand (0 warnings!)
    pts = [
        (77.40, 620, 820),
        (77.75, 168, 540),
        (78.20, 268, 540),
        (78.25, 344, 540),
        (78.50, 405, 540),
        (78.55, 470, 540),
        (79.00, 570, 540),
        (79.15, 238, 700),
        (79.45, 305, 700),
        (79.50, 366, 700),
        (80.00, 488, 700),
        (80.10, 340, 686),
        (80.32, 430, 632),
        (80.55, 514, 700),
        (80.78, 560, 760),
    ]
    js.append(f'tl.set("#penhand",{{x:{pts[0][1]},y:{pts[0][2]}}},0);')
    for k in range(1, len(pts)):
        t_prev = pts[k - 1][0]
        t_cur, x, y = pts[k]
        dur = max(0.04, round(t_cur - t_prev - 0.01, 3))
        js.append(f'tl.to("#penhand",{{x:{x},y:{y},duration:{dur},ease:"power1.inOut"}},{t(t_prev)});')

    html = f'''<template>
  <style>
    {FONTS_CSS}
    #root {{ position:absolute; inset:0; overflow:hidden; background:#E8B879; }}
    #root svg {{ position:absolute; inset:0; width:100%; height:100%; }}
  </style>
  <div id="root" data-composition-id="note" data-width="{W}" data-height="{H}">
    <svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
      <defs>{"".join(clips)}</defs>
      {bg}{paper}{"".join(items)}{circ}</g>{pen}
    </svg>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join(js)}
    window.__timelines["note"] = tl;
  </script>
</template>
'''
    open(os.path.join(OUT, "note.html"), "w").write(html)


# =========================================================================
# B11: 80.8 - 93.0  (Revolusi Prancis 10-hour clock -> kids laugh -> X + BATAL!)
# =========================================================================
s = Scene("b11", 80.8, 93.0); SCENES.append(s)
s.cam(80.8, CAM_BOARD)
s.cam(87.25, CAM_WIDE, 0.5)
s.cam(89.35, CAM_BOARD, 0.45)
s.eraser_wipe(80.8, 0.55)

s.pointer_mode(80.8, False)
s.pointer_mode(83.9, True)
s.point_at(83.9, 360, 420, 0.0)
s.point_at(84.6, 390, 495, 0.6)
s.point_at(86.0, 405, 535, 0.6)
s.pointer_mode(87.2, False)
s.pointer_mode(89.9, True)
s.point_at(89.9, 395, 575, 0.0)
s.point_at(91.4, 420, 440, 0.5)

cx, cy, r = BCX, 344, 100
s.draw(f'<circle id="b11-face" cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{B}" stroke-width="3.8" pathLength="1" stroke-dasharray="1 1.2" stroke-dashoffset="1.1"/>', 81.15, 0.7)
tk = "".join(f'<line x1="{cx+(r-10)*math.sin(math.radians(a)):.1f}" y1="{cy-(r-10)*math.cos(math.radians(a)):.1f}" x2="{cx+(r-1)*math.sin(math.radians(a)):.1f}" y2="{cy-(r-1)*math.cos(math.radians(a)):.1f}" stroke="{B}" stroke-width="2.4"/>' for a in range(0, 360, 36))
s.pop("b11-tk", tk, 81.8, cx, cy, 0.25, 0.94)
s.text(T("?", P), 478, 258, 56, 81.85, 0.25, plain_len=1)
s.text("REVOLUSI PRANCIS", BCX, 206, 34, 82.8, 1.15, plain_len=16)

# Numbers 1..10 pop clockwise around the 10-hour clock!
for k in range(1, 11):
    a = math.radians((k % 10) * 36)
    nx = cx + (r - 25) * math.sin(a)
    ny = cy - (r - 25) * math.cos(a) + 7
    s.pop(f"b11-n{k}", f'<text x="{nx:.1f}" y="{ny:.1f}" font-family="Caveat Brush" font-size="22" fill="{B}" text-anchor="middle">{k}</text>', 84.1 + (k - 1) * 0.11, nx, ny, 0.14, 0.5)

s.pop("b11-hands", f'<line x1="{cx}" y1="{cy}" x2="{cx-64}" y2="{cy+14}" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/><line x1="{cx}" y1="{cy}" x2="{cx+46}" y2="{cy+8}" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="4" fill="#FFFFFF"/>', 85.2, cx, cy, 0.25, 0.8)
s.text("1 hari = 10 jam", BCX, 496, 28, 84.0, 1.0, fill=B, plain_len=15)
s.text("1 jam = 100 menit", BCX, 534, 28, 85.9, 1.0, fill=B, plain_len=17)
s.text("1793 – 1795", BCX, 574, 28, 89.9, 0.9, fill=P, plain_len=11)

s.draw(line("b11-x1", f"M{cx-86} {cy-86} L{cx+86} {cy+86}", P, 5.5), 91.35, 0.3)
s.draw(line("b11-x2", f"M{cx+86} {cy-86} L{cx-86} {cy+86}", P, 5.5), 91.65, 0.3)
s.stamp("b11-batal", "BATAL!", cx, cy, 134, 52, P, 92.25, -8, 38)
s.students_laugh(87.4, 89.5)
s.teacher_talk(81.2, 87.2); s.teacher_talk(89.9, 92.6)

# =========================================================================
# B12: 93.0 - 99.0  (1 jam = 60 menit + wall clock gold glow + matematika -> wide cheer + bell!)
# =========================================================================
s = Scene("b12", 93.0, 99.0); SCENES.append(s)
s.cam(93.0, CAM_BOARD)
s.cam(93.8, CAM_RIGHT_MED, 0.55)       # reveals teacher beside board!
s.cam(97.45, CAM_WIDE, 0.5)            # smooth zoom out to FULL wide cheering finale!
s.eraser_wipe(93.0, 0.5)

s.pointer_mode(93.0, False)
s.pointer_mode(93.9, True)
s.point_at(93.9, 325, 492, 0.0)
s.point_at(94.5, 365, 190, 0.45)       # points UP toward the glowing golden wall clock!
s.point_at(95.8, 395, 340, 0.45)       # points back to "matematika umur ribuan tahun"
s.pointer_mode(97.45, False)

s.text("1 jam = 60 menit", BCX, 224, 38, 93.25, 0.95, plain_len=16)
# Small centered chalk clock at bottom of board (matching f_98.5.png!)
ckx, cky, ckr = BCX, 496, 46
s.draw(f'<circle id="b12-ck" cx="{ckx}" cy="{cky}" r="{ckr}" fill="none" stroke="#FFFFFF" stroke-width="3.2" pathLength="1" stroke-dasharray="1 1.2" stroke-dashoffset="1.1"/>', 93.9, 0.45)
ck_tk = "".join(f'<line x1="{ckx+(ckr-6)*math.sin(math.radians(a)):.1f}" y1="{cky-(ckr-6)*math.cos(math.radians(a)):.1f}" x2="{ckx+(ckr-1)*math.sin(math.radians(a)):.1f}" y2="{cky-(ckr-1)*math.cos(math.radians(a)):.1f}" stroke="#FFFFFF" stroke-width="2"/>' for a in range(0, 360, 30))
s.pop("b12-ckh", ck_tk + f'<line x1="{ckx}" y1="{cky}" x2="{ckx}" y2="{cky-28}" stroke="{Y}" stroke-width="3.6" stroke-linecap="round"/><line x1="{ckx}" y1="{cky}" x2="{ckx+26}" y2="{cky+14}" stroke="{Y}" stroke-width="3.6" stroke-linecap="round"/>', 94.35, ckx, cky, 0.25, 0.85)

s.gold_clock(94.85)
s.text("matematika", BCX, 326, 62, 95.85, 0.8, fill=Y, plain_len=10)
s.text("umur ribuan tahun", BCX, 396, 36, 96.65, 0.85, plain_len=17)
s.draw(line("b12-u1", "M172 414 Q325 422 478 412", Y, 3.4), 97.25, 0.35)
s.draw(line("b12-u2", "M186 423 Q325 430 464 421", Y, 2.2), 97.4, 0.3)

s.teacher_talk(93.3, 97.8)
s.ring_bell(97.95)
for i in range(3):
    s.student_cheer(i, 97.9 + i * 0.05, bounce_reps=4)

# =========================================================================
# CAPTIONS (exact timing & yellow highlight matching all 17 sheets!)
# =========================================================================
CAPS = [
 (0.0, 1.0, "Kenapa [1 jam]"), (1.0, 2.5, "itu [60 menit?]"), (2.5, 3.5, "Kenapa nggak [100]"), (3.5, 4.95, "[biar] gampang?"),
 (4.95, 6.5, "Jawabannya ada [di]"), (6.5, 7.5, "zaman [kuno]"), (7.5, 9.0, "Lebih dari [4.000]"), (9.0, 10.0, "tahun [lalu] di"),
 (10.0, 11.4, "[Mesopotamia]"), (11.4, 12.6, "Orang [Sumeria]"), (12.6, 13.9, "lalu [Babilonia]"), (13.9, 15.0, "ngitung [pakai]"),
 (15.0, 16.4, "[basis 60]"), (16.4, 17.0, "bukan [10] kayak"), (17.0, 17.9, "[kita]"), (17.9, 19.4, "Kenapa [60?]"),
 (19.4, 20.4, "Karena dia [gampang]"), (20.4, 21.5, "[banget] dibagi"), (21.5, 23.5, "Dibagi [2 3]"), (23.5, 26.0, "[4 5 6]"),
 (26.0, 28.5, "10 12 [15]"), (28.5, 30.0, "20 [30]"), (30.0, 31.0, "Semua [hasilnya]"), (31.0, 31.6, "[bulat]"),
 (31.6, 33.0, "Coba [100]"), (33.0, 34.0, "Dibagi [3]"), (34.0, 37.3, "[33,333...]"), (37.3, 38.5, "Nggak [abis-abis]"),
 (38.5, 40.5, "Makanya [setengah]"), (40.5, 42.0, "jam itu [30]"), (42.0, 42.5, "[menit]"), (42.5, 44.0, "Sepertiga jam [20]"),
 (44.0, 44.5, "[menit]"), (44.5, 46.0, "[Rapi]"), (46.0, 47.0, "Ada juga [teori]"), (47.0, 47.9, "yang [seru]"),
 (47.9, 48.5, "Coba lihat [jari]"), (48.5, 49.0, "[kamu]"), (49.0, 50.5, "Tiap jari [punya]"), (50.5, 51.5, "[3 ruas]"),
 (51.5, 53.3, "4 jari [jadi]"), (53.3, 54.5, "[12 ruas]"), (54.5, 55.5, "[jempol]"), (55.5, 56.5, "Tangan [satunya]"),
 (56.5, 57.0, "nyimpen [berapa]"), (57.0, 58.6, "kali [12?]"), (58.6, 60.4, "[5 jari 12]"), (60.4, 62.5, "kali 5 [60]"),
 (62.5, 63.5, "Tapi [ini] baru"), (63.5, 65.0, "[teori] ya belum"), (65.0, 66.3, "ada [bukti] pasti"), (66.3, 68.0, "Terus [kenapa]"),
 (68.0, 69.5, "sehari [24 jam?]"), (69.5, 70.5, "Itu dari [Mesir]"), (70.5, 71.5, "[kuno]"), (71.5, 73.0, "Siang [dibagi 12]"),
 (73.0, 74.9, "malam [juga 12]"), (74.9, 75.5, "Ngikutin [bintang]"), (75.5, 76.5, "yang [muncul satu]"), (76.5, 77.9, "[per satu]"),
 (77.9, 79.6, "12 tambah [12]"), (79.6, 80.8, "[24]"), (80.8, 81.5, "Pernah ada [yang]"), (81.5, 82.5, "coba [ganti lho]"),
 (82.5, 83.5, "Waktu [Revolusi]"), (83.5, 84.5, "Prancis [sehari]"), (84.5, 86.0, "dibikin [10 jam]"), (86.0, 87.5, "Sejam [100 menit]"),
 (87.5, 89.8, "Nggak [laku belum]"), (89.8, 91.5, "sampai [2 tahun]"), (91.5, 93.0, "udah [dibatalin]"), (93.0, 94.3, "Jadi [tiap kamu]"),
 (94.3, 95.3, "lihat [jam kamu]"), (95.3, 95.9, "lagi [pakai]"), (95.9, 96.6, "[matematika] umur"), (96.6, 97.9, "[ribuan tahun]"),
]


def build_caps():
    divs, js = [], []
    for i, (a, b, txt) in enumerate(CAPS):
        html = re.sub(r"\[(.+?)\]", r"<em>\1</em>", txt)
        divs.append(f'<div id="cp{i}" class="cap clip" data-start="{a}" data-duration="{b-a:.3f}"><span class="pill">{html}</span></div>')
        js.append(f'tl.fromTo("#cp{i}",{{opacity:0,y:8,scale:0.94}},{{opacity:1,y:0,scale:1,duration:0.09,ease:"back.out(2)"}},{a});')
    # Single-line punchy climax matching f_98.5.png!
    divs.append('<div id="capbig" class="clip" data-start="97.9" data-duration="1.1">1 JAM = <em>60 MENIT</em></div>')
    js.append('tl.fromTo("#capbig",{opacity:0,scale:0.55},{opacity:1,scale:1,duration:0.28,ease:"back.out(2.2)"},97.9);')
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
    open(os.path.join(OUT, "caps.html"), "w").write(html)


def build_index():
    order = [
        ("b1", 0.0, 4.95), ("b2", 4.95, 11.4), ("b3", 11.4, 17.9), ("b4", 17.9, 31.6),
        ("b5", 31.6, 38.5), ("b6", 38.5, 46.0), ("b7", 46.0, 49.0), ("hands", 49.0, 59.92),
        ("b8", 59.92, 66.3), ("b9", 66.3, 77.4), ("note", 77.4, 80.8), ("b11", 80.8, 93.0),
        ("b12", 93.0, 99.0),
    ]
    hosts = "\n".join(
        f'      <div id="{i}" data-composition-id="{i}" data-composition-src="compositions/{i}.html" '
        f'data-start="{a}" data-duration="{b-a:.3f}" data-track-index="1" data-track-kind="graphics" '
        f'data-width="{W}" data-height="{H}"></div>'
        for i, a, b in order
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
    <div id="root" data-composition-id="main" data-start="0" data-duration="99" data-width="{W}" data-height="{H}" data-fps="30">
{hosts}
      <div id="caps" data-composition-id="caps" data-composition-src="compositions/caps.html" data-start="0" data-duration="99" data-track-index="2" data-track-kind="captions" data-width="{W}" data-height="{H}"></div>
      <audio id="orig-audio" src="assets/audio.m4a" data-start="0" data-duration="99"></audio>
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
    open("index.html", "w").write(html)


if __name__ == "__main__":
    for sc in SCENES:
        sc.build()
    build_hands()
    build_note()
    build_caps()
    build_index()
    print("built:", [x.p for x in SCENES] + ["hands", "note", "caps"])
