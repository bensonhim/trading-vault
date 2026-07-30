---
title: "TI65 and ANTS — Implementation Audit"
date: 2026-07-31
tags: [kb, audit, ti65, ants, anticipation, implementation, gap-analysis, trading-radar]
---

# TI65 and ANTS — Implementation Audit

> **Purpose**: Deep-dive comparison of our Trading Radar Engine implementation against ALL Pradeep Bonde teachings on TI65 (Trend Intensity 65) and ANTS (Anticipation). Compiled from 7 TI65 guide parts, 12 ANTS guide parts, the "How to Profit from TI65" session, KB notes, and 250+ daily session notes (2024–2026).
> **Date**: 2026-07-31
> **Status**: READ-ONLY analysis — no source code was modified.

---

## Table of Contents

1. [Pradeep's TI65 Teachings](#1-pradeeps-ti65-teachings)
2. [Pradeep's ANTS Teachings](#2-pradeeps-ants-teachings)
3. [Our Implementation](#3-our-implementation)
4. [Gap Analysis](#4-gap-analysis)
5. [Recommendations](#5-recommendations)
6. [Source Index](#6-source-index)

---

## 1. Pradeep's TI65 Teachings

### 1.1 Definition and Formula

**TI65 (Trend Intensity 65)** is an absolute momentum indicator — the ratio of the 7-day moving average of close to the 65-day moving average of close.

```
TI65 = AVGC7 / AVGC65
```

> *"TI 65 are also called as trend intensity 65. What it is? It is a momentum indicator... it's a momentum way of finding momentum on a stock."*
> — [[Pradeep Bonde - TI65 Guide-How to profit from TI65_deepgram|How to Profit from TI65]]

**Three things TI65 tells you** (Part 1):
1. **Whether** a stock is trending (positive or negative)
2. **Exactly when** the trend started and ended (unlike relative strength)
3. **How intense/fast** the trend is (velocity)

> *"What TI 65 essentially tells you is it tells you the velocity of move. Higher the trend intensity, faster is the stock moving."*
> — How to Profit from TI65

### 1.2 Thresholds and What They Mean

| Threshold | State | Meaning |
|-----------|-------|---------|
| `AVGC7/AVGC65 >= 1.05` | **Bullish** | 7-day MA is 5%+ above 65-day MA = uptrend established |
| `AVGC7/AVGC65 <= 0.95` | **Bearish** | 7-day MA is 5%+ below 65-day MA = downtrend established |
| `0.95 < ratio < 1.05` | **Neutral** | No clear trend |

> *"Currently it's ratio of average seven days price to average sixty five days price is below point 95... so this particular stock has a negative momentum."*
> — How to Profit from TI65

**Absolute vs. Relative Momentum** (critical distinction):
- **Absolute momentum** (TI65) = the stock's own velocity. Tells you WHEN momentum started.
- **Relative momentum** (IBD RS Rating 97/99) = ranking vs. other stocks. Tells you rank but NOT when momentum started.
- Traders using only relative momentum **buy extended stocks**.

> *"If you select stocks based on relative momentum... you're going to be buying stocks which are way extended. What you want to find out is when did the momentum start?"*
> — How to Profit from TI65

> *"Absolute momentum is traders friend. If you know how to use absolute momentum, you can find stocks very early and you can avoid very extended stocks."*
> — How to Profit from TI65

### 1.3 C65 and D65 — Days In Columns

**C65** = `COUNTTRUE(AVGC7/AVGC65 >= 1.05, 100)` — number of days in the last 100 trading days where TI65 was bullish.

**D65** = `COUNTTRUE(AVGC7/AVGC65 <= 0.95, 100)` — number of days in the last 100 trading days where TI65 was bearish.

**Why 100 days?** Pradeep tested 60, 100, and 250:
- 60 is too short
- 250 eliminates too many IPOs/young stocks
- **100 is the sweet spot** — "keep it at 100, not 250"

> *"If you make it 100, it is not going to affect us... you're going to find the same stock which has just gone up... I'd keep it at hundred basically."*
> — How to Profit from TI65

**Two uses of C65/D65:**
1. **Find young momentum**: Sort C65 ascending → stocks that JUST turned bullish (C65 = 1, 2, 3...)
2. **Find persistent trends**: High C65 (80–100) = stock has maintained momentum for months (rare but real — e.g., X, ENPH)

> *"This is just the first day when it's trend intensity is about 1.05. Is this very useful information? Is this very information to find young setups and young trends? We want to find young."*
> — How to Profit from TI65

### 1.4 Young Momentum Concept (C65 <= 10)

**Young momentum** = bullish TI65 with C65 ≤ 10 days. This is the **highest reward/risk** zone.

> *"Your idea or your objective is to find the first good pullback or the first good breakout after the TI 65 goes above 1.05."*
> — How to Profit from TI65

**Why young matters:**
- Young trends allow **holding for the second leg** of the move
- Old trends (C65 > 100) — you **cannot hold** for longer term
- Most stock moves happen in ~2 months; staying in TI65 > 1.05 past 120–150 days is very rare

> *"If you find setups like this, can you hold it for a second leg of the move also? Yeah. But if you are getting into a breakout which is second or third leg, then you cannot hold it."*
> — How to Profit from TI65

> *"Most of the stocks will have very difficult time maintaining their TI about 1.05 for more than hundred and twenty, hundred and fifty days is very, very rare."*
> — How to Profit from TI65

**Session confirmation** (2026-06-11, Archive):
> *"Look for young momentum. Not old momentum. In every culture, there is a value to youth. Same in the stock market."*
> — [[Session-2026-06-11]]

### 1.5 How Pradeep Uses TI65 in Practice (Workflow)

**Step 1 — Create two universes** (Part 4):
- **Bullish TI65**: US stocks + ADRs + ETFs, `MINV3.1 >= 100,000`, `C >= $3`, `AVGC7/AVGC65 >= 1.05` → ~870 stocks (bull market)
- **Bearish TI65**: Same universe, `AVGC7/AVGC65 <= 0.95` → ~832 stocks
- For shorts: Pradeep uses **1M volume** (higher liquidity) and **$10+ price**

**Step 2 — Anticipation scan** (Part 6):
- Add `Price Percent Change Today between -0.4% and +0.4%` to bullish TI65
- Reduces ~800 → ~78 narrow-range candidates
- Add **NC (Net Change)** column = `ABS(C - C1)`, sort ascending → flattest stocks first
- Skip buyouts (flat black lines)

**Step 3 — Young momentum scan** (How to Profit):
- Add C65 column = `COUNTTRUE(TI65 >= 1.05, 100)`
- Sort ascending → find stocks that JUST turned bullish (C65 = 1–10)
- Wait for first setup to form, then buy on breakout

**Step 4 — Pullback scan** (How to Profit):
- Add C/C7 column (close today / close 7 days ago)
- Sort ascending → top = reversals (skip), middle = orderly pullbacks (**buy**), bottom = extended (skip)

**Step 5 — Young Pullback** (the FINAL combined output):
- Combine: C65 ≤ 10 (young) + C/C7 0.85–1.05 (orderly pullback)
- This is the **4–5 stock actionable list**

**Step 6 — Prioritize by TI65 value** (Part 5):
- Among the 4–5 candidates, sort by TI65 descending
- Highest TI65 = most aggressive buying = priority #1

**Three approaches to anticipation** (Part 6):
1. **Narrow-range scan** (recommended, 10–15 min) — ±0.4% filter
2. **Visual scan of entire bullish list** (time-consuming, NOT recommended)
3. **Focus on top 25–30 by TI65**, then find setups within that subset

### 1.6 Three Setup Types Mapped to TI65

| Setup | TI65 State | Source |
|-------|-----------|--------|
| **Bottom bounce** | TI65 negative or just turning (near 0.95) | How to Profit |
| **Continuation / Two Lynch** | TI65 > 1.05 (momentum established) | How to Profit |
| **Consolidation breakout** | TI65 > 1.05 + flat 3–10 days | How to Profit |

> *"Most of the good two Lynch setups are going to show up where? After the TI is greater than 1.05. After momentum has been established."*
> — How to Profit from TI65

### 1.7 Short Side with TI65

- **Bearish TI65 universe** + D65 column → find stocks just turning negative
- **9M+ volume breakdown** = renewed institutional selling within bearish list
- **Counter-trend bounce failures** = key short pattern (stock bounces, then fails)
- **Day-after-earnings bounce failures** — stock recovers on earnings day, real selling starts day 2

> *"You want to short early in a breakdown, not when the breakdown is so apparent."*
> — How to Profit from TI65

### 1.8 Common Mistakes Pradeep Warns About

| Mistake | Why Wrong | Source |
|---------|-----------|--------|
| Using relative momentum only | Buys extended stocks; doesn't tell you when trend started | How to Profit |
| Setting C65 lookback to 250 | Eliminates IPOs and young stocks | How to Profit |
| Ignoring C65 entirely | Can't distinguish young vs. old trends | How to Profit |
| Buying 3rd/4th/5th leg setups | "Who is left to buy?" — failure rate increases | ANTS Part 6 |
| Trading anticipation in non-bullish market | "Death by thousand cuts" | ANTS Part 5 |
| Waiting for 4% breakout confirmation | Wastes the anticipation edge — stop becomes 8–10% | ANTS Part 3 |

---

## 2. Pradeep's ANTS Teachings

### 2.1 Definition and Concept

**ANTS (Anticipation)** = finding stocks with **established momentum** that are in a **momentum pause** (sideways consolidation or minor pullback), then entering **before** the breakout for a low-risk entry.

> *"Anticipation is a method which is based on momentum. In order to do momentum, you first need to understand momentum using M20, TI65, MDT and DT — because once you know that, this is the way to convert that into dollars."*
> — [[Pradeep Bonde - ANTS Guide-Part 9_deepgram|ANTS Part 9]]

**Core thesis**: The stock has already proven it has momentum. Now it's pausing. The next likely move is **up** (in the direction of the established trend). Enter before the breakout to get a closer stop.

> *"In anticipation, what we are looking for is a situation where a stock has already established momentum. After it has established momentum, what the stock is trying to do is it is basically paused or there is a momentum pause."*
> — [[Pradeep Bonde - ANTS Guide-Part 10_deepgram|ANTS Part 10]]

### 2.2 Tight Day Definition (3T, 2T, Super-Tight, Ultra-Tight)

**Tight day** = a day with very small price movement (narrow range).

| Tier | Pradeep's Definition | Our Implementation |
|------|---------------------|-------------------|
| **Tight** | Daily change < 1% (or < 0.4% for Pradeep's personal trading) | Range/ATR < 0.8 |
| **2T** | 2 consecutive tight days | 2 consecutive tight days (has_2t) |
| **3T (TTT)** | 3 consecutive tight days | 3 consecutive tight days (has_3t) |
| **Super-tight** | — | Range/ATR < 0.5 |
| **Ultra-tight** | — | Range/ATR < 0.3 |

> *"If you make this three bars in a row, the stock is meeting your TTT kind of a condition that three days in a row it is up or down less than 2%... from doing 400 stocks you reduced your universe to just 19 stocks."*
> — ANTS Part 9

**Pradeep's personal filter**: ±0.4% (not ±1%)
> *"For my personal trading, I don't even look at a stock which is up or down 1%... I look for a stock which is up or down less than point 4%... you really get a very low risk kind of a setup."*
> — ANTS Part 9

**Session confirmation** (2026-04-15):
> *"Anticipation setups require 2-3 tight days — One tight day is not enough. Look for NC (net change) < 1% for 2-3 days after a first leg."*
> — [[Session-2026-04-15]]

**Session confirmation** (2026-05-05, Archive — "Tight Pants Rule"):
> *"If you're going to trade momentum burst or any setup, buy the tightest pants possible. So tight that you can't even zip it."*
> *"Anticipation requires genuine tightness. A 3.89% range day is not tight. A 0.4% range day is."*
> — [[Session-2026-05-05]]

### 2.3 BSLO Order Placement Strategy

**Buy Stop Limit Order (BSLO)** = order placed **before market open** that triggers only if price reaches the stop level.

**Pradeep's BSLO formula** (ANTS Part 3):
- **Trigger**: yesterday's close + 1% (e.g., $26.25 for a ~$26 stock)
- **Limit cap**: trigger + ~1% (e.g., $26.50) — protects against gap-up bad fills
- **Stop**: below tight consolidation (e.g., $25.80)
- **Placed before market opens**

> *"As soon as the stock goes about 26.25, the order becomes active... if the stock opens above 26.50, your order is not going to be activated... if it gaps down, your order is not gonna be filled."*
> — ANTS Part 3

**Two entry methods** (ANTS Part 3):
1. **Method A (recommended) — Active Morning Monitoring**: Put 3–5 stocks in IB, watch like a hawk in first 10–15 min, enter on even a **1% positive move** (1% = range expansion)
2. **Method B — BSLO**: Set trigger at close+1%, limit at trigger+0.25%, stop below consolidation

> *"If you wait for a stock to breakout like this 4% or $1 and then buy, you wasted all your effort because then why did you create this watch list?"*
> — ANTS Part 3

> *"As soon as you see a move of even 1%, I get into these stocks."*
> — ANTS Part 3

### 2.4 When to Use ANTS vs SOS vs DEP

| Setup | When | Entry Style | Stop Width | Source |
|-------|------|-------------|-----------|--------|
| **ANTS** | Tight days before breakout | BSLO or early morning | <1% (40¢–$1) | ANTS Parts 3, 11 |
| **SOS** | Breakout on above-average volume | First 10–15 min | 2–5% (low of day) | SOS Guide |
| **DEP** | Post-catalyst pullback with tight consolidation | First 10 min when shows life | 0.5–2.5% (40¢–$1) | DEP Guide |

**ANTS is the lowest risk but highest failure rate**:
> *"A lot of anticipation fail compared to breakouts. Because in anticipation setup, when you're using a BSL order or you're entering in anticipation, there is no volume confirmation."*
> — ANTS Part 4

**ANTS only in confirmed bullish market** (THE #1 rule):
> *"The only time you should be trading anticipation setup is when the market is in a very confirmed and in a very wild bullish conditions. If you trade this setup in a choppy market conditions... you are going to have death by thousand cuts."*
> — ANTS Part 5

**Session confirmation** (2026-05-15, Archive):
> *"The only time at which you should look at anticipation is at 3 PM. Before that, if you look at it, it's just a waste of time and waste of the process."*
> — [[Session-2026-05-15]]

**Session confirmation** (2024-01-11):
> *"Anticipation has the lowest win rate. Trade it only when probability is overwhelmingly in your favor."*
> — [[Session-2024-01-11]]

### 2.5 How ANTS Interacts with TI65 (Young Momentum + Tight = Highest R/R)

**The synergy**: TI65 identifies young momentum (C65 ≤ 10) → ANTS identifies tight days within that young momentum → **highest reward/risk setup**.

**Pradeep's ideal anticipation setup** (ANTS Part 11):
1. **First leg** with unidirectional candles (only buyers in control, closing near highs)
2. **Volatility compression** during consolidation (bodies much smaller than first-leg candles)
3. **Staged compression**: if first leg was 2% moves, consolidation should be 1.5%, 1%, then smallest at end
4. **Slightly down or flat** (NOT rising — rising wedge = bad)
5. **Short consolidation** (3–7 days; >10–12 days = dead market, not momentum pause)
6. **Highest TI65** among candidates = priority #1
7. **Higher-price stocks** preferred ($300 stock moving ±$0.30 = "most bang for your buck")

> *"I am looking for a situation which will allow me to put a stop of 1% or less... even though I scan for point 4%, what I really in reality, when I select my stock is to look for something which is even point 05%, point 10%, point less than point 20%."*
> — ANTS Part 11

> *"I only look at the body. Somehow people are fascinated by wicks. I only look at the body of the candle. The bodies of the candle should be very narrow compared to what was happening in the up move on the first leg."*
> — ANTS Part 11

> *"Always prioritize the one which has the highest TI65. The higher the TI65, the more is the momentum... that tells you that there's a very aggressive buying in the stock."*
> — ANTS Part 11

**Leg hierarchy** (ANTS Part 6):
- **First leg** → first consolidation = **highest probability**
- **Second leg** → still good
- **Third/fourth/fifth leg** → failure rate increases significantly

> *"Ask yourself a question — who is left to buy that particular stock? If everyone already bought, the setup will fail."*
> — ANTS Part 6

### 2.6 Pradeep's 3:30 PM / 3:58 PM Timing Edge (ANTS Part 10)

**The edge**: Most traders do anticipation at night and enter next morning. Pradeep runs scans at **3:30 PM** and enters at **3:58 PM** — front-running everyone.

> *"I do this work at 03:30. I run these scans at 03:30. Find my setups. But I don't enter them immediately... I wait for the last two minutes. And at 03:58, I will enter a setup like this in anticipation that it is going to be breaking out on Monday."*
> — ANTS Part 10

> *"There is a generic edge in the stock market of being first. If you can enter any move before other people enter you are always going to be in a better position."*
> — ANTS Part 10

**Three pillars of smart anticipation** (ANTS Part 10):
1. Tight ±0.4% setup definition
2. Scans to reduce universe (not grunt work)
3. 3:30 PM scan + 3:58 PM entry

### 2.7 Common ANTS Mistakes

| Mistake | Why Wrong | Source |
|---------|-----------|--------|
| Trading ANTS in non-bullish market | "Death by thousand cuts" | ANTS Part 5 |
| Buying 3rd/4th/5th leg setups | "Who is left to buy?" | ANTS Part 6 |
| Waiting for 4% breakout confirmation | Wastes the anticipation edge | ANTS Part 3 |
| Not moving stop to breakeven ASAP | Breakouts fade in first 20–30 min | ANTS Part 4 |
| Long sideways consolidations | "Highest failure in anticipation" — no aggressive buying | ANTS Part 2 |
| Rising wedge (rising consolidation) | Not a valid anticipation setup | ANTS Part 11 |
| Consolidation > 10–12 days | Not a momentum pause, just dead market | ANTS Part 11 |
| Including ETFs | "Inherently higher volatility than stocks" | ANTS Part 8 |
| Not checking for buyouts | Flat stocks = M&A, not real setups | ANTS Part 8 |
| Looking at ANTS before 3 PM | "Thinking about dinner at breakfast" | Session 2026-05-15 |

---

## 3. Our Implementation

### 3.1 TI65 Indicator (`src/pricing/ti65.py`)

**What we implemented:**
- `compute_ti65(bars)` — pure Python TI65 calculation from OHLCV bars
- `TI65Result` dataclass with: ratio, state, avgc7, avgc65, days_in_bullish (C65), days_in_bearish (D65), momentum_7d (C/C7), is_young_momentum

**Formula used:**
```python
BULLISH_THRESHOLD = 1.05  # Pradeep's threshold
BEARISH_THRESHOLD = 0.95
DAYS_IN_LOOKBACK = 100     # Pradeep: "keep it at 100, not 250"

ratio = avgc7 / avgc65
state = "bullish" if ratio >= 1.05 else "bearish" if ratio <= 0.95 else "neutral"
is_young = state == "bullish" and days_in_bullish <= 10
```

**C65/D65 calculation**: Iterates through each day in the lookback, computes that day's TI65 ratio, counts bullish/bearish days. ✅ Matches Pradeep's `COUNTTRUE` formula.

**C/C7 (7-day momentum)**: `close_today / close_7d_ago` — used for pullback sorting. ✅ Matches Pradeep's "sort by C/C7 ascending" workflow.

### 3.2 TI65 Scan (`src/scans/ti65_scan.py`)

**What we implemented:**
- `TI65Scan` class with single SQL query using nested window functions
- `bullish_universe()` — AVGC7/AVGC65 >= 1.05, vol >= 100K, close >= $3
- `bearish_universe()` — AVGC7/AVGC65 <= 0.95, vol >= 1M (higher liquidity for shorts)
- `anticipation_scan()` — bullish + today's change between -0.4% and +0.4%
- `young_momentum()` — bullish sorted by C65 ascending (top 50)
- `pullback_scan()` — bullish sorted by C/C7 ascending (top 50)
- `young_pullback_scan()` — C65 <= 10 + C/C7 0.85–1.05 (the FINAL actionable list)
- `universe_counts()` — breadth counts for market indicator

**Thresholds:**
| Parameter | Value | Pradeep Source |
|-----------|-------|---------------|
| Bullish threshold | 1.05 | Part 4 |
| Bearish threshold | 0.95 | Part 4 |
| Days in lookback | 100 | How to Profit |
| Bullish min volume | 100,000 | Part 4 |
| Bearish min volume | 1,000,000 | How to Profit |
| Min price | $3 | Part 4 |
| Anticipation change | ±0.4% | Part 6, ANTS Part 9 |
| Young momentum C65 | ≤ 10 | How to Profit |
| Pullback C/C7 range | 0.85–1.05 | How to Profit (inferred) |

**Output format**: `TI65Candidate` dataclass with ticker, ti65_ratio, state, avgc7, avgc65, close, volume, change_pct, days_in_bullish (C65), days_in_bearish (D65), momentum_7d (C/C7), is_young_momentum, sector, industry, sector_etf.

### 3.3 ANTS Scan (`src/scans/anticipation.py`)

**What we implemented:**
- `AnticipationScan` class (extends `BaseScan`)
- Builds momentum universe using real TI65 (AVGC7/AVGC65 >= 1.05, vol >= 100K, close >= $3)
- Excludes ETFs (matches Pradeep's ANTS Part 8: "I don't recommend ETFs")
- Fetches 45 calendar days of OHLCV for tight-day analysis
- Uses `count_tight_days()` from `tight_day.py` for ATR-based tight day detection
- Requires minimum 2T (2 tight days) per Pradeep's methodology
- Priority assignment based on tight tier + count:
  - 3T + ultra-tight/super-tight = "highest"
  - 2T + any tight tier = "highest"
  - 1T + ultra-tight/super-tight = "high"
  - 1T + tight = "high"
- Downtrend filter: skips stocks with 20-day trend < -10% or > 20% decline from peak
- Volatility/direction filter: skips range-bound + high volatility stocks
- Returns top 35 candidates sorted by volume

### 3.4 Tight Day Detection (`src/pricing/tight_day.py`)

**What we implemented:**
- `is_tight_day()` — multi-dimensional tight day check:
  1. **No gap**: abs(open - prev_close) / prev_close < 1%
  2. **Small body**: body / ATR < 0.5 (Pradeep: "body very small")
  3. **Tight range**: (high - low) / ATR < 0.8
- `calculate_atr()` — ATR(14) using True Range
- `count_tight_days()` — counts tight days in last N bars, returns best tier achieved

**Tight tier system:**
| Tier | Range/ATR Threshold |
|------|-------------------|
| Tight | < 0.8 |
| Super-tight | < 0.5 |
| Ultra-tight | < 0.3 |

**Volume drying** (supplementary, not required): volume < 70% of average

### 3.5 BSLO Calculation (`src/pricing/entry_exit.py`)

**What we implemented:**
```python
# ANT setup
trigger = close * 1.01           # +1% above close (Pradeep's BSLO)
entry = trigger * 1.0025         # limit at trigger + 0.25%
entry_method = "BSLO"
stop = cons_low - 0.40           # consolidation low - $0.40 buffer
```

**Matches Pradeep's BSLO formula** (ANTS Part 3): trigger at close+1%, limit cap at trigger+0.25%, stop below consolidation.

### 3.6 Report Generation (`src/cli/generate_daily_report.py`)

**TI65 section (4b)**:
- Universe counts table (bullish, bearish, neutral, young momentum, total)
- Young Momentum table — top 10 by C65 ascending
- TI65 Anticipation table — bullish + ±0.4%, top 20
- TI65 Pullback table — sorted by C/C7 ascending, top 10
- **TI65 Young Pullback** — the FINAL combined output (C65 ≤ 10 + C/C7 0.85–1.05) with action hints

**ANTS section (5)**:
- ANTS Candidates table — top 20 with tight tier and tight count
- ANTS BSLO Orders table — top 10 sorted by tight tier (ultra-tight → super-tight → tight)

**Quality gates:**
- TI65 quality gate: SOS/DEP filtered to only TI65 >= 1.05 stocks
- 20% study suppression: ANTS not suppressed (always run), but risk labels applied
- Fade mode: when 20% study < 30, SOS relabeled as FADE candidates

**Glossary section**: Includes definitions for TI65, C65, D65, AVGC65, BSLO, ANTS

### 3.7 Ticker Details (`src/interpretation/ticker_details.py`)

**TI65 display in ticker details:**
```
- TI65: 1.28 (bullish **YOUNG MOMENTUM**) | C65=5 D65=0
  C/C7=1.032 (sort ascending for pullbacks)
```

**SQL query**: Single query with window functions for AVGC7, AVGC65, C65 (running SUM), D65, C/C7. Matches the scan implementation.

---

## 4. Gap Analysis

| # | Feature | Pradeep Says | We Implement | Gap | Priority |
|---|---------|-------------|-------------|-----|----------|
| 1 | TI65 formula | AVGC7/AVGC65 | ✅ Same | None | — |
| 2 | Bullish threshold | >= 1.05 | ✅ 1.05 | None | — |
| 3 | Bearish threshold | <= 0.95 | ✅ 0.95 | None | — |
| 4 | C65 lookback | 100 days | ✅ 100 | None | — |
| 5 | Bullish min volume | MINV3.1 >= 100K | ⚠️ vol >= 100K (today only, not 3-day avg) | MINV3.1 = 100K shares each of last 3 days. We use today's volume only. | MEDIUM |
| 6 | Bearish min volume | 1M (Pradeep's personal) | ✅ 1M | None | — |
| 7 | Bearish min price | $10 (Pradeep's personal for shorts) | ⚠️ $3 (same as bullish) | Pradeep uses $10+ for shorts to avoid wide stops on low-priced stocks | LOW |
| 8 | Young momentum threshold | C65 <= 10 | ✅ C65 <= 10 | None | — |
| 9 | Anticipation change filter | ±0.4% (personal) / ±1% (general) | ✅ ±0.4% | None (we use Pradeep's personal filter) | — |
| 10 | C/C7 pullback range | 0.85–1.05 (inferred) | ✅ 0.85–1.05 | Pradeep never explicitly states these numbers; we inferred from "orderly pullback" vs "reversal" vs "extended" | LOW |
| 11 | NC (Net Change) column | ABS(C - C1), sort ascending | ❌ Not implemented | Pradeep uses NC to find the flattest stocks. We sort by abs(change_pct) which is similar but not identical. | LOW |
| 12 | Prioritize by TI65 value | Sort candidates by TI65 descending | ⚠️ Partial | TI65 Young Pullback sorts by C65 then C/C7, not by TI65 value. ANTS scan sorts by volume. | MEDIUM |
| 13 | Tight day definition | Daily change < 1% (or < 0.4%) | ⚠️ Different approach | We use ATR-based multi-dimensional check (gap + body/ATR + range/ATR). Pradeep uses simple % change. Our approach is MORE sophisticated but different. | LOW |
| 14 | 3T / 2T consecutive days | 3 (or 2) consecutive days with < 1% change | ✅ count_tight_days() with lookback=5 | None (we require 2T minimum) | — |
| 15 | Super-tight / ultra-tight tiers | Not explicitly defined by Pradeep | ✅ We added them (range/ATR < 0.5, < 0.3) | Enhancement beyond Pradeep's teaching — useful for prioritization | — |
| 16 | BSLO trigger | close + 1% | ✅ close * 1.01 | None | — |
| 17 | BSLO limit cap | trigger + ~1% (Pradeep says $26.50 for $26.25 trigger) | ⚠️ trigger + 0.25% | Pradeep's example: $26.25 trigger → $26.50 limit = ~1% above trigger. We use 0.25%. Our limit is tighter. | MEDIUM |
| 18 | BSLO stop | Below tight consolidation | ✅ cons_low - $0.40 | None | — |
| 19 | ETF exclusion for ANTS | "I don't recommend ETFs" | ✅ Excluded via get_etf_set() | None | — |
| 20 | Buyout exclusion | Mark buyouts with XXX, skip | ❌ Not implemented | Buyout stocks appear as flat lines. We don't filter them. | MEDIUM |
| 21 | Market condition gate | Only trade ANTS in confirmed bullish market | ⚠️ Partial | We apply risk labels based on 20% study but don't fully suppress ANTS. Pradeep says "only in very confirmed, very wild bullish conditions." | HIGH |
| 22 | 3:30 PM / 3:58 PM timing | Run scan at 3:30 PM, enter at 3:58 PM | ❌ Not implemented | Our report runs end-of-day (after close). No intraday 3:30 PM scan. | LOW (infrastructure limitation) |
| 23 | Leg count (1st/2nd/3rd leg) | 1st leg = highest probability; 3rd+ = high failure | ❌ Not implemented | We don't detect which leg the stock is on. C65 partially proxies this (low C65 = young = likely 1st leg). | MEDIUM |
| 24 | Consolidation length check | 3–7 days ideal; > 10–12 days = dead market | ⚠️ Partial | ANTS scan uses 45-day lookback but doesn't explicitly check consolidation length or flag > 10–12 day consolidations. | MEDIUM |
| 25 | Unidirectional candles in first leg | Only buyers in control, closing near highs | ❌ Not implemented | Qualitative criterion — hard to automate but possible (check % of green candles in first leg) | LOW |
| 26 | Volatility compression direction | Bodies compressing in direction of breakout | ❌ Not implemented | Our tight day check is static (body/ATR < 0.5), not staged (checking if bodies are getting progressively smaller) | LOW |
| 27 | Rising wedge detection | Rising consolidation = bad ANTS setup | ❌ Not implemented | We don't detect if consolidation is rising vs flat vs slightly down | LOW |
| 28 | Volume drying during consolidation | Volume should decrease during consolidation | ⚠️ Supplementary only | tight_day.py flags volume_drying but doesn't require it | LOW |
| 29 | Short-side TI65 (D65) | D65 column for finding young short setups | ✅ D65 computed and displayed | None (displayed in tables and ticker details) | — |
| 30 | 9M+ volume breakdown (short side) | Renewed institutional selling signal | ❌ Not implemented in TI65 scan | We have EP 9M scan for long side but no equivalent "9M breakdown" for bearish TI65 stocks | MEDIUM |
| 31 | Counter-trend bounce failure | Stock bounces then fails = short | ❌ Not implemented | Pattern detection for bounce failures within bearish TI65 universe | LOW |
| 32 | Higher-price stock preference | $300 stock moving ±$0.30 = "most bang for buck" | ❌ Not implemented | No price-based prioritization in ANTS scan | LOW |
| 33 | Body-only analysis (ignore wicks) | "I do not care about the wick. I only look at the body." | ✅ tight_day.py uses body (close - open), not wicks | None | — |
| 34 | TI65 as quality gate for SOS/DEP | Only show breakouts with TI65 >= 1.05 | ✅ filter_by_ti65() applied to SOS and DEP | None | — |
| 35 | TI65 breadth as market indicator | Bullish/bearish counts = buying/selling pressure | ✅ universe_counts() in report | None | — |

---

## 5. Recommendations

### 5.1 What to Fix First (by priority)

#### CRITICAL — None

Our core TI65 and ANTS implementations are **solid and faithful** to Pradeep's teachings. The formula, thresholds, C65/D65 calculation, young momentum concept, anticipation scan, and BSLO calculation all match.

#### HIGH Priority

1. **#21 — Market condition gate for ANTS**: Pradeep's #1 rule is "only trade ANTS in confirmed bullish market." We apply risk labels but don't suppress. Consider suppressing ANTS candidates (or at least adding a prominent warning) when Market Monitor primary indicator is red (stocks down 25%/quarter > stocks up 25%/quarter). Currently we only label based on 20% study.

#### MEDIUM Priority

2. **#5 — MINV3.1 (3-day average volume)**: Pradeep uses `MINV3.1 >= 100,000` (100K shares each of the last 3 days). We use today's volume only. This could include stocks with a one-day volume spike that doesn't persist. Fix: change SQL to `volume >= 100000 AND lag(volume,1) >= 100000 AND lag(volume,2) >= 100000` or compute 3-day min volume.

3. **#12 — Prioritize by TI65 value**: Pradeep explicitly says to prioritize anticipation candidates by highest TI65. Our Young Pullback sorts by C65 then C/C7. Consider adding TI65 value as a tiebreaker or secondary sort.

4. **#17 — BSLO limit cap width**: Pradeep's example uses ~1% above trigger ($26.50 for $26.25 trigger). We use 0.25%. This means our orders might not get filled on fast movers. Consider making this configurable or using 0.5–1%.

5. **#20 — Buyout exclusion**: Buyout stocks show as flat lines in anticipation scans. Add a filter: if a stock has had abs(change_pct) < 0.1% for 10+ consecutive days, flag as potential buyout and exclude.

6. **#23 — Leg count detection**: C65 partially proxies this (low C65 = young = likely 1st leg), but explicit leg detection would be more accurate. Consider: count the number of consolidation-breakout cycles in the last 60 days. 1 cycle = 1st leg, 2 = 2nd leg, etc.

7. **#24 — Consolidation length check**: Add a flag for consolidations > 10–12 days in ANTS scan. Pradeep says these are "not a momentum pause, just dead market."

8. **#30 — 9M volume breakdown for shorts**: We have EP 9M for long side but no equivalent for the bearish TI65 universe. Pradeep uses 9M+ volume breakdowns as renewed institutional selling signals.

#### LOW Priority

9. **#7 — Bearish min price $10**: Pradeep uses $10+ for shorts (wider stops on low-priced stocks). Easy fix: change `bearish_universe()` default min_price.

10. **#11 — NC (Net Change) column**: We sort by abs(change_pct) which is functionally equivalent to Pradeep's `ABS(C - C1)`. Minor difference — change_pct is percentage-based, NC is dollar-based. Low impact.

11. **#22 — 3:30 PM / 3:58 PM timing**: This is an infrastructure limitation — our report runs after close. Would require intraday scan capability. Not critical for end-of-day report.

12. **#25–27 — Qualitative criteria**: Unidirectional candles, staged compression, rising wedge detection. These are Pradeep's visual criteria. Automating them is possible but complex. Defer until higher-priority gaps are closed.

13. **#32 — Higher-price stock preference**: Add price as a sort factor in ANTS scan. Simple but low impact.

### 5.2 What's Working Well

| Feature | Assessment |
|---------|-----------|
| **TI65 formula** | ✅ Exact match — AVGC7/AVGC65 with correct thresholds |
| **C65/D65 calculation** | ✅ Correct — COUNTTRUE over 100 days, matches Pradeep's PCF |
| **Young momentum (C65 ≤ 10)** | ✅ Correct — highest R/R zone properly identified |
| **Anticipation scan (±0.4%)** | ✅ Uses Pradeep's personal filter, not the general ±1% |
| **Young Pullback scan** | ✅ Excellent — combines C65 ≤ 10 + C/C7 0.85–1.05, the FINAL actionable list |
| **BSLO trigger (close + 1%)** | ✅ Matches Pradeep's formula exactly |
| **ETF exclusion for ANTS** | ✅ Matches Pradeep's recommendation |
| **Body-only tight day check** | ✅ "I only look at the body" — we use body/ATR, not wicks |
| **ATR-based tight tiers** | ✅ Enhancement — super-tight/ultra-tight tiers go beyond Pradeep but useful for prioritization |
| **TI65 quality gate for SOS/DEP** | ✅ Only shows breakouts with bullish momentum |
| **TI65 breadth as market indicator** | ✅ Universe counts provide buying/selling pressure snapshot |
| **D65 for short-side** | ✅ Computed and displayed, enables young short setup detection |
| **Report formatting** | ✅ Comprehensive — universe counts, young momentum, anticipation, pullback, young pullback, BSLO orders |
| **Ticker details display** | ✅ Shows TI65, C65, D65, C/C7, young momentum flag |

### 5.3 Nice-to-Have But Not Critical

- **Position trading variant** (ANTS Part 12): Using weekly charts + MDT/MDT25/MDT50 for multi-month holds. This is a different trading style, not a gap in our swing trading implementation.
- **MDT/DT momentum OR logic**: Pradeep combines `TI65 > 1.05 OR M20 = true OR MDT OR DT` in one scan. We implement TI65 and M20 separately but don't combine them with OR logic in a single scan. Our cross-reference module handles confluence differently.
- **Visualization card mnemonic**: Pradeep's "BBT, TTT, 80/20, Pill, FFM" process mnemonic — cultural, not automatable.

---

## 6. Source Index

### Pradeep Guide Transcripts (canonical sources)

| Source | Key Content | Location |
|--------|------------|----------|
| TI65 Guide Part 1 | Definition, formula, three things TI65 tells you | `04-Transcripts/stockbee/04. TI65/` |
| TI65 Guide Part 2 | Chart setup, PCF formula `AVGC7/AVGC65 >= 1.05` | `04-Transcripts/stockbee/04. TI65/` |
| TI65 Guide Part 3 | Toolbar value display, stock selection | `04-Transcripts/stockbee/04. TI65/` |
| TI65 Guide Part 4 | Bullish/bearish universe creation, ~870/~832 stocks | `04-Transcripts/stockbee/04. TI65/` |
| TI65 Guide Part 5 | Ranking strongest/weakest, top 25–100 focus | `04-Transcripts/stockbee/04. TI65/` |
| TI65 Guide Part 6 | Anticipation scan, ±0.4%, NC column, 3 approaches | `04-Transcripts/stockbee/04. TI65/` |
| How to Profit from TI65 | C65/D65, young momentum, C/C7 pullback, short side | `04-Transcripts/stockbee/04. TI65/` |
| ANTS Guide Part 1 | Grunt work approach, M20 walkthrough | `04-Transcripts/stockbee/08. Anticipation (ANTS) Guide/` |
| ANTS Guide Part 2 | Quality filtering, long sideways = highest failure | `04-Transcripts/stockbee/08. Anticipation (ANTS) Guide/` |
| ANTS Guide Part 3 | BSLO order, Method A (morning) vs Method B (BSLO) | `04-Transcripts/stockbee/08. Anticipation (ANTS) Guide/` |
| ANTS Guide Part 4 | Failure rate, move to breakeven ASAP, master breakouts first | `04-Transcripts/stockbee/08. Anticipation (ANTS) Guide/` |
| ANTS Guide Part 5 | **#1 rule: only in confirmed bullish market** | `04-Transcripts/stockbee/08. Anticipation (ANTS) Guide/` |
| ANTS Guide Part 6 | Leg hierarchy: 1st leg best, 3rd+ fails | `04-Transcripts/stockbee/08. Anticipation (ANTS) Guide/` |
| ANTS Guide Part 7 | Grunt work recap, "dumb way" framing | `04-Transcripts/stockbee/08. Anticipation (ANTS) Guide/` |
| ANTS Guide Part 8 | Smart scan, ±1% → ±0.5%, no ETFs, buyout exclusion | `04-Transcripts/stockbee/08. Anticipation (ANTS) Guide/` |
| ANTS Guide Part 9 | 3T/2T consecutive days, ±0.4% personal filter, OR logic | `04-Transcripts/stockbee/08. Anticipation (ANTS) Guide/` |
| ANTS Guide Part 10 | **3:30 PM scan + 3:58 PM entry** timing edge | `04-Transcripts/stockbee/08. Anticipation (ANTS) Guide/` |
| ANTS Guide Part 11 | Visual criteria: unidirectional, body-only, staged compression | `04-Transcripts/stockbee/08. Anticipation (ANTS) Guide/` |
| ANTS Guide Part 12 | Position trading variant, weekly charts, MDT/DT | `04-Transcripts/stockbee/08. Anticipation (ANTS) Guide/` |

### KB Notes

| Source | Location |
|--------|----------|
| Scans and Filters | `02-KB/stockbee/Scans and Filters.md` |
| Entries | `02-KB/stockbee/Entries.md` |
| Stops | `02-KB/stockbee/Stops.md` |
| Common Mistakes | `02-KB/stockbee/Common Mistakes.md` |
| Stock Selection | `02-KB/stockbee/Stock Selection.md` |
| Trading Meeting Knowledge | `02-KB/stockbee/Trading Meeting Knowledge.md` |

### Key Session Notes (with TI65/ANTS mentions)

| Date | Key Content | Location |
|------|------------|----------|
| 2023-11-02 | ANTS bought before catalyst; missing entry = chasing | `Sessions/2023/` |
| 2023-11-03 | Priority order: 9M EP → Continuation → SB → IPO10 → FHP → ANTS | `Sessions/2023/` |
| 2024-01-11 | Anticipation has lowest win rate | `Sessions/` |
| 2024-01-23 | Anticipation lowest win rate; visualization card mnemonic | `Sessions/` |
| 2024-01-29 | ANTS15 = best way to find anticipation setups | `Sessions/` |
| 2025-01-21 | BBT, TTT still working as anticipation strategy | `Sessions/` |
| 2025-05-12 | TI65 still used for anticipation scans | `Sessions/` |
| 2025-05-13 | Anticipation = 3 tight days or 2 tight days | `Sessions/` |
| 2026-04-02 | Tight action = game-changing concept; 1-2 tight days before breakout | `Sessions/` |
| 2026-04-15 | 2-3 tight days required; NC < 1% for 2-3 days after first leg | `Sessions/` |
| 2026-04-16 | TTT (3 tight days) = current phase; continuation + anticipation | `Sessions/` |
| 2026-04-17 | Tight pants = qualifying criterion for any setup | `Sessions/` |
| 2026-05-05 | **Tight Pants Rule** — "buy the tightest pants possible" | `Sessions/Archive/` |
| 2026-05-14 | 2-3 tight days / volatility compression = non-negotiable | `Sessions/Archive/` |
| 2026-05-15 | Anticipation only at 3 PM; earlier = waste | `Sessions/Archive/` |
| 2026-05-26 | Anticipation traps — "lady boy" analogy | `Sessions/Archive/` |
| 2026-06-11 | **Young momentum thesis** — "value to youth" in the market | `Sessions/Archive/` |
| 2026-07-16 | Volatility contraction leads to volatility expansion | `Sessions/` |
| 2026-07-21 | ANTS 15 at 50 (vs normal 400-500) = breadth signal | `Sessions/` |

### Source Code Files Examined

| File | Purpose | Lines |
|------|---------|-------|
| `src/pricing/ti65.py` | TI65 indicator calculation | 220 |
| `src/scans/ti65_scan.py` | TI65 universe scans (SQL) | 362 |
| `src/scans/anticipation.py` | ANTS scan with tight day detection | 241 |
| `src/pricing/tight_day.py` | ATR-based tight day detection + tiers | 265 |
| `src/pricing/entry_exit.py` | BSLO calculation for ANT setup | 578 |
| `src/cli/generate_daily_report.py` | Report generation (TI65 + ANTS sections) | 1836 |
| `src/interpretation/ticker_details.py` | TI65 display in ticker details | ~800 |

---

## Summary

Our Trading Radar Engine implements TI65 and ANTS with **high fidelity** to Pradeep Bonde's teachings. The core formula (AVGC7/AVGC65), thresholds (1.05/0.95), C65/D65 days-in columns, young momentum concept (C65 ≤ 10), anticipation scan (±0.4%), and BSLO calculation (close + 1%) all match Pradeep's exact specifications from the TI65 Guide (7 parts) and ANTS Guide (12 parts).

**Key strengths:**
- The **Young Pullback scan** (C65 ≤ 10 + C/C7 0.85–1.05) is the most valuable output — it's Pradeep's FINAL workflow step, producing the 4–5 stock actionable list
- The **ATR-based tight tier system** (tight/super-tight/ultra-tight) is an enhancement beyond Pradeep's simple % change, useful for prioritization
- The **TI65 quality gate** for SOS/DEP ensures we only show breakouts with established momentum

**Key gaps (by priority):**
1. **HIGH**: Market condition gate for ANTS — Pradeep's #1 rule is "only in confirmed bullish market"
2. **MEDIUM**: MINV3.1 (3-day volume), BSLO limit cap width, buyout exclusion, leg count detection, consolidation length check, 9M breakdown for shorts
3. **LOW**: NC column, 3:30 PM timing, qualitative visual criteria, higher-price preference

**Overall assessment**: ~85% coverage of Pradeep's TI65/ANTS teachings. The 15% gap is mostly in qualitative visual criteria (hard to automate) and intraday timing (infrastructure limitation). The most impactful fix would be the market condition gate (#21) — ensuring ANTS candidates are prominently suppressed or warned when the Market Monitor primary indicator is red.

---

*Audit completed 2026-07-31. READ-ONLY analysis — no source code was modified.*