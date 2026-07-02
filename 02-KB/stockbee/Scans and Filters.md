---
title: Scans and Filters
date: 2026-06-03
tags: [kb, scans, filters, PCF, TC2000, formulas, watchlist, screening]
---

# Scans and Filters

> **Index note** — brief summaries with [[wikilinks]] to guides and transcripts.
> For full detail, follow the links. The transcripts are the most comprehensive source.

## Core Scans

| Scan | PCF Formula | Purpose | Output | Source |
|------|------------|---------|--------|--------|
| **EP 9M** | `C/C1 >= 1.04 AND V >= V1 AND V >= 8,900,000` | Find today's explosive moves | ~10–20 stocks by 09:45; ~60–70 by 11:00 | [[21. Process Guide|Process EP9M]] |
| **DEP** | `C/C1 >= 1.04 AND V >= 8,900,000` (last 25 days) | Find catalyst + pullback candidates | ~405–500 stocks | [[16. DEP Guide|DEP Part 1]] |
| **Sugar Baby Count** | Same as EP 9M, Count Through 1450/756/504/252/126/50/20/10/5 days | Find market's "madly in love" stocks | ~87–91 master list | [[14. Sugar Babies Guide|Sugar Babies Part 6]] |
| **M20 Bullish** | `C >= 1.2 * MINC30 OR C >= MINC30 + 20` | Absolute anchored momentum | Variable; sort by negative NC for pullbacks | [[05. M20 Guide|M20 Part 2]] |
| **TI65 Bullish** | `AVGC7 / AVGC65 >= 1.05` | Trend intensity | ~415 stocks; +3T = ~19 | [[04. TI65 Guide|TI65 Part 2]] |
| **MDT Rank** | `C / AVGC126` | 126-day momentum ranking | Top 100–200 | [[07. MDT Guide|MDT]] |
| **MDT Absolute** | `C / AVGC126 >= 1.18` | Stocks that have broken out | Variable | [[07. MDT Guide|MDT]] |
| **DT** | `C / MINL252 >= 1.8` | Darvas-style (80% from 52-week low) | Variable | [[06. DT Guide|DT Part 2]] |
| **3T (Tight Days)** | 3 consecutive days with daily change <1% | Volatility contraction | Reduces ~415 to ~19 | [[08. Anticipation (ANTS) Guide|ANTS Part 9]] |
| **2T** | 2 consecutive days with daily change <1% | Slightly looser contraction | Slightly more than 3T | [[08. Anticipation (ANTS) Guide|ANTS Part 9]] |

## DEP Scan Variations

| Variation | Filter | Output | Use Case | Source |
|-----------|--------|--------|----------|--------|
| **Max V25 sort** | Sort DEP results by max volume in last 25 days | Top 25–35 of ~500 | Prioritize most significant catalysts | [[16. DEP Guide|DEP Part 8]] |
| **V > V1** | Add volume > previous day | ~251 (vs 261 without) | Slightly refined list | [[16. DEP Guide|DEP Part 2]] |
| **20M+ volume** | Volume >= 20,000,000 | ~85 stocks | For very busy traders | [[16. DEP Guide|DEP Part 2]] |
| **Last 5–10 days** | Catalyst within last 5–10 days | Fewer stocks | Genuine DEPs usually break out quickly | [[16. DEP Guide|DEP Part 7]] |
| **1000+ funds** | Run on institutional list (~181 stocks) | Simpler, higher quality | For simpler DEP selection | [[16. DEP Guide|DEP Part 2]] |

## Sugar Baby Process

1. **Run Count Through** for each timeframe: 5, 10, 20, 50, 126, 252, 504, 756, 1,450 days
2. **Sort descending** by count
3. **Select top 20–30** per timeframe
4. **For 5-day, 10-day, and 20-day**: require minimum 3 hits
5. **Flag all symbols** and combine into one master list (~90 stocks)
6. **Trade only the ones that give a setup** — "When a Sugar Baby calls, you take the call"

## Momentum OR Logic (Smart Scan)

Instead of running four separate scans, combine with OR:
```
TI65 > 1.05 OR M20 = true OR MDT condition OR DT condition
```
Then apply 3T/2T filter on top.

## Daily Watchlist Size

| Setup | Max Watchlist Size | Rationale | Source |
|-------|-------------------|-----------|--------|
| **DEP** | 5–6 stocks | "Never more than five" — couple's success secret | [[21. Process Guide|Process — Fine Tune]] |
| **EP 9M** | 1–2 stocks at any moment | Out of 20 EP 9M stocks, only 1–2 have SOS | [[21. Process Guide|Process EP9M]] |
| **MDT weekly** | 10–15 stocks | Weekend prep → 1–2 breakouts per week | [[07. MDTE Guide|MDT]] |
| **Anticipation** | 19–32 stocks (after 3T/2T) | Very manageable | [[08. Anticipation (ANTS) Guide|ANTS Part 9]] |
| **Sugar Babies master** | ~90 stocks | But only trade the ones that give a setup | [[14. Sugar Babies Guide|Sugar Babies Part 6]] |

## Weekend vs Daily Process

| Task | Weekend | Daily | Source |
|------|---------|-------|--------|
| **DEP scan** | Full 25-day scan, sort Max V25, create weekly watchlist | Sort by Max V25, update for next day | [[16. DEP Guide|DEP Part 6]] |
| **Sugar Babies** | Run Count Through (10 min) | Go through master list for setups | [[14. Sugar Babies Guide|Sugar Babies Part 6]] |
| **MDT** | Build universe (~410 stocks), eliminate biotech/reversals | Monitor for breakouts | [[07. MDT Guide|MDT]] |
| **Anticipation** | Run M20/TI65/MDT/DT scans, find tight days | Check watchlist in first 15 min | [[08. Anticipation (ANTS) Guide|ANTS]] |
| **EP 9M** | N/A | Run at 09:30, monitor through day | [[21. Process Guide|Process EP9M]] |

## FMP API Mapping (for Python Scanner)

| Pradeep Scan | FMP Endpoint | Parameters |
|-------------|-------------|-----------|
| **EP 9M today** | `GET /stable/biggest-gainers` + `GET /stable/biggest-losers` | Filter: `changePercentage >= 4`, `volume >= 9M`, `price >= 3` |
| **DEP (last 25 days)** | `GET /stable/company-screener` + `GET /stable/historical-price-eod/full` | Screener: `priceMoreThan=3`, `volumeMoreThan=9M`; then check 25-day history for 4% days |
| **Sugar Baby Count** | `GET /stable/historical-price-eod/full` (1,450 days) | Count 4%+ days with 9M+ volume per stock per timeframe (5/10/20/50/126/252/504/756/1450) |
| **Max V25** | `GET /stable/historical-price-eod/full` (25 days) | Find `max(volume)` per stock |
| **Institutional filter** | `GET /stable/institutional-ownership/symbol-positions-summary` | Filter: `numberOfHolders >= 1000` |
| **Bucket 0/1/2** | `GET /stable/income-statement-growth` | Filter: `growthRevenue > 0.39` |
| **Earnings calendar** | `GET /stable/earnings-calendar` | Check for today's announcements |
| **Earnings surprises** | `GET /stable/earnings-surprises-bulk` | Filter: `epsActual > epsEstimated` |

## See Also

- [[Entries]] — how scans convert into tradable setups
- [[Catalysts]] — how to validate what the scan found
- [[Stock Selection]] — how to filter scan results for quality
- [[Market Monitor]] — daily process for running scans
- [[Short Side]] — bearish scan variations
