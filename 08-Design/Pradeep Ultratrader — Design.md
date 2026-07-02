---
title: "Pradeep Ultratrader — Design"
date: 2026-06-30
tags: [design, pradeep-ultratrader, stockbee, trading-radar, architecture]
---

# Pradeep Ultratrader — Design

> Agent + Python daemon hybrid system for daily US stock market monitoring and trade idea screening using Pradeep Bonde's StockBee methodology.

## 1. System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Home Workstation (Server)                  │
│                                                             │
│  ┌──────────────┐     ┌──────────────┐     ┌─────────────┐  │
│  │  Nightly     │     │  Intraday    │     │  OpenCode   │  │
│  │  Pipeline    │     │  Daemon      │     │  Agent      │  │
│  │  (5 PM ET)   │     │  (9:25 AM ET)│     │  (on-demand)│  │
│  └──────┬───────┘     └──────┬───────┘     └──────┬──────┘  │
│         │                    │                     │         │
│         ▼                    ▼                     ▼         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              SQLite (trading_radar.db)                │   │
│  │  OHLCV | TC2000 | ETF | Sugar Babies | Scans |        │   │
│  │  Catalysts | Confluence | Trades | Magna53          │   │
│  └─────────────────────────────────────────────────────┘   │
│         │                    │                     │         │
│         ▼                    ▼                     ▼         │
│  ┌──────────────┐     ┌──────────────┐     ┌─────────────┐  │
│  │  Obsidian    │     │  Telegram    │     │  Email      │  │
│  │  Daily Notes │     │  Real-time   │     │  Fallback   │  │
│  └──────────────┘     └──────────────┘     └─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Hybrid Runtime

| Component                                  | Role                                                                                                                           | When                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **Python daemon** (`intraday_runner.py`)   | Hard real-time: 5-min bar polling, 4% breakout detection, low-of-day stops, 2:58 PM ANTS, 3:58 PM reversal                     | Market hours (9:25 AM – 4:00 PM ET) |
| **Python pipeline** (`nightly_runner.py`)  | End-of-day: backfill OHLCV, compute Sugar Babies, run all scans, catalyst enrichment, cross-reference, generate Obsidian notes | 5:00 PM ET post-close               |
| **OpenCode agent** ("Pradeep Ultratrader") | Judgment: Two Lynch LLM review on A/A+ candidates, deep dive research, daily briefing generation, manual analysis              | On-demand / triggered by pipeline   |

### Scheduling

| Time (ET) | Task                                                                                  | Component            |
| --------- | ------------------------------------------------------------------------------------- | -------------------- |
| 5:00 PM   | Nightly pipeline: backfill, scans, catalysts, confluence, Obsidian notes              | `nightly_runner.py`  |
| 9:25 AM   | Pre-market scan: check watchlist tickers for 4%+ pre-market gains → Telegram alert    | `intraday_runner.py` |
| 9:30 AM   | Market open: start 5-min bar polling for SOS breakout triggers                        | `intraday_runner.py` |
| Every 60s | Poll live quotes for watchlist tickers; alert when 4% breakout triggers               | `intraday_runner.py` |
| 2:58 PM   | ANTS scan: find 3T/2T tight day stocks → calculate BSLO trigger/stop → Telegram alert | `intraday_runner.py` |
| 3:58 PM   | Reversal scan: find exhaustion patterns → Telegram alert                              | `intraday_runner.py` |
| 4:00 PM   | Market close: stop polling, run end-of-day summary                                    | `intraday_runner.py` |

Windows Task Scheduler starts `intraday_runner.py` at boot. The daemon uses `pandas_market_calendars` to check if today is a trading day; if not, it sleeps.

## 2. Data Sources

| Source | Purpose | API |
|--------|---------|-----|
| **StockBee scraper** | Market Monitor (sole truth) | `stockbee_scraper.py` (web scraping) |
| **FMP Premium** | All stock data | `/stable/` endpoints |
| **TC2000 universe** | Stock universe (~6,080 common stocks) | Pre-loaded in SQLite |
| **FMP 5-min intraday** | Low-of-day, half-of-day, opening range, real-time breakout detection | `/stable/historical-chart/5min` |
| **FMP batch quotes** | Daily OHLCV for universe (100 symbols/batch) | `/stable/batch-request-quote` |
| **FMP earnings calendar** | EP 9M candidate discovery | `/stable/earning-calendar` |
| **FMP press releases** | Catalyst identification | `/stable/press-releases` |
| **FMP SEC filings** | 8-K material events | `/stable/sec_filings` |
| **FMP analyst upgrades** | Magna 53 "3" criterion | `/stable/analyst-estimates` |
| **FMP income statement** | Sales growth (Magna 53 "A") | `/stable/income-statement` |
| **FMP company profile** | Market cap, IPO date (Cap 10×10) | `/stable/profile` |

### FMP Premium 5-Minute Data — What It Unlocks

