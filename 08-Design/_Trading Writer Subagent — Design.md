---
title: "Trading Writer Subagent — Design Document"
date: 2026-06-10
tags: [opencode, agent, subagent, trading, trading-writer, architecture, design]
---

# Trading Writer Subagent — Design Document

> **Status**: Implemented
> **Date**: 2026-06-10
> **Related**: `opencode.json`, `.opencode/agents/trading-writer.md`, `.opencode/skills/trading-summary/SKILL.md`, `AGENTS.md`

---

## Problem Statement

The build agent (kimi-k2.6) is excellent at programming and pipeline operations but produces shallow, extractive trading notes. The docs-writer agent (glm-5.1) is better at prose but has zero domain knowledge about trading.

When the pipeline auto-generates curated notes from StockBee meeting transcripts, common errors include:

| Error | Example | Root Cause |
|-------|---------|------------|
| Setup abbreviations treated as tickers | `[[EP]]` (147 mentions) | EP = Episodic Pivot setup, not a stock |
| Shallow extraction | Quotes are raw Deepgram fragments with garbled words | No comprehension, just regex extraction |
| Missing context | "market_condition: not explicitly stated" | Agent didn't understand the transcript |
| Wrong terminology | "AI" listed as ticker | AI theme, not AppLovin ticker |
| No Pradeep voice | Generic summaries, no analogies or punchiness | No domain knowledge baked in |

