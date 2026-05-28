---
title: Transcription Engine — Design Notes
date: 2026-05-27
tags: [trading, transcription, architecture, design]
---

# Trading Transcription Engine — Design Notes

## Overview

A 3-layer transcription pipeline that turns YouTube videos and local audio/video files into clean `.md` transcripts with auto-generated bullet-point summaries, stored in an Obsidian vault for trading analysis.

**Location:** `D:/opencodeworkspace/.trading/`
**Vault:** `C:/Users/%USERPROFILE%/Documents/Obsidian/trading-vault/`

---

## Architecture

```
Input: YouTube URL or local file
         │
         ├── Layer 1: YouTube subtitles (fastest, free)
         │    yt-dlp --write-auto-sub --write-sub
         │    Supports: en, en-GB, en-US, en-orig, zh, yue, etc.
         │         │
         ├── Layer 2: faster-whisper (local, CPU/GPU)
         │    ffmpeg extract → chunk_audio.py (10-min segments)
         │    large-v3, int8, beam_size=5
         │    Resume support via progress.json
         │         │
         └── Layer 3: Deepgram (cloud fallback)
              Nova-3 Multilingual, requests POST directly
              ~50x faster than CPU Whisper
         │
         ▼
    merge_transcripts.py
    ┌───────────────────────────────────────┐
    │ 1. Clean text (strip &nbsp;,         │
    │    normalize whitespace)              │
    │ 2. Build flowing paragraphs         │
    │    (merge fragments into sentences) │
    │ 3. Extractive summary               │
    │    (keyword-dense bullets)          │
    │ 4. YAML frontmatter + full text     │
    └───────────────────────────────────────┘
         │
         ▼
    C:/.../trading-vault/transcripts/
    Channel - Video Title_{backend}.md
```

---

## File Map

| File | Purpose | Key Features |
|------|---------|-------------|
| `transcribe.py` | **Main CLI** | `argparse`, auto-detects YouTube vs local, routes to layers, auto-fetches video title/channel |
| `chunk_audio.py` | Audio chunking | 10-min chunks + 5s overlap, `progress.json` resume, `ffprobe` duration detection |
| `merge_transcripts.py` | Output builder | Flowing paragraphs, YAML frontmatter, calls `summarize_text.py` |
| `summarize_text.py` | Summary engine | Extractive keyword scoring, stop-word filtering, deduplication |
| `config.json` | Defaults | Backend, model, language, chunking params, device (`cpu`/`cuda`) |
| `requirements.txt` | Dependencies | `yt-dlp`, `faster-whisper`, `requests`, `pyyaml`, `opencc` |

---

## Why No PowerShell Wrapper?

Originally planned `transcribe.ps1` as a CLI wrapper, but dropped it because:
- Python already handles `argparse` natively
- One less layer to maintain
- Works identically on Windows + macOS + Linux
- Direct `python transcribe.py --url ... --lang yue` is clean

---

## Layer Behavior

### Layer 1: YouTube Subtitles (Always Tried First)

**When it works:** Video has manual or auto-generated subtitles in supported languages.

**Language search order:**
1. `en`, `en-US`, `en-GB`, `en-orig`
2. `zh-Hant`, `zh`, `zh-CN`, `zh-Hans`, `zh-TW`, `zh-HK`
3. `yue`
4. `".*"` (any language wildcard fallback)

**Output:** Direct `.vtt`/`.srt` → instant merge, no audio download.

### Layer 2: faster-whisper (Local)

**When it runs:** No subtitles found, or user forces `--force-whisper`.

**Process:**
1. `yt-dlp` downloads best audio → WAV (16kHz mono)
2. `ffmpeg` extracts audio from video files
3. `chunk_audio.py` splits into 10-min WAV chunks
4. `faster-whisper` transcribes each chunk with `condition_on_previous_text`
5. Per-chunk progress tracked in `progress.json`
6. All chunks merged into final `.md`

**Performance (home AMD workstation):**
- `large-v3` on CPU (`int8`): ~5-10 min per 10-min chunk
- `large-v3` on GPU (if ROCm/DirectML): ~30 sec per chunk (TBD)