With `/stable/historical-chart/5min`, we can compute:
- **Low of day** — real intraday low (SOS/EP stop)
- **Half of day** = `(open + low_of_day) / 2` — Pradeep's preferred stop
- **Opening range** (first 15-30 min) — SOS entry confirmation
- **Close near high** check — Two Lynch "H" criterion (intraday)
- **Range expansion detection** — compare current 5-min candle vs prior 2-5 days
- **Real-time 4% breakout detection** — scan during market hours
- **3:58 PM reversal scan** — intraday exhaustion pattern
- **2:58 PM ANTS** — BSLO trigger price calculation

## 3. StockBee Methodology Mapping

Each StockBee concept maps to a concrete implementation:

### Layer 1: Market Monitor
- **Source:** StockBee scraper (sole truth)
- **Output:** Traffic light (GREEN/YELLOW/RED) + breadth numbers
- **Gating:** Scans filter by MM color — longs only when GREEN/YELLOW; shorts only when RED

### Layer 2: 4% Breakout + 9M Volume
- **Scan:** `close >= prev_close × 1.04 AND volume > prev_volume AND volume >= 100_000`
- **Dollar breakout (>$60 stocks):** `close - open >= $0.90 AND volume >= 100_000`
- **9M volume (EP):** `volume >= 9_000_000` (absolute)

### Layer 3: Five Entry Methods

| Setup | Entry | Stop | Size | When |
|-------|-------|------|------|------|
| EP 9M | OPG (market open) | Low of day (8-20%) | Small (10-20%) | Catalyst day, first 15 min |
| SOS | When 4% triggers (intraday) | Low of day or half-of-day (2-5%) | 3-5K shares | First day of breakout |
| DEP | When stock "shows life" above consolidation | Below consolidation (0.5-2.5%) | Large (50-100%) | Days 3-10 after catalyst |
| ANTS | BSLO at close+1% (2:58 PM) | Below tight consolidation (<1%) | 10-20% | Day before breakout |
| Reversal | 3:58 PM price | Below open/prior close (0.5-2.5%) | 3-5K shares | Last 2 min of market |

### Layer 4: Stops — Percentage-Based, Not Fixed Dollar

| Setup | Stop Width | Source |
|-------|-----------|--------|
| DEP | 0.5%–2.5% | Below consolidation low; buffer scales with price level |
| EP Day 1 | 8–20% | Low of day (intraday 5-min data) |
| SOS | 2–5% | Low of day (high-priced) or half-of-day (cheaper) |
| ANTS | <1% | Below tight consolidation |
| Reversal | 0.5–2.5% | Below open/prior close |

**DEP buffer is NOT fixed $0.20/$0.40** — those are examples for low-priced stocks. The real rule is stop width = 0.5%–2.5%. For a $300 stock, the buffer is $1.50–$7.50, not $0.40.

### Layer 5: Position Sizing

```
Position Size = (Account × Risk%) / Stop Width
```
- Account: 1,000,000 HKD
- Risk per trade: 3,000 HKD (~$385 USD)
- USD/HKD: 7.8
- Soft cap: 25% of account
- Hard cap: 50% (DEP + Sugar Baby confluence)

### Layer 6: Catalysts (CatalystHunter)

- Earnings calendar (FMP)
- Press releases (FMP)
- SEC 8-K filings (FMP)
- Analyst upgrades (FMP)
- Insider trading (FMP)
- Keyword classification: FDA/Contract/Earnings/Guidance/Analyst/Insider

### Layer 7: Magna 53 + Cap 10×10 (for EP)

| Letter | Stands For | Requirement | Essential? |
|--------|-----------|-------------|-----------|
| **M** | Massive | Earnings acceleration 100%+ OR massive sales acceleration OR massive earnings surprise | ✅ Yes |
| **A** | Acceleration of sales | 39%+ sales growth back-to-back 2 quarters | ✅ Yes |
| **G** | Gap up | Gaps up 4%+ in pre-market on 100K+ volume | ✅ Yes |
| **N** | Neglect | No rally into earnings, low fund ownership, low analyst coverage, no news flow | ✅ Yes |
| **5** | 5-day short interest | Short interest ratio ≥5 days | Optional |
| **3** | 3+ analysts raise target | 3+ analysts raise price target after earnings | Optional |

**Cap 10×10:**
- Market cap < $10B
- IPO'd within 10 years

### Layer 8: Trade Management

- 80/20 rule: sell 80% into strength, trail 20%
- Move to breakeven first morning if positive
- Time stop: momentum burst day 3-5; reversal next day
- Tighten stop at 40-50% profit; sell 80% at 100%+

### Layer 9: Confluences

| Tier | Criteria | Action |
|------|----------|--------|
| A+ | Active setup + Sugar Baby + strong catalyst | Maximum size |
| A | Active setup + Sugar Baby | Standard size |
| B+ | Active setup + catalyst | Standard size |
| B | Active setup only | Smaller size |
| C | Sugar Baby only (no active setup) | Watch only — no position |

### Layer 10: Daily Process

