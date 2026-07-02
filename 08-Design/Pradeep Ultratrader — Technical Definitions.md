---
title: "Pradeep Ultratrader — Technical Definitions"
date: 2026-06-30
tags: [design, pradeep-ultratrader, stockbee, definitions, technical]
---

# Pradeep Ultratrader — Technical Definitions

> Precise, unambiguous technical definitions for every StockBee concept implemented in code.
> Source: Pradeep Bonde's StockBee guides and transcripts in this vault.
> These definitions are the single source of truth — both Python code and agent prompts reference them.

## 1. Price Moves

### Daily Move (Close-to-Close)

```
daily_move_pct = (close_today - close_yesterday) / close_yesterday × 100
```

This is the full day's result relative to the previous day's close. Pradeep's TC2000 formula `C/C1` means Close / Close[1].

**NOT** intraday (open-to-close). **NOT** high-to-low. It is close-to-close.

### 4% Breakout

```
close >= prev_close × 1.04
AND volume > prev_volume          # volume expansion (V > V1)
AND volume >= 100,000             # minimum liquidity
```

This is the "atom" of the StockBee system — the universal trigger for explosive moves.

### Dollar Breakout (for high-priced stocks ≥ $60)

```
(close - open) >= $0.90
AND volume >= 100,000
```

High-priced stocks ($60+) often don't achieve 4% on breakout day, but a $0.90+ move from open can start a 6-12 day swing. Stops are dramatically tighter (1-2.5% vs 5-10%).

### 9M Volume (EP specific)

```
volume >= 9,000,000    # absolute, for EP 9M scan
```

### Volume Expansion

```
volume_today > volume_yesterday    # V > V1
```

Required for 4% breakout confirmation. Without volume expansion, the breakout lacks conviction.

## 2. Tight Day

A "tight day" is a day where the close-to-close change is within a threshold.

### Thresholds (Configurable)

| Level | Threshold | Use Case | Source |
|-------|-----------|----------|--------|
| Beginner scan | ±1.0% | ANTS scan for new traders | ANTS Guide Part 8 |
| Intermediate scan | ±0.5% | Tighter ANTS scan | ANTS Guide Part 8 |
| Pradeep's personal | ±0.4% | Pradeep's own setting | ANTS Guide Part 10 |
| Actual selection | 0.05%–0.20% | Final manual selection from scan | ANTS Guide Part 11 |
| Low-price stocks (<$10) | ±1.0%–1.5% | Wider (0.4% on $8 = pennies) | ANTS Guide Part 11 |

### Definition

```
is_tight_day(change_pct, threshold=1.0):
    return abs(change_pct) < threshold
```

### 3T (Three Tight Days)

3 consecutive trading days where each day meets the tight day threshold.

### 2T (Two Tight Days)

2 consecutive trading days where each day meets the tight day threshold.

### Where Tight Day Is Used

Tight day is a **common function** used by:
- **ANTS** — scan filter (±0.4% to ±1% for 2-3 consecutive days)
- **SOS (Two Lynch "N")** — day before breakout should be narrow/negative
- **SOS (Two Lynch "C")** — consolidation quality (compact, low-volatility pause)
- **DEP** — "3 tight days, 2 tight days, or orderly pullback = ideal setup pattern"

## 3. Consolidation / Pullback

Consolidation is **multi-dimensional** — not a single threshold.

### Valid Consolidation Requires ALL of:

| Dimension | Criterion | Source |
|-----------|-----------|--------|
| **Body size** | Candle bodies smaller than first-leg bodies | ANTS Guide Part 11 |
| **Daily range** | Each day's range (high-low) smaller than breakout day's range | MB Guide Section 2 |
| **No distribution** | No 4%+ breakdown (close ≤ prev_close × 0.96) during consolidation | MB Guide Section 2, Two Lynch "C" |
| **Volume** | Volume lower than first-leg volume (sellers absent) | ANTS Guide Part 11, MB Guide Section 2 |
| **Direction** | Flat or slightly down (rising wedge = avoid) | ANTS Guide Part 11 |
| **Duration** | 3-7 days ideal; >12 days = stalemate, not momentum pause | ANTS Guide Part 11 |
| **Holds the gain** | Close stays ≥85% of breakout close (for DEP) | Our existing implementation |

### What is NOT a Consolidation

- A single day with 8%+ drop = **breakdown**, not consolidation
- A rising pattern where each day closes higher = **rising wedge**, avoid
- >12 days sideways = **stalemate**, not momentum pause
- High-volume selling during consolidation = distribution, avoid

### Common Function

```python
detect_consolidation(bars, breakout_bar, max_days=10, min_days=2,
                     tight_threshold=1.5, no_breakdown_pct=4.0):
    # Check: duration, no breakdowns, volume declining, body smaller,
    # direction flat/down, holds 85% of breakout close
```

