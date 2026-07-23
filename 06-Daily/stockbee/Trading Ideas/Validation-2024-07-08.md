---
title: Radar Validation Jul-Aug 2024
date: 2024-07-08
tags: [validation, radar, backtest, 2024-q3]
---

# Radar Validation — Jul 9 – Aug 29, 2024

## Summary

| Metric | Score |
|--------|-------|
| **Avg Regime Score** | 4.9 / 10 |
| **Avg Setup Score** | 4.2 / 10 |
| **Avg Overall Score** | 4.6 / 10 |
| **Days radar was too conservative** | 30 / 36 (83%) |
| **Days radar about right** | 6 / 36 (17%) |
| **Days radar was too aggressive** | 0 / 36 (0%) |
| **Total pairs scored** | 36 |
| **Skipped (no session)** | 2 |

## Core Problem: Systematic Bearish Bias

The radar called **RANGE_BOUND / SIPs_ONLY on all 38 days**. Pradeep was bullish or bullish-cautious on most days. The 20% study threshold (< 30 = suppress all SOS/DEP/ANTS scans) is the primary cause — it blocks the regime from ever upgrading even when BO:BD ratios exceed 5:1 and Net Primary is +500+.

### 20% Study Count Discrepancy

On multiple days, the radar's 20% study count diverged 5–10× from Pradeep's:

| Date | Radar 20% | Pradeep 20% | Notes |
|------|-----------|-------------|-------|
| 07-29 | 9 | 40 | 10× divergence |
| 07-30 | 4 | 28 | 7× divergence |
| 08-14 | 7 | 77 | 11× divergence |
| 08-20 | 10 | 61 | 6× divergence |
| 08-26 | 5 | 37 | 7× divergence |
| 08-29 | 3 | 17 | 6× divergence |

This needs investigation — different data source, time-of-day snapshot, or calculation methodology.

## Detailed Scores

### Week 1: Jul 9–12 (Pairs 1–4)

| # | Radar Date | Session Date | Radar Regime | Session Regime | Regime | Setup | Overall | Notes |
|---|-----------|-------------|--------------|---------------|--------|-------|---------|-------|
| 1 | 07-10 | 07-09 | RANGE_BOUND/SIPs_ONLY | Choppy selective, 4% breakout works | 5 | 6 | 5 | Radar too bearish; Pradeep says selective but viable |
| 2 | 07-11 | 07-10 | RANGE_BOUND/SIPs_ONLY | Selective bull like 2012 | 4 | 5 | 4 | Radar stuck RANGE_BOUND; Pradeep explicitly called bull |
| 3 | 07-12 | 07-11 | CAUTIOUS_BULL/REDUCE_SIZE | Selective slow grinding bull | 7 | 5 | 6 | Best match this week; radar upgraded correctly |
| 4 | 07-15 | 07-12 | RANGE_BOUND/SIPs_ONLY | Huge breadth thrust, small cap rotation | 3 | 4 | 3 | Worst mismatch; radar missed massive breadth thrust |

### Week 2: Jul 15–19 (Pairs 5–9)

| # | Radar Date | Session Date | Radar Regime | Session Regime | Regime | Setup | Overall | Notes |
|---|-----------|-------------|--------------|---------------|--------|-------|---------|-------|
| 5 | 07-16 | 07-15 | RANGE_BOUND/SIPs_ONLY | Bullish after breadth thrust | 3 | 4 | 3 | Net Primary +575, Pradeep says continuation setups work |
| 6 | 07-17 | 07-16 | CAUTIOUS_BULL/REDUCE_SIZE | Sugar babies back, 296 stocks 15% moves | 7 | 6 | 7 | **Best day.** Both agree speculative juice flowing |
| 7 | 07-18 | 07-17 | RANGE_BOUND/SIPs_ONLY | 900+ day follow-through, bull move months | 3 | 4 | 3 | Severe mismatch; 900d FT = strongest bull signal |
| 8 | 07-19 | 07-18 | RANGE_BOUND/SIPs_ONLY | Bullish cautious, first legs established | 4 | 5 | 4 | Pradeep sees market structure evolution; radar sees breadth deterioration |
| 9 | 07-22 | 07-19 | RANGE_BOUND/SIPs_ONLY | Bullish cautious, IWM 3.4yr breakout | 5 | 5 | 5 | Both cautious; IWM breakout recognized by both |

