---
title: "Trading Radar Engine — Design Notes"
date: 2026-06-04
tags: [trading-radar, design, architecture, market-monitor, sugar-babies, sos, dep, ep, automation, phase6]
---

# Trading Radar Engine — Design Notes

> **Purpose**: Automate Pradeep Bonde's market monitoring, idea generation, and cross-validation with daily sessions.
> **Status**: Phase 6 COMPLETE (all core features built and tested)
> **Backfill**: 96% ready (8,407/8,753 tickers with ≥65 rows)

---

## 1. Architecture Overview

The system is a **6-layer funnel** that narrows from market regime to actionable trades:

```
Layer 1: MARKET MONITOR — "Should I trade at all?"
         ↓ (if bullish primary)
Layer 2: CATALYST DETECTION — "What's moving and why?"
         ↓ (classify lifespan)
Layer 3: STOCK SELECTION — "Is this stock the market loves?"
         ↓ (Sugar Babies = highest priority)
Layer 4: SETUP TYPE — "SOS? DEP? EP? Anticipation?"
         ↓ (choose based on catalyst type + timing)
Layer 5: ENTRY + SIZING — "How big? What stop?"
         ↓
Layer 6: DAILY SESSION VALIDATION — "Does Pradeep agree?"
```

---

## 2. Three Subvaults

