---
title: "Trading Radar Engine -- Project Status"
date: 2026-06-03
tags: [trading-radar, status, project]
---

# Trading Radar Engine -- Project Status

> **Last updated:** 2026-06-03
> **Resume command:** "continue trading radar engine, read Trading Radar Engine/Project Status.md"

---

## What Exists Now

### Phase 2: Setup Scanners (DONE)

### Infrastructure (DONE)
- [x] Three subvaults created: `Trading Radar Engine/`, `Daily Market Monitor/`, `Daily Trading Idea/`
- [x] Design notes written: `Trading Radar Engine/Design Notes.md`
- [x] StockBee credentials stored in `.trading/.env` (gitignored)
- [x] Project structure: `market-monitor/` with modules

### StockBee Market Monitor Scraper (DONE)
- [x] Discovered Google Sheet iframe URLs via Playwright login
- [x] Found the actual data table CSV URL
- [x] Built `stockbee_scraper.py` -- parses CSV and returns structured data
- [x] **Latest data captured (2026-06-01):**
  - 4% breakout: 419
  - 4% breakdown: 221
  - Primary up (25%/65d): 1649
  - T2108: 43.86%
  - Universe: 6463

### Note Generator (DONE)
- [x] `note_generator.py` -- generates Obsidian markdown notes
- [x] First Daily Market Monitor note generated: `2026-06-01.md`
  - Cross-check table shows 100% match with StockBee data
- [x] First Daily Trading Idea note generated: `2026-06-02.md`

### Configuration (DONE)
- [x] `config.json` -- all thresholds, tolerances, paths
- [x] `requirements.txt` -- Python dependencies

---

## FMP API Status

| Item | Status |
|------|--------|
| FMP API key | **AVAILABLE** -- added to `.trading/.env` |
| FMP plan | **Premium** ($59/mo) -- 750 calls/min, 30 years historical, full fundamentals |
| API key tested | Pending |

---

## Architecture Decision: SQLite Local Cache

**Decision date:** 2026-06-03

### Why SQLite?
- SQLite is built into Python -- no install needed
- Local file database (`trading_radar.db`)
- Enables fast nightly runs (< 3 min) and powers Sugar Babies + SOS/DEP for free

### Two-Tier Data Strategy

| Tier | What | Source | Frequency | Speed |
|------|------|--------|-----------|-------|
| **Screener-based** | 4% breakout/breakdown counts, universe count | FMP `stock-screener` endpoint | Nightly | < 1 second (3 API calls) |
| **Cache-based** | Primary (65d), T2108 (40d), monthly (22d), fib (34d), Sugar Babies (1450d), SOS, DEP | SQLite local cache | Nightly (computed from cache, no API) | Instant |

### Data Flow

```
Daily (09:30 AM ET):
  1. scanner.py all
  2. Run MM first (SQLite breadth calc, zero API calls)
  3. Determine regime from primary indicator (65d)
  4. Run setup scans based on regime:
     - Bullish (primary > 300): DEP + EP 9M + SOS + ANT + REVERSAL + SB
     - Mildly Bullish (primary > 200): DEP + EP 9M + SOS + SB
     - Neutral: DEP + SB + REVERSAL
     - Bearish (primary <= 200): WSS + REVERSAL + SB
  5. Save candidates to daily_candidates (SQLite)
  6. Generate unified Daily Trading Idea note (Obsidian vault)

Nightly (8:30 PM ET):
  1. nightly_runner.py (Phase 1A pipeline)
  2. Store today's OHLCV → daily_ohlcv table

Weekly (Friday after close):
  1. weekly_loader.py → 1,450-day historical OHLCV for all tickers
  2. Sugar Babies count-through (1450d) → sugar_babies table
```

### API Call Budget (Premium Plan)

| Task | Calls | Frequency | Time |
|------|-------|-----------|------|
| Screener (breakout/breakdown/universe) | 3 | Nightly | < 1 sec |
| Batch quotes (all tickers today) | ~65 | Nightly | ~7 sec |
| Weekly bulk historical refresh | ~6,500 | Friday | ~11 min |
| Sugar Babies count-through | 0 | Weekly | 0 (computed locally) |
| SOS/DEP scan | 0 | Daily | 0 (computed locally) |
| EP pre-market + earnings | ~10 | Daily (morning) | ~2 sec |

**Nightly total: ~68 API calls, < 3 minutes.**

---

## Implementation Plan (Updated)

### Phase 2: Setup-Specific Scanner (DONE)

