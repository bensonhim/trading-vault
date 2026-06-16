---
title: "Phase 5 Integration — Development Notes"
date: 2026-06-16
tags: [trading, v2, phase-5, cross-reference, nightly-runner, briefing, backfill]
---

# Phase 5 — SB Cross-Reference + Nightly Pipeline Integration

> **Completed:** 2026-06-16
> **Design doc:** `D:\opencodeworkspace\.trading\docs\v2-design\PHASE-5-Integration.md`
> **Depends on:** Phase 1 (pricing) + Phase 2 (interpretation)

---

## Overview

Phase 5 connects all the pieces built in Phases 1 and 2 into a working nightly pipeline. Three deliverables:

1. **SB × Setup Confluence Engine** — cross-references Sugar Babies with active setups, calculates entry/exit + position sizing, assigns confluence tiers
2. **9-Step Nightly Runner** — complete pipeline from StockBee MM fetch to Obsidian daily briefing
3. **Scanner `--briefing` flag** — v2 briefing generation from within the scanner CLI

---

## 1. Cross-Reference Engine — `src/scans/cross_reference.py` (487 lines)

### Problem

Sugar Babies are Pradeep's A-list stocks — they repeatedly break out on 9M+ volume. But a Sugar Baby without an active setup (DEP, SOS, ANT, EP 9M) is just a watchlist entry. The confluence of SB + active setup is where the real edge is.

### Solution

The `cross_reference()` function:
1. Loads all Sugar Babies from `sugar_babies` table
2. Loads all active setup candidates from scan results
3. Groups candidates by ticker (a ticker can have multiple setups)
4. Picks the highest-priority setup per ticker
5. Checks catalyst strength from `catalyst_results`
6. Assigns a confluence tier (A+ / A / B+ / B / C)
7. For top-tier candidates (A+/A/B+/B), enriches with entry/exit + position sizing
8. Persists results to `confluence_results` SQLite table

### Confluence Tiers

| Tier | Criteria | Position Cap | Size Multiplier |
|------|----------|-------------|----------------|
| **A+** | SB + active setup + strong catalyst | 50% | 1.0x (bullish regime) |
| **A** | SB + active setup | 50% | 1.0x (bullish regime) |
| **B+** | Active setup + catalyst (no SB) | 25% | 0.8x |
| **B** | Active setup only | 25% | 0.5x |
| **C** | SB only (watchlist) | N/A | N/A |

### Enrichment Logic

For A+/A/B+/B candidates (max 150 by default), the engine:
1. Fetches VWAP via `get_effective_vwap()` — tries daily FMP VWAP first, falls back to intraday 5-min calculation
2. Calculates consolidation range for DEP/ANT setups (used for stop placement)
3. Calls `calc_setup_entry_exit()` → `EntryExitResult` with entry, stop, target, VWAP signal
4. Calls `calculate_position()` with `is_sugar_baby=True` for DEP/ANT → enables 50% hard cap
5. Records any VWAP blocks or cap warnings

### Data Class: `ConfluenceResult`

```python
@dataclass
class ConfluenceResult:
    ticker: str
    confluence_tier: str          # A+, A, B+, B, C
    setup_type: str
    is_sugar_baby: bool
    has_active_setup: bool
    has_strong_catalyst: bool
    sugar_baby_rank: int | None
    setup_priority: str | None
    catalyst_note: str | None
    entry_exit: EntryExitResult | None
    position: PositionResult | None
    warning: str | None
    details: dict
```

### New SQLite Table: `confluence_results`

Stores daily cross-reference results, unique on (date, ticker):
- `confluence_tier`, `setup_type`, `is_sugar_baby`, `has_active_setup`, `has_strong_catalyst`
- `entry_price`, `stop_price`, `target`, `shares`, `position_usd`, `position_pct`, `risk_hkd`
- `warning`, `details`, `created_at`

### Key Functions

| Function | Purpose |
|----------|---------|
| `cross_reference(scan_results, target_date, ...)` | Main engine — returns `list[ConfluenceResult]` |
| `summarize_confluences(results)` | Count by tier + setup type, top A+/A tickers |
| `save_cross_reference_results(results, target_date)` | Persist to SQLite |
| `load_cross_reference_results(target_date)` | Load from SQLite |
| `run_full_confluence_pipeline(target_date)` | High-level: MM → cross-ref → save → summarize |

