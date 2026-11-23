---
name: classroom-chalkboard-explainer
description: >-
  Make a vertical (9:16, 720x1280) Indonesian classroom chalkboard animated explainer video in HyperFrames using the exact locked flat-vector classroom rig (batik teacher with active pointer stick, 3 SD students, 12-tick wall clock, dual red-white bunting, green chalkboard with porous chalk texture and animated eraser, smooth unified 2D camera pan/zooms, ruled pencil notebook, and Fredoka pill captions). Use when asked for a mograph/explainer in the style of galeri-mograph-papan or "bikin video papan tulis / guru batik".
---

# Classroom Chalkboard Explainer (Locked Reusable Rig)

This skill bundles the **exact, verified classroom rig, fonts, and templates** so every new episode preserves the **identical visual identity and animation mechanics** with zero drift.

> **STRICT LOCK RULE — DO NOT REDRAW FROM SCRATCH:**
> Never hand-code replacement SVGs for the classroom, bunting, wall clock, chalkboard, teacher desk, batik teacher, 3 students, eraser, cloud bubbles, ruled notebook, or caption pills. Always scaffold from [scripts/scaffold.py](./scripts/scaffold.py) and import the locked [scripts/classroom_lib.py](./scripts/classroom_lib.py) and [scripts/reusable_templates.py](./scripts/reusable_templates.py) verbatim, using the bundled fonts in `assets/fonts/`.

Read `/hyperframes` first for the HyperFrames render contract (`plugin-cli.mjs` launcher, paused GSAP timelines, no overlapping tweens, `check --json`, `snapshot`, `render`).

---

## Bundled Files (Locked Identity)

- [scripts/scaffold.py](./scripts/scaffold.py) — Bootstraps a new project directory with the locked rig, templates, fonts, and HyperFrames config.
- [scripts/classroom_lib.py](./scripts/classroom_lib.py) — Unified 720×1280 classroom world stage (`Scene`, smooth camera presets, pointer stick rig, back-and-forth eraser wipe, porous chalk filter, teacher & 3 SD student expressions, fluffy cloud bubbles, `HA!` laugh, cheering 5-finger arms, golden wall clock glow, ringing school bell).
- [scripts/reusable_templates.py](./scripts/reusable_templates.py) — Locked `build_captions()`, `build_index()`, `build_notebook_scene()`, and chalkboard pictograms (`sun_svg`, `moon_svg`, `star_svg`, `brick_pyr`, `CHALK_HAND`).
- `assets/fonts/caveat-brush.ttf` (289 KB) & `assets/fonts/fredoka.ttf` (156 KB) — Copied offline by `scaffold.py` (both well under the 2 MB inline limit).
- [examples/build_episode_1jam_60menit.py](./examples/build_episode_1jam_60menit.py) — Complete verified 99-second reference episode demonstrating every beat type (clock zoom intro, river map, tablet, divisor chips, wall-overflow text gag, clock slices, stamps, 2-hand counter, pyramids + 12 stars, pencil notebook, crossed-out 10-hour clock, golden clock + bell + cheering finale).

---

## Locked Visual & Motion Rules (Never Change)

1. **Canvas & fps:** `720×1280` (9:16), `30 fps` (`60 fps` only if explicitly requested).
2. **Unified world coordinates (no teleporting characters):**
   - Chalkboard interior: `x = 130..520` (`BCX = 325`), `y = 154..600` (`BCY = 377`). Author all board drawings inside `x ∈ [142, 508]`, `y ∈ [172, 586]`.
   - Teacher stands at `cx = 632` with clear round glasses (NO white fill), kawung batik shirt, and dual right-arm rig: vertical resting stick (`pointer_mode(t, False)`) in wide shots, active aiming pointer (`pointer_mode(t, True)` + `point_at(t, bx, by, dur)`) during board close-ups.
   - 3 SD students sit in foreground (`st0` girl with red bow at `cx=90`, `st1` center boy at `cx=324`, `st2` right boy with cowlick at `cx=562`).
   - **Reserved ID warning:** Never name custom board elements `<scene>-st0`, `<scene>-st1`, or `<scene>-st2` — those IDs belong to the 3 students (`classroom_lib.py`). Use `<scene>-star0` etc. instead.