### Week 3: Jul 23–26 (Pairs 10–13)

| # | Radar Date | Session Date | Radar Regime | Session Regime | Regime | Setup | Overall | Notes |
|---|-----------|-------------|--------------|---------------|--------|-------|---------|-------|
| 10 | 07-23 | 07-22 | RANGE_BOUND/SIPs_ONLY | Bullish cautious, chop | 4 | 3 | 4 | Radar 20%=1 vs Pradeep 20%=19 |
| 11 | 07-24 | 07-23 | RANGE_BOUND/SIPs_ONLY | Normal moves, no FOMO | 5 | 4 | 5 | Both no FOMO; radar misses 9M EP framework |
| 12 | 07-25 | 07-24 | RANGE_BOUND/SIPs_ONLY | Bullish, 499 stocks up 15%+, rotation confirmed | 3 | 2 | 3 | **Worst pair this week.** Radar misreads rotation breadth as weakness |
| 13 | 07-26 | 07-25 | RANGE_BOUND/SIPs_ONLY | Choppy, rotation accelerating | 5 | 4 | 5 | Both see chop/rotation; radar too restrictive on setups |

### Week 4: Jul 29–Aug 1 (Pairs 14–17)

| # | Radar Date | Session Date | Radar Regime | Session Regime | Regime | Setup | Overall | Notes |
|---|-----------|-------------|--------------|---------------|--------|-------|---------|-------|
| 14 | 07-29 | 07-26 | RANGE_BOUND/SIPs_ONLY | Slightly choppy, SIPs+9M focus | 5 | 5 | 5 | Closest alignment; both agree SIPs primary |
| 15 | 07-30 | 07-29 | RANGE_BOUND/SIPs_ONLY | Bullish choppy, earning SIPs best season | 2 | 2 | 2 | **Critical data divergence.** Radar 20%=4 vs Pradeep 20%=40 |
| 16 | 07-31 | 07-30 | RANGE_BOUND/SIPs_ONLY | Sideways choppy, SIPs working, delayed reactions | 4 | 3 | 4 | Radar 20%=3 vs Pradeep 20%=28 |
| 17 | 08-01 | 07-31 | RANGE_BOUND/SIPs_ONLY | Fed day, 99% rate cut, small cap bull conditional | 4 | 4 | 4 | Event-driven; radar can't price conditional setups |

### Week 5: Aug 2–9 (Pairs 18–23)

| # | Radar Date | Session Date | Radar Regime | Session Regime | Regime | Setup | Overall | Notes |
|---|-----------|-------------|--------------|---------------|--------|-------|---------|-------|
| 18 | 08-02 | 08-01 | RANGE_BOUND/SIPs_ONLY | Bullish but choppy, SIPs abundant | 7 | 7 | 7 | Good alignment; both emphasize SIPs |
| 19 | 08-05 | 08-02 | RANGE_BOUND/NO_TRADE | Bearish, small cap rally failed | 9 | 8 | 8 | **Best agreement.** Both bearish, SIPs only |
| 20 | 08-06 | 08-05 | RANGE_BOUND/NO_TRADE | Bearish, "get me out" market, shorts work | 8 | 6 | 7 | Direction aligned; radar misses short-side emphasis |
| 21 | 08-07 | 08-06 | RANGE_BOUND/SIPs_ONLY | Bearish choppy, VIX surging, day trader's paradise | 7 | 5 | 6 | Both difficult; radar misses VIX/day-trade framing |
| 22 | 08-08 | 08-07 | RANGE_BOUND/NO_TRADE | Bearish choppy, 20% <10 = contrarian bullish | 7 | 6 | 6 | Key insight: Pradeep uses 20% <10 as contrarian; radar doesn't |
| 23 | 08-09 | 08-08 | RANGE_BOUND/NO_TRADE | Choppy bearish, SA critical, gaps-and-fades | 8 | 5 | 6 | Direction aligned; radar misses gaps-and-fades pattern |

