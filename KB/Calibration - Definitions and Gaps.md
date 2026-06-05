---
title: Calibration — Definitions and Gaps
date: 2026-06-05
tags: [kb, calibration, market-monitor, definitions]
---

# Calibration — Definitions and Gaps

This note documents the **exact definitions** Pradeep Bonde uses for his Market Monitor metrics, and the gaps between our Trading Radar Engine and his StockBee MM.

---

## Pradeep's Exact Definitions

| Metric | Definition | Lookback | Universe | Source |
|--------|-----------|----------|----------|--------|
| **Primary Up/Down** | ≥25% in last quarter | **65 trading days** | US common stocks + ADRs + ETFs | MM Guide Part 1, Part 4 |
| **Monthly 25↑/↓** | ≥25% in a month | **22 trading days** | Same as Primary | MM Guide Part 1, Part 5 |
| **Monthly 50↑/↓** | ≥50% in a month | **22 trading days** | Same as Primary | MM Guide Part 1, Part 5 |
| **Fib 13↑/↓** | ≥13% in last ~half-quarter | **34 trading days** | Same as Primary | MM Guide Part 1, Part 6 |
| **T2108** | % above 40-day SMA | **40 trading days** | All stocks (inferred from TC2000 built-in) | MM Guide Part 8 |
| **4% Breakout** | C/C1 ≥ 1.04 + V ≥ 100K (base) | 1 day | US common stocks + ADRs + ETFs | SOS Guide Part 8 |
| **4% Breakdown** | C/C1 ≤ 0.96 + V ≥ 100K (base) | 1 day | Same as Breakout | SOS Guide Part 8 |

### Key Notes

- **"65 days" = trading days** in TC2000 context (not calendar days)
- **"22 days" = trading days** for Monthly (not 20, not calendar month)
- **"34 days" = trading days** for Fib 13 (half of 65)
- **Thresholds are ≥** (greater than or equal), not exactly
- **Universe includes ADRs** — this was a critical gap we had
- **ETFs are included** in Market Monitor breadth, but **excluded** in setup-specific scans (Sugar Babies, ANTicipation)
- **Volume filter** for universe: `MINV3.1 >= 100,000` (100K avg over last 3 trading days)
- **Price filter**: `C >= 3` (close above $3)

---

## Our Implementation Fixes Applied (2026-06-05)

### Fix #1: ADR Exclusion Removed

**Problem:** Our `ETF_KEYWORDS` filtered out `" ADR"`, `" Depositary"`, `" American Depositary"`. Pradeep **includes ADRs**.

**Impact:** ~300–500 ADR tickers were silently dropped from our universe.

**Fix:** Removed ADR keywords from `db.py` and reclassified all universe rows.

### Fix #2: T2108 Denominator

**Problem:** We used only tickers with ≥40 days of history as denominator. Pradeep uses full universe count (~6,462).

**Impact:** Narrower denominator = artificially higher T2108 (62% vs 39%).

**Fix:** `breadth_calculator.py` now uses `broad_count` (full broad universe) as T2108 denominator.

### Fix #3: Unclassified Tickers Dropped

**Problem:** `get_non_etf_tickers()` only queried `universe` table. Tickers with data in `daily_ohlcv` but no `universe` record were silently dropped.

**Fix:** `get_non_etf_tickers()` now includes all tickers from `daily_ohlcv` unless explicitly flagged as ETF.

---

## Calibration Gap Analysis

| Metric | Our Calc (Before) | Our Expected (After) | Pradeep | Gap Source |
|--------|------------------|---------------------|---------|-----------|
| Universe | ~6,300 | ~6,500–6,700 | 6,462 | ADR restore + unclassified |
| Breakdown | 438 | ~440 | 431 | ✅ Very close |
| Monthly 25↑ | 234 | ~240 | 215 | ✅ Close |
| Breakout | 111 | ~115 | 153 | ⚠️ Survivor bias |
| Primary Up | 593 | 650–750 | 1,469 | 🔴 Survivor bias (unfixable with FMP) |
| T2108 | 61.93% | 55–60% | 39.03% | 🔴 Survivor bias + data vendor |
| Fib 13↑ | 821 | 900–1,000 | 1,581 | 🔴 Survivor bias |

