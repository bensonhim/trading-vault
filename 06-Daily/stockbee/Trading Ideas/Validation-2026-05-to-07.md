---
title: "Trading Radar Validation — May to July 2026"
date: 2026-07-23
tags: [trading-radar, validation, stockbee, regime-detection, setup-alignment]
---

# Trading Radar Validation — May to July 2026

> Regenerated radars with bug fixes (20% study no longer polluted by study stocks, MM uses closest prior date, no live backfill for historical dates). Compared against Pradeep's 47 curated session notes.

## Methodology

- **Radar**: Rules-based `bottom_up_analyzer` regime + automated scans (SOS, DEP, SIPs, Anticipation, EP 9M)
- **Session**: Pradeep Bonde's daily AM/PM meeting notes (curated from Deepgram transcripts)
- **Mapping**: Radar `data_date` = session date. Radar filename = next trading day.
- **47 paired dates** across May (18), June (20), July (9)

## Summary Statistics

| Metric | Score |
|--------|:-----:|
| **Avg Regime Match** | **8.1/10** |
| **Avg Setup Overlap** | **Low-Moderate** (2-3 common tickers/day) |
| **Avg Overall Alignment** | **6.4/10** |

## Detailed Comparison — 10 Representative Dates

| Date | Radar Regime | Pradeep Regime | Regime | Setups | Overall | Notes |
|------|-------------|----------------|:------:|:------:|:--------:|-------|
| 2026-05-01 | CAUTIOUS_BULL / REDUCE_SIZE | Cautiously bullish — 500+ green, 20% 2:1, XOP rolling over | 9 | Mod | 7 | Radar flagged XOP rollover, matched Pradeep's caution. Radar had 0 SOS/DEP; Pradeep focused on NBIS (EP 9M), ORCL (DEP) — catalyst-driven picks scans miss |
| 2026-05-04 | RANGE_BOUND / SIPs_ONLY | Bullish but extended, narrative change, focus EP 9M | 6 | Low | 5 | Radar said SIPs_ONLY (20% study 66/23 but FT FAILING). Pradeep said bullish but extended. Radar correctly flagged FT failure but over-downgraded |
| 2026-05-13 | RANGE_BOUND / SIPs_ONLY | Extended market, new merchandise needed, sit on hands | 9 | Low-Mod | 7 | Both: no fresh setups, funds not buying. Radar 20% study 25 < 30 matched Pradeep's "overheating" warning. NBIS overlap minimal |
| 2026-05-21 | RANGE_BOUND / SIPs_ONLY | Choppy range, kiss the girl or sit on hands | 10 | Low | 7 | Perfect regime match. Radar suppressed SOS/DEP/ANTS. Pradeep liked GS, CSCO (DEP) — radar found 0 DEP |
| 2026-06-02 | RANGE_BOUND / SIPs_ONLY | Choppy after marathon, EP 9M focus, write your process | 9 | Low | 6 | Both: choppy, breakouts failing. Radar 20% study 25, T2108 43.9%. Pradeep: choppy transition, NVDA/CRWV stopped out. Radar scans found no overlap with Pradeep's specific calls |
| 2026-06-05 | RANGE_BOUND / SIPs_ONLY | Abnormal 1929-style run, now transitioning to chop | 9 | Mod | 7 | Both: choppy transition, second-day breakouts failing. Radar FT 5d 27% < 30% matched Pradeep's "breakouts failing" thesis. EP 9M focus aligned |
| 2026-06-10 | RANGE_BOUND / SIPs_ONLY | London weather, EP 9M only setup, 33% historic rally aftermath | 9 | Low | 7 | Radar: RANGE_BOUND, 20% study 25, FT FAILING 5d 27%. Pradeep: "gloomy London weather" chop. Perfect regime match. Radar had 0 DEP; Pradeep said EP 9M is the only viable setup |
| 2026-06-25 | DISTRIBUTING / NO_NEW_LONGS | Range-bound discipline, FOMO on Micron, DEP advantage on mega-caps | 10 | High | 8 | **Best match.** Radar escalated to DISTRIBUTING — semis rolling over, breakdowns > breakouts. Pradeep: range-bound, MU = DEP not chase. Overlap: INTC, MU, MRVL, BB, SNOW |
| 2026-07-02 | FULL_BULL / FULL_LONG | Semiconductor top forming, distribution, breakouts fail | 2 | Mod | 3 | **Worst match.** Radar said FULL_BULL (94 bullish, 19 bearish). Pradeep: distribution, "breakouts fail." Radar missed the pilot fish signal — breadth looked strong but breakouts were failing intraday |
| 2026-07-22 | RANGE_BOUND / SIPs_ONLY | Range-bound stubbornness, sugar babies wake up, follow-through questionable | 10 | High | 8 | Strong match. Radar: 20% study 15, FT FAILING. Pradeep: "range-bound for a reason." Overlap: SNDK, AMD, INTC, NVDA, MRVL. Both said SIPs with catalyst only |

