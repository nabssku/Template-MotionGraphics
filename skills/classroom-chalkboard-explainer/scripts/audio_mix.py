#!/usr/bin/env python3
"""Locked classroom audio mixer (VO + synced SFX cues + optional soft looping BGM)
for the classroom-chalkboard-explainer HyperFrames skill.
Uses sample-exact float32 stereo mixing (48 kHz) via stdlib array + ffmpeg encode,
avoiding ffmpeg version quirks and amix volume pumping."""
import os, math, array, subprocess

SR = 48000
DEFAULT_GAINS = {
    "chalk":  0.34,
    "eraser": 0.48,
    "whoosh": 0.36,
    "pop":    0.50,
    "stamp":  0.68,
    "pencil": 0.48,
    "drop":   0.52,
    "tick":   0.42,
    "laugh":  0.44,
    "chime":  0.55,
    "bell":   0.52,
    "cheer":  0.50,
}


def _decode_f32_stereo(path):
    """Decode any audio file to interleaved float32 stereo PCM at 48 kHz."""
    proc = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-f", "f32le", "-acodec", "pcm_f32le", "-ar", str(SR), "-ac", "2", "pipe:1"],
        stdout=subprocess.PIPE, check=True,
    )
    buf = array.array("f")
    buf.frombytes(proc.stdout)
    return buf


def mix_episode_audio(
    total_dur,
    cues,
    vo_path="assets/vo.mp3",
    bgm_path="assets/sfx/bgm.mp3",
    sfx_dir="assets/sfx",
    out_path="assets/audio_mix.m4a",
    vo_gain=1.0,
    bgm_gain=0.11,
):
    """Mix VO + optional looping BGM + timed SFX cues into a 48 kHz stereo AAC track.

    cues: list of (time_sec, sfx_name) or (time_sec, sfx_name, gain)
    """
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    n_frames = int(round(total_dur * SR))
    mix = array.array("f", [0.0]) * (n_frames * 2)

    # 1. Gentle looping BGM with smooth fade-in (0.6s) & fade-out (1.2s)
    if bgm_path and bgm_gain > 0 and os.path.exists(bgm_path):
        bgm = _decode_f32_stereo(bgm_path)
        blen = len(bgm) // 2
        if blen > 0:
            fin = int(0.6 * SR)
            fout = int(1.2 * SR)
            fout_start = max(0, n_frames - fout)
            for f in range(n_frames):
                env = bgm_gain
                if f < fin:
                    env *= f / fin
                elif f > fout_start:
                    env *= max(0.0, (n_frames - f) / fout)
                bi = (f % blen) * 2
                mi = f * 2
                mix[mi] += bgm[bi] * env
                mix[mi + 1] += bgm[bi + 1] * env

    # 2. VO track
    if vo_path and os.path.exists(vo_path):
        vo = _decode_f32_stereo(vo_path)
        lim = min(len(vo), len(mix))
        g = vo_gain
        for i in range(lim):
            mix[i] += vo[i] * g

    # 3. Synced SFX cues (decode each unique SFX file only once!)
    sfx_cache = {}
    for cue in cues:
        if len(cue) == 2:
            t_sec, name = cue
            gain = DEFAULT_GAINS.get(name, 0.45)
        else:
            t_sec, name, gain = cue
        if name not in sfx_cache:
            fpath = os.path.join(sfx_dir, f"{name}.mp3")
            if not os.path.exists(fpath):
                raise FileNotFoundError(f"Missing SFX clip: {fpath}")
            sfx_cache[name] = _decode_f32_stereo(fpath)
        clip = sfx_cache[name]
        start_idx = max(0, int(round(t_sec * SR))) * 2
        end_idx = min(len(mix), start_idx + len(clip))
        for j in range(end_idx - start_idx):
            mix[start_idx + j] += clip[j] * gain

    # 4. Smooth soft-knee limiter above 0.85 so peaks never hard-clip
    for i in range(len(mix)):
        v = mix[i]
        av = abs(v)
        if av > 0.85:
            over = av - 0.85
            clamped = 0.85 + 0.11 * math.tanh(over / 0.11)
            mix[i] = clamped if v > 0 else -clamped

    # 5. Encode stereo float32 PCM -> 48 kHz AAC 192 kbps
    subprocess.run(
        [
            "ffmpeg", "-v", "error", "-y",
            "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "pipe:0",
            "-c:a", "aac", "-b:a", "192k", "-ar", str(SR), "-ac", "2",
            out_path,
        ],
        input=mix.tobytes(),
        check=True,
    )
    return out_path