| Subvault                  | Purpose                                                  | Update Frequency                      |
| ------------------------- | -------------------------------------------------------- | ------------------------------------- |
| **Trading Radar Engine/** | Design docs, architecture, calibration history           | On design changes                     |
| **Daily Market Monitor/** | Breadth metrics, regime assessment, StockBee cross-check | Every trading day (~8:30 PM ET)       |
| **Daily Trading Idea/**   | Radar candidates, session ideas, cross-validation        | Every trading day (morning + evening) |
| **Daily Sessions/**       | Transcript summaries, cross-validation matches/misses     | After each session video              |

---

## 3. Market Monitor Design

### 3.1 Data Source

| Component | Source | Cost | Why Chosen |
|-----------|--------|------|------------|
| Daily OHLCV + real-time quotes | FMP (Financial Modeling Prep) | $22–59/mo | **Best for Pradeep's strategy**: real-time data, earnings calendar, sales/revenue, analyst estimates, fund ownership, short interest — all needed for EP Magna 53 |
| Earnings calendar | FMP (same) | Included | Built-in earnings surprise (actual vs. estimate) |
| Sales/revenue data | FMP fundamentals | Included | Back-to-back 39%+ sales growth check |
| Analyst estimates | FMP analyst API | Included | 3+ analyst upgrades check |
| Fund ownership | FMP institutional/13F | Included | Fund neglect check |
| Short interest | FMP key metrics | Included | Short interest ratio check |
| StockBee MM reference | Google Sheet (public CSV export) | Free | Cross-validation source |
| Daily session videos | StockBee CDN | Included in membership | Transcription + idea extraction |

### 3.2 Calculated Metrics

| Metric | Formula | Thresholds |
|--------|---------|-----------|
| 4% breakout count | `count(close / prev_close ≥ 1.04)` | 300 = unusual; 1000+ = turn |
| 4% breakdown count | `count(close / prev_close ≤ 0.96)` | Same as above |
| Primary indicator (up) | `count(close / close_65d ≥ 1.25)` | >200 = bullish; <200 = bearish; <100 = capitulation |
| Primary indicator (down) | `count(close / close_65d ≤ 0.75)` | Mirror of above |
| Monthly 25% up | `count(close / close_22d ≥ 1.25)` | Moderate breadth |
| Monthly 25% down | `count(close / close_22d ≤ 0.75)` | Moderate breadth |
| Monthly 50% up | `count(close / close_22d ≥ 1.50)` | High breadth |
| Monthly 50% down | `count(close / close_22d ≤ 0.50)` | High breadth |
| 13%/34d up | `count(close / close_34d ≥ 1.13)` | Fibonacci half-quarter |
| 13%/34d down | `count(close / close_34d ≤ 0.87)` | Fibonacci half-quarter |
| T2108 | `count(close > SMA40) / total` | <20% = bear market; <10% = capitulation |
| Universe count | `count(active tickers)` | 5000→7000 surge = bubble |
| 5-day ratio | `sum(breakouts last 5d) / sum(breakdowns last 5d)` | >2 = aggressive buying; <0.5 = heavy selling |
| 10-day ratio | `sum(breakouts last 10d) / sum(breakdowns last 10d)` | Same thresholds |
| 20% study | `count(close / close_5d ≥ 1.20)` | 150+ stocks at 300 = pullback imminent |

### 3.3 StockBee Cross-Check

The Market Monitor page on StockBee (`https://stockbee.biz/market-monitor/`) embeds a Google Sheet via iframe:
- **Sheet URL**: `https://docs.google.com/spreadsheets/d/e/2PACX-1vQbKlbJlLTHytL-3U5ZAfffEbJCO8g2qqAeIloETbtIuPw4hYsuRli-Cs2CCaFpiDnNwE5ezbJY1zan/pubhtml`
- **CSV Export**: `.../pub?output=csv&gid=0`

**Critical finding**: The CSV export (gid=0) returns a **calendar traffic light view** — not the daily data table. The daily data table with numbers is in a different sheet (gid unknown, possibly 1 or a named sheet). We need to discover the correct gid or parse the HTML directly.

**Alternative approach**: Use Playwright to log in, access the iframe, and extract the table data directly from the rendered page.

### 3.4 Tolerance Thresholds

| Metric | Acceptable Tolerance | Action if Exceeded |
|--------|---------------------|-------------------|
| 4% breakout/breakdown | ±10 stocks | Investigate universe filter |
| Quarterly/monthly breadth | ±15 stocks | Check universe + adjusted close |
| T2108 | ±2% | Check MA calculation method |
| Stock count | ±50 | Check delisted/excluded tickers |
| Ratios (5/10 day) | ±0.2 | Derived from raw numbers; check sum |

### 3.5 Calibration Drift Detection

Track systematic offsets over time in `Calibration Log.md`:

```markdown
## Calibration History

| Date | Metric | Our Calc | Pradeep's | Delta | Status |
|------|--------|---------|-----------|-------|--------|
| 2026-06-02 | 4% breakout | 187 | 185 | +2 | ✅ OK |
```

If a metric consistently deviates > tolerance for 5+ days, investigate:
1. Universe filter mismatch
2. Adjusted close vs. raw close
3. MA calculation differences
4. TC2000 scan conditions

---

## 4. Sugar Babies Scanner Design

### 4.1 Core Algorithm

```python
def sugar_baby_score(ticker, history_1450d):
    """Count how many times stock had 4% breakout + 9M+ volume in each timeframe."""
    timeframes = [5, 10, 20, 50, 126, 252, 504, 756, 1450]
    counts = {}
    for tf in timeframes:
        window = history_1450d[-tf:]
        count = sum(1 for day in window if day.return_pct >= 4 and day.volume >= 8_900_000)
        counts[tf] = count
        # Min 3 hits required for 5d, 10d, 20d windows
        if tf in (5, 10, 20) and count < 3:
            counts[tf] = 0  # Disqualified
    return counts
```

### 4.2 Timeframes & Selection

Based on Pradeep's TC2000 setup (Sugar Babies Guide Part 6, transcript line 109):

| Timeframe (days) | ~Calendar | Min Hits | Selection |
|-----------------|-----------|----------|-----------|
| 5 | 1 week | ≥ 3 | Top 20–30 |
| 10 | 2 weeks | ≥ 3 | Top 20–30 |
| 20 | 1 month | ≥ 3 | Top 20–30 |
| 50 | 2.5 months | Top 20–30 | Top 20–30 |
| 126 | 6 months | Top 20–30 | Top 20–30 |
| 252 | 1 year | Top 20–30 | Top 20–30 |
| 504 | 2 years | Top 20–30 | Top 20–30 |
| 756 | 3 years | Top 20–30 | Top 20–30 |
| 1,450 | 5.7 years (max) | Top 20–30 | Top 20–30 |

Combine all flagged symbols into one master list (~87–90 names).
Add ~30 "SugarMamas" (market cap >$10B) for institutional quality balance → ~143 total.

### 4.4 Refresh Frequency

- **Daily** (after market close): Re-rank + cross-reference with EP 9M and DEP scans
- **Weekend**: Full review of master list composition
- **Output**: Obsidian note with ranked list + overlap flags (🔥 SB+EP9M, 🔴 SB+DEP)

### 4.5 Selection

- Top 20–30 stocks = core watchlist
- Top 60–150 stocks = expanded list
- Each Sugar Baby produces ~4 tradable setups/year

---

## 5. SOS & DEP Radar Design

### 5.1 SOS Detection (Range Expansion)

```python
def detect_sos(ticker, today, history_5d):
    """Today's return > max of prior 2-5 days' returns."""
    prior_returns = [day.return for day in history_5d[-5:-1]]
    return today.return > max(prior_returns) and today.volume > today.avg_volume * 2
```

### 5.2 DEP Scan

```python
def detect_dep(ticker, history_25d):
    """4% breakout + 9M volume in last 25 days + current ATR consolidation."""
    had_breakout = any(d.return >= 0.04 and d.volume >= 9_000_000 for d in history_25d)
    is_consolidating = atr_5d(ticker) < atr_20d(ticker) * 0.5
    return had_breakout and is_consolidating
```

### 5.3 EP Suspect Detection

- Pre-market gap > 4% on 100K+ volume
- Earnings calendar match (today or yesterday)
- Compute earnings surprise % (actual vs. estimate)

### 5.4 Priority Flagging

| Priority | Condition |
|----------|-----------|
| 🔥 Highest | SOS on Sugar Baby list |
| 🔴 High | DEP on Sugar Baby list |
| 🟡 Medium | SOS on non-Sugar Baby |
| 🟢 Low | DEP on non-Sugar Baby |

---

## 6. Pattern Recognition = Numerical, Not Visual

**Key insight**: Pradeep's patterns are defined by precise numerical thresholds, not visual chart shapes.

| "Pattern" | Quantifiable Condition |
|-----------|----------------------|
| Range expansion (SOS Day 1) | `today_return > max(prior_5_day_returns)` |
| 4% breakout | `close / prev_close ≥ 1.04` |
| $ breakout (FHP) | `close - open ≥ $0.90` |
| 9M volume | `volume ≥ 9,000,000` |
| Tight consolidation | `ATR_5d < ATR_20d × 0.5` |
| Volume expansion | `volume / avg_volume > 2` |
| Bullish breadth | `close / close_65d ≥ 1.25` |
| Capitulation | `T2108 < 10%` AND `primary < 200` |

The visual "small candles → big candle" is just a representation of the numerical condition.

---

## 7. Daily Session Pipeline Design

### 7.1 Discovery

StockBee video URLs follow the pattern:
```
Page URL: https://stockbee.biz/video/YYYY-MM-DD-slug/
CDN URL:  https://stockbee-videos.b-cdn.net/YYYY-MM-DD-slug/YYYY-MM-DD-slug.mp4
```

Discovery method:
1. Playwright login to stockbee.biz
2. Navigate to `/video/` or `/meetings/`
3. Extract new video URLs from the page
4. Derive CDN URLs from page URLs

### 7.2 Transcription

- Use existing `transcribe.py` with `--backend deepgram`
- New flag: `--cdn-url` for direct CDN input
- Output: Raw transcript JSON in `trading-vault/sessions/YYYY/MM/YYYY-MM-DD-{session}.md`

### 7.3 Idea Extraction

After each transcription, run extraction to find:
1. **Tickers mentioned** — regex `[A-Z]{2,5}` with NON_TICKER filter
2. **Setup types** — SOS, DEP, EP, Sugar Baby, Anticipation, etc.
3. **Catalysts** — Earnings, sales, product, government, story
4. **Key phrases** — "buy", "watch", "avoid", "stop at"

### 7.4 Cross-Validation

Compare Pradeep's daily ideas with our radar output:

| Radar Found It? | Pradeep Mentioned It? | Action |
|-----------------|------------------------|--------|
| ✅ Yes | ✅ Yes | ✅ Match — high confidence |
| ✅ Yes | ❌ No | ⚠️ Our radar flagged something Pradeep missed — investigate if it's a genuine setup |
| ❌ No | ✅ Yes | ⚠️ Pradeep found something our radar missed — investigate why |
| ❌ No | ❌ No | — Neither of us found it (probably not a setup) |

### 7.5 Discrepancy Investigation

**When our radar misses a stock Pradeep discusses:**

| Miss Reason | Investigation | System Fix |
|-------------|-------------|------------|
| Universe filter excluded it | Check if stock was in our data | Adjust universe filter |
| Scan threshold was wrong | Compare 4% vs. actual move | Calibrate threshold |
| Catalyst type not in calendar | Earnings date not in feed | Add data source |
| Pattern not detected | Was it an anticipation setup? | Add anticipation scan |
| Pradeep's subjective judgment | Pattern quality assessment | Flag as "human judgment" |
| Story EP we can't detect | News/NLP gap | Add story EP scanning |

**When our radar flags something Pradeep doesn't discuss:**

| Flag Reason | Investigation | Action |
|-------------|-------------|--------|
| False positive from scan | Check if it was a genuine setup | Refine scan |
| Pradeep didn't cover it that day | Check next sessions | Track over time |
| Our thesis was wrong | Compare outcome | Learning |
| Pradeep mentioned it but not by ticker | Search transcript for description | Improve NLP extraction |

---

## 8. Bug Fixes & Calibration History

### 2026-06-04 — Breadth Calculator Window Bug (CRITICAL)

**Problem:** `breadth_calculator.py` loaded only 75 calendar days (~55 trading days), so `pos - 65` was negative. Primary Up, Monthly 25, Fib 13 all returned 0.
**Fix:** Changed window from 75d to 400d (~280 trading days).
**Impact:**
- Primary Up: 0 → 588
- Breakout: 74 → 111
- Breakdown: 382 → 438 (vs Pradeep's 431 — near exact!)

### 2026-06-04 — Scanner Dict Mutation Bug

**Problem:** `scanner.py` Phase 3 mutated `results` dict during iteration, causing RuntimeError.
**Fix:** Changed `results.items()` → `list(results.items())`.

---

## 9. Technology Stack

| Component | Tool | Notes |
|-----------|------|-------|
| Market data | FMP ($22–59/mo) | Real-time + fundamentals + earnings |
| Transcription | Deepgram `nova-2` | English sessions work best |
| Scraping | Playwright | Login walls require real browser |
| Processing | Python + pandas | Standard data science stack |
| Scheduling | APScheduler or Windows Task Scheduler | Nightly + morning runs |
| Storage | SQLite (local) | 7.6M rows, 1.1GB |
| Primary interface | Obsidian notes | Searchable, permanent, versioned |
| Dashboard | TypeScript (Phase 7) | Real-time visualization |

---

## 10. Implementation Status

### Phase 0: Discovery & Infrastructure (COMPLETE)
- [x] Playwright login to StockBee, snapshot MM page structure ✅ (2026-06-02)
- [x] Discover daily session video page structure ✅ (2026-06-02)
- [x] Create Python project structure ✅ (2026-06-02)
- [x] Create Obsidian subvault folders ✅ (2026-06-02)
- [x] Set up FMP API key ✅ (2026-06-03)
- [x] Build SQLite schema (8 tables) ✅ (2026-06-03)
- [x] Build breadth calculator ✅ (2026-06-03, window bug fixed 2026-06-04)
- [x] Build nightly runner ✅ (2026-06-03)
- [x] Backfill historical data (8,753 tickers, 7.6M rows) ✅ (2026-06-04)

### Phase 1: Setup Scanner (COMPLETE)
- [x] BaseScan abstract class ✅ (2026-06-03)
- [x] 8 scan modules (DEP, SOS, ANT, EP 9M, WSS, Reversal, Sugar Baby, MM) ✅ (2026-06-03)
- [x] CLI orchestrator (`scanner.py`) ✅ (2026-06-03)
- [x] Regime gating ✅ (2026-06-03)

### Phase 2: Catalyst Detection (COMPLETE)
- [x] Earnings calendar integration ✅ (2026-06-03)
- [x] Momentum signal enhancement ✅ (2026-06-03)
- [x] Multi-ticker batch enrichment ✅ (2026-06-03)

### Phase 3: Entry Signals (COMPLETE)
- [x] Signal scoring engine ✅ (2026-06-03)
- [x] Position sizing with setup-specific stops ✅ (2026-06-03)
- [x] A+/A/B/C ratings ✅ (2026-06-03)
- [x] Scanner integration ✅ (2026-06-03)

### Phase 4: Obsidian Note Generation (COMPLETE)
- [x] Daily Market Monitor notes ✅ (2026-06-02)
- [x] Daily Trading Idea notes ✅ (2026-06-03)
- [x] Session Pipeline notes ✅ (2026-06-04)
- [x] KB concept index notes (12) ✅ (2026-06-04)

### Phase 5: Session Pipeline (COMPLETE)
- [x] Video discovery ✅ (2026-06-03)
- [x] CDN download with resume ✅ (2026-06-03)
- [x] Deepgram transcription wrapper ✅ (2026-06-03)
- [x] Idea extractor (regex-based) ✅ (2026-06-04)
- [x] Cross-validator ✅ (2026-06-04)
- [x] Session note generator ✅ (2026-06-04)

### Phase 6: Dashboard (PENDING — Next)
- [ ] TypeScript dashboard
- [ ] Real-time visualization
- [ ] WebSocket or SSE for live updates

---

## 11. Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **Obsidian-first** | Your stated preference; notes are searchable, permanent, versioned |
| **Numerical patterns, not visual** | Pradeep's methods are data-driven; patterns = formulas |
| **Cross-check with StockBee MM** | Validate our calculations against the master; detect drift |
| **Decision support, not auto-trade** | Human judgment on catalyst quality and setup qualification is the edge |
| **FMP over polygon.io** | FMP has real-time + earnings + sales + analyst data — critical for EP Magna 53 |
| **Daily session transcription** | Living method updates + real-time validation feedback loop |
| **SQLite, not Postgres/Neo4j** | Lightweight, single-file, no additional infra; 7.6M rows already stored |
| **Pure Python, not PowerShell** | Cross-platform, version-controlled, testable |

---

## 12. Credential Security

StockBee credentials stored in:
```
D:\opencodeworkspace\.trading\.env  (gitignored)
```

Never:
- Hardcoded in Python files
- Included in Obsidian notes
- Committed to git
- Shared in chat history (rotate if exposed)

---

*Last updated: 2026-06-04*
*Next action: Phase 7 Dashboard (TypeScript real-time) or T2108/Primary gap investigation*