### Usage

```python
from src.scans.cross_reference import cross_reference, summarize_confluences

results = cross_reference(
    scan_results={"ep_9m": [...], "dep": [...], "sb": [...], ...},
    target_date=date(2026, 6, 16),
    catalyst_results=catalysts,
    interpretation=interpretation,
)

for r in results:
    if r.confluence_tier in ("A+", "A"):
        print(f"{r.ticker}: {r.confluence_tier} | Entry={r.entry_exit.entry_price} | Stop={r.entry_exit.stop_price} | Shares={r.position.shares}")

summary = summarize_confluences(results)
print(f"A+ tickers: {summary['a_plus_tickers']}")
```

---

## 2. Nightly Runner — `src/cli/nightly_runner.py` (487 lines, fully refactored)

### Old Pipeline (5 Steps)

```
Step 0: Fetch StockBee
Step 1: Fetch quotes
Step 2: Breadth calc (our own)
Step 3: Cross-check with StockBee
Step 4: Generate Obsidian note (MM table only)
```

### New Pipeline (9 Steps)

```
Step 0: Fetch StockBee MM data (sole truth)
Step 1: Fetch FMP daily quotes for all TC2000 tickers (~6K)
Step 2: Insert OHLCV into SQLite
Step 3: Run all setup scans (EP, SOS, DEP, ANT, WSS, Reversal, SB)
Step 4: Calculate 20% study from SQLite
Step 5: Calculate entry/stop/target + VWAP filter for each candidate
Step 6: Calculate position sizing (HKD 3,000 risk, 25%/50% caps)
   → Catalyst enrichment (between Steps 6 and 7)
Step 7: Cross-reference Sugar Babies with setups (confluence engine)
Step 8: Interpret MM regime + generate regime call
Step 9: Generate Obsidian daily briefing note
```

### New CLI Flags

| Flag | Purpose |
|------|---------|
| `--date YYYY-MM-DD` | Target date (default: last US trading day) |
| `--sample N` | Limit quote batches for testing |
| `--no-briefing` | Skip Step 9 (Obsidian briefing) |
| `--no-scans` | Skip Step 3 (setup scans) |
| `--force` | Force recalculation |

### Usage

```bash
# Full nightly pipeline
cd D:\opencodeworkspace\.trading
py src/cli/nightly_runner.py

# Quick test (2 quote batches only)
py src/cli/nightly_runner.py --sample 2 --no-briefing

# Specific date
py src/cli/nightly_runner.py --date 2026-06-13
```

### Output Summary

After completing all 9 steps, the runner prints a JSON summary:

```json
{
  "date": "2026-06-16",
  "stockbee_date": "2026-06-16",
  "regime": "bullish",
  "net_primary": 789,
  "t2108": 42.22,
  "quotes": 6080,
  "ohlcv_inserted": 6080,
  "scans": {"ep_9m": 8, "sos": 12, "dep": 5, "ant": 3, "wss": 2, "reversal": 1, "sb": 150},
  "confluences": {"A+": 3, "A": 7, "B+": 5, "B": 16, "C": 119},
  "briefing": "C:\\Users\\msh897\\Documents\\Obsidian\\trading-vault\\Daily Briefing\\2026-06-16.md"
}
```

---

## 3. Scanner `--briefing` Flag — `src/cli/scanner.py` (606 lines)

Added `--briefing` flag to `scanner.py all` that generates the v2 daily briefing:

1. Runs 20% study via `calc_20pct_study()`
2. Fetches fresh StockBee MM data → `interpret_mm()`
3. Runs cross-reference engine with current scan results + catalysts
4. Calculates entry/exit + position sizing for all candidates
5. Calls `generate_daily_briefing()` → writes to Obsidian vault

### Usage

```bash
# Run all scans + generate v2 daily briefing
py src/cli/scanner.py all --briefing

# Run all scans + v1 note only (original behavior)
py src/cli/scanner.py all

# Specific date with briefing
py src/cli/scanner.py all --briefing --date 2026-06-13
```

---

## 4. Data Backfill — Complete

### What Was Done