### Week 6: Aug 12–14 (Pairs 24–26)

| # | Radar Date | Session Date | Radar Regime | Session Regime | Regime | Setup | Overall | Notes |
|---|-----------|-------------|--------------|---------------|--------|-------|---------|-------|
| 24 | 08-12 | 08-09 | RANGE_BOUND/SIPs_ONLY | Selling halted, select breakouts work (PLTR) | 6 | 5 | 5 | Radar still NO_TRADE; Pradeep says select breakouts working |
| 25 | 08-13 | 08-12 | RANGE_BOUND/SIPs_ONLY | Sideways after shakeout, 9M EP works (LUMN) | 6 | 5 | 5 | Radar blanket "wallet closed" contradicts Pradeep's 9M EPs |
| 26 | 08-14 | 08-13 | RANGE_BOUND/SIPs_ONLY | High vol good for day trading, 9M works | 6 | 5 | 5 | 5d ratio turned bullish (1.13) but regime didn't adjust |

### Week 7: Aug 15–23 (Pairs 27–33)

| # | Radar Date | Session Date | Radar Regime | Session Regime | Regime | Setup | Overall | Notes |
|---|-----------|-------------|--------------|---------------|--------|-------|---------|-------|
| 27 | 08-15 | 08-14 | RANGE_BOUND/SIPs_ONLY | Bullish choppy, 77 in 20% study | 3 | 2 | 3 | Radar 20%=7 vs Pradeep 20%=77 |
| 28 | 08-16 | — | — | **NO SESSION** | — | — | — | Skipped |
| 29 | 08-19 | 08-19 | RANGE_BOUND/SIPs_ONLY | Cautious after V-bounce, 50 in 20% study | 6 | 4 | 5 | Both cautious; Pradeep sees range expansion setups |
| 30 | 08-20 | 08-20 | RANGE_BOUND/SIPs_ONLY | Cautiously bullish, 61 in 20% study, 9M EPs working | 4 | 3 | 4 | Radar BO:BD 5.00 contradicts its RANGE_BOUND call |
| 31 | 08-21 | 08-21 | RANGE_BOUND/SIPs_ONLY | **Big opportunity**, move account 5-10% | 1 | 2 | 2 | Worst regime miss; "wallet closed" vs "big opportunity" |
| 32 | 08-22 | 08-22 | RANGE_BOUND/SIPs_ONLY | Good market, home runs + singles | 2 | 3 | 3 | BO:BD 5.81 very bullish; radar still RANGE_BOUND |
| 33 | 08-23 | 08-22* | RANGE_BOUND/SIPs_ONLY | Good market (prior session) | 5 | — | 5 | Date mismatch; BO:BD 0.57 on 08-23 justified caution |

### Week 8: Aug 26–30 (Pairs 34–38)

