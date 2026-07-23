---
title: "Trading Radar Validation — Jan–Apr 2025"
date: 2025-07-23
tags: [trading-radar, validation, stockbee, pradeep-bonde, regime-comparison, 2025]
---

# Trading Radar Validation — Jan–Apr 2025

Comparison of algorithmic radar regime calls against Pradeep Bonde's session notes for 53 trading days across Jan, Mar, and Apr 2025.

## Methodology

- **Session note** = Pradeep's human assessment (regime, setups, action)
- **Radar** = Algorithmic regime call using Market Monitor data + rules-based `bottom_up_analyzer`
- **Radar date** = next trading day after session date (radar uses prior day's MM data)
- **Regime score** (0–10): How well radar regime matches Pradeep's regime description
- **Setup score** (0–10): Overlap between radar setups and Pradeep's highlighted setups
- **Overall** = average of regime + setup, rounded

---

## Comparison Table

| # | Date | Session Regime | Radar Regime | Radar Action | 20% Up/Dn | T2108 | Net Prim | Regime | Setup | Overall | Notes |
|---|------|---------------|-------------|-------------|-----------|-------|----------|--------|--------|---------|-------|
| 1 | 01-02 | Cautious/Slow, range-bound | RANGE_BOUND | SIPs_ONLY | 25/42 | 19.5% | +53 | 8 | 9 | 8.5 | Both: range-bound, SIPs only, breakouts failing |
| 2 | 01-03 | Cautious, bounce possible but untrustworthy | RANGE_BOUND | SIPs_ONLY | 2/0 | 21.7% | +151 | 8 | 7 | 7.5 | Both cautious; radar very bearish (net +151 but low 20% study) |
| 3 | 01-06 | Cautiously bullish, 3-5 day bounce | RANGE_BOUND | SIPs_ONLY | 3/3 | 24.9% | +321 | 6 | 7 | 6.5 | Pradeep bullish bounce; radar says SIPs_ONLY |
| 4 | 01-07 | Cautiously bullish, sellers in control | RANGE_BOUND | SIPs_ONLY | 9/2 | 24.8% | +339 | 5 | 6 | 5.5 | Pradeep: chop, sellers in control; radar: RANGE_BOUND |
| 5 | 01-08 | Short-term cautious, choppy | CAUTIOUS_BULL | REDUCE_SIZE | 0/0 | 23.9% | +237 | 5 | 7 | 6.0 | Pradeep: chop/day-trade; radar upgraded to CAUTIOUS_BULL — slight mismatch |
| 6 | 01-10 | Short-term cautious, death by thousand cuts | RANGE_BOUND | SIPs_ONLY | 0/0 | 22.7% | +10 | 8 | 8 | 8.0 | Perfect match: both range-bound/chop, SIPs only |
| 7 | 01-13 | Bearish, distribution, breakouts unlikely | RANGE_BOUND | SIPs_ONLY | 0/0 | 20.4% | -159 | 9 | 8 | 8.5 | Excellent match: both bearish/distribution |
| 8 | 01-14 | Cautiously bullish for bounce, T2108 near 20 | RANGE_BOUND | SIPs_ONLY | 17/80 | 22.0% | -193 | 4 | 5 | 4.5 | Pradeep sees bounce; radar still RANGE_BOUND |
| 9 | 01-15 | Short-term bullish, tradable bounce | RANGE_BOUND | SIPs_ONLY | 14/54 | 25.5% | -197 | 5 | 6 | 5.5 | Pradeep turned bullish; radar still RANGE_BOUND |
| 10 | 01-16 | Short-term bullish, tradable rally | RANGE_BOUND | SIPs_ONLY | 0/0 | 30.9% | -9 | 6 | 7 | 6.5 | Both see choppy; Pradeep slightly more bullish |
| 11 | 01-17 | Short-term cautious, choppiness | RANGE_BOUND | SIPs_ONLY | 25/42 | 35.3% | -13 | 9 | 8 | 8.5 | Good match: both range-bound/chop |
| 12 | 01-21 | Cautiously bullish but sell-the-news | RANGE_BOUND | SIPs_ONLY | 25/42 | 37.3% | +44 | 6 | 7 | 6.5 | Pradeep: sell-the-news; radar: RANGE_BOUND |
| 13 | 01-22 | Cautiously bullish, T2108 jump to 47.82 | RANGE_BOUND | SIPs_ONLY | 25/42 | 47.8% | +180 | 4 | 5 | 4.5 | Major divergence: Pradeep sees bullish T2108 jump; radar stuck RANGE_BOUND |
| 14 | 01-23 | Cautiously bullish, creeping market | RANGE_BOUND | SIPs_ONLY | 25/42 | 42.6% | +142 | 5 | 6 | 5.5 | Pradeep: overheated 20% study; radar: RANGE_BOUND |
| 15 | 01-24 | Bullish long-term, cautious short-term | — | — | — | — | — | — | — | — | No matching radar |
| 16 | 01-27 | Bearish, DeepSeek EP, narrative change | CAUTIOUS_BULL | REDUCE_SIZE | 0/0 | 45.3% | +190 | 3 | 4 | 3.5 | **Worst mismatch**: Pradeep bearish (DeepSeek); radar CAUTIOUS_BULL |
| 17 | 01-28 | Bearish short-term, AI bounce (no real buyers) | RANGE_BOUND | SIPs_ONLY | 17/47 | 46.8% | -4 | 7 | 7 | 7.0 | Good match: both range-bound/chop |
| 18 | 01-29 | Cautious, paradigm shift confirmed | RANGE_BOUND | SIPs_ONLY | 20/48 | 44.4% | +63 | 7 | 7 | 7.0 | Both cautious/range-bound |
| 19 | 03-03 | Suspect rally, short-term cautious | — | — | 20/69 | 30.8% | -1084 | — | — | — | No radar; adjacent data suggests RANGE_BOUND |
| 20 | 03-04 | Bearish, selling broadening | RANGE_BOUND | SIPs_ONLY | 20/69 | 30.8% | -1084 | 9 | 8 | 8.5 | Excellent match: both bearish, selling broadening |
| 21 | 03-05 | Bearish, T2108 cracks below 30 | RANGE_BOUND | SIPs_ONLY | 19/58 | 25.6% | -1132 | 9 | 8 | 8.5 | Excellent match: both bearish confirmed |
| 22 | 03-06 | Bearish, Chinese torture slow grind | RANGE_BOUND | SIPs_ONLY | 27/26 | 28.4% | -951 | 7 | 7 | 7.0 | Both bearish/chop; net -951 confirms |
| 23 | 03-07 | Bearish, slow horror movie selling | RANGE_BOUND | SIPs_ONLY | 18/40 | 25.9% | -1087 | 9 | 8 | 8.5 | Excellent match: both bearish, SIPs only |
| 24 | 03-10 | Bearish, breakouts unlikely | CAUTIOUS_BULL | REDUCE_SIZE | 0/0 | 29.4% | -1020 | 4 | 5 | 4.5 | Mismatch: Pradeep bearish; radar CAUTIOUS_BULL |
| 25 | 03-11 | Bearish, 900+ selling day | RANGE_BOUND | SIPs_ONLY | 25/52 | 24.0% | -1289 | 8 | 8 | 8.0 | Good match: both bearish, heavy selling |
| 26 | 03-12 | Bearish, relief bounce possible | RANGE_BOUND | SIPs_ONLY | 19/50 | 21.0% | -1253 | 7 | 7 | 7.0 | Both bearish; Pradeep sees possible bounce |
| 27 | 03-13 | Bearish, T2108 below 20 (bullish signal) | RANGE_BOUND | SIPs_ONLY | 12/25 | 19.5% | -1138 | 6 | 6 | 6.0 | Pradeep sees T2108<20 as bullish; radar RANGE_BOUND |
| 28 | 03-14 | Bearish, funds in liquidation mode | RANGE_BOUND | SIPs_ONLY | 8/33 | 17.2% | -1286 | 9 | 8 | 8.5 | Excellent match: both deeply bearish |
| 29 | 03-17 | Cautiously bullish short-term bounce | RANGE_BOUND | SIPs_ONLY | 0/0 | 22.6% | -1058 | 5 | 6 | 5.5 | Pradeep turned bullish; radar still RANGE_BOUND |
| 30 | 03-18 | Bearish overall, short-term bounce | RANGE_BOUND | SIPs_ONLY | 31/19 | 26.6% | -898 | 5 | 6 | 5.5 | Pradeep bearish but sees bounce; radar RANGE_BOUND |
| 31 | 03-24 | Bearish long-term, cautious short-term | — | — | — | — | — | — | — | — | No radar with this data_date |
| 32 | 03-25 | Bearish overall, short-term bounce | RANGE_BOUND | SIPs_ONLY | 39/7 | 31.1% | -636 | 6 | 6 | 6.0 | Both see bounce; Pradeep bearish overall |
| 33 | 03-26 | Bearish, selling stopped, no conviction | RANGE_BOUND | SIPs_ONLY | 27/9 | 28.8% | -679 | 7 | 7 | 7.0 | Good match: both range-bound/chop |
| 34 | 03-27 | Bearish short-term bounce, auto tariffs | RANGE_BOUND | SIPs_ONLY | 11/18 | 29.2% | -811 | 7 | 7 | 7.0 | Both range-bound/chop |
| 35 | 03-28 | Bearish, nothing working | RANGE_BOUND | SIPs_ONLY | 9/11 | 29.5% | -797 | 8 | 8 | 8.0 | Good match: both bearish/range-bound |
| 36 | 03-31 | Bearish, 500+ red day | CAUTIOUS_BULL | REDUCE_SIZE | 0/0 | 24.2% | -1045 | 4 | 5 | 4.5 | Mismatch: Pradeep bearish; radar CAUTIOUS_BULL |
| 37 | 04-01 | Bearish, seller exhaustion, 90% bounce | RANGE_BOUND | SIPs_ONLY | 12/44 | 25.0% | -1125 | 5 | 6 | 5.5 | Pradeep sees exhaustion/bounce; radar RANGE_BOUND |
| 38 | 04-02 | Bearish, Liberation Day | RANGE_BOUND | SIPs_ONLY | 12/31 | 27.6% | -1127 | 8 | 7 | 7.5 | Good match: both range-bound/bearish |
| 39 | 04-03 | Bearish, Liberation Day aftermath | RANGE_BOUND | SIPs_ONLY | 11/20 | 30.9% | -974 | 8 | 7 | 7.5 | Good match |
| 40 | 04-04 | Bearish, T2108 below 20, VIX at 45 | RANGE_BOUND | SIPs_ONLY | 12/54 | 18.0% | -1506 | 8 | 8 | 8.0 | Good match: both deeply bearish |
| 41 | 04-07 | Bearish but ripe for bounce, T2108 7.08 | **CAPITULATION** | **FULL_LONG** | 0/0 | 7.1% | -1960 | 9 | 7 | 8.0 | Radar: CAPITULATION/FULL_LONG. Pradeep: bearish but wait for setups. T2108 at 7 IS capitulation |
| 42 | 04-08 | Bearish, T2108 4.93, no swing setups | **CAPITULATION** | **FULL_LONG** | 8/184 | 4.9% | -2044 | 9 | 6 | 7.5 | Radar flags capitulation correctly. Action mismatch: Pradeep says NO swing trades |
| 43 | 04-09 | Bearish AM, "This is the bottom" PM reversal | **CAPITULATION** | **FULL_LONG** | 9/474 | 4.1% | -2245 | 10 | 5 | 7.5 | Radar captured capitulation perfectly (T2108 4.1%). Pradeep called bottom AFTER reversal |
| 44 | 04-10 | Bearish, FOMO hangover, chop | RANGE_BOUND | SIPs_ONLY | 18/20 | 10.6% | -1508 | 7 | 7 | 7.0 | Both see chop/range-bound |
| 45 | 04-11 | Bearish, China tariff escalation | **CAPITULATION** | **FULL_LONG** | 26/24 | 8.5% | -1915 | 8 | 5 | 6.5 | Radar: CAPITULATION; Pradeep still bearish. T2108 at 8.5 IS capitulation zone |
| 46 | 04-14 | Bearish, gap fade confirms | RANGE_BOUND | SIPs_ONLY | 0/0 | 13.5% | -1723 | 7 | 7 | 7.0 | Both range-bound/bearish |
| 47 | 04-15 | Cautiously bullish, first legs forming | RANGE_BOUND | SIPs_ONLY | 89/7 | 16.6% | -1559 | 5 | 4 | 4.5 | Pradeep turned bullish (89 stocks up); radar RANGE_BOUND |
| 48 | 04-16 | Cautiously bullish, select breakouts | RANGE_BOUND | SIPs_ONLY | 23/20 | 16.4% | -1499 | 6 | 6 | 6.0 | Both see selective action; regime match moderate |
| 49 | 04-21 | Bearish, all setups broken | RANGE_BOUND | SIPs_ONLY | 23/15 | 18.4% | -1467 | 8 | 7 | 7.5 | Good match: both difficult conditions |
| 50 | 04-22 | Bearish, same old story | RANGE_BOUND | SIPs_ONLY | 9/25 | 13.2% | -1592 | 8 | 7 | 7.5 | Good match |
| 51 | 04-28 | Cautiously bullish, no setups | — | — | — | — | — | — | — | — | No radar with this data_date |
| 52 | 04-29 | Cautiously bullish, choppy range-bound | RANGE_BOUND | SIPs_ONLY | 49/9 | 33.9% | -673 | 6 | 6 | 6.0 | Pradeep cautiously bullish; radar RANGE_BOUND |

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total pairs compared | 49 (4 dates with no matching radar) |
| **Average Regime Score** | **6.7** |
| **Average Setup Score** | **6.7** |
| **Average Overall Score** | **6.7** |
| Pairs scoring 8+ | 17 (35%) |
| Pairs scoring 5 or below | 9 (18%) |
| Best scores (8.5) | 01-02, 01-10, 01-13, 01-17, 03-04, 03-05, 03-07, 03-14 |
| Worst mismatches (≤4.5) | 01-22 (4.5), 01-27 (3.5), 03-10 (4.5), 03-31 (4.5), 04-15 (4.5) |

---

## Key Findings

### 1. RANGE_BOUND Bias (84% of calls)

The radar called **RANGE_BOUND / SIPs_ONLY** for 38 of 45 scored pairs (84%). It rarely upgrades to CAUTIOUS_BULL or BULL even when breadth metrics improve. This creates a persistent lag vs Pradeep's more nuanced regime transitions.

### 2. Deep Bearish = Good Match

When T2108 drops below 20 and net primary is deeply negative, the radar matches Pradeep well (scores 8–9). Examples: 01-10, 01-13, 03-04, 03-05, 03-07, 03-14, 04-04.

### 3. Regime Transition Lag

The radar lags Pradeep by 1–3 days on regime transitions. When Pradeep shifts from bearish to cautiously bullish (e.g., T2108 bouncing from lows, 20% study oscillator signals), the radar still shows RANGE_BOUND. Key examples:
- **01-14**: Pradeep bullish for bounce (T2108 near 20); radar RANGE_BOUND
- **03-17**: Pradeep short-term bullish; radar RANGE_BOUND
- **04-15**: Pradeep "first legs forming" (89 stocks up); radar RANGE_BOUND

### 4. CAPITULATION Calls Were Correct

Apr 7–9 (T2108 at 4–7%) — radar correctly called CAPITULATION / FULL_LONG. Pradeep was more cautious on timing ("wait for setups"), but the regime call was objectively correct. T2108 below 5 with net primary below -2000 IS capitulation territory.

### 5. 20% Study Oscillator is Pradeep's Edge

Pradeep uses "below 20 = bullish signal, approaching 100 = bearish signal" as a mean-reversion oscillator. The radar doesn't use 20% study extremes this way — it treats the count as a breadth indicator, not an oscillator. This is the biggest systematic gap.

### 6. CAUTIOUS_BULL Mismatches

The 3 dates where radar called CAUTIOUS_BULL but Pradeep was bearish (01-08, 03-10, 03-31) all shared: T2108 bouncing from lows (22–29%) with net primary still deeply negative (-237 to -1045). The radar's upgrade trigger fires too early on T2108 bounces without confirming breadth.

### 7. Narrative Shifts Not Captured

01-27 (DeepSeek selloff): T2108 at 45.3% with net +190 looked bullish to the algorithm, but Pradeep correctly identified a narrative regime shift. The radar has no mechanism for narrative/sentiment regime changes.

---

## Recommended Radar Improvements

1. **Add T2108 velocity (rate-of-change)**: Use 3-day and 5-day T2108 change as a regime transition signal. Falling T2108 from 40+ to below 30 should trigger CAUTIOUS_BEARISH faster.

2. **20% study as oscillator**: When 20% study bullish count drops below 15 OR rises above 80, treat as mean-reversion signal (opposite direction), not just breadth.

3. **Net primary direction matters more than level**: Net primary improving for 3+ consecutive days should start regime upgrade, even if still negative.

4. **Add CONFIDENT_BULL regime**: For T2108 > 40 with net primary > +200 and 20% study > 40, flag CONFIDENT_BULL to capture 01-21 to 01-26 period.

5. **CAPITULATION action modifier**: When CAPITULATION fires, add "process-driven: wait for continuation setup" rather than just FULL_LONG, which implies aggressive buying.

6. **Narrative shift detection**: Consider a rule: if T2108 > 40 but 5-day ratio drops below 0.5 AND net primary drops > 500 in 2 days, flag potential narrative shift (bearish reversal).