Used by: ANTS, DEP, SOS (Two Lynch C).

## 4. Leg Counting

A **leg** is a complete swing cycle: breakout → consolidation/pullback → resumption (or failure).

### Key Distinction

| What | Definition |
|------|-----------|
| **4% breakout day** | A single day where close >= prev_close × 1.04 |
| **Leg** | A complete move: one breakout + subsequent consolidation (3-10 days) + resumption/failure |

**Consecutive 4%+ days = ONE leg** (same momentum burst, no consolidation between them).

For a stock up 4%, 5%, 6%, 4%, 3% over 5 consecutive days = **1 leg** (continuous burst).

For a stock that went: 4% breakout → 3 tight days → 4% breakout → 3 tight days → 4% breakout = **3 legs**.

### Counting Algorithm

1. Find all 4%+ breakout days in lookback period (25 trading days)
2. Group consecutive breakouts (within 2 days of each other) as the **same leg**
3. A **new leg** starts only after a consolidation/pullback of ≥3 tight days
4. Count distinct legs

### Tradability

| Leg | Probability | Action |
|-----|------------|--------|
| First leg | Highest | ✅ Trade (fresh momentum) |
| Second leg | Good | ✅ Trade (momentum confirmed) |
| Third+ leg | Declining | ❌ Avoid ("who is left to buy?") |

## 5. Momentum Burst

### Definition

```
today's percentage move > last 2-5 days' percentage moves
```

A stock that was barely moving (small candles) suddenly has a large range-expansion candle. That's the burst starting.

### Duration by Price Level

| Price Level | Typical Hold | Expected Move |
|------------|-------------|---------------|
| Below $40 | 3-5 days | 8-40% |
| $40-$100 | 5-7 days | 5-15% |
| Above $100 | 6-10+ days | $10-$300 per share |

## 6. Two Lynch Framework (SOS Quality Filter)

Eliminates 80-90% of 4% breakout scan results.

| Letter | Criterion | Technical Check |
|--------|-----------|----------------|
| **T** (Two) | Stock NOT up two days in a row before breakout | `abs(change_pct[-2]) < 0.5 AND abs(change_pct[-1]) < 0.5` (minor uptick ≤0.5% tolerated) |
| **L** (Linearity) | Clean first leg, no choppy candles | `max_daily_range / min_daily_range < 2.5` over 5 days (heuristic) |
| **Y** (Young) | First or second leg only | `leg_count <= 2` |
| **N** (Narrow/negative) | Day before breakout = small-range or down day | `abs(change_pct[-1]) < 1.0 OR change_pct[-1] < 0` |
| **C** (Consolidation quality) | Orderly, low-volume pause; no 4% breakdowns | `detect_consolidation() returns valid` |
| **H** (High close) | Close near intraday high (≥70% of range) | `close >= low + 0.7 × (high - low)` (intraday 5-min data) |

## 7. Stops — Percentage-Based

### DEP Stop

```
stop = consolidation_low × (1 - buffer_pct)
where buffer_pct ensures total stop width = 0.5% to 2.5%
```

**NOT fixed $0.40.** The $0.40 is an example for low-priced stocks. For a $300 stock, the buffer is $1.50-$7.50 (0.5%-2.5% of price).

### EP 9M Stop

```
stop = low_of_day    # from 5-min intraday bars (9:30 AM - 4:00 PM ET)
width = 8% to 20%
```

### SOS Stop

```
# High-priced stocks (≥ $100):
stop = low_of_day

# Cheaper stocks (< $100):
stop = (open + low_of_day) / 2    # "half of day"

width = 2% to 5%
```

### ANTS Stop

```
stop = tight_consolidation_low
width < 1%
```

### Reversal Stop

```
stop = below open or prior close
width = 0.5% to 2.5%
```

## 8. Low of Day / Half of Day (Intraday)

### Low of Day

```
low_of_day = min(low) from 5-min bars
where time >= 09:30 ET AND time <= 16:00 ET
```

### Half of Day

```
half_of_day = (open + low_of_day) / 2
```

Pradeep's preferred stop for SOS — "if it gives back half of Day 1's gain, the burst thesis is invalidated."

## 9. VWAP — NOT Used

Pradeep explicitly does NOT use VWAP:
> *"I don't pay attention to ADR, VWAP, all these things."*
> *"If you don't have clarity, then you are putting in VWAP."*

**Implementation:** VWAP removed as gating filter. Kept as optional informational field in deep_dive notes only.