| Time | Activity |
|------|----------|
| Pre-market (8:00-9:25) | Review MM, pre-market movers, DEP/SB watchlist, EP candidates |
| Morning (9:30-10:30) | SOS breakout alerts, EP entries, DEP entries |
| Midday (10:30-2:00) | Dead zone (Pradeep: go to gym) |
| Afternoon (2:00-4:00) | ANTS scan (2:58 PM), reversal scan (3:58 PM) |
| Post-market | Nightly pipeline: backfill, scans, notes, tomorrow prep |

## 4. Sugar Baby — Stock Selection (Not a Setup)

Sugar Babies is a **stock selection strategy**, not a setup. It identifies WHICH stocks to trade. You still use SOS/DEP/ANTS/EP for actual entries.

### Computation

- Count 4%+ breakout days with 9M+ volume over the full OHLCV lookback
- Multi-timeframe: 504d, 252d, 126d, 63d, 21d, 10d, 5d
- Top 20-30 by count = core list; up to 150 = expanded list
- SB candidates get confluence priority in cross-reference

### SB + Position Sizing

- DEP + SB = maximum size (25-50%+)
- SBs are choppy — wider intra-trade swings expected
- Tight DEP stop compensates: small stop width → large position size

## 5. VWAP — Not Used by Pradeep

Pradeep explicitly rejects VWAP:
> *"I don't pay attention to ADR, VWAP, all these things."*
> *"If you don't have clarity, then you are putting in VWAP."*

**Implementation:** Remove VWAP as a gating filter. Keep as informational field only (optional, in deep_dive notes). The real entry filters are:
1. 4%+ breakout (or dollar breakout for >$60)
2. Volume expansion (V > V1)
3. Two Lynch qualification
4. Market Monitor bullish
5. Not third+ leg
6. Catalyst identifiable
7. Sugar Baby = higher priority

## 6. Pre-Market 4% Detection

If a watchlist ticker is already up 4%+ in pre-market (before 9:30 AM):
- **This IS the breakout** — it happened in pre-market
- For EP 9M: gap up on earnings = classic EP pattern, enter at market open (OPG)
- For SOS: watchlist stock already triggered — alert at 9:25 AM, enter at/near open

**Daemon flow:**
1. At 9:25 AM ET: fetch pre-market quotes for all watchlist tickers
2. If any up 4%+ → immediate Telegram alert
3. At 9:30 AM: continue monitoring for intraday 4% breakouts
4. Set `trigger_price = yesterday_close × 1.04` for each watchlist ticker
5. Poll every 60 seconds; alert when `current_price >= trigger_price`

## 7. EP 9M vs DEP — When to Use Which

| Scenario | EP 9M (Day 0) | DEP (Days 3-10) |
|----------|--------------|-----------------|
| Life-changing catalyst (Magna 53 + Cap 10×10) | ✅ Enter at open, accept wide stop | ✅ Also set up DEP for later entry with tight stop |
| Good catalyst but wide stop uncomfortable | ⚠️ Consider waiting for DEP | ✅ Better risk/reward |
| Missed day 0 | ❌ Too late for EP | ✅ Wait for pullback, enter DEP |
| Working people (limited screen time) | ⚠️ Hard to execute fast | ✅ Better — days to research |

**Pipeline generates BOTH** — you decide based on conviction and risk tolerance.

## 8. Environment Variables

All credentials in `.env` (gitignored):

| Variable | Purpose | Status |
|----------|---------|--------|
| `STOCKBEE_USERNAME` | StockBee scraper | ✅ Set |
| `STOCKBEE_PASSWORD` | StockBee scraper | ✅ Set |
| `FMP_API_KEY` | FMP Premium API | ✅ Set |
| `TELEGRAM_BOT_TOKEN` | Telegram alerts | ✅ Set |
| `TELEGRAM_CHAT_ID` | Telegram alerts | ✅ Set |
| `EMAIL_APP_PASSWORD` | Gmail fallback | ✅ Set |
| `EMAIL_FROM_ADDRESS` | Gmail fallback | ✅ Set |
| `EMAIL_TO_ADDRESS` | Gmail fallback | ✅ Set |
| `DEEPGRAM_API_KEY` | Transcription | ✅ Set |

`config.json` references env vars via `{env:VAR_NAME}` — no secrets in git.

## 9. Output

### Obsidian Daily Notes
- Path: `C:\Users\msh897\Documents\Obsidian\trading-vault\06-Daily\stockbee\`
- Files: `Market Monitor-YYYY-MM-DD.md`, `Trade Ideas-YYYY-MM-DD.md`, `Daily Briefing-YYYY-MM-DD.md`

### Telegram Alerts
- Pre-market breakout (9:25 AM)
- SOS 4% trigger (intraday, real-time)
- ANTS setup (2:58 PM)
- Reversal setup (3:58 PM)
- EOD summary (4:00 PM)

### Email Fallback
- When Telegram blocked (corporate proxy)
- Same alert content

## See Also

- [[Pradeep Ultratrader — Technical Definitions]] — precise technical definitions for all concepts
- [[Pradeep Ultratrader — Implementation Plan]] — step-by-step implementation plan
- [[_Trading Radar Engine v2 — Implementation Notes]] — previous design (for reference)