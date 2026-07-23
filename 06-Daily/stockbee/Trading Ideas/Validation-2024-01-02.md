---
title: "Radar Validation — Jan-Feb 2024"
date: 2024-01-02
tags: [validation, radar, stockbee, pradeep-bonde, backtest]
---

# Radar Validation — Jan-Feb 2024

## Method

Compare offline-generated radar files with Pradeep's curated session notes for each trading day where both exist. Radar file dated T+1 uses data from date T (matching the session date).

Scoring: 0 (completely wrong) to 10 (perfect match).

- **Regime**: Does the radar's regime label match Pradeep's described market environment?
- **Setup**: Do the radar's trade ideas / setup types match what Pradeep highlighted?
- **Overall**: Weighted blend of regime + setup accuracy.

## Per-Date Scorecard

| Date | Radar Regime | Pradeep Call | Regime | Setup | Overall | Notes |
|------|-------------|-------------|--------|-------|---------|-------|
| 2024-01-02 | RANGE_BOUND/SIPs_ONLY | Pullback likely after relentless rally, selective phase, EP 9M short | 7 | 6 | 6 | Radar says range-bound (correct direction) but misses that it's specifically a pullback from overbought. SIPs_ONLY aligns with "only right setups work" |
| 2024-01-03 | RANGE_BOUND/SIPs_ONLY | Pullback day 2, oversold bounces only, breakouts failing | 7 | 7 | 7 | Range-bound/choppy is right. SIPs_ONLY matches "no setup = no trade" |
| 2024-01-04 | RANGE_BOUND/SIPs_ONLY | Day 4 pullback, oversold bounces, breakouts failing | 7 | 7 | 7 | Same — regime correct, action matches |
| 2024-01-05 | RANGE_BOUND/SIPs_ONLY | Buy-the-dip bounce, SA framework, 80/20 | 6 | 5 | 5 | Radar says SIPs_ONLY but Pradeep saw a bounce day with actionable buys. Missed the shift |
| 2024-01-08 | RANGE_BOUND/SIPs_ONLY | Rally stalls, buy program day, no setup = no trade | 7 | 7 | 7 | Correct — choppy, no clean setups |
| 2024-01-09 | RANGE_BOUND/SIPs_ONLY | No follow-through, choppy, bottom-of-barrel only | 8 | 7 | 7 | Good match |
| 2024-01-10 | RANGE_BOUND/SIPs_ONLY | Choppy, earnings season starts, 20% study recovery | 7 | 6 | 6 | Radar doesn't show 20% study recovery (data=0). Regime ok |
| 2024-01-11 | RANGE_BOUND/SIPs_ONLY | Process over pattern, hit and run, delayed reaction | 7 | 5 | 6 | Setup types (hit-and-run, delayed reaction) not surfaced |
| 2024-01-16 | RANGE_BOUND/SIPs_ONLY | Short-term bearish, 80/20 engineering | 8 | 5 | 6 | Radar regime right but "short-term bearish" is more directional than RANGE_BOUND implies |
| 2024-01-17 | RANGE_BOUND/SIPs_ONLY | Slow deterioration, SA is everything | 8 | 5 | 6 | Match on regime, setups thin |
| 2024-01-18 | RANGE_BOUND/SIPs_ONLY | Bounce likely, buy nothing without setup | 5 | 6 | 5 | "Bounce likely" suggests CAUTIOUS_BULL not RANGE_BOUND |
| 2024-01-19 | RANGE_BOUND/SIPs_ONLY | 20% study screams bounce, SMCI 33%, combo bearish | 4 | 6 | 5 | "Screams bounce" = should be CAUTIOUS_BULL. 20% study shows 0 in radar, Pradeep says 5 |
| 2024-01-22 | RANGE_BOUND/SIPs_ONLY | KLP day, ADM CFO fraud, sell into strength | 6 | 5 | 5 | Choppy/mixed — range ok |
| 2024-01-23 | RANGE_BOUND/SIPs_ONLY | Mind clarity, SMCI gift, high-priced stocks | 6 | 5 | 5 | Still choppy but SMCI trade working — selective setups |
| 2024-01-24 | RANGE_BOUND/SIPs_ONLY | Netflix day, one trade big move | 6 | 4 | 5 | One big trade = specific catalyst, radar generic |
| 2024-01-25 | RANGE_BOUND/SIPs_ONLY | Short/long consolidations, size matters | 7 | 5 | 6 | Consolidation = range, ok |
| 2024-01-26 | RANGE_BOUND/SIPs_ONLY | Mind clarity, gestalt moment | 5 | 3 | 4 | Vague session, radar doesn't capture nuance |
| 2024-01-29 | RANGE_BOUND/SIPs_ONLY | Eureka moment, hard work alone won't make you trader | 3 | 2 | 2 | Meta/teaching day, no market regime signal |
| 2024-01-30 | RANGE_BOUND/SIPs_ONLY | Don't arrive at party at 12:30 for cleaning | 5 | 4 | 4 | Late-to-party warning = market extended but still running |
| 2024-01-31 | RANGE_BOUND/SIPs_ONLY | Must-buy setup, paradigm killing you | 5 | 4 | 4 | "Must-buy setup" suggests setups exist, radar says SIPs_ONLY |
| 2024-02-01 | RANGE_BOUND/SIPs_ONLY | Don't call everything EP, red flags, process | 7 | 5 | 6 | Choppy regime correct |
| 2024-02-02 | RANGE_BOUND/SIPs_ONLY | SIPs is a hookup, not marriage | 7 | 6 | 6 | Quick trades in chop — matches |
| 2024-02-05 | RANGE_BOUND/SIPs_ONLY | Buy setups not stocks, discrete info is fugazi | 6 | 5 | 5 | Still selective but setups exist — radar too cautious |
| 2024-02-06 | RANGE_BOUND/SIPs_ONLY | Choppy, catalyst creates charts | 7 | 6 | 6 | Choppy = range, match |
| 2024-02-07 | RANGE_BOUND/SIPs_ONLY | Where is the party? Barcelona pickpocket rule | 6 | 4 | 5 | No party = range, but radar missing nuance |
| 2024-02-08 | RANGE_BOUND/SIPs_ONLY | Bonkers earnings, size matters below 10B, hit and run | 5 | 5 | 5 | Earnings = actionable, radar too cautious |
| 2024-02-12 | RANGE_BOUND/SIPs_ONLY | Breadth thrust, breakouts working, sugar babies flying | 2 | 4 | 3 | **Major miss**. 3 consecutive 300+ breadth days, breakouts working, 20% study at 52. Should be FULL_BULL |
| 2024-02-13 | RANGE_BOUND/SIPs_ONLY | Breadth thrust confirmed, CPI is noise, marry method | 2 | 4 | 3 | **Major miss**. BO:BD ratio 4.69, T2108 rising, 20% study expanding. Should be CAUTIOUS_BULL+ |
| 2024-02-14 | RANGE_BOUND/SIPs_ONLY | CPI pullback is overreaction, bull market intact, selective | 4 | 5 | 4 | "Bull market intact" = CAUTIOUS_BULL at minimum |
| 2024-02-15 | RANGE_BOUND/SIPs_ONLY | Bullish with biotech, selective breakouts | 3 | 5 | 4 | **Says bullish** but radar says RANGE_BOUND |
| 2024-02-16 | RANGE_BOUND/SIPs_ONLY | Bull market overreacts, stay bullish, veterans make money | 3 | 5 | 4 | **Explicitly bullish** but radar RANGE_BOUND |
| 2024-02-20 | RANGE_BOUND/SIPs_ONLY | Pullback starting, be selective, stopped out | 7 | 5 | 6 | Correct — pullback after bull run |
| 2024-02-21 | RANGE_BOUND/SIPs_ONLY | Sugar babies working, biotech delayed EPs | 5 | 6 | 5 | Selective works, range-ish |
| 2024-02-26 | RANGE_BOUND/SIPs_ONLY | One-day overreaction best rate, breakouts working selectively | 5 | 6 | 5 | Selective but working |
| 2024-02-27 | RANGE_BOUND/SIPs_ONLY | Sugar babies going crazy, 4% breakout most important | 3 | 5 | 4 | Things are working = should be CAUTIOUS_BULL |
| 2024-02-28 | RANGE_BOUND/SIPs_ONLY | Themes everything, crypto/bio/semi crazy, long side only | 2 | 6 | 4 | **"Long side only" = clearly bullish**. Radar says RANGE_BOUND |

