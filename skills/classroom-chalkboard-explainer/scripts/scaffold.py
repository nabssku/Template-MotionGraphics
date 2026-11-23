#!/usr/bin/env python3
"""Bootstrap a new HyperFrames classroom-chalkboard-explainer project with locked assets & rig.

Usage:
  python3 "<SKILL_DIR>/scripts/scaffold.py" <project_dir>
"""
import os, sys, json, shutil

SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def scaffold(project_dir):
    project_dir = os.path.abspath(project_dir)
    os.makedirs(os.path.join(project_dir, "assets", "fonts"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "assets", "sfx"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "compositions"), exist_ok=True)

    # Copy locked fonts verbatim (no network download required, zero drift)
    for fn in ("caveat-brush.ttf", "fredoka.ttf"):
        shutil.copy2(
            os.path.join(SKILL_ROOT, "assets", "fonts", fn),
            os.path.join(project_dir, "assets", "fonts", fn),
        )

    # Copy locked classroom SFX + soft BGM loop verbatim (offline, zero drift)
    sfx_src = os.path.join(SKILL_ROOT, "assets", "sfx")
    if os.path.isdir(sfx_src):
        for fn in sorted(os.listdir(sfx_src)):
            if fn.endswith(".mp3"):
                shutil.copy2(os.path.join(sfx_src, fn), os.path.join(project_dir, "assets", "sfx", fn))

    # Copy locked classroom rig, reusable templates, and audio mixer verbatim
    for fn in ("classroom_lib.py", "reusable_templates.py", "audio_mix.py"):
        shutil.copy2(
            os.path.join(SKILL_ROOT, "scripts", fn),
            os.path.join(project_dir, fn),
        )

    name = os.path.basename(project_dir)
    hf_json = os.path.join(project_dir, "hyperframes.json")
    if not os.path.exists(hf_json):
        open(hf_json, "w").write(json.dumps({
            "version": 1,
            "entry": "index.html",
            "width": 720,
            "height": 1280,
            "fps": 30,
        }, indent=2) + "\n")

    meta_json = os.path.join(project_dir, "meta.json")
    if not os.path.exists(meta_json):
        open(meta_json, "w").write(json.dumps({
            "name": name,
            "skill": "classroom-chalkboard-explainer",
        }, indent=2) + "\n")

    pkg_json = os.path.join(project_dir, "package.json")
    if not os.path.exists(pkg_json):
        open(pkg_json, "w").write(json.dumps({
            "name": name,
            "private": True,
            "type": "module",
            "scripts": {
                "dev": "npx --yes hyperframes preview",
                "check": "npx --yes hyperframes check",
                "render": "npx --yes hyperframes render",
            },
        }, indent=2) + "\n")

    print(f"Scaffolded locked classroom-chalkboard-explainer project at: {project_dir}")
    print("Files installed: classroom_lib.py, reusable_templates.py, assets/fonts/{caveat-brush.ttf,fredoka.ttf}")
    print("Next: write build_episode.py importing classroom_lib & reusable_templates, run python3 build_episode.py, then hyperframes check / snapshot / render.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scaffold.py <project_dir>", file=sys.stderr)
        sys.exit(1)
    scaffold(sys.argv[1])