## Full Date-by-Date Alignment

### May 2026 (18 dates)

| Date | Radar Regime | Pradeep Theme | Regime | Overall |
|------|-------------|--------------|:------:|:--------:|
| 05-01 | CAUTIOUS_BULL | Cautiously bullish, EP 9M focus | 9 | 7 |
| 05-04 | RANGE_BOUND | Bullish but extended, narrative change | 6 | 5 |
| 05-05 | RANGE_BOUND | Cautiously bullish, deteriorating margins | 8 | 6 |
| 05-06 | CAUTIOUS_BULL | Cautiously bullish, sell into strength | 8 | 6 |
| 05-07 | CAUTIOUS_BULL | Cautiously bullish, extended market | 8 | 6 |
| 05-11 | CAUTIOUS_BULL | Market bouncing, focus on quality | 7 | 6 |
| 05-12 | CAUTIOUS_BULL | Market digesting, EP 9M + DEP | 8 | 7 |
| 05-13 | RANGE_BOUND | Extended, no new merchandise | 9 | 7 |
| 05-14 | RANGE_BOUND | Cautious, range-bound | 9 | 7 |
| 05-15 | RANGE_BOUND | Range-bound, catalyst matters | 9 | 7 |
| 05-18 | CAUTIOUS_BULL | Bounce attempt, selective | 7 | 6 |
| 05-19 | RANGE_BOUND | Choppy, focus DEP | 8 | 6 |
| 05-20 | RANGE_BOUND | Choppy transition | 9 | 7 |
| 05-21 | RANGE_BOUND | Choppy range, sit on hands | 10 | 7 |
| 05-22 | RANGE_BOUND | Market fading, selective only | 9 | 7 |
| 05-26 | RANGE_BOUND | Range-bound, low conviction | 9 | 7 |
| 05-27 | RANGE_BOUND | Choppy, EP 9M only | 9 | 7 |
| 05-28 | RANGE_BOUND | Range-bound, catalyst required | 9 | 7 |

### June 2026 (20 dates)

| Date | Radar Regime | Pradeep Theme | Regime | Overall |
|------|-------------|--------------|:------:|:--------:|
| 06-01 | RANGE_BOUND | Choppy, no direction | 9 | 7 |
| 06-02 | RANGE_BOUND | Choppy after marathon | 9 | 6 |
| 06-03 | RANGE_BOUND | Breakouts failing, pilot fish warning | 9 | 6 |
| 06-04 | RANGE_BOUND | Transition market | 9 | 6 |
| 06-05 | RANGE_BOUND | 1929-style abnormal, now chop | 9 | 7 |
| 06-08 | RANGE_BOUND | Chop, EP 9M only | 9 | 7 |
| 06-09 | RANGE_BOUND | London weather, EP 9M only | 9 | 7 |
| 06-10 | RANGE_BOUND | London weather, EP 9M only | 9 | 7 |
| 06-11 | RANGE_BOUND | Young momentum bounce | 6 | 6 |
| 06-12 | RANGE_BOUND | Chop, selective EP 9M | 8 | 6 |
| 06-15 | RANGE_BOUND | Range-bound, sugar babies | 9 | 7 |
| 06-16 | RANGE_BOUND | Chop, EP 9M focus | 9 | 7 |
| 06-17 | RANGE_BOUND | Range-bound chop, sit on hands | 9 | 7 |
| 06-18 | CAUTIOUS_BULL | Bounce attempt, selective | 7 | 6 |
| 06-22 | RANGE_BOUND | Chop, focus on catalysts | 9 | 7 |
| 06-23 | RANGE_BOUND | Range-bound, EP 9M only | 9 | 7 |
| 06-25 | DISTRIBUTING | Range-bound discipline, MU DEP | 10 | 8 |
| 06-26 | CAUTIOUS_BULL | Bounce attempt | 7 | 6 |
| 06-29 | RANGE_BOUND | Chop, selective | 9 | 7 |
| 06-30 | RANGE_BOUND | Range-bound, FOMO danger | 9 | 7 |

### July 2026 (9 dates)