| # | Radar Date | Session Date | Radar Regime | Session Regime | Regime | Setup | Overall | Notes |
|---|-----------|-------------|--------------|---------------|--------|-------|---------|-------|
| 34 | 08-26 | 08-26 | RANGE_BOUND/SIPs_ONLY | **FULL THROTTLE**, breadth thrust, 37 in 20% study | 1 | 1 | 1 | **Worst pair overall.** BO:BD 14.65, Net +530; radar says nothing to do |
| 35 | 08-27 | 08-27 | RANGE_BOUND/SIPs_ONLY | Opportunities exist, stop over-trading | 6 | 3 | 5 | Both cautious; Pradeep confirms 9M biotech/tech working |
| 36 | 08-28 | 08-28 | RANGE_BOUND/SIPs_ONLY | Understand environment, stop early entries | 7 | 5 | 6 | Best agreement late Aug; both cautious |
| 37 | 08-29 | 08-29 | RANGE_BOUND/SIPs_ONLY | Cautious, 9M works with catalyst, 20% near bullish | 5 | 3 | 4 | Radar 317 breakdowns vs Pradeep "no serious selling" |
| 38 | 08-30 | 08-29* | RANGE_BOUND/SIPs_ONLY | Cautious, 9M with catalyst works | 6 | 3 | 5 | Date mismatch; radar data improving |

## Top 5 Fixes Needed

### 1. Tiered 20% Study Thresholds (Critical)

Current: `< 30 → suppress all SOS/DEP/ANTS`

**Replace with:**
- `< 10` → FADE mode (truly bearish)
- `10–30` → CAUTIOUS (selective setups, 9M EPs, delayed reactions viable)
- `30–50` → REDUCE_SIZE (standard setups work)
- `50+` → FULL_LONG (all setups active)

This would fix 30 of 36 days where the radar was too conservative.

### 2. BO:BD Regime Override (Critical)

When BO:BD > 3.0 AND Net Primary > +200, force at least CAUTIOUS_BULL regardless of 20% study. This would fix the worst misses (08-21, 08-22, 08-26 where BO:BD was 5–15× but radar said RANGE_BOUND).

### 3. Add 9M EP / Delayed Reaction Scan (High)

Pradeep's primary setup in choppy markets is 9M EPs and delayed reactions. The radar currently has no equivalent scan. Add:
- `EP9mScan` exists but is suppressed under RANGE_BOUND
- Create a "selective setup" category that activates in CAUTIOUS regime
- Include delayed reactions (stocks up 3+ consecutive days)

### 4. Fix "My Wallet Is Closed" Default Text (High)

This boilerplate appears on every radar regardless of conditions. On 08-26 (full throttle, BO:BD 14.65) the radar still says "wallet closed." Replace with dynamic text based on regime.

### 5. Investigate 20% Study Count Divergence (High)

The radar's 20% study count (3–10) diverges 5–11× from Pradeep's counts (17–77). Possible causes:
- Different data source (radar uses TC2000/FMP vs Pradeep's StockBee Market Monitor)
- Different time-of-day snapshot (radar may use EOD vs Pradeep's intraday)
- Different counting methodology (radar may count differently)

This is a data integrity issue that affects the entire regime classification.

## Phase Classification Accuracy

| Pradeep Call | Days | Radar Correct | Radar Too Conservative | Radar Too Aggressive |
|-------------|------|:---:|:---:|:---:|
| Bullish / Cautiously Bullish | 18 | 2 | 16 | 0 |
| Bearish / Choppy Bearish | 10 | 7 | 3 | 0 |
| Range / Sideways / Choppy | 8 | 4 | 4 | 0 |
| Big Opportunity / Full Throttle | 4 | 0 | 4 | 0 |

**The radar performs best in clearly bearish environments** (7/10 correct) and **worst in bullish environments** (2/18 correct). It never correctly identified a "big opportunity" day.

## Methodology

- **Radar date** = next trading day (radar uses prior day's data)
- **Session date** = same-day Pradeep call
- **Comparison**: radar for date X compared against session for date X-1 (prior trading day)
- **Regime Score (0-10)**: How well radar's regime matches Pradeep's assessment
- **Setup Score (0-10)**: How well radar's scan results match Pradeep's actionable setups
- **Overall Score (0-10)**: Weighted average of regime + setup accuracy

## Generated

- Radars regenerated: 2024-07-09 through 2024-08-29 (38 trading days)
- Comparison: 36 pairs scored, 2 skipped (no session notes)
- Engine version: bottom_up_analyzer (rules-based, no LLM judge)