## Summary Statistics

| Metric | Regime | Setup | Overall |
|--------|--------|-------|---------|
| **Mean** | 5.4 | 5.2 | 5.2 |
| **Median** | 6 | 5 | 5 |
| **Min** | 2 | 2 | 2 |
| **Max** | 8 | 7 | 7 |

## Key Findings

### 1. 20% Study Data Missing for Historical Dates (Critical Bug)

The radar shows 20% study (bullish) = 0 for all Jan dates and very low values (5-14) for Feb dates. Pradeep's sessions reference 20% study values of 5 (Jan 19), 52 (Feb 12), and much higher. The batch regen cannot backfill 20% study data from offline sources, causing the regime judge to default to RANGE_BOUND for every date.

**Impact**: Every date is labeled RANGE_BOUND/SIPs_ONLY regardless of actual market conditions. This is the #1 accuracy blocker.

### 2. Regime Assessment is Flat (No Bull Detection)

The radar never transitions to CAUTIOUS_BULL or FULL_BULL even when Pradeep explicitly says "breadth thrust confirmed, breakouts working" (Feb 12-13) or "bull market overreacts, stay bullish" (Feb 16). The BO:BD ratio data is present and shows 4.69 on Feb 12 — clearly bullish — but the judge doesn't use it to override the missing 20% study.

### 3. Setup Identification is Generic

Trade ideas default to SIPs (stocks-in-play) without distinguishing Pradeep's specific setup vocabulary: EP 9M breakdown, delayed reaction, sugar babies, hit-and-run, combo bearish. The setup types in the radar are undifferentiated.

### 4. Best Matches: Choppy/Range Markets

The radar scores highest (7-8) when the actual market was indeed choppy with no clear direction (Jan 3-4, 8-9, 16-17). RANGE_BOUND/SIPs_ONLY is accurate for these periods.

### 5. Worst Matches: Bullish Transitions

The radar scores lowest (2-3 regime) when Pradeep identifies a bullish shift that the radar misses entirely (Feb 12-13 breadth thrust, Feb 15-16 bull continuation, Feb 28 "long side only").

## Recommendations

1. **Backfill 20% study from historical data** — even a rough proxy (TI65 universe size × sector breadth) would improve regime detection
2. **Add BO:BD ratio as primary regime signal** — ratio > 3.0 should trigger at least CAUTIOUS_BULL regardless of 20% study
3. **Add trend detection** — if Net Primary improving 3+ days and T2108 rising, upgrade from RANGE_BOUND
4. **Surface setup vocabulary** — map Pradeep's named setups (EP 9M, delayed reaction, sugar babies, hit-and-run) to pattern definitions
5. **Add "market phase" secondary label** — even if primary regime is RANGE_BOUND, note "bounce likely" or "pullback starting" from breadth trends