The real entry filters are:
1. 4%+ breakout (or dollar breakout for >$60)
2. Volume expansion (V > V1)
3. Two Lynch qualification (T, L, Y, N, C, H)
4. Market Monitor bullish
5. Not third+ leg
6. Catalyst identifiable
7. Sugar Baby = higher priority

## 10. Magna 53 + Cap 10×10

### Magna 53 (6 Criteria)

| Letter | Stands For | Technical Check | Essential? |
|--------|-----------|-----------------|-----------|
| **M** | Massive | `eps_growth_yoy >= 100 OR sales_growth_qoq >= 100` | ✅ Yes |
| **A** | Acceleration of sales | `sales_growth[-1] >= 39 AND sales_growth[-2] >= 39` (back-to-back 2 quarters) | ✅ Yes |
| **G** | Gap up | `open >= prev_close × 1.04 AND volume >= 100,000` | ✅ Yes |
| **N** | Neglect | No rally into earnings (`price_change_3m_pre < 10%`), low volume, low coverage | ✅ Yes |
| **5** | 5-day short interest | `short_interest_ratio >= 5` (from FMP if available) | Optional |
| **3** | 3+ analysts raise target | `count(analyst_target_raise after earnings) >= 3` | Optional |

### Cap 10×10

| Criterion | Technical Check |
|-----------|----------------|
| **Cap** | `market_cap < 10,000,000,000` (< $10B) |
| **10** | `(today - ipo_date).days / 365 < 10` (IPO < 10 years) |

### Expected Move

| Magna 53 | Cap 10×10 | Expected Move |
|----------|-----------|---------------|
| ✓ | ✗ | 50-100% move possible |
| ✓ | ✓ | 300-800%+ move likely |

## 11. Sugar Baby (Stock Selection)

### Definition

Sugar Babies = stocks that repeatedly produce 4%+ breakouts with 9M+ volume.

### Computation

```
count = number of days where:
    close >= prev_close × 1.04
    AND volume >= 9,000,000
    AND volume > prev_volume
over the lookback period (up to 1,450 trading days)
```

### Multi-Timeframe

| Timeframe | Trading Days | Purpose |
|-----------|-------------|---------|
| 504d | ~2 years | Long-term momentum frequency |
| 252d | ~1 year | Annual momentum |
| 126d | ~6 months | Half-year momentum |
| 63d | ~3 months | Quarter momentum |
| 21d | ~1 month | Recent momentum |
| 10d | ~2 weeks | Short-term |
| 5d | ~1 week | Immediate momentum |

### Ranking

- Top 20-30 by count (per timeframe) = core list
- Up to 150 = expanded list
- `sb_master_flag = True` if ticker in top-30 of ANY timeframe

### Sugar Baby is NOT a Setup

Sugar Babies identifies WHICH stocks to trade. You still use SOS/DEP/ANTS/EP for entries. SB candidates get confluence priority in cross-reference.

## 12. Market Monitor (Traffic Light)

### Primary Indicator

```
MM = (stocks up 25%+ in 65 days) - (stocks down 25%+ in 65 days)
```

### Regime

| MM Value | Regime | Action |
|---------|--------|--------|
| > 400 | Strong bull | Full size longs |
| 200-400 | Normal bull | Standard longs |
| 0-200 | Weak bull | ANTS only (confirmed bullish) |
| < 0 | Bear | Shorts only |
| < -200 | Capitulation | Generational buy (longs) |

### T2108 (Secondary)

```
T2108 = % of stocks above 40-day MA
```

| T2108 | Signal |
|-------|--------|
| > 90% | New bull started (NOT a top) |
| < 10% | Capitulation bottom |

### Critical Asymmetry

Breadth finds BOTTOMS, NOT tops. Excessive bullishness is NOT bearish.

## 13. Entry/Stop Calculation Timing

| Setup | Calculate Before Open? | Entry Source | Stop Source |
|-------|------------------------|-------------|------------|
| **DEP** | ✅ Yes (fully pre-market) | consolidation_high + buffer | consolidation_low - buffer |
| **ANTS** | ✅ Yes (placed day before) | close + 1% (BSLO trigger) | tight consolidation low |
| **SOS** | ⚠️ Stop = prior_low (preliminary); updated intraday | When 4% triggers (intraday) | Low of day (5-min bars) |
| **EP 9M** | ⚠️ Stop = prior_low (preliminary); updated intraday | OPG (market open price) | Low of day (5-min bars) |
| **Reversal** | ❌ No (fully intraday) | 3:58 PM price | Below open/prior close |

**Pre-market order sheet:** DEP + ANTS candidates with exact limit/stop orders to place before 9:30 AM.

## See Also

- [[Pradeep Ultratrader — Design]] — overall architecture
- [[Pradeep Ultratrader — Implementation Plan]] — step-by-step implementation plan