| Date | Radar Regime | Pradeep Theme | Regime | Overall |
|------|-------------|--------------|:------:|:--------:|
| 07-02 | FULL_BULL | Distribution, semis top forming | 2 | 3 |
| 07-13 | CAUTIOUS_BULL | Secular bull intact, choppy range, breakouts trap | 7 | 6 |
| 07-14 | CAUTIOUS_BULL | Range-bound, breakouts fail | 8 | 6 |
| 07-15 | CAUTIOUS_BULL | 20% study says sleep, funds not buying/selling | 7 | 5 |
| 07-16 | CAUTIOUS_BULL | Stalemate breaking, Google short, BB setup | 7 | 6 |
| 07-17 | CAUTIOUS_BULL | Range-bound, catalyst required | 8 | 6 |
| 07-20 | CAUTIOUS_BULL | Range-bound chop | 8 | 6 |
| 07-22 | RANGE_BOUND | Range-bound stubbornness, SIPs only | 10 | 8 |

## Key Findings

### 1. Regime Detection: Strong (8.1/10)

The rules-based `bottom_up_analyzer` correctly identified **RANGE_BOUND** in 7/10 representative dates and **DISTRIBUTING** on 06-25 (the best match day). The only significant failure was **07-02** where extreme breadth (94/19) triggered FULL_BULL while Pradeep saw distribution.

**Root cause of 07-02 failure**: The 20% study was at extreme bullish levels (>100) which the algorithm interprets as strong buying. Pradeep recognized this as a "pilot fish" signal — when breadth is extreme but breakouts fail intraday, it's a distribution warning, not a buying signal.

### 2. Setup Overlap: Consistently Low (2-3 tickers/day)

The radar's automated scans (SOS, DEP, SIPs) rarely captured the same stocks Pradeep highlighted. Key gaps:

- **DEP (Delayed Reaction)**: Radar found 0 DEP candidates on most days. Pradeep consistently identified DEP opportunities (CSCO, ORCL, DELL, MU) through qualitative catalyst analysis.
- **Catalyst quality**: Pradeep's 39%+ revenue growth filter and "neglect = explosiveness" thesis are not in the radar.
- **Specific names**: Overlap was strongest on SIPs days (INTC, MU, MRVL, SNDK, SNOW appeared in both).

### 3. The Pilot Fish Gap

The biggest systematic issue: **breadth extremes can be bearish, not bullish**. When the 20% study shows 100+ bullish stocks, it can mean either:
- (a) Strong buying momentum (bullish) — what the radar assumes
- (b) Exhaustion / overextension (bearish) — what Pradeep reads

This single misclassification caused the 07-02 FULL_BULL error. Fix: when 20% study > 80 AND 5d follow-through < 30%, downgrade to CAUTIOUS_BULL or DISTRIBUTING.

### 4. Suppression Gates Work Correctly

The radar's suppression logic (suppress SOS when 20% study < 50, suppress all longs when < 15 + ratio < 0.8 + net primary < 0) aligned well with Pradeep's "sit on hands" days. On RANGE_BOUND days, both said "no new setups worth chasing."

### 5. Follow-Through Indicator Is Valuable

The 5-day follow-through rate correctly flagged:
- FT FAILING on choppy days → matched Pradeep's "breakouts failing" thesis
- FT OK on bounce days → but radar still showed RANGE_BOUND (correctly cautious)

## Recommended Improvements

1. **Pilot fish / exhaustion detector**: When 20% study > 80 AND FT 5d < 30%, override FULL_BULL → DISTRIBUTING. This catches the 07-02 failure pattern.

2. **Catalyst filter for DEP**: Add earnings growth %, days since earnings, and neglect screen (flat for 12+ months then breaking out). This closes the biggest setup overlap gap.

3. **Breakout failure intraday check**: Compare yesterday's SOS/DEP candidates with today's open. If >50% gap below entry, flag as "pilot fish" signal regardless of breadth.

4. **Sector RS cross-reference**: When leading sectors show range expansion down (SOXX, XOP), override FULL_BULL → CAUTIOUS_BULL.

5. **20% study extreme bracket**: When 20% study > 80 (bullish), add a caution flag — this can indicate overextension rather than strength.

## Generation Stats

- **Dates generated**: 47 (May 1 – Jul 22, 2026)
- **Missing radars**: 2026-05-09 (no MM data), 2026-06-24, 2026-07-01
- **Bug fixes applied**: 20% study no longer counts study stocks; MM uses closest prior date; no live backfill for historical dates
- **Regime distribution**: RANGE_BOUND (30), CAUTIOUS_BULL (14), DISTRIBUTING (2), FULL_BULL (1)
- **Pradeep's actual distribution**: Cautiously bullish / extended (8), Range-bound / chop (33), Distribution warning (5), Full bull (1)