We need a **subagent** that combines:
- **Writing quality** (glm-5.1's strength)
- **Trading domain awareness** (not hardcoded to one speaker)
- **Transcript comprehension** (deep reading, not surface extraction)

---

## Design: Three-Layer Knowledge Architecture

The trading-writer uses three layers of knowledge, with strict priority ordering:

### Layer A — Technical (always applies, hardcoded)

Contains transcription error patterns and formatting rules that apply to **all** trading transcripts regardless of speaker:

- **Deepgram/ASR error patterns** — common misparses in trading transcripts
- **Ticker vs abbreviation heuristics** — distinguish EP (setup) from NVDA (stock)
- **Obsidian formatting rules** — YAML frontmatter, wikilinks, markdown tables
- **Writing process workflow** — read → comprehend → rewrite → tag → save

### Layer B — Universal Trading Defaults (fallback only, MINIMAL)

Generic, non-controversial trading terms that **no speaker would dispute**:

| Term | Generic Definition |
|------|-------------------|
| Breakout | Price clears resistance on volume |
| Catalyst | News or event driving a price move |
| Stop | Price level to exit a losing trade |
| Volume | Number of shares traded |
| Pullback | Temporary decline within an uptrend |
| Position sizing | How much capital to allocate |
| Risk management | Controlling potential losses |

**Layer B does NOT include** speaker-specific definitions, setup names, indicator names, or methodology concepts. Those belong in Layer C.

### Layer C — Speaker-Specific Context (highest priority, runtime)

Passed at delegation time by the build agent. Contains the speaker's own:

- Setup names and definitions (EP, DEP, SIPs, etc.)
- Breadth indicators and market monitor methodology
- Unique vocabulary (cat/dog/liquid lava, neglect, tightness, OLC)
- Personality markers (analogies, humor style, pet phrases)
- Daily routine and process

**Priority rule**: When Layer C conflicts with Layer B, **Layer C ALWAYS wins**. The speaker's own words and definitions override generic defaults.

If no Layer C is provided, the agent operates in **pure discovery mode** — relying entirely on transcript content.

---

## Speaker Identification (MANDATORY)

Before writing ANY curated note, the trading-writer MUST know who the speaker is.

```
IF task prompt specifies speaker (e.g., "Speaker: Pradeep Bonde") → proceed
IF task prompt does NOT specify speaker:
  1. Check transcript filename for speaker hints
  2. Check transcript content for self-identification
  3. If still unclear → STOP and ASK: 
     "Who is the speaker? This affects which domain context I use."
  
NEVER assume the speaker.
NEVER apply a speaker's Layer C context to a different speaker.
```

### Why This Matters

| Scenario | Without Guardrail | With Guardrail |
|----------|-------------------|----------------|
| Pradeep transcript, no context | Falls back to Layer B, misses SIPs, EP 9M, neglect | Asks → gets Pradeep context → accurate |
| Quallamaggie transcript, Pradeep context applied | Writes "EP = Episodic Pivot" for someone who doesn't use that term | Asks → gets Quallamaggie context or discovery mode |
| Unknown trader, Pradeep context applied | Misattributes Pradeep's methodology to unknown speaker | Asks → user clarifies → uses correct context |

---

## Deepgram Error Correction Table

Trading transcripts from Deepgram commonly contain these errors. The trading-writer corrects them in curated output:

| Deepgram Output | Correct Interpretation | Explanation |
|-----------------|----------------------|-------------|
| "EP 9,000,000" | EP 9M | Nine million volume threshold for Episodic Pivot |
| "nine d p" | EP 9M | Same — ASR misparse |
| "c p 9,000,000" | EP 9M | Consonant confusion |
| "e p died williard" | EP died on the Williard indicator | Stock failed EP setup |
| "SIPs" / "stocks in play" | SIPs (Stocks in Play) | Same concept, different phrasing |
| "cat, dog, liquid lava" | Stock classification tiers | Not animals — institutional/speculative/mega-cap |
| "OLC" | Organized Like Crazy | Process discipline acronym |
| "two zero percent" | 20% Study | Market breadth indicator |
| "t two one zero eight" | T2108 | Market breadth indicator |
| Random 2-5 letter caps | Check: ticker or abbreviation? | "EP", "DEP", "AI" are setups, not stocks |

**Ticker detection heuristic**: Before listing something as a stock ticker, verify it isn't a setup abbreviation. Common false positives: EP, DEP, SOS, ANT, SIP, IPO, CEO, US, PR, AI (when used as "AI theme" not AppLovin).

---

## Writing Process

### Step 1 — Read the Full Transcript
Read the auto-generated transcript completely. All of it. Do not skip sections.

### Step 2 — Comprehend & Identify Structure
From the full transcript, identify:
- **Main themes** — what single question does this session answer?
- **Sub-themes** — distinct arguments, analogies, concepts
- **Key quotes** — verbatim statements capturing core insights (punchy, memorable, counter-intuitive)
- **Structure** — how the speaker organized the argument
- **Parameters/numbers** — specific percentages, dollar amounts, thresholds
- **People/sources referenced** — traders, books, methods cited
- **Analogies used** — metaphors explaining concepts (these make concepts searchable)

### Step 3 — Write the Curated Note
Write from comprehension, not extraction. Include:

1. **YAML frontmatter** with rich tags
2. **One-sentence overview** — the session's radical claim or core argument
3. **Numbered sections** — each covering one sub-theme
4. **Direct quotes throughout** — `> "verbatim quote"` for key insights
5. **Tables** — comparisons, examples, choices
6. **Key Takeaways** — numbered principles readable standalone
7. **Cross-References** — wikilinks to related transcripts or concepts
8. **Full Transcript link** — `[[transcript-file|Full Transcript]]` at bottom

### Step 4 — Tagging
Always include: `transcript`, language tag (`en`/`yue`/`zh`), backend tag (`deepgram`/`whisper`), speaker name tag (e.g., `pradeep-bonde`).

Add content-specific tags as kebab-case:
- Analogies: `barcelona-pickpocket`, `victoria-secret-model`
- Concepts: `three-setups`, `neglect-equals-explosiveness`
- Parameters: `1.5x-volume-breakout`, `4-percent-momentum-burst`
- Names: `mark-minervini`, `dan-zanger`, `warren-buffett`
- Warnings: `career-aborted-before-decision`

### Step 5 — Save
Save to the vault path specified in the task prompt. Use Obsidian `[[wikilink]]` syntax. Never use absolute Windows paths.

---

## Scope

The trading-writer handles three writing tasks:

| Task | Input | Output |
|------|-------|--------|
| **Daily curated notes** | Raw transcript + speaker context | Per-meeting deep comprehension note |
| **Weekly summaries** | All daily notes for a week | Synthesis: themes, setups, tickers, quotes |
| **Knowledge base updates** | All daily notes | Aggregated methodology document |

---

## Multi-Speaker Support

The architecture supports multiple traders in the same vault. Each speaker has their own Layer C context document:

```
trading-vault/KB/
├── Trading Meeting Knowledge.md          ← Pradeep Bonde
├── Quallamaggie Trading Knowledge.md     ← Quallamaggie
├── Minervini Trading Knowledge.md        ← (future)
└── ...
```

When the build agent delegates to trading-writer, it passes the appropriate context:

```
# Pradeep meeting
"Rewrite curated note for May 13. Speaker: Pradeep Bonde. 
 Context: [[Trading Meeting Knowledge.md]]"

# Quallamaggie webinar
"Rewrite curated note for Jun 5. Speaker: Quallamaggie.
 Context: [[Quallamaggie Trading Knowledge.md]]"

# Unknown trader
"Rewrite curated note for Jul 1. Speaker: unknown.
 No context document. Use pure discovery mode."
```

---

## Delegation Pattern (from build agent)

The typical flow when build agent encounters a writing task:

```
User: "rewrite the May 13 note using the full transcript"

Build agent (kimi-k2.6):
  1. Identifies this is a writing task, not a code task
  2. Determines speaker: "Pradeep Bonde" (from vault structure)
  3. Delegates to trading-writer subagent:
     "Rewrite curated note for May 13 (9:15 AM). 
      Speaker: Pradeep Bonde.
      Context: [[Trading Meeting Knowledge.md]]
      Transcript: [[meeting_2026-05-13_8db5e63e...]]
      Output: Daily Meetings/Meeting — May 13 (9_15 Am 1505).md"

Trading-writer (glm-5.1):
  1. Reads the context document for Layer C
  2. Reads the full transcript
  3. Comprehends and rewrites
  4. Saves the curated note
  5. Returns summary to build agent
```

---

## Files to Create/Modify

| File | Action | Description |
|------|--------|-------------|
| `.opencode/agents/trading-writer.md` | **Create** | Subagent definition with Layers A+B |
| `.opencode/skills/trading-summary/SKILL.md` | **Update** | Add delegation section pointing to trading-writer |
| `opencode.json` | **Update** | Add `trading-writer` entry in `agent` section |
| `AGENTS.md` | **Update** | Add trading-writer to agent model table |

---

## Agent Configuration

```json
{
  "trading-writer": {
    "description": "Reads trading transcripts and writes curated Obsidian notes with speaker-specific domain context. Delegate from build agent with speaker context.",
    "mode": "subagent",
    "model": "ollama-cloud/glm-5.1",
    "permission": {
      "edit": "allow",
      "bash": "allow"
    }
  }
}
```

| Agent | Model | Purpose |
|-------|-------|---------|
| build | `ollama-cloud/kimi-k2.6` | Code generation, pipeline, delegation |
| plan | `ollama-cloud/glm-5.1` | Read-only analysis |
| code-reviewer | `ollama-cloud/kimi-k2.6` | Subagent: code review |
| security-auditor | `ollama-cloud/kimi-k2.6` | Subagent: security audit |
| docs-writer | `ollama-cloud/glm-5.1` | Agent: generic documentation |
| **trading-writer** | **`ollama-cloud/glm-5.1`** | **Subagent: trading transcript comprehension & curated notes** |
| debug | `ollama-cloud/kimi-k2.6` | Subagent: investigation |
| image-viewer | `ollama-cloud/qwen3.5` | Subagent: image interpretation |
| extract-map-locator | `ollama-cloud/qwen3.5` | Subagent: HK map identification |
| default/small tasks | `ollama-cloud/gpt-5-nano` | Session titles, summaries |

---

## Comparison: docs-writer vs trading-writer

| Aspect | docs-writer | trading-writer |
|--------|------------|---------------|
| Mode | `all` (primary) | `subagent` (invoked by build) |
| Model | glm-5.1 | glm-5.1 |
| Domain knowledge | Generic technical writing | Trading-specific (Layers A+B) |
| Speaker context | None | Runtime Layer C (Pradeep, Quallamaggie, etc.) |
| Error correction | None | Deepgram/ASR trading error patterns |
| Speaker guardrail | N/A | Must identify speaker or ask |
| Scope | Config docs, READMEs | Transcripts, summaries, KB |
| Vault location | Any | `trading-vault/` |
| Skill linkage | None | Linked from `trading-summary` SKILL.md |

---

## Future Extensions

- **New speaker onboarding**: When adding a new trader (e.g., Quallamaggie), create a `KB/{Speaker} Trading Knowledge.md` document with their methodology. The trading-writer picks it up automatically via Layer C.
- **Multi-speaker notes**: When a transcript features two speakers, pass both context documents and instruct the writer to attribute ideas to each speaker.
- **Language support**: Layer A could include error patterns for Cantonese (yue) or Mandarin (zh) ASR when processing non-English trading content.
- **Quality scoring**: After writing, the build agent could run a lightweight check: "does the curated note contain setup abbreviations listed as tickers?" to catch common errors.

---

*Documented 2026-06-10. Implementation pending user confirmation.*