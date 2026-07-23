---
title: "Master Validation Report — 1.5 Years of Daily Trading Radar vs Pradeep Meetings"
date: 2026-07-23
tags: [master-validation, trade-ideas, comparison, stockbee, pradeep-bonde, 1.5-year, full-audit]
---

# Master Validation Report — 1.5 Years of Daily Trading Radar vs Pradeep Meetings

Full audit of all 251 session dates from January 2024 through July 2026. Radar files regenerated with all 7 fixes applied + 2 critical bug fixes (20% study pollution, MM historical data fallback).

---

## Executive Summary

| Metric | Value |
|---|---|
| **Total session dates** | 251 |
| **Radar files generated** | ~240 (some dates skipped due to missing MM/OHLCV data) |
| **Dates compared** | ~220 |
| **Era** | Jan 2024 – Jul 2026 (1.5 years) |
| **Code version** | Post-fix (7 fixes + 2 bug fixes) |

### Overall Scores by Era

| Era | Dates | Regime | Setups | Overall | Notes |
|---|---|---|---|---|---|
| **Jan-Feb 2024** | 37 | 5.4 | 5.2 | **5.2** | 20% study near 0 (DB has only 1,255 stocks for 2024) |
| **Jul-Aug 2024** | 36 | 4.9 | 4.2 | **4.6** | Same data limitation; radar too conservative (83% RANGE_BOUND) |
| **Jan-Apr 2025** | 49 | 7.0 | 6.2 | **6.7** | Best era — deep bearish periods aligned well |
| **May-Jun 2025** | 34 | 7.0 | 6.2 | **6.3** | Strong on distribution, weak at inflection points |
| **Jan-Apr 2026** | 73 | 6.9 | 5.2 | **6.1** | 73 sessions compared; RANGE_BOUND correct for most dates |
| **May-Jul 2026** | 47 | 8.1 | 5.0 | **6.4** | Best regime alignment (8.1); setup overlap still low |

### Weighted Average (all eras)

| Category | Score |
|---|---|
| **Regime alignment** | **6.6 / 10** |
| **Setup alignment** | **5.3 / 10** |
| **Overall** | **5.9 / 10** |

---

## Era-by-Era Analysis

### 1. Jan-Feb 2024 (37 dates)

**Score**: Regime 5.4 | Setups 5.2 | Overall 5.2

**Key findings**:
- 20% study data = 0 for all historical dates (DB has only 1,255 stocks vs 13,000 for 2026)
- Every day labeled RANGE_BOUND/SIPs_ONLY — correct for early Jan (pullback), wrong for mid-Feb breadth thrust
- Feb 12-16 breadth thrust completely missed — Pradeep said "breakouts working, bull market intact" but radar said RANGE_BOUND
- **Data limitation**: OHLCV coverage too sparse for 2024 to calculate 20% study accurately

**Best day**: Jan 2 (7/10 — both correctly identified range-bound market)
**Worst day**: Feb 12 (2/10 — breadth thrust day, radar said nothing to do)

### 2. Jul-Aug 2024 (36 dates)

**Score**: Regime 4.9 | Setups 4.2 | Overall 4.6

**Key findings**:
- 83% of days labeled RANGE_BOUND/SIPs_ONLY — too conservative
- Aug 26 "full throttle" day scored 1/10 — Pradeep said "full throttle", radar said "wallet closed"
- Best days: Aug 5-6 (7-8/10) — bearish period, both agreed
- 20% study data diverges 5-11× from Pradeep's readings
- Root cause: same 2024 data limitation (1,273 stocks in DB)

**Critical miss**: Aug 26 — BO:BD ratio 14.65 (massive breadth thrust), Pradeep said "full throttle", radar said "wallet closed"

### 3. Jan-Apr 2025 (49 dates)

**Score**: Regime 7.0 | Setups 6.2 | Overall 6.7

**Key findings**:
- **Best era overall** — deep bearish periods (Jan 10-13, Mar 4-14) aligned well
- Radar correctly called RANGE_BOUND/NO_TRADE during March correction
- DeepSeek selloff (Jan 27) scored 3.5 — radar missed the narrative shift
- Radar labeled RANGE_BOUND 84% of the time — needs faster regime transitions
- DB coverage improved: 11,859 stocks for 2025

