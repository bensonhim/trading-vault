---
title: "Trading Radar Engine - Project Status"
date: 2026-06-05
tags: [project, status, trading-radar, phase6, calibration, rewrite]
---

# Trading Radar Engine — Project Status

> **Phase:** 6 → **Phase 6b (REWRITE)** — MM Calculation Rewrite from First Principles
> **Last updated:** 2026-06-05
> **Decision:** Full Q2 comparison revealed systematic per-stock qualification rate gap (our 6.2% vs Pradeep's 15.3% for Primary Up). Patching is insufficient — **rewriting from first principles.**

---

## Phase Overview

| Phase | Name | Status | Description |
|-------|------|--------|-------------|
| 1a | Infrastructure | ✅ | SQLite DB, FMP `/stable/` adapter, breadth calculator |
| 1b | Universe Backfill | ⚠️ **Needs redo** | Must switch to split-adjusted close + remove volume filter |
| 2 | Setup Scanner | ✅ | 8 scan modules: DEP, SOS, ANT, EP 9M, WSS, Reversal, Sugar Baby, MM |
| 3 | Catalyst Detection | ✅ | Earnings calendar + momentum signals |
| 4 | Entry Signals | ✅ | Regime × Setup × Catalyst scoring (A+/A/B/C ratings) |
| 5 | Position Sizing | ✅ | Risk-based sizing with setup-specific stops |
| 6 | Session Pipeline | ✅ | Video → Transcript → Ideas → Cross-validation → Obsidian notes |
| **6b** | **MM Rewrite** | 🔄 **In Progress** | Rewrite breadth calculator from first principles |
| 7 | Dashboard | ⏳ | TypeScript real-time dashboard (blocked until 6b done) |

---

## Why Rewrite? (Proven by Q2 Comparison)

Full quarter comparison (`_q2_comparison.md`) revealed the gap is **not just universe size** — it's per-stock qualification rate:

| Metric | Our Rate | Pradeep Rate | Our Count | Pradeep Count |
|--------|----------|-------------|-----------|---------------|
| Primary Up / Universe | **6.2%** | **15.3%** | 364 / 5866 | 987 / ~6400 |
| Primary Down / Universe | **6.0%** | **21.9%** | 379 / 5866 | 1400 / ~6400 |

At our 6.2% rate, adding 600 missing stocks only adds ~37 Primary Up (37 << 623 gap). The ~2.5x rate difference means **our calculation logic is fundamentally wrong**, not just our data.

### Three Root Causes Identified

| # | Root Cause | Impact | Fix |
|---|-----------|--------|-----|
| 1 | **Non-split-adjusted close prices** | ~100-200 stocks misclassified per day (any stock with a split in the lookback window gets corrupted returns) | Switch `weekly_loader.py` to `get_historical_daily()` (split-adjusted endpoint) |
| 2 | **Volume filter in universe fetch** | ~500-700 low-volume stocks excluded from DB entirely | Remove `volume_min=100000` from `fetch_universe_tickers()` |
| 3 | **ETF exclusion from breadth** | Unknown magnitude — Pradeep likely includes ETFs in Primary/Monthly counts | Verify from transcripts, add ETFs back if included |

### Open Questions (Phase 0 will resolve)

1. Does Pradeep include ETFs in Primary Up/Down, Monthly, Fib, T2108?
2. Does Pradeep use split-adjusted close in TC2000 scans? (Almost certainly yes — TC2000 default)
3. Is the 40-day SMA on split-adjusted or raw close?
4. What exactly is the TC2000 scan universe filter?

---

## Previous Calibration Fixes (Phase 6 — Applied but Insufficient)

| # | Fix Applied | Result |
|---|------------|--------|
| 1 | ADRs restored to universe | +122 universe count; slight improvement |
| 2 | T2108 denominator = broad_count | Dropped T2108 from 61.9% to ~56% |
| 3 | Delisted stocks pipeline built | Impact minimal (~+1pp T2108) |
| 4 | Regime = Net (Up − Down) | Fixed classification; now matches Pradeep's direction |

These fixes were correct but insufficient — the structural gap remains.

---

## Phase 6b: MM Rewrite Plan

📄 **Full plan:** `_04. Rewrite MM Plan.md`

| Step | Task | Estimate | Dependency |
|------|------|----------|------------|
| 0 | Write exact definitions from transcripts | 2-3h | None |
| 1a | Switch to split-adjusted close | 4-6h (API time) | Phase 0 |
| 1b | Remove volume filter from universe | 1h | Phase 0 |
| 1c | Run delisted stock backfill | 2-4h | Independent |
| 2a | Rewrite breadth calculator per indicator | 3-4h | Phase 0 conclusions |
| 2b | ETF inclusion decision | 1h | Phase 0 research |
| 2c | T2108 rewrite (verify after data changes) | 1h | Phase 1 |
| 3a | Per-stock verification (AAPL, MSFT, NVDA) | 2h | Phase 2 |
| 3b | Full Q2 recalculation vs Pradeep | 1-2h | Phase 2 |
| **Total** | | **~16-24h** | |

---

## Research Notes

📄 **`_03. Calibration Research & Action Plan.md`** — Previous root cause analysis (ADRs, T2108 denominator, delisted)
📄 **`_02. FMP API - Delisted Stocks.md`** — FMP delisted API test results
📄 **`_04. Rewrite MM Plan.md`** — **NEW:** Full rewrite plan from first principles

---

*Last updated: 2026-06-05*