- Ran `weekly_loader.py` to backfill ~1,450 days of OHLCV data for the TC2000 universe
- Process completed over ~2 hours across multiple resume runs
- 399 tickers had no FMP data available — these are SPAC units (`.U`), rights (`.RT`), warrants (`.WI`), and delisted shells
- Marked all 399 as `fmp_available=0` in `tc2000_universe` table

### Final DB Status

| Metric | Value |
|--------|-------|
| OHLCV rows | 6,847,562 |
| TC2000 universe tickers | 6,479 |
| Tickers with FMP data | 6,080 (93.8%) |
| Tickers marked unavailable | 399 |
| Sugar Babies | 600 |
| Date range | 2022-06-23 to 2026-06-15 |

### Sample of Unavailable Tickers

| Pattern | Examples | Count (approx) |
|---------|----------|----------------|
| SPAC units (`.U`) | `AIIA.U`, `ALUB.U`, `ASZ.U`, `WARR.U` | ~150 |
| Rights (`.RT`) | `AIIA.RT`, `WENC.RT`, `XFLH.RT`, `WPAC.RT` | ~60 |
| Warrants (`.WI`) | `ACP.RT.WI`, `XKEYV` | ~15 |
| Delisted/bankrupt (`Q` suffix) | `ALPSQ`, `AMRSQ`, `VRMMQ`, `VLRXQ` | ~50 |
| Obscure OTC | `AIMTF`, `AIMUF`, `WELNF`, `ZAPPF` | ~124 |

These are not tradeable stocks per Pradeep's methodology — SPAC units have no edge, rights/warrants are derivatives, and delisted/bankrupt stocks are anti-patterns.

---

## 5. What Changed in Existing Files

### `src/cli/scanner.py` — New imports + `--briefing` flag

**Added imports:**
- `from src.pricing.range_detector import calc_20pct_study`
- `from src.pricing.vwap import get_effective_vwap, calc_vwap_signal`
- `from src.pricing.entry_exit import calc_setup_entry_exit`
- `from src.interpretation.mm_interpreter import interpret_mm`
- `from src.interpretation.briefing_generator import generate_daily_briefing`
- `from src.scans.cross_reference import cross_reference, save_cross_reference_results, summarize_confluences`
- `from src.config import get_obsidian_vault_path, get_trading_config`

**Added flag:** `--briefing` triggers Phase 4b block that:
1. Calculates 20% study from SQLite
2. Fetches StockBee MM + interprets regime
3. Runs cross-reference with scan results + catalysts
4. Computes entry/exit + position sizing for all candidates
5. Generates v2 daily briefing to Obsidian

### `src/data/weekly_loader.py` — Import path fix

Added `sys.path.insert(0, ...)` to fix `ModuleNotFoundError` when running directly with `py src/data/weekly_loader.py`.

### `src/data/db.py` — `confluence_results` table

New table created by `cross_reference.py` on first save:
- Schema: id, date, ticker, confluence_tier, setup_type, is_sugar_baby, has_active_setup, has_strong_catalyst, sugar_baby_rank, entry_price, stop_price, target, shares, position_usd, position_pct, risk_hkd, warning, details, created_at
- Unique constraint on (date, ticker)

### `tc2000_universe` table — 399 rows updated

`fmp_available` set to `0` for 399 tickers with no FMP data.

---

## 6. How to Run the Full Pipeline

```bash
cd D:\opencodeworkspace\.trading

# Option 1: Full 9-step nightly pipeline
py src/cli/nightly_runner.py

# Option 2: Scanner with v2 briefing
py src/cli/scanner.py all --briefing

# Option 3: Scanner with v1 note only (original)
py src/cli/scanner.py all

# Quick test (limited quotes)
py src/cli/nightly_runner.py --sample 2 --no-briefing
```

---

## 7. Remaining Work

| Phase | Status | Next |
|-------|--------|------|
| 1 — Pricing | ✅ Done | — |
| 2 — Interpretation | ✅ Done | — |
| 5 — Integration | ✅ Done | — |
| 3 — Telegram Alerts | 🔜 Next | `src/alerts/telegram_alerts.py`, `trade_recorder.py`, `bot_handler.py` |
| 4 — Transcript Backfill | 🔄 Parallel | ~150 meetings, Deepgram, $135 budget |

---

*Last updated: 2026-06-16*