### Layer 3: Deepgram (Cloud)

**When it runs:** User forces `--force-deepgram`, or Whisper fails.

**Endpoint:** `https://api.deepgram.com/v1/listen` via `requests.POST`

**Rate:** ~50x faster than CPU Whisper (near real-time).

**Cost:** ~$0.0043/min ($200 credit ≈ 800 hrs).

---

## Output Format

Each transcript is a `.md` file:

```markdown
---
title: 'Channel - Video Title'
source: 'https://youtube.com/watch?v=...'
language: en
backend: youtube_subs
duration_seconds: 3720
tags:
  - transcript
  - en
  - youtube_subs
---

# Channel - Video Title

## Summary

- Key concept 1 from the video (keyword-dense sentence)
- Key concept 2
- ...

## Full Transcript

This is a flowing paragraph. Sentences that span multiple subtitle cues
are merged into continuous text so it's readable like a blog post.

Another paragraph here. The text has been cleaned of HTML entities
and whitespace normalized.
```

**Filename:** `{sanitized_title}_{backend}.md`

---

## Configuration (`config.json`)

Key settings to know:

| Key | Default | When to Change |
|-----|---------|---------------|
| `whisper.device` | `cpu` | Set to `cuda` on NVIDIA GPU |
| `whisper.compute_type` | `int8` | `fp16` on GPU with VRAM |
| `whisper.cpu_threads` | `8` | Match CPU cores |
| `chunking.chunk_duration_sec` | `600` | Lower for more frequent resume |
| `chunking.overlap_sec` | `5` | Increase if sentences get cut at boundaries |
| `output.default_language` | `en` | `yue` for Cantonese, `zh` for Mandarin |

---

## Resume Behavior

When a transcription crashes mid-way (e.g., power loss, network timeout):

1. Re-run the same command
2. `chunk_audio.py` scans `progress.json` in the chunk temp dir
3. Already-completed chunks are skipped
4. Transcription resumes from the next pending chunk

**No data lost** — only the currently-processing 10-min chunk needs restart.

---

## Hardware Strategy

| Workstation | Use Case |
|-------------|----------|
| **Office** (no GPU) | Layer 1 (subs) + Layer 3 (Deepgram). Layer 2 works but is slow (~1 hr for 1 hr video) |
| **Home** (AMD 8060S) | Layer 2 on CPU via `int8`. Investigate ROCm/DirectML for GPU speedup later |

**Rule of thumb:**
- Short clips (< 15 min): Whisper CPU is fine
- Long videos (> 15 min): Default to Deepgram on office, Whisper on home GPU if available

---

## Roadmap / Backlog

| Priority | Item | Status |
|----------|------|--------|
| High | Test Deepgram end-to-end (env var needs new shell) | ⏳ Blocked on shell restart |
| High | Test Whisper on home workstation (AMD) | ⏳ Needs model download |
| Medium | AssemblyAI Layer 4 backup | ⏳ Deferred — Deepgram credit sufficient |
| Low | ROCm / DirectML for AMD GPU | 🔮 Future optimization |
| Low | Auto-tagging (extract tickers, strategy names) | 🔮 Future enhancement |

---

## Quick Commands

```powershell
# Default: subtitles first, then Whisper
py transcribe.py --url "https://youtube.com/watch?v=..." --lang en

# Force subtitles skip, go straight to Whisper
py transcribe.py --url "..." --lang en --force-whisper

# Force cloud (fast, no local compute)
py transcribe.py --url "..." --lang en --force-deepgram

# Local audio file
py transcribe.py --file "C:\audio\interview.mp3" --lang yue --backend whisper

# Convert Simplified → Traditional Chinese
py transcribe.py --url "..." --lang zh --to-traditional
```

---

## References

- [[Welcome]] — Vault overview and folder structure
- [[Transcripts Index]] — Auto-generated index of all transcripts (coming soon)
- `D:/opencodeworkspace/.trading/README.md` — Full technical documentation
- `D:/opencodeworkspace/.trading/STATUS.md` — Live build status