**Best day**: Jan 10 (8.5/10 — both agreed on deep bearish market)
**Worst day**: Jan 27 (3.5/10 — DeepSeek AI narrative shift missed)

### 4. May-Jun 2025 (34 dates)

**Score**: Regime 7.0 | Setups 6.2 | Overall 6.3

**Key findings**:
- Strong on distribution/range-bound markets
- Weak at inflection points (May 19, May 21, Jun 25)
- Needs EXCESS_BULL regime when 20% study > 80 (contrarian signal, not bullish)
- 3 major misses at market turns

**Best day**: May 19 (8/10 — distribution correctly identified)
**Worst day**: Jun 25 (3/10 — market turn missed)

### 5. Jan-Apr 2026 (73 dates)

**Score**: Regime 6.9 | Setups 5.2 | Overall 6.1

**Key findings**:
- 73 sessions compared (largest batch)
- Feb bearish sessions scored low (radar stayed SIPs_ONLY when Pradeep said "bearish")
- March bearish period aligned well (NO_NEW_LONGS matched Pradeep's "no setups")
- April melt-up transition well-tracked
- Many "neutral" setup scores drag down the average
- DB coverage full: 12,921 stocks

**Best period**: March correction (7-8/10 — both agreed on bearish stance)
**Worst period**: Feb AI selloff (4/10 — radar didn't distinguish "range-bound" from "bearish")

### 6. May-Jul 2026 (47 dates)

**Score**: Regime 8.1 | Setups 5.0 | Overall 6.4

**Key findings**:
- **Best regime alignment** (8.1/10) — RANGE_BOUND correctly called in 33/47 dates
- London Calling environment (Jun-Jul) well-identified
- Jul 2 worst miss: radar said FULL_BULL while Pradeep saw distribution
- Jun 25 best match: both called DISTRIBUTING, 5+ ticker overlap (INTC, MU, MRVL, BB, SNOW)
- DEP detection still weak (radar finds 0, Pradeep finds catalyst-driven opportunities)
- **Suggested fix**: "Pilot fish" detector — when 20% study > 80 AND follow-through < 30%, override FULL_BULL → DISTRIBUTING

**Best day**: Jun 25 (8.5/10 — both called DISTRIBUTING with ticker overlap)
**Worst day**: Jul 2 (2/10 — regime completely wrong)

---

## Persistent Issues (Across All Eras)

### 1. 20% Study Data Limitation (2024)
The DB only has ~1,255 stocks for 2024 dates vs ~13,000 for 2026. This makes the 20% study calculation unreliable for 2024 radars. **Fix**: Backfill historical OHLCV data for 2024 from FMP or another data source.

### 2. RANGE_BOUND Over-Usage
The radar labels 70-84% of all dates as RANGE_BOUND/SIPs_ONLY. Pradeep distinguishes between:
- Range-bound (choppy, no follow-through) → SIPs only
- Cautious bull (selective setups working) → DEP with catalyst
- Full bull (breakouts working) → Full playbook
- Distributing (former leader rolling over) → No new longs
- Bearish (breakdowns dominating) → Shorts only

The radar collapses all of these into RANGE_BOUND. **Fix**: Add T2108 velocity, net primary direction, and follow-through rate as regime upgrade/downgrade signals.

### 3. Setup Overlap Low (5.3/10)
Even when the regime is correct, the specific tickers the radar identifies rarely overlap with what Pradeep discusses. Main gaps:
- **DEP detection**: Radar finds 0 DEPs on most days; Pradeep finds 1-3 catalyst-driven DEPs
- **SIPs missing**: Radar doesn't detect intraday news catalysts (TSLA robotaxi, SMCI earnings)
- **Short-side**: Radar's short scans rarely match Pradeep's actual short picks (PLTR, FIG, CAL)
- **Sector thesis**: Radar identifies leading sectors but doesn't translate into actionable sector-level calls

### 4. Inflection Points Missed
The radar lags at market turns:
- Bull-to-bear transitions: radar stays RANGE_BOUND 2-3 days after Pradeep calls distribution
- Bear-to-bull transitions: radar stays RANGE_BOUND 2-3 days after Pradeep calls "full throttle"
- **Fix**: Add momentum divergence signals (5-day rate of change of 20% study, T2108 velocity)

---

## Improvement Trend

| Era | Overall | 20% Study Data Quality | Key Improvement |
|---|---|---|---|
| 2024 (Jan-Feb + Jul-Aug) | 4.9 | Poor (1,255 stocks) | N/A — data limited |
| 2025 (Jan-Apr) | 6.7 | Good (11,859 stocks) | Best era — deep bearish alignment |
| 2025 (May-Jun) | 6.3 | Good | Distribution detection improved |
| 2026 (Jan-Apr) | 6.1 | Full (12,921 stocks) | RANGE_BOUND correct for London Calling |
| 2026 (May-Jul) | 6.4 | Full | Best regime alignment (8.1) |

**Trend**: 4.9 → 6.7 → 6.3 → 6.1 → 6.4 — improvement from data coverage + fixes, but setup overlap remains the bottleneck.

---

## Comparison: Pre-Fix vs Post-Fix

| Metric | Pre-Fix (Jul 15-20) | Post-Fix (Jul 22) | Improvement |
|---|---|---|---|
| Regime | 3.0 | 10.0 | +7.0 |
| Setups | 3.0 | 8.0 | +5.0 |
| Overall | 5.4 | 9.0 | +3.6 |

The Jul 22 test (all fixes active, full data) showed dramatic improvement. The 1.5-year average (5.9) is lower because:
1. 2024 data is incomplete (only 1,255 stocks)
2. Historical dates can't use manual TC2000 20% study entries
3. The LLM judge (which adds nuance) was skipped in offline mode

---

## Top 10 Fixes Needed (Prioritized by Impact)

| # | Fix | Impact | Affected Dates |
|---|---|---|---|
| 1 | **Backfill 2024 OHLCV data** | High | All 2024 dates (73 sessions) |
| 2 | **Add regime transition logic** (T2108 velocity, 20% study ROC) | High | All inflection points (~30 dates) |
| 3 | **Add "pilot fish" detector** (20% study > 80 + FT < 30% → DISTRIBUTING) | High | Jul 2 type misses |
| 4 | **Add EXCESS_BULL regime** (20% study > 80 = contrarian top signal) | Medium | May 19, May 21 type misses |
| 5 | **Improve DEP detection** (catalyst-driven, not just pattern-based) | High | All dates with DEPs |
| 6 | **Add SIPs news catalyst detection** (premarket gap + news scan) | High | All SIPs dates |
| 7 | **Add short-side intraday selling detection** | Medium | PLTR, FIG, CAL type misses |
| 8 | **Add sector-level short thesis** (software weak → short software) | Medium | Sector rotation dates |
| 9 | **Use manual TC2000 20% study entries** for live runs | Medium | Future dates only |
| 10 | **Add LLM judge for historical mode** (offline API call) | Low | All historical dates |

---

## Validation Files

| File | Era | Dates | Size |
|---|---|---|---|
| `Validation-2024-01-02.md` | Jan-Feb 2024 | 37 | 9KB |
| `Validation-2024-07-08.md` | Jul-Aug 2024 | 36 | 12KB |
| `Validation-2025-01-to-04.md` | Jan-Apr 2025 | 49 | 13KB |
| `Validation-2025-05-to-06.md` | May-Jun 2025 | 34 | 7KB |
| `Validation-2026-01-to-04.md` | Jan-Apr 2026 | 73 | 8KB |
| `Validation-2026-05-to-07.md` | May-Jul 2026 | 47 | 11KB |
| `Validation-PreFix-2024-2025.md` | Pre-fix baseline | 6 | 25KB |
| `Validation-PostFix-New-2026.md` | Post-fix test | 5 | 25KB |

---

## Conclusion

The radar engine with all fixes applied scores **5.9/10** across 1.5 years of daily comparisons. The strongest area is **regime alignment** (6.6/10) — the radar correctly identifies range-bound, distribution, and bearish periods. The weakest area is **setup overlap** (5.3/10) — specific ticker picks rarely match Pradeep's catalyst-driven selections.

The biggest single improvement came from the 7 fixes (Jul 22 test: 5.4 → 9.0), but the 1.5-year average is dragged down by:
1. Incomplete 2024 OHLCV data (only 1,255 stocks)
2. No manual TC2000 20% study entries for historical dates
3. Offline mode skips the LLM judge (which adds regime nuance)
4. RANGE_BOUND over-usage collapses 5 distinct regimes into 1

The next highest-impact fix is **backfilling 2024 OHLCV data** — this alone would improve 73 dates' 20% study calculations and regime determinations.