3. **Smooth 2D camera presets** (`s.cam(global_t, preset, duration)` with `0.45–0.6s`, `power2.inOut`):
   - `CAM_WIDE` `(1.0, 360, 640)` — full classroom (window, bell, board, teacher, 3 students).
   - `CAM_BOARD` `(1.66, 325, 412)` — board close-up (clock at top, teacher desk at bottom, teacher's pointer arm entering from right edge).
   - `CAM_CLOCK` `(2.8, 325, 130)` — tight intro shot on wall clock.
   - `CAM_RIGHT_MED` `(1.32, 428, 535)` — board + teacher standing beside it.
   - `CAM_TEACHER` `(1.66, 515, 445)` — right pan framing board right edge + teacher (ideal for wall-overflow gags using `free=True, stroke=DARK, sw=7`).
   - `CAM_BOY_MID` `(2.35, 324, 920)` / `CAM_GIRL` `(2.35, 135, 935)` — student close-ups.
4. **Board transitions:** Start every new chalkboard topic with `s.eraser_wipe(t0, 0.55)` (hides resting tray eraser, sweeps horizontally back-and-forth, fades translucent smudge bars & dust dots).
5. **Typography & Captions:**
   - Chalkboard & notebook handwriting: `'Caveat Brush'`.
   - Captions & callout pills: `'Fredoka'` weight 700.
   - Captions via `build_captions(caps, climax_html, climax_start, climax_dur)`: pill `#1F1812` at `top: 1042px`, 2–4 words per beat, wrap emphasized word in `[brackets]` for `#F2D45C` yellow; finale single-line climax at `top: 780px`.
6. **Zero overlapping GSAP tweens:** Chain sequential `.to()` animations with strictly non-overlapping timestamps, and use `repeat: N, yoyo: true` instead of looped `fromTo()` calls on the same element.

---

## Step-by-Step Workflow

### 1. Brief
Confirm only what is missing: topic & core question, target length (30–100 s), language (default Indonesian), and audio mode (silent, user-provided `assets/audio.m4a`, or voiceover via `/media-use`).

### 2. Scaffold the Project
Let `<SKILL_DIR>` be the folder containing this `SKILL.md` (e.g. `~/.agents/skills/classroom-chalkboard-explainer`):
```bash
python3 "<SKILL_DIR>/scripts/scaffold.py" <project_dir>
```

### 3. Write `build_episode.py`
Inside `<project_dir>`, write `build_episode.py` importing `Scene`, camera presets, `ell`, `line`, `T` from `classroom_lib`, and `build_captions`, `build_index`, `build_notebook_scene`, pictograms from `reusable_templates`. Follow the narrative arc of [examples/build_episode_1jam_60menit.py](./examples/build_episode_1jam_60menit.py):
1. **Hook:** Clock zoom-out → main question on board → student raises hand + `cloud_bubble`.
2. **Core explanation:** Smooth camera pans + live chalk write-on (`s.text`, `s.draw`, `s.pop`) tracked by `s.point_at`.
3. **Visual proof / gag:** Diagram (pie/clock slices, chips, comparison, or wall-overflow `free=True` gag) + `s.stamp` verdict (`RAPI!`, `TEORI`, `BATAL!`) + `s.students_laugh`.
4. **Alternate angle (optional):** `build_notebook_scene(...)` for step-by-step arithmetic/notes with the pencil hand, or a top-down hands scene (see `build_hands()` in the example).
5. **Finale:** `s.gold_clock` + `s.ring_bell` + `CAM_WIDE` + all 3 `s.student_cheer` + single-line `climax_html` caption.

Run `python3 build_episode.py` to generate `compositions/*.html` and `index.html`.

### 4. Validate, Visually Inspect, and Render
Always run the HyperFrames CLI through its launcher (`<SKILLS>/hyperframes/scripts/plugin-cli.mjs`) inside `<project_dir>`, ensuring `ffmpeg` and `ffprobe` are available on `PATH` and `HYPERFRAMES_CACHE_DIR` points to a private `chmod 700` directory if `~/.cache` is group-writable:

```bash
cd <project_dir>
export HYPERFRAMES_CACHE_DIR="$HOME/.hf-cache"
mkdir -p -m 700 "$HYPERFRAMES_CACHE_DIR"
L="$HOME/.agents/skills/hyperframes/scripts/plugin-cli.mjs"

# 1. Check (must have 0 lint, runtime, and layout errors)
node "$L" check --json

# 2. Snapshot every scene beat and visually inspect the contact sheet(s)
node "$L" snapshot --at <comma-separated-timestamps>

# 3. Render final MP4
node "$L" render -o <output>.mp4 --fps 30
```

Inspect every generated contact sheet before rendering to verify text bounds inside the board (`x ∈ [142, 508]`), pointer alignment, character visibility, and caption sync.