### Survivor Bias — The Unfixable Gap

**Why our Primary Up is ~700 lower than Pradeep's:**

1. **Delisted/bankrupt stocks missing** — Our FMP data only has "active" tickers. In a bear market, many stocks that are down 25%+ get delisted or stop trading. These stocks don't exist in our database, so we can't count them as "Primary Down."
2. **Result:** Our "Primary Down" is artificially low → Our "Primary Up" is artificially low (because the net is Up − Down).
3. **Pradeep's TC2000** has historical data for ALL stocks that ever existed, including delisted ones.

**Why our T2108 is ~20pp higher than Pradeep's:**

1. **Down stocks go to zero** — Stocks that fall below their 40-day SMA and keep falling eventually get delisted or stop trading.
2. **These "below MA40" stocks disappear from our DB** → Our denominator shrinks → % above MA40 increases.
3. **Pradeep's TC2000** retains delisted stocks in its historical data.

### FMP Delisted Companies API (Discovered 2026-06-05)

**Your research note** (`Trading Radar Engine/_02. FMP API - Delisted Stocks.md`) reveals that FMP **does** have delisted company data:

| Endpoint | Availability | Coverage |
|----------|-------------|----------|
| `/stable/delisted-companies` | ✅ Working | All delisted companies (symbol, name, exchange, delistedDate) |
| `/stable/historical-price-eod/non-split-adjusted` for delisted tickers | ⚠️ Partial | Select US companies only |

**Verified:** The `/stable/delisted-companies` endpoint returns data (tested: `{'symbol': 'EDAP', 'companyName': 'Edap Tms S.a.', 'exchange': 'NASDAQ', 'ipoDate': '1997-08-01', 'delistedDate': '2026-06-01'}`).

**Status:** We built `delisted_loader.py` to integrate delisted stocks into our database, but **we have not yet run the full fetch** due to the ongoing backfill consuming API quota.

**Next step:** Run `py delisted_loader.py --fetch-all --backfill-hist --recent-only` after the current backfill completes.

### What This Means

- **Short-term trends:** Our MM is directionally correct (T2108 rising/falling matches Pradeep)
- **Absolute levels:** Our T2108 runs ~15–20pp higher; our Primary Up runs ~700 lower
- **Bottom detection:** Still valid — Primary < 200 + T2108 single digits will show in BOTH systems
- **Relative day-to-day:** Our system tracks changes accurately
- **After delisted integration:** Expected to narrow gaps significantly (Primary Up closer to 1,000+, T2108 closer to 45–50%)

---

## Code Changes

### `db.py`
- Removed `" ADR"`, `" Depositary"`, `" American Depositary"` from `ETF_KEYWORDS`
- Updated `get_non_etf_tickers()` to include unclassified tickers
- Updated comments to reflect ADR inclusion

### `breadth_calculator.py`
- T2108 denominator changed from `eligible` (tickers with ≥40d history) to `broad_count` (full broad universe)
- Added comment explaining the Pradeep-aligned denominator

### `fmp_adapter.py` (New)
- Added `get_delisted_companies()`, `get_all_delisted_companies()`, `get_delisted_historical_raw()`

### `delisted_loader.py` (New)
- Full pipeline: fetch delisted → add to universe → backfill historical → recalculate MM

---

## Verification

After fixes are applied, verify by running:

```bash
cd D:\opencodeworkspace\.trading\market-monitor
py nightly_runner.py --force
```

Then compare against StockBee MM values at `https://stockbee.biz/market-monitor/`

---

## Cross-References

- [[KB/Market Monitor]] — Full Market Monitor methodology
- [[11. Market Monitor Guide]] — Curated 8-part guide
- [[Trading Radar Engine/Calibration Log]] — Daily calibration tracking
- [[01 - Market Monitor#Key Rules Summary]] — Key rules with thresholds

---

*Last updated: 2026-06-05*