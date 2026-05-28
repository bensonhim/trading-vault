---
title: "Trading Vault"
date: 2026-05-26
tags: [trading, vault]
---

# Welcome to Trading Vault

This is a dedicated Obsidian vault for trading content analysis.

## Structure

| Folder | Purpose |
|--------|---------|
| `transcripts/` | Generated transcripts from YouTube and local media |
| `notes/` | Your analysis, insights, and backlinks |
| `resources/` | Screenshots, charts, and reference materials |

## How to Use

1. Run `python .trading/transcribe.py --url "..." --lang en` to generate transcripts
2. Read transcripts in the `transcripts/` folder
3. Create notes in `notes/` and link back to relevant transcripts using `[[filename]]`
4. Tag entries with `#ticker #strategy #language` for easy filtering

## Example Note

```markdown
---
title: "SPY Analysis May 2026"
date: 2026-05-26
tags: [SPY, technical-analysis, en]
---

Key points from [[SPY_Market_Update_2026-05-26_whisper]]:

- Support at $510, resistance at $525
- RSI showing divergence on 4H
- Volume declining — caution

#SPY #technical-analysis
```

## Backlinks

Use Obsidian's graph view to see connections between transcripts and your notes.
