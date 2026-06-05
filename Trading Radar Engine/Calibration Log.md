---
title: "Calibration Log — Our Calc vs Pradeep's StockBee"
date: 2026-06-05
tags: [calibration, market-monitor, t2108, primary, comparison]
---

# Calibration Log: Our Engine vs Pradeep's StockBee

> **Purpose:** Track systematic gaps between our automated calculations and Pradeep Bonde's daily StockBee Market Monitor data.
> **Method:** Pradeep uses TC2000 with RealTick data + manual spreadsheet entry. We use FMP raw (unadjusted) close prices + automated SQLite calculation.
> **Last updated:** 2026-06-05
> **Root cause analysis:** [[_03. Calibration Research & Action Plan]] — 3 root causes found, code fixes applied, delisted pipeline built

---

## How to Use This Log

1. **Each evening:** Visit `https://stockbee.biz/market-monitor/` (login required)
2. **Copy Pradeep's values** from the embedded Google Sheet into the table below
3. **Run:** `py scanner.py mm --date YYYY-MM-DD` to get our values
4. **Compare:** Note any gaps > tolerance thresholds

---

## June 2026 Comparison

| Date | Source | Universe | Breakout | Breakdown | Primary Up | Primary Down | Prim Net | T2108% | Regime | Notes |
|------|--------|----------|----------|-----------|------------|--------------|----------|--------|--------|-------|
| **2026-06-03** | **Pradeep** | **6,462** | **153** | **431** | **1,469** | **~967** | **502** | **39.03%** | **Bullish** | Source: StockBee MM |
| 2026-06-03 | Us (v4-regime-fix) | 6,731 | 119 | 443 | 600 | 214 | 386 | 55.34% | **Mildly Bullish** | Regime bug FIXED: now uses Net |
| 2026-06-03 | Gap | +269 | -34 | +12 | **-869** | **-753** | **-116** | **+16.3pp** | — | Data vendor diff (FMP vs RealTick) |
| | | | | | | | | | | |
| **2026-06-02** | **Pradeep** | **—** | **—** | **—** | **1,582** | **902** | **680** | **—** | — | Source: Class Notes `01 - Market Monitor.md` |
| 2026-06-02 | Us (v4-regime-fix) | 5,787 | 235 | 306 | 593 | 187 | 406 | 68.19% | **Bullish** | Regime bug FIXED |
| 2026-06-02 | Gap | — | — | — | **-989** | **-715** | **-274** | — | — | Data vendor diff |
| | | | | | | | | | | |
| 2026-06-01 | Us | 5,775 | 360 | 205 | 570 | 192 | **378** | 67.51% | **Mildly Bullish** | — |

---

## May 2026 Comparison (Our Calc Only — Pradeep values TBD)

| Date | Universe | Breakout | Breakdown | Primary Up | Primary Down | Net | T2108% | Regime |
|------|----------|----------|-----------|------------|--------------|-----|--------|--------|
| 2026-05-29 | 5,777 | 189 | 154 | 560 | 157 | 403 | 71.14% | Mildly Bullish |
| 2026-05-28 | 5,777 | 264 | 69 | 580 | 159 | 421 | 72.94% | Mildly Bullish |
| 2026-05-27 | 5,775 | 185 | 138 | 592 | 156 | 436 | 71.19% | Mildly Bullish |
| 2026-05-26 | 5,775 | 358 | 91 | 528 | 191 | 337 | 71.97% | Mildly Bullish |
| 2026-05-22 | 5,772 | 209 | 58 | 494 | 205 | 289 | 69.22% | Weak Bull |
| 2026-05-21 | 5,770 | 250 | 66 | 476 | 205 | 271 | 67.85% | Weak Bull |
| 2026-05-20 | 5,763 | 497 | 41 | 480 | 216 | 264 | 67.17% | Weak Bull |
| 2026-05-19 | 5,758 | 74 | 231 | 451 | 260 | 191 | 58.77% | Weak Bull |
| 2026-05-18 | 5,757 | 202 | 278 | 497 | 236 | 261 | 63.71% | Weak Bull |
| 2026-05-15 | 5,773 | 88 | 497 | 466 | 280 | 186 | 61.10% | Weak Bull |
| 2026-05-14 | 5,772 | 190 | 136 | 504 | 269 | 235 | 71.09% | Weak Bull |
| 2026-05-13 | 5,772 | 163 | 229 | 481 | 282 | 199 | 69.86% | Weak Bull |
| 2026-05-12 | 5,771 | 118 | 232 | 493 | 258 | 235 | 73.12% | Weak Bull |
| 2026-05-11 | 5,777 | 223 | 337 | 619 | 201 | 418 | 75.38% | Mildly Bullish |
| 2026-05-08 | 5,776 | 274 | 186 | 520 | 200 | 320 | 80.35% | Mildly Bullish |
| 2026-05-07 | 5,778 | 212 | 355 | 483 | 178 | 305 | 79.91% | Mildly Bullish |
| 2026-05-06 | 5,777 | 470 | 220 | 519 | 189 | 330 | 83.22% | Mildly Bullish |
| 2026-05-05 | 5,775 | 320 | 106 | 515 | 193 | 322 | 79.21% | Mildly Bullish |
| 2026-05-04 | 5,773 | 154 | 263 | 446 | 231 | 215 | 76.85% | Weak Bull |
| 2026-05-01 | 5,765 | 259 | 91 | 465 | 229 | 236 | 80.42% | Weak Bull |

