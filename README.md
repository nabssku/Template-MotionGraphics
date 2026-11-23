# Template-MotionGraphics

Kumpulan skill template motion graphics siap pakai untuk HyperFrames & AI coding agent (Antigravity, Claude Code, Codex, Cursor, dll.).

Setiap skill di folder `skills/` mengunci aset visual, font, rig SVG, dan mekanik animasinya secara penuh agar hasil setiap episode baru selalu konsisten.

## Pasang Semua Skill

```bash
npx skills add nabssku/Template-MotionGraphics
```

Atau pasang satu skill tertentu:

```bash
npx skills add nabssku/Template-MotionGraphics --skill classroom-chalkboard-explainer
```

## Daftar Skill Tersedia

| Skill | Format | Gaya & Komponen Terkunci | Path |
| --- | --- | --- | --- |
| `classroom-chalkboard-explainer` | 720×1280 (9:16), 30 fps | Kelas papan tulis flat-vector Indonesia: guru batik + kacamata bening + tongkat penunjuk aktif, 3 murid SD ekspresif, papan tulis kapur berpori + penghapus bolak-balik, kamera 2D terpadu, buku catatan pensil, font `Caveat Brush` & `Fredoka`, caption pill TikTok/Reels, plus paket 12 SFX kelas & BGM lembut (`audio_mix.py`). | [skills/classroom-chalkboard-explainer](./skills/classroom-chalkboard-explainer/SKILL.md) |

## Cara Menambah Skill Baru

Setiap kali menganalisis gaya video motion graphics baru, simpan di folder baru di bawah `skills/<nama-skill>/` dengan struktur standar:

```text
skills/<nama-skill>/
├── SKILL.md        # Panduan & aturan visual terkunci (frontmatter name + description)
├── assets/         # Font & aset offline
├── scripts/        # Rig SVG/HTML terkunci + scaffold.py
└── examples/       # Contoh episode lengkap terverifikasi
```

Lalu tambahkan baris baru ke tabel **Daftar Skill Tersedia** di atas.