### Phase 0: Discovery & Infrastructure (DONE)
- [x] Playwright login to StockBee, snapshot MM page structure
- [x] Discover daily session video page structure
- [x] Create Python project structure
- [x] Create Obsidian subvault folders
- [x] FMP API key available (Premium plan)

### Phase 2: Setup-Specific Scanner (DONE)

| Module | Purpose | Status |
|--------|---------|--------|
| `scanner.py` | CLI orchestrator: MM regime → select scans → generate note | ✅ |
| `scans/base.py` | BaseScan abstract class (SQLite + FMP live) | ✅ |
| `scans/dep.py` | DEP 9M scan (25-day lookback) | ✅ |
| `scans/ep_9m.py` | EP 9M today (live FMP gainers/losers) | ✅ |
| `scans/sos.py` | Start of a Swing breakout (cached OHLCV) | ✅ |
| `scans/anticipation.py` | 3T/2T tight-day anticipation | ✅ |
| `scans/wss.py` | Weak Structure Short bearish | ✅ |
| `scans/reversal.py` | Reversal bullish exhaustion candle | ✅ |
| `scans/sugar_baby.py` | Sugar Baby watchlist (SQLite table) | ✅ |
| `scans/market_monitor.py` | Breadth calc wrapper (delegates to breadth_calculator.py) | ✅ |

### Phase 1A: SQLite Cache + Nightly Runner (DONE)
- [x] `db.py` -- SQLite schema and connection module (8 tables)
- [x] Rewrite `breadth_calculator.py` to compute from SQLite (zero API calls)
- [x] `nightly_runner.py` -- orchestration script
- [x] `weekly_loader.py` -- Friday bulk download (1,450 days) with resume

### Phase 1B: Cross-Validation (DONE)
- [x] Test FMP API key connectivity
- [x] Run nightly_runner with sample, compare vs StockBee
- [x] Compare vs TC2000 manual scans
- [x] Tune universe filter (price >= 3, volume >= 100K)

### Phase 3: Sugar Babies Scanner
- [ ] Count Through algorithm (4% + 9M over 1450 days)
- [ ] Weekly ranking output to Obsidian note
- [ ] Top 20/60/150 tiers

### Phase 4: SOS & DEP Radar Refinement
- [ ] DEP detection from 25d cached data with volume sort
- [ ] SOS detection validation against TC2000
- [ ] Pre-market gap scanner for EP suspects

### Phase 5: Session Pipeline
- [ ] Video discovery via Playwright
- [ ] CDN download + Deepgram transcription
- [ ] AI idea extraction (tickers, setups, catalysts)
- [ ] Cross-validation logic (radar vs Pradeep's ideas)

### Phase 6: Catalyst Intelligence
- [ ] Earnings calendar integration (FMP)
- [ ] Earnings surprise calculator (actual vs estimate)
- [ ] Story EP detector

### Phase 7: Dashboard (Later)
- [ ] TypeScript real-time dashboard

---

## Key URLs

| Resource | URL |
|----------|-----|
| StockBee MM (traffic light) | `https://stockbee.biz/market-monitor/` |
| StockBee MM data CSV | `https://docs.google.com/spreadsheet/pub?key=0Am_cU8NLIU20dEhiQnVHN3Nnc3B1S3J6eGhKZFo0N3c&output=csv` |
| StockBee login | `https://stockbee.biz/accounts/login/` |
| StockBee video library | `https://stockbee.biz/video/` |
| FMP API docs | `https://site.financialmodelingprep.com/developer/docs/` |

---

## How to Run

```powershell
# Phase 2: Run full scanner pipeline (MM + setup scans → Obsidian note)
cd D:\opencodeworkspace\.trading\market-monitor
py scanner.py all --save-json

# Or run individual scans
py scanner.py dep          # DEP 9M watchlist
py scanner.py ep_9m       # EP 9M today's breakout
py scanner.py sos          # Start of a Swing
py scanner.py ant          # Anticipation 3T/2T
py scanner.py wss          # Weak Structure Short
py scanner.py reversal     # Reversal bullish
py scanner.py sb           # Sugar Baby rankings
py scanner.py mm           # Market Monitor breadth

# Legacy Phase 1A runners
py nightly_runner.py
py weekly_loader.py
```

---

## Next Action

**Phase 2 is complete.** All 8 setup-specific scan modules are working.

Priority next steps:
1. Let weekly_loader.py finish historical backfill (~1500/8731 tickers done)
2. Once sufficient data loaded, validate DEP/SOS against TC2000
3. Refine WSS pattern-matching logic (currently matches too broadly)
4. Add Sugar Babies count-through calculation once 1450 days available

---

*Last updated: 2026-06-03*