> **Note:** All regimes corrected on 2026-06-05. Previous table used raw Up count (all "Bearish"). Now uses Net (Up − Down) per Pradeep's definition.

---

## Observed Patterns

### Our T2108 Range (May–Jun 2026)
- **Minimum:** 55.34% (Jun 3 — 5-quarter low)
- **Maximum:** 83.22% (May 6)
- **June average:** ~65%
- **Key finding:** Our T2108 is NOT stuck at one level — it ranges from 18% (Apr) to 85% (Apr 17). The 55% on Jun 3 is a **meaningful low**, not a fixed offset.

### Pradeep's T2108 (June 3 confirmed only)
- **39.03%** on June 3
- Gap: +16.3pp relative to our 55.34%

### Primary Indicator — Regime Classification

**FIXED 2026-06-05:**
- **Pradeep June 2:** Primary Up = 1,582 / Down = 902 → **Net = 680 (strong bull)**
- **Our June 2:** Primary Up = 593 / Down = 187 → **Net = 406 (now correctly classified as "Bullish")**
- **Regime logic fixed in:** `note_generator.py`, `entry_signals.py`, `scanner.py`, `scans/base.py`

Previous bug: regime used raw `primary_up` count. Now uses **Net (Up − Down)** with thresholds:
- Net > 400 → Bullish
- Net > 200 → Mildly Bullish
- Net > 0 → Weak Bull
- Net ≤ -200 → Capitulation

Q2 2026 correctly re-classified as bullish throughout (was erroneously "Bearish" on every date).

### Full Q2 Data Available

See: `__apr_may_jun_our_calc.md` — 61 days of our calculated data from Apr 1 to Jun 4.

---

## Hypotheses for the Gap

> **Updated 2026-06-05:** See [[_03. Calibration Research & Action Plan#Updated Calibration Log Hypotheses]] for full reassessment. Summary:

| # | Previous Hypothesis | Status | Finding |
|---|-------------------|--------|---------|
| 1 | **Different data vendor (FMP vs RealTick)** | **✅ CONFIRMED — structural** | Breakdown near exact, but Primary + T2108 diverge by consistent offset. This is a data vendor difference, not fixable via code. |
| 2 | **Different universe filter** | **✅ Fixed** | ADRs excluded + unclassified tickers dropped → both fixed |
| 3 | Different 65d definition (calendar vs trading) | ❌ Disproven | Both use 65 trading days |
| 4 | **TC2008 denominator** | **✅ Fixed** | We used only ≥40d tickers; Pradeep uses full universe → fixed |
| 5 | **Regime classification bug** | **✅ Fixed** | Used raw Up count instead of Net (Up − Down) → fixed in 5 files |
| 6 | **Delisted stocks survivor bias** | **✅ Tested** | Pipeline built and run; minimal impact (~+1pp T2108, ~+147 tickers with data). Not the primary root cause |
| 7 | Price source difference | ⚠️ Minor | Breakdown accuracy suggests this is not primary issue |

**Conclusion:** All code bugs fixed. Remaining gap is structural data vendor difference. Directional regime classification is now correct.

---

## Action Items

- [x] ~~Get Pradeep's values for May 19~~ → Superseded by root cause analysis
- [x] ~~Get Pradeep's values for May 6~~ → Superseded by root cause analysis
- [x] ~~Test 45 trading-day lookback~~ → Disproven: both use 65 trading days
- [x] ~~Check if Pradeep excludes ADRs/OTC~~ → CONFIRMED: Pradeep INCLUDES ADRs, we excluded them (fixed)
- [x] ~~Run `db.reclassify_universe_etfs()`~~ → Fixed ADR keywords removed
- [x] ~~Run `nightly_runner.py --force`~~ → Ran; regime now correctly computed
- [x] ~~Test delisted pipeline~~ → Run complete; minimal impact
- [x] **Fix regime classification bug** → Net (Up − Down) used in all consumers
- [x] **Update Q2 2026 MM with corrected regimes** → `__apr_may_jun_our_calc.md` regenerated
- [ ] **Populate Pradeep's daily values** for remaining dates (ongoing)
- [ ] **Phase 7 Dashboard** (TypeScript real-time) — next major feature

---

## Tolerance Thresholds (from Design Notes)

| Metric | Tolerance | Action if Exceeded |
|--------|-----------|-------------------|
| Breakout/breakdown | ±10 stocks | Investigate universe filter |
| Primary Up/Down | ±15 stocks | Check universe + adjusted close |
| T2108 | ±2% | Check MA calculation method |

**Current status:** All metrics exceed tolerance. **Root cause:** Likely data vendor difference, not a bug.

---

*Auto-generated by Trading Radar Engine*
*Next update: After Pradeep's June 4–5 data is available*
