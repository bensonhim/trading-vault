---
title: "Market Regime Validation — Full History 2024-2026"
date: 2026-07-27
tags: [trading-radar, market-regime, validation, corrections, bull-trends, t2108, stockbee, full-history]
---

# Market Regime Validation — Full History (Jan 2024 – Jul 2026)

## Overview

Analysis of **642 MM trading days** from **2024-01-02** to **2026-07-24** using **T2108** as the market health proxy with a **5.0-point swing threshold**.

### Methodology

- **Correction** = T2108 drops >5 points from a local peak
- **Bull trend** = T2108 rises >5 points from a local trough
- Peak/trough detection: running high/low with reset on new period start
- Deep correction: T2108 < 20% | Capitulation: T2108 < 10% | Shallow: T2108 20-40%

### Data Coverage

| Source | Start | End | Rows/Dates | Notes |
|---|---|---|---|---|
| market_monitor_results | 2024-01-02 | 2026-07-24 | 642 | T2108, Net Primary, BO/BD, 5d/10d ratio |
| daily_ohlcv | 2024-12-04 | 2026-07-24 | 480 dates | ~19 dates in 2024 (limited) |
| ETF OHLCV (sub-sector) | 2024-12-04 | 2026-07-24 | 14 ETFs | Sector RS only for periods after Dec 2024 |

> [!warning] 2024 OHLCV Limitation
> daily_ohlcv has only **19 dates in 2024** (backfill was ~500 days from Jul 2026 ≈ Feb 2025). For 2024 periods, we can identify correction/bull phases from T2108 but **cannot compute 20% study, follow-through, or sector RS**. ETF sector RS is only available from Dec 4, 2024.

## Summary of All Periods

**Total periods detected: 134** (67 corrections, 67 bull trends)

| # | Type | Start | End | Days | T2108 Start | T2108 End | T2108 Min | Net Start | Net End | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 🔴 CORRECTION | 2024-01-02 | 2024-01-17 | 11 | 75.4% | 44.0% | 44.0% | +1732 | +949 | — |
| 2 | 🟢 BULL | 2024-01-17 | 2024-01-22 | 4 | 44.0% | 55.1% | 44.0% | +949 | +1286 | — |
| 3 | 🔴 CORRECTION | 2024-01-22 | 2024-01-24 | 3 | 55.1% | 49.0% | 49.0% | +1286 | +1229 | — |
| 4 | 🟢 BULL | 2024-01-24 | 2024-01-29 | 4 | 49.0% | 59.1% | 49.0% | +1229 | +1462 | — |
| 5 | 🔴 CORRECTION | 2024-01-29 | 2024-01-31 | 3 | 59.1% | 42.8% | 42.8% | +1462 | +1040 | — |
| 6 | 🟢 BULL | 2024-01-31 | 2024-02-01 | 2 | 42.8% | 48.9% | 42.8% | +1040 | +1096 | — |
| 7 | 🔴 CORRECTION | 2024-02-01 | 2024-02-05 | 3 | 48.9% | 37.4% | 37.4% | +1096 | +745 | SHALLOW |
| 8 | 🟢 BULL | 2024-02-05 | 2024-02-12 | 6 | 37.4% | 51.9% | 37.4% | +745 | +1055 | — |
| 9 | 🔴 CORRECTION | 2024-02-12 | 2024-02-13 | 2 | 51.9% | 37.1% | 37.1% | +1055 | +562 | SHALLOW |
| 10 | 🟢 BULL | 2024-02-13 | 2024-02-15 | 3 | 37.1% | 52.8% | 37.1% | +562 | +947 | — |
| 11 | 🔴 CORRECTION | 2024-02-15 | 2024-02-20 | 3 | 52.8% | 45.8% | 45.8% | +947 | +542 | — |
| 12 | 🟢 BULL | 2024-02-20 | 2024-03-13 | 17 | 45.8% | 61.3% | 45.8% | +542 | +372 | — |
| 13 | 🔴 CORRECTION | 2024-03-13 | 2024-03-14 | 2 | 61.3% | 52.8% | 52.8% | +372 | +167 | — |
| 14 | 🟢 BULL | 2024-03-14 | 2024-03-21 | 6 | 52.8% | 65.9% | 52.8% | +167 | +406 | — |
| 15 | 🔴 CORRECTION | 2024-03-21 | 2024-03-25 | 3 | 65.9% | 60.3% | 60.3% | +406 | +259 | — |
| 16 | 🟢 BULL | 2024-03-25 | 2024-03-28 | 4 | 60.3% | 68.9% | 58.5% | +259 | +459 | — |
| 17 | 🔴 CORRECTION | 2024-03-28 | 2024-04-04 | 5 | 68.9% | 53.0% | 53.0% | +459 | +283 | — |
| 18 | 🟢 BULL | 2024-04-04 | 2024-04-08 | 3 | 53.0% | 58.1% | 53.0% | +283 | +386 | — |
| 19 | 🔴 CORRECTION | 2024-04-08 | 2024-04-17 | 8 | 58.1% | 21.6% | 21.6% | +386 | -294 | SHALLOW |
| 20 | 🟢 BULL | 2024-04-17 | 2024-04-23 | 5 | 21.6% | 40.0% | 21.6% | -294 | -131 | — |
| 21 | 🔴 CORRECTION | 2024-04-23 | 2024-04-25 | 3 | 40.0% | 34.8% | 34.8% | -131 | -233 | SHALLOW |
| 22 | 🟢 BULL | 2024-04-25 | 2024-04-29 | 3 | 34.8% | 40.5% | 34.8% | -233 | -81 | — |
| 23 | 🔴 CORRECTION | 2024-04-29 | 2024-04-30 | 2 | 40.5% | 31.8% | 31.8% | -81 | -224 | SHALLOW |
| 24 | 🟢 BULL | 2024-04-30 | 2024-05-15 | 12 | 31.8% | 57.9% | 31.8% | -224 | +324 | — |
| 25 | 🔴 CORRECTION | 2024-05-15 | 2024-05-22 | 6 | 57.9% | 51.3% | 51.3% | +324 | +232 | — |
| 26 | 🟢 BULL | 2024-05-22 | 2024-05-22 | 1 | 51.3% | 51.3% | 51.3% | +232 | +232 | — |
| 27 | 🔴 CORRECTION | 2024-05-22 | 2024-05-29 | 5 | 51.3% | 36.6% | 36.6% | +232 | -14 | SHALLOW |
| 28 | 🟢 BULL | 2024-05-29 | 2024-05-31 | 3 | 36.6% | 51.4% | 36.6% | -14 | +88 | — |
| 29 | 🔴 CORRECTION | 2024-05-31 | 2024-06-04 | 3 | 51.4% | 43.4% | 43.4% | +88 | -52 | — |
| 30 | 🟢 BULL | 2024-06-04 | 2024-06-05 | 2 | 43.4% | 47.3% | 43.4% | -52 | +92 | — |
| 31 | 🔴 CORRECTION | 2024-06-05 | 2024-06-11 | 5 | 47.3% | 35.9% | 35.9% | +92 | -45 | SHALLOW |
| 32 | 🟢 BULL | 2024-06-11 | 2024-06-12 | 2 | 35.9% | 42.1% | 35.9% | -45 | +30 | — |
| 33 | 🔴 CORRECTION | 2024-06-12 | 2024-06-14 | 3 | 42.1% | 30.7% | 30.7% | +30 | -204 | SHALLOW |
| 34 | 🟢 BULL | 2024-06-14 | 2024-06-24 | 6 | 30.7% | 39.0% | 30.7% | -204 | -288 | — |
| 35 | 🔴 CORRECTION | 2024-06-24 | 2024-07-01 | 6 | 39.0% | 31.1% | 31.1% | -288 | -323 | SHALLOW |
| 36 | 🟢 BULL | 2024-07-01 | 2024-07-16 | 11 | 31.1% | 70.7% | 31.1% | -323 | +1022 | — |
| 37 | 🔴 CORRECTION | 2024-07-16 | 2024-07-18 | 3 | 70.7% | 65.0% | 65.0% | +1022 | +635 | — |
| 38 | 🟢 BULL | 2024-07-18 | 2024-07-22 | 3 | 65.0% | 66.4% | 61.1% | +635 | +711 | — |
| 39 | 🔴 CORRECTION | 2024-07-22 | 2024-07-24 | 3 | 66.4% | 57.4% | 57.4% | +711 | +502 | — |
| 40 | 🟢 BULL | 2024-07-24 | 2024-07-26 | 3 | 57.4% | 67.0% | 57.4% | +502 | +797 | — |
| 41 | 🔴 CORRECTION | 2024-07-26 | 2024-08-05 | 7 | 67.0% | 31.4% | 31.4% | +797 | -500 | SHALLOW |
| 42 | 🟢 BULL | 2024-08-05 | 2024-08-26 | 16 | 31.4% | 63.4% | 31.4% | -500 | +533 | — |
| 43 | 🔴 CORRECTION | 2024-08-26 | 2024-09-03 | 6 | 63.4% | 51.4% | 51.4% | +533 | +104 | — |
| 44 | 🟢 BULL | 2024-09-03 | 2024-09-03 | 1 | 51.4% | 51.4% | 51.4% | +104 | +104 | — |
| 45 | 🔴 CORRECTION | 2024-09-03 | 2024-09-06 | 4 | 51.4% | 37.5% | 37.5% | +104 | -174 | SHALLOW |
| 46 | 🟢 BULL | 2024-09-06 | 2024-09-19 | 10 | 37.5% | 68.8% | 37.5% | -174 | +650 | — |
| 47 | 🔴 CORRECTION | 2024-09-19 | 2024-09-20 | 2 | 68.8% | 63.4% | 63.4% | +650 | +518 | — |
| 48 | 🟢 BULL | 2024-09-20 | 2024-09-24 | 3 | 63.4% | 65.7% | 63.4% | +518 | +525 | — |
| 49 | 🔴 CORRECTION | 2024-09-24 | 2024-09-25 | 2 | 65.7% | 59.7% | 59.7% | +525 | +371 | — |
| 50 | 🟢 BULL | 2024-09-25 | 2024-09-27 | 3 | 59.7% | 66.9% | 59.7% | +371 | +560 | — |
| 51 | 🔴 CORRECTION | 2024-09-27 | 2024-10-10 | 10 | 66.9% | 48.4% | 48.4% | +560 | +100 | — |
| 52 | 🟢 BULL | 2024-10-10 | 2024-10-16 | 5 | 48.4% | 63.6% | 48.4% | +100 | +522 | — |
| 53 | 🔴 CORRECTION | 2024-10-16 | 2024-10-31 | 12 | 63.6% | 38.1% | 38.1% | +522 | +373 | SHALLOW |
| 54 | 🟢 BULL | 2024-10-31 | 2024-11-11 | 8 | 38.1% | 58.3% | 38.1% | +373 | +1054 | — |
| 55 | 🔴 CORRECTION | 2024-11-11 | 2024-11-13 | 3 | 58.3% | 52.0% | 52.0% | +1054 | +644 | — |
| 56 | 🟢 BULL | 2024-11-13 | 2024-11-29 | 12 | 52.0% | 61.8% | 47.6% | +644 | +874 | — |
| 57 | 🔴 CORRECTION | 2024-11-29 | 2024-12-05 | 5 | 61.8% | 54.8% | 54.8% | +874 | +701 | — |
| 58 | 🟢 BULL | 2024-12-05 | 2024-12-05 | 1 | 54.8% | 54.8% | 54.8% | +701 | +701 | — |
| 59 | 🔴 CORRECTION | 2024-12-05 | 2024-12-18 | 10 | 54.8% | 18.1% | 18.1% | +701 | -141 | DEEP |
| 60 | 🟢 BULL | 2024-12-18 | 2024-12-26 | 6 | 18.1% | 26.2% | 18.1% | -141 | +185 | DEEP |
| 61 | 🔴 CORRECTION | 2024-12-26 | 2024-12-30 | 3 | 26.2% | 18.7% | 18.7% | +185 | +69 | DEEP |
| 62 | 🟢 BULL | 2024-12-30 | 2025-01-21 | 14 | 18.7% | 47.8% | 18.7% | +69 | +180 | DEEP |
| 63 | 🔴 CORRECTION | 2025-01-21 | 2025-01-22 | 2 | 47.8% | 42.6% | 42.6% | +180 | +142 | — |
| 64 | 🟢 BULL | 2025-01-22 | 2025-01-30 | 7 | 42.6% | 50.6% | 42.6% | +142 | +146 | DEF_LEAD |
| 65 | 🔴 CORRECTION | 2025-01-30 | 2025-02-03 | 3 | 50.6% | 39.8% | 39.8% | +146 | -128 | SHALLOW, DEF_LEAD |
| 66 | 🟢 BULL | 2025-02-03 | 2025-02-05 | 3 | 39.8% | 50.6% | 39.8% | -128 | +197 | DEF_LEAD |
| 67 | 🔴 CORRECTION | 2025-02-05 | 2025-02-12 | 6 | 50.6% | 45.0% | 45.0% | +197 | -149 | DEF_LEAD |
| 68 | 🟢 BULL | 2025-02-12 | 2025-02-18 | 4 | 45.0% | 51.5% | 45.0% | -149 | +29 | — |
| 69 | 🔴 CORRECTION | 2025-02-18 | 2025-03-13 | 18 | 51.5% | 17.2% | 17.2% | +29 | -1286 | DEEP, DEF_LEAD |
| 70 | 🟢 BULL | 2025-03-13 | 2025-03-19 | 5 | 17.2% | 29.2% | 17.2% | -1286 | -800 | DEEP, DEF_LEAD |
| 71 | 🔴 CORRECTION | 2025-03-19 | 2025-03-21 | 3 | 29.2% | 24.1% | 24.1% | -800 | -832 | SHALLOW, DEF_LEAD |
| 72 | 🟢 BULL | 2025-03-21 | 2025-03-24 | 2 | 24.1% | 31.1% | 24.1% | -832 | -636 | DEF_LEAD |
| 73 | 🔴 CORRECTION | 2025-03-24 | 2025-03-28 | 5 | 31.1% | 24.2% | 24.2% | -636 | -1045 | SHALLOW, DEF_LEAD |
| 74 | 🟢 BULL | 2025-03-28 | 2025-04-02 | 4 | 24.2% | 30.9% | 24.2% | -1045 | -974 | DEF_LEAD |
| 75 | 🔴 CORRECTION | 2025-04-02 | 2025-04-08 | 5 | 30.9% | 4.1% | 4.1% | -974 | -2245 | DEEP, CAPIT |
| 76 | 🟢 BULL | 2025-04-08 | 2025-04-17 | 8 | 4.1% | 18.4% | 4.1% | -2245 | -1467 | DEEP, CAPIT, DEF_LEAD |
| 77 | 🔴 CORRECTION | 2025-04-17 | 2025-04-21 | 2 | 18.4% | 13.2% | 13.2% | -1467 | -1592 | DEEP, DEF_LEAD |
| 78 | 🟢 BULL | 2025-04-21 | 2025-05-02 | 10 | 13.2% | 50.0% | 13.2% | -1592 | -221 | DEEP, DEF_LEAD |
| 79 | 🔴 CORRECTION | 2025-05-02 | 2025-05-06 | 3 | 50.0% | 44.8% | 44.8% | -221 | -499 | — |
| 80 | 🟢 BULL | 2025-05-06 | 2025-05-19 | 10 | 44.8% | 67.3% | 44.8% | -499 | +697 | — |
| 81 | 🔴 CORRECTION | 2025-05-19 | 2025-05-21 | 3 | 67.3% | 55.1% | 55.1% | +697 | +367 | — |
| 82 | 🟢 BULL | 2025-05-21 | 2025-06-10 | 14 | 55.1% | 69.0% | 53.3% | +367 | +1424 | — |
| 83 | 🔴 CORRECTION | 2025-06-10 | 2025-06-20 | 8 | 69.0% | 50.6% | 50.6% | +1424 | +1042 | — |
| 84 | 🟢 BULL | 2025-06-20 | 2025-06-24 | 3 | 50.6% | 61.2% | 50.6% | +1042 | +1229 | — |
| 85 | 🔴 CORRECTION | 2025-06-24 | 2025-06-25 | 2 | 61.2% | 53.5% | 53.5% | +1229 | +1115 | — |
| 86 | 🟢 BULL | 2025-06-25 | 2025-07-03 | 7 | 53.5% | 69.3% | 53.5% | +1115 | +1740 | — |
| 87 | 🔴 CORRECTION | 2025-07-03 | 2025-07-07 | 2 | 69.3% | 62.8% | 62.8% | +1740 | +1566 | — |
| 88 | 🟢 BULL | 2025-07-07 | 2025-07-10 | 4 | 62.8% | 66.9% | 62.8% | +1566 | +1903 | — |
| 89 | 🔴 CORRECTION | 2025-07-10 | 2025-07-15 | 4 | 66.9% | 53.4% | 53.4% | +1903 | +1332 | — |
| 90 | 🟢 BULL | 2025-07-15 | 2025-07-23 | 7 | 53.4% | 67.6% | 53.4% | +1332 | +1677 | — |
| 91 | 🔴 CORRECTION | 2025-07-23 | 2025-07-28 | 4 | 67.6% | 59.5% | 59.5% | +1677 | +1201 | — |
| 92 | 🟢 BULL | 2025-07-28 | 2025-07-28 | 1 | 59.5% | 59.5% | 59.5% | +1201 | +1201 | — |
| 93 | 🔴 CORRECTION | 2025-07-28 | 2025-08-01 | 5 | 59.5% | 37.0% | 37.0% | +1201 | +474 | SHALLOW |
| 94 | 🟢 BULL | 2025-08-01 | 2025-08-13 | 9 | 37.0% | 57.7% | 37.0% | +474 | +747 | — |
| 95 | 🔴 CORRECTION | 2025-08-13 | 2025-08-15 | 3 | 57.7% | 50.0% | 50.0% | +747 | +641 | — |
| 96 | 🟢 BULL | 2025-08-15 | 2025-08-22 | 6 | 50.0% | 62.8% | 49.5% | +641 | +861 | — |
| 97 | 🔴 CORRECTION | 2025-08-22 | 2025-09-02 | 7 | 62.8% | 56.7% | 56.7% | +861 | +692 | DEF_LEAD |
| 98 | 🟢 BULL | 2025-09-02 | 2025-09-11 | 8 | 56.7% | 63.2% | 55.9% | +692 | +881 | — |
| 99 | 🔴 CORRECTION | 2025-09-11 | 2025-09-17 | 5 | 63.2% | 54.3% | 54.3% | +881 | +763 | DEF_LEAD |
| 100 | 🟢 BULL | 2025-09-17 | 2025-09-18 | 2 | 54.3% | 59.8% | 54.3% | +763 | +1029 | — |
| 101 | 🔴 CORRECTION | 2025-09-18 | 2025-10-10 | 17 | 59.8% | 25.5% | 25.5% | +1029 | +387 | SHALLOW |
| 102 | 🟢 BULL | 2025-10-10 | 2025-10-14 | 3 | 25.5% | 35.6% | 25.5% | +387 | +708 | DEF_LEAD |
| 103 | 🔴 CORRECTION | 2025-10-14 | 2025-10-16 | 3 | 35.6% | 29.4% | 29.4% | +708 | +525 | SHALLOW, DEF_LEAD |
| 104 | 🟢 BULL | 2025-10-16 | 2025-10-27 | 8 | 29.4% | 43.0% | 29.4% | +525 | +643 | DEF_LEAD |
| 105 | 🔴 CORRECTION | 2025-10-27 | 2025-11-04 | 7 | 43.0% | 27.7% | 27.7% | +643 | -94 | SHALLOW, DEF_LEAD |
| 106 | 🟢 BULL | 2025-11-04 | 2025-11-12 | 7 | 27.7% | 42.6% | 27.7% | -94 | -65 | — |
| 107 | 🔴 CORRECTION | 2025-11-12 | 2025-11-13 | 2 | 42.6% | 37.2% | 37.2% | -65 | -278 | SHALLOW, DEF_LEAD |
| 108 | 🟢 BULL | 2025-11-13 | 2025-11-13 | 1 | 37.2% | 37.2% | 37.2% | -278 | -278 | DEF_LEAD |
| 109 | 🔴 CORRECTION | 2025-11-13 | 2025-11-20 | 6 | 37.2% | 25.4% | 25.4% | -278 | -751 | SHALLOW, DEF_LEAD |
| 110 | 🟢 BULL | 2025-11-20 | 2025-12-03 | 9 | 25.4% | 53.4% | 25.4% | -751 | +65 | DEF_LEAD |
| 111 | 🔴 CORRECTION | 2025-12-03 | 2025-12-08 | 4 | 53.4% | 47.3% | 47.3% | +65 | +76 | DEF_LEAD |
| 112 | 🟢 BULL | 2025-12-08 | 2025-12-11 | 4 | 47.3% | 57.2% | 47.3% | +76 | +411 | DEF_LEAD |
| 113 | 🔴 CORRECTION | 2025-12-11 | 2025-12-31 | 14 | 57.2% | 46.3% | 46.3% | +411 | -81 | — |
| 114 | 🟢 BULL | 2025-12-31 | 2026-01-15 | 11 | 46.3% | 66.9% | 46.3% | -81 | +676 | — |
| 115 | 🔴 CORRECTION | 2026-01-15 | 2026-01-20 | 3 | 66.9% | 58.6% | 58.6% | +676 | +425 | — |
| 116 | 🟢 BULL | 2026-01-20 | 2026-01-22 | 3 | 58.6% | 64.9% | 58.6% | +425 | +769 | — |
| 117 | 🔴 CORRECTION | 2026-01-22 | 2026-02-05 | 11 | 64.9% | 53.5% | 53.5% | +769 | -53 | DEF_LEAD |
| 118 | 🟢 BULL | 2026-02-05 | 2026-02-10 | 4 | 53.5% | 61.6% | 53.5% | -53 | +390 | — |
| 119 | 🔴 CORRECTION | 2026-02-10 | 2026-03-20 | 28 | 61.6% | 16.7% | 16.7% | +390 | -743 | DEEP |
| 120 | 🟢 BULL | 2026-03-20 | 2026-03-25 | 4 | 16.7% | 24.5% | 16.7% | -743 | -397 | DEEP |
| 121 | 🔴 CORRECTION | 2026-03-25 | 2026-03-27 | 3 | 24.5% | 19.2% | 19.2% | -397 | -778 | DEEP |
| 122 | 🟢 BULL | 2026-03-27 | 2026-04-20 | 16 | 19.2% | 63.0% | 19.2% | -778 | +718 | DEEP |
| 123 | 🔴 CORRECTION | 2026-04-20 | 2026-04-29 | 8 | 63.0% | 54.9% | 54.9% | +718 | +215 | — |
| 124 | 🟢 BULL | 2026-04-29 | 2026-05-06 | 6 | 54.9% | 60.6% | 54.9% | +215 | +782 | — |
| 125 | 🔴 CORRECTION | 2026-05-06 | 2026-05-19 | 10 | 60.6% | 38.9% | 38.9% | +782 | +73 | SHALLOW |
| 126 | 🟢 BULL | 2026-05-19 | 2026-05-20 | 2 | 38.9% | 53.0% | 38.9% | +73 | +43 | — |
| 127 | 🔴 CORRECTION | 2026-05-20 | 2026-05-21 | 2 | 53.0% | 46.5% | 46.5% | +43 | +399 | — |
| 128 | 🟢 BULL | 2026-05-21 | 2026-05-26 | 3 | 46.5% | 50.1% | 46.5% | +399 | +590 | — |
| 129 | 🔴 CORRECTION | 2026-05-26 | 2026-06-03 | 7 | 50.1% | 39.3% | 39.3% | +590 | +502 | SHALLOW, DEF_LEAD |
| 130 | 🟢 BULL | 2026-06-03 | 2026-06-12 | 8 | 39.3% | 50.2% | 39.3% | +502 | +535 | — |
| 131 | 🔴 CORRECTION | 2026-06-12 | 2026-06-17 | 4 | 50.2% | 42.9% | 42.9% | +535 | +452 | DEF_LEAD |
| 132 | 🟢 BULL | 2026-06-17 | 2026-07-16 | 20 | 42.9% | 56.6% | 42.9% | +452 | +143 | DEF_LEAD |
| 133 | 🔴 CORRECTION | 2026-07-16 | 2026-07-20 | 3 | 56.6% | 49.4% | 49.4% | +143 | -55 | DEF_LEAD |
| 134 | 🟢 BULL | 2026-07-20 | 2026-07-24 | 5 | 49.4% | 51.0% | 47.2% | -55 | -199 | DEF_LEAD |

## Aggregate Statistics

| Metric | Corrections | Bull Trends |
|---|---|---|
| Count | 67 | 67 |
| Avg duration (days) | 5.5 | 6.1 |
| Duration range | 2–28 | 1–20 |
| T2108 range | min 4.1% – max 65.0% | min 4.1% – max 70.7% |
| Deep corrections (T2108<20%) | 7 | — |
| Capitulation events (T2108<10%) | 1 | — |
| Shallow corrections (T2108 20-40%) | 23 | — |

## 🚨 Capitulation Events (T2108 < 10%)

- **2025-04-02 to 2025-04-08** — T2108 troughed at **4.1%** (Net Primary -2245)
- **2025-04-08 to 2025-04-17** — T2108 troughed at **4.1%** (Net Primary -2245)

## 🔴 Deep Corrections (T2108 < 20%, non-capitulation)

- **2024-12-05 to 2024-12-18** — T2108 troughed at **18.1%** (Net Primary -141)
- **2024-12-18 to 2024-12-26** — T2108 troughed at **18.1%** (Net Primary -193)
- **2024-12-26 to 2024-12-30** — T2108 troughed at **18.7%** (Net Primary +69)
- **2024-12-30 to 2025-01-21** — T2108 troughed at **18.7%** (Net Primary -197)
- **2025-02-18 to 2025-03-13** — T2108 troughed at **17.2%** (Net Primary -1289)
- **2025-03-13 to 2025-03-19** — T2108 troughed at **17.2%** (Net Primary -1286)
- **2025-04-17 to 2025-04-21** — T2108 troughed at **13.2%** (Net Primary -1592)
- **2025-04-21 to 2025-05-02** — T2108 troughed at **13.2%** (Net Primary -1592)
- **2026-02-10 to 2026-03-20** — T2108 troughed at **16.7%** (Net Primary -743)
- **2026-03-20 to 2026-03-25** — T2108 troughed at **16.7%** (Net Primary -743)
- **2026-03-25 to 2026-03-27** — T2108 troughed at **19.2%** (Net Primary -778)
- **2026-03-27 to 2026-04-20** — T2108 troughed at **19.2%** (Net Primary -880)

## Did 5d Ratio ≥ 2.0 Precede Recoveries?

For each bull trend, checked the 5 trading days **before** the bull trend started for 5d ratio ≥ 2.0 (aggressive buying).

| Bull # | Start | Pre-5d Max 5d Ratio | Pre-5d Days ≥ 2.0 | Verdict |
|---|---|---|---|---|
| 1 | 2024-01-17 | 1.44 | 0 | ❌ No |
| 2 | 2024-01-24 | 1.33 | 0 | ❌ No |
| 3 | 2024-01-31 | 2.14 | 1 | ✅ Yes |
| 4 | 2024-02-05 | 2.14 | 1 | ✅ Yes |
| 5 | 2024-02-13 | 2.57 | 1 | ✅ Yes |
| 6 | 2024-02-20 | 2.57 | 1 | ✅ Yes |
| 7 | 2024-03-14 | 1.44 | 0 | ❌ No |
| 8 | 2024-03-25 | 2.22 | 1 | ✅ Yes |
| 9 | 2024-04-04 | 1.65 | 0 | ❌ No |
| 10 | 2024-04-17 | 0.75 | 0 | ❌ No |
| 11 | 2024-04-25 | 1.35 | 0 | ❌ No |
| 12 | 2024-04-30 | 1.76 | 0 | ❌ No |
| 13 | 2024-05-22 | 2.03 | 1 | ✅ Yes |
| 14 | 2024-05-29 | 1.43 | 0 | ❌ No |
| 15 | 2024-06-04 | 1.37 | 0 | ❌ No |
| 16 | 2024-06-11 | 1.27 | 0 | ❌ No |
| 17 | 2024-06-14 | 1.20 | 0 | ❌ No |
| 18 | 2024-07-01 | 1.31 | 0 | ❌ No |
| 19 | 2024-07-18 | 7.36 | 5 | ✅ Yes |
| 20 | 2024-07-24 | 4.75 | 2 | ✅ Yes |
| 21 | 2024-08-05 | 1.52 | 0 | ❌ No |
| 22 | 2024-09-03 | 2.65 | 2 | ✅ Yes |
| 23 | 2024-09-06 | 1.78 | 0 | ❌ No |
| 24 | 2024-09-20 | 2.74 | 5 | ✅ Yes |
| 25 | 2024-09-25 | 2.54 | 2 | ✅ Yes |
| 26 | 2024-10-10 | 1.35 | 0 | ❌ No |
| 27 | 2024-10-31 | 1.62 | 0 | ❌ No |
| 28 | 2024-11-13 | 3.06 | 5 | ✅ Yes |
| 29 | 2024-12-05 | 3.12 | 3 | ✅ Yes |
| 30 | 2024-12-18 | 1.21 | 0 | ❌ No |
| 31 | 2024-12-30 | 3.09 | 2 | ✅ Yes |
| 32 | 2025-01-22 | 2.18 | 1 | ✅ Yes |
| 33 | 2025-02-03 | 1.11 | 0 | ❌ No |
| 34 | 2025-02-12 | 1.34 | 0 | ❌ No |
| 35 | 2025-03-13 | 0.59 | 0 | ❌ No |
| 36 | 2025-03-21 | 2.25 | 1 | ✅ Yes |
| 37 | 2025-03-28 | 1.52 | 0 | ❌ No |
| 38 | 2025-04-08 | 0.49 | 0 | ❌ No |
| 39 | 2025-04-21 | 6.42 | 4 | ✅ Yes |
| 40 | 2025-05-06 | 3.08 | 1 | ✅ Yes |
| 41 | 2025-05-21 | 2.76 | 3 | ✅ Yes |
| 42 | 2025-06-20 | 2.11 | 1 | ✅ Yes |
| 43 | 2025-06-25 | 1.23 | 0 | ❌ No |
| 44 | 2025-07-07 | 2.05 | 1 | ✅ Yes |
| 45 | 2025-07-15 | 2.17 | 3 | ✅ Yes |
| 46 | 2025-07-28 | 3.28 | 4 | ✅ Yes |
| 47 | 2025-08-01 | 2.23 | 1 | ✅ Yes |
| 48 | 2025-08-15 | 2.16 | 1 | ✅ Yes |
| 49 | 2025-09-02 | 5.04 | 4 | ✅ Yes |
| 50 | 2025-09-17 | 2.48 | 4 | ✅ Yes |
| 51 | 2025-10-10 | 2.26 | 3 | ✅ Yes |
| 52 | 2025-10-16 | 1.87 | 0 | ❌ No |
| 53 | 2025-11-04 | 1.27 | 0 | ❌ No |
| 54 | 2025-11-13 | 1.12 | 0 | ❌ No |
| 55 | 2025-11-20 | 0.90 | 0 | ❌ No |
| 56 | 2025-12-08 | 1.70 | 0 | ❌ No |
| 57 | 2025-12-31 | 1.56 | 0 | ❌ No |
| 58 | 2026-01-20 | 2.22 | 1 | ✅ Yes |
| 59 | 2026-02-05 | 0.71 | 0 | ❌ No |
| 60 | 2026-03-20 | 0.79 | 0 | ❌ No |
| 61 | 2026-03-27 | 0.79 | 0 | ❌ No |
| 62 | 2026-04-29 | 1.92 | 0 | ❌ No |
| 63 | 2026-05-19 | 1.16 | 0 | ❌ No |
| 64 | 2026-05-21 | 1.06 | 0 | ❌ No |
| 65 | 2026-06-03 | 2.94 | 4 | ✅ Yes |
| 66 | 2026-06-17 | 1.68 | 0 | ❌ No |
| 67 | 2026-07-20 | 0.93 | 0 | ❌ No |

## Did Defensive Sector Leading Precede Corrections?

For each period, checked the 30 calendar days **before** the period started. Compared equal-weight returns of defensive ETFs (XLP, XLU, XLV) vs cyclical ETFs (XLY, XLF, XLI, XLE, XLK, XLB, XLC). Only available for periods starting after 2024-12-04.

| # | Type | Start | Defensive Ret | Cyclical Ret | Leading |
|---|---|---|---|---|---|
| 1 | correction | 2024-01-02 | — | — | No ETF data |
| 2 | bull | 2024-01-17 | — | — | No ETF data |
| 3 | correction | 2024-01-22 | — | — | No ETF data |
| 4 | bull | 2024-01-24 | — | — | No ETF data |
| 5 | correction | 2024-01-29 | — | — | No ETF data |
| 6 | bull | 2024-01-31 | — | — | No ETF data |
| 7 | correction | 2024-02-01 | — | — | No ETF data |
| 8 | bull | 2024-02-05 | — | — | No ETF data |
| 9 | correction | 2024-02-12 | — | — | No ETF data |
| 10 | bull | 2024-02-13 | — | — | No ETF data |
| 11 | correction | 2024-02-15 | — | — | No ETF data |
| 12 | bull | 2024-02-20 | — | — | No ETF data |
| 13 | correction | 2024-03-13 | — | — | No ETF data |
| 14 | bull | 2024-03-14 | — | — | No ETF data |
| 15 | correction | 2024-03-21 | — | — | No ETF data |
| 16 | bull | 2024-03-25 | — | — | No ETF data |
| 17 | correction | 2024-03-28 | — | — | No ETF data |
| 18 | bull | 2024-04-04 | — | — | No ETF data |
| 19 | correction | 2024-04-08 | — | — | No ETF data |
| 20 | bull | 2024-04-17 | — | — | No ETF data |
| 21 | correction | 2024-04-23 | — | — | No ETF data |
| 22 | bull | 2024-04-25 | — | — | No ETF data |
| 23 | correction | 2024-04-29 | — | — | No ETF data |
| 24 | bull | 2024-04-30 | — | — | No ETF data |
| 25 | correction | 2024-05-15 | — | — | No ETF data |
| 26 | bull | 2024-05-22 | — | — | No ETF data |
| 27 | correction | 2024-05-22 | — | — | No ETF data |
| 28 | bull | 2024-05-29 | — | — | No ETF data |
| 29 | correction | 2024-05-31 | — | — | No ETF data |
| 30 | bull | 2024-06-04 | — | — | No ETF data |
| 31 | correction | 2024-06-05 | — | — | No ETF data |
| 32 | bull | 2024-06-11 | — | — | No ETF data |
| 33 | correction | 2024-06-12 | — | — | No ETF data |
| 34 | bull | 2024-06-14 | — | — | No ETF data |
| 35 | correction | 2024-06-24 | — | — | No ETF data |
| 36 | bull | 2024-07-01 | — | — | No ETF data |
| 37 | correction | 2024-07-16 | — | — | No ETF data |
| 38 | bull | 2024-07-18 | — | — | No ETF data |
| 39 | correction | 2024-07-22 | — | — | No ETF data |
| 40 | bull | 2024-07-24 | — | — | No ETF data |
| 41 | correction | 2024-07-26 | — | — | No ETF data |
| 42 | bull | 2024-08-05 | — | — | No ETF data |
| 43 | correction | 2024-08-26 | — | — | No ETF data |
| 44 | bull | 2024-09-03 | — | — | No ETF data |
| 45 | correction | 2024-09-03 | — | — | No ETF data |
| 46 | bull | 2024-09-06 | — | — | No ETF data |
| 47 | correction | 2024-09-19 | — | — | No ETF data |
| 48 | bull | 2024-09-20 | — | — | No ETF data |
| 49 | correction | 2024-09-24 | — | — | No ETF data |
| 50 | bull | 2024-09-25 | — | — | No ETF data |
| 51 | correction | 2024-09-27 | — | — | No ETF data |
| 52 | bull | 2024-10-10 | — | — | No ETF data |
| 53 | correction | 2024-10-16 | — | — | No ETF data |
| 54 | bull | 2024-10-31 | — | — | No ETF data |
| 55 | correction | 2024-11-11 | — | — | No ETF data |
| 56 | bull | 2024-11-13 | — | — | No ETF data |
| 57 | correction | 2024-11-29 | — | — | No ETF data |
| 58 | bull | 2024-12-05 | — | — | No ETF data |
| 59 | correction | 2024-12-05 | — | — | No ETF data |
| 60 | bull | 2024-12-18 | — | — | No ETF data |
| 61 | correction | 2024-12-26 | — | — | No ETF data |
| 62 | bull | 2024-12-30 | — | — | No ETF data |
| 63 | correction | 2025-01-21 | +1.6% | +1.7% | 🔄 Cyclical |
| 64 | bull | 2025-01-22 | +3.3% | +2.8% | 🛡️ Defensive |
| 65 | correction | 2025-01-30 | +4.9% | +3.6% | 🛡️ Defensive |
| 66 | bull | 2025-02-03 | +4.9% | +2.3% | 🛡️ Defensive |
| 67 | correction | 2025-02-05 | +4.9% | +2.5% | 🛡️ Defensive |
| 68 | bull | 2025-02-12 | +3.9% | +4.3% | 🔄 Cyclical |
| 69 | correction | 2025-02-18 | +1.0% | +0.6% | 🛡️ Defensive |
| 70 | bull | 2025-03-13 | -1.4% | -7.9% | 🛡️ Defensive |
| 71 | correction | 2025-03-19 | +0.9% | -8.4% | 🛡️ Defensive |
| 72 | bull | 2025-03-21 | +0.1% | -7.5% | 🛡️ Defensive |
| 73 | correction | 2025-03-24 | -0.8% | -4.7% | 🛡️ Defensive |
| 74 | bull | 2025-03-28 | -2.2% | -3.4% | 🛡️ Defensive |
| 75 | correction | 2025-04-02 | -3.4% | -3.0% | 🔄 Cyclical |
| 76 | bull | 2025-04-08 | -8.3% | -10.6% | 🛡️ Defensive |
| 77 | correction | 2025-04-17 | -6.1% | -6.9% | 🛡️ Defensive |
| 78 | bull | 2025-04-21 | -6.4% | -8.8% | 🛡️ Defensive |
| 79 | correction | 2025-05-02 | -4.2% | -2.1% | 🔄 Cyclical |
| 80 | bull | 2025-05-06 | +3.9% | +12.4% | 🔄 Cyclical |
| 81 | correction | 2025-05-19 | +2.1% | +17.3% | 🔄 Cyclical |
| 82 | bull | 2025-05-21 | +3.3% | +16.7% | 🔄 Cyclical |
| 83 | correction | 2025-06-10 | -0.8% | +2.7% | 🔄 Cyclical |
| 84 | bull | 2025-06-20 | +0.8% | +2.1% | 🔄 Cyclical |
| 85 | correction | 2025-06-24 | -0.1% | +1.3% | 🔄 Cyclical |
| 86 | bull | 2025-06-25 | +0.9% | +2.3% | 🔄 Cyclical |
| 87 | correction | 2025-07-03 | +1.0% | +4.3% | 🔄 Cyclical |
| 88 | bull | 2025-07-07 | +1.1% | +4.4% | 🔄 Cyclical |
| 89 | correction | 2025-07-10 | +0.2% | +3.6% | 🔄 Cyclical |
| 90 | bull | 2025-07-15 | +0.1% | +3.9% | 🔄 Cyclical |
| 91 | correction | 2025-07-23 | +1.9% | +4.7% | 🔄 Cyclical |
| 92 | bull | 2025-07-28 | +1.8% | +3.0% | 🔄 Cyclical |
| 93 | correction | 2025-07-28 | +1.8% | +3.0% | 🔄 Cyclical |
| 94 | bull | 2025-08-01 | -1.5% | +1.1% | 🔄 Cyclical |
| 95 | correction | 2025-08-13 | -1.2% | +1.6% | 🔄 Cyclical |
| 96 | bull | 2025-08-15 | +0.9% | +2.6% | 🔄 Cyclical |
| 97 | correction | 2025-08-22 | +0.8% | -0.6% | 🛡️ Defensive |
| 98 | bull | 2025-09-02 | +1.7% | +2.7% | 🔄 Cyclical |
| 99 | correction | 2025-09-11 | +3.0% | +1.8% | 🛡️ Defensive |
| 100 | bull | 2025-09-17 | +0.3% | +3.3% | 🔄 Cyclical |
| 101 | correction | 2025-09-18 | -0.2% | +3.6% | 🔄 Cyclical |
| 102 | bull | 2025-10-10 | +5.5% | +1.8% | 🛡️ Defensive |
| 103 | correction | 2025-10-14 | +4.2% | -1.0% | 🛡️ Defensive |
| 104 | bull | 2025-10-16 | +5.6% | -0.5% | 🛡️ Defensive |
| 105 | correction | 2025-10-27 | +6.9% | +0.3% | 🛡️ Defensive |
| 106 | bull | 2025-11-04 | +0.0% | +0.0% | 🔄 Cyclical |
| 107 | correction | 2025-11-12 | +4.3% | +1.9% | 🛡️ Defensive |
| 108 | bull | 2025-11-13 | +5.1% | +1.5% | 🛡️ Defensive |
| 109 | correction | 2025-11-13 | +5.1% | +1.5% | 🛡️ Defensive |
| 110 | bull | 2025-11-20 | +3.2% | -3.3% | 🛡️ Defensive |
| 111 | correction | 2025-12-03 | +4.9% | -0.9% | 🛡️ Defensive |
| 112 | bull | 2025-12-08 | +2.3% | +0.8% | 🛡️ Defensive |
| 113 | correction | 2025-12-11 | -0.3% | +1.2% | 🔄 Cyclical |
| 114 | bull | 2025-12-31 | -0.5% | +2.3% | 🔄 Cyclical |
| 115 | correction | 2026-01-15 | +2.0% | +2.7% | 🔄 Cyclical |
| 116 | bull | 2026-01-20 | +0.7% | +2.1% | 🔄 Cyclical |
| 117 | correction | 2026-01-22 | +1.9% | +1.4% | 🛡️ Defensive |
| 118 | bull | 2026-02-05 | -0.9% | +0.9% | 🔄 Cyclical |
| 119 | correction | 2026-02-10 | -0.1% | +1.3% | 🔄 Cyclical |
| 120 | bull | 2026-03-20 | -5.0% | -3.7% | 🔄 Cyclical |
| 121 | correction | 2026-03-25 | -7.5% | -3.3% | 🔄 Cyclical |
| 122 | bull | 2026-03-27 | -6.9% | -5.7% | 🔄 Cyclical |
| 123 | correction | 2026-04-20 | +2.9% | +7.0% | 🔄 Cyclical |
| 124 | bull | 2026-04-29 | +0.2% | +10.0% | 🔄 Cyclical |
| 125 | correction | 2026-05-06 | -0.4% | +7.7% | 🔄 Cyclical |
| 126 | bull | 2026-05-19 | -1.8% | +1.9% | 🔄 Cyclical |
| 127 | correction | 2026-05-20 | -0.8% | +1.0% | 🔄 Cyclical |
| 128 | bull | 2026-05-21 | +0.4% | +2.9% | 🔄 Cyclical |
| 129 | correction | 2026-05-26 | +2.9% | +2.9% | 🛡️ Defensive |
| 130 | bull | 2026-06-03 | -0.4% | +4.9% | 🔄 Cyclical |
| 131 | correction | 2026-06-12 | +3.5% | +0.1% | 🛡️ Defensive |
| 132 | bull | 2026-06-17 | +4.4% | +2.5% | 🛡️ Defensive |
| 133 | correction | 2026-07-16 | +2.8% | -0.5% | 🛡️ Defensive |
| 134 | bull | 2026-07-20 | +5.9% | -1.3% | 🛡️ Defensive |

## Detailed Period Breakdown

### Period 1: CORRECTION — 2024-01-02 to 2024-01-17

**T2108: 75.4% → 44.0%** (drop of 31.4 points; min 44.0%)
**Net Primary: +1732 → +949** (range +949 to +1732, trend: deteriorating)
**Duration: 11 trading days**

| Metric | Value |
|---|---|
| T2108 min | 44.0% |
| T2108 max | 75.4% |
| T2108 avg | 63.0% |
| 5d ratio min | 0.48 |
| 5d ratio max | 1.47 |
| 5d ratio avg | 0.91 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.01 |
| Classification | Normal |

### Period 2: BULL — 2024-01-17 to 2024-01-22

**T2108: 44.0% → 55.1%** (rise of 11.1 points; max 55.1%)
**Net Primary: +949 → +1286** (range +949 to +1286, trend: improving)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 44.0% |
| T2108 max | 55.1% |
| T2108 avg | 48.6% |
| 5d ratio min | 0.45 |
| 5d ratio max | 0.86 |
| 5d ratio avg | 0.59 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.56 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.44 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 3: CORRECTION — 2024-01-22 to 2024-01-24

**T2108: 55.1% → 49.0%** (drop of 6.1 points; min 49.0%)
**Net Primary: +1286 → +1229** (range +1229 to +1286, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 49.0% |
| T2108 max | 55.1% |
| T2108 avg | 52.5% |
| 5d ratio min | 0.86 |
| 5d ratio max | 1.46 |
| 5d ratio avg | 1.22 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.21 |
| Classification | Normal |

### Period 4: BULL — 2024-01-24 to 2024-01-29

**T2108: 49.0% → 59.1%** (rise of 10.2 points; max 59.1%)
**Net Primary: +1229 → +1462** (range +1229 to +1462, trend: improving)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 49.0% |
| T2108 max | 59.1% |
| T2108 avg | 54.5% |
| 5d ratio min | 1.46 |
| 5d ratio max | 2.14 |
| 5d ratio avg | 1.83 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.76 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.33 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 5: CORRECTION — 2024-01-29 to 2024-01-31

**T2108: 59.1% → 42.8%** (drop of 16.4 points; min 42.8%)
**Net Primary: +1462 → +1040** (range +1040 to +1462, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 42.8% |
| T2108 max | 59.1% |
| T2108 avg | 52.3% |
| 5d ratio min | 1.18 |
| 5d ratio max | 2.14 |
| 5d ratio avg | 1.65 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.24 |
| Classification | Normal |

### Period 6: BULL — 2024-01-31 to 2024-02-01

**T2108: 42.8% → 48.9%** (rise of 6.1 points; max 48.9%)
**Net Primary: +1040 → +1096** (range +1040 to +1096, trend: improving)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 42.8% |
| T2108 max | 48.9% |
| T2108 avg | 45.8% |
| 5d ratio min | 1.18 |
| 5d ratio max | 1.23 |
| 5d ratio avg | 1.21 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.12 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.14 |
| Pre-period days 5d ≥ 2.0 | 1 |

### Period 7: CORRECTION — 2024-02-01 to 2024-02-05

**T2108: 48.9% → 37.4%** (drop of 11.5 points; min 37.4%)
**Net Primary: +1096 → +745** (range +745 to +1096, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 37.4% |
| T2108 max | 48.9% |
| T2108 avg | 43.5% |
| 5d ratio min | 0.58 |
| 5d ratio max | 1.23 |
| 5d ratio avg | 0.95 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.00 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |

### Period 8: BULL — 2024-02-05 to 2024-02-12

**T2108: 37.4% → 51.9%** (rise of 14.5 points; max 51.9%)
**Net Primary: +745 → +1055** (range +628 to +1055, trend: improving)
**Duration: 6 trading days**

| Metric | Value |
|---|---|
| T2108 min | 37.4% |
| T2108 max | 51.9% |
| T2108 avg | 42.7% |
| 5d ratio min | 0.58 |
| 5d ratio max | 2.57 |
| 5d ratio avg | 1.27 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.54 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.14 |
| Pre-period days 5d ≥ 2.0 | 1 |

### Period 9: CORRECTION — 2024-02-12 to 2024-02-13

**T2108: 51.9% → 37.1%** (drop of 14.8 points; min 37.1%)
**Net Primary: +1055 → +562** (range +562 to +1055, trend: deteriorating)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 37.1% |
| T2108 max | 51.9% |
| T2108 avg | 44.5% |
| 5d ratio min | 0.94 |
| 5d ratio max | 2.57 |
| 5d ratio avg | 1.75 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.39 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |

### Period 10: BULL — 2024-02-13 to 2024-02-15

**T2108: 37.1% → 52.8%** (rise of 15.7 points; max 52.8%)
**Net Primary: +562 → +947** (range +562 to +947, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 37.1% |
| T2108 max | 52.8% |
| T2108 avg | 44.5% |
| 5d ratio min | 0.94 |
| 5d ratio max | 1.41 |
| 5d ratio avg | 1.19 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 3.76 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.57 |
| Pre-period days 5d ≥ 2.0 | 1 |

### Period 11: CORRECTION — 2024-02-15 to 2024-02-20

**T2108: 52.8% → 45.8%** (drop of 7.0 points; min 45.8%)
**Net Primary: +947 → +542** (range +542 to +947, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 45.8% |
| T2108 max | 52.8% |
| T2108 avg | 49.3% |
| 5d ratio min | 0.90 |
| 5d ratio max | 1.41 |
| 5d ratio avg | 1.19 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.57 |
| Classification | Normal |

### Period 12: BULL — 2024-02-20 to 2024-03-13

**T2108: 45.8% → 61.3%** (rise of 15.5 points; max 61.3%)
**Net Primary: +542 → +372** (range +372 to +691, trend: deteriorating)
**Duration: 17 trading days**

| Metric | Value |
|---|---|
| T2108 min | 45.8% |
| T2108 max | 61.3% |
| T2108 avg | 53.5% |
| 5d ratio min | 0.86 |
| 5d ratio max | 2.16 |
| 5d ratio avg | 1.38 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.55 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.57 |
| Pre-period days 5d ≥ 2.0 | 1 |

### Period 13: CORRECTION — 2024-03-13 to 2024-03-14

**T2108: 61.3% → 52.8%** (drop of 8.5 points; min 52.8%)
**Net Primary: +372 → +167** (range +167 to +372, trend: deteriorating)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 52.8% |
| T2108 max | 61.3% |
| T2108 avg | 57.0% |
| 5d ratio min | 0.63 |
| 5d ratio max | 1.12 |
| 5d ratio avg | 0.88 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 0.71 |
| Classification | Normal |

### Period 14: BULL — 2024-03-14 to 2024-03-21

**T2108: 52.8% → 65.9%** (rise of 13.1 points; max 65.9%)
**Net Primary: +167 → +406** (range +141 to +406, trend: improving)
**Duration: 6 trading days**

| Metric | Value |
|---|---|
| T2108 min | 52.8% |
| T2108 max | 65.9% |
| T2108 avg | 57.5% |
| 5d ratio min | 0.63 |
| 5d ratio max | 2.22 |
| 5d ratio avg | 1.08 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.14 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.44 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 15: CORRECTION — 2024-03-21 to 2024-03-25

**T2108: 65.9% → 60.3%** (drop of 5.6 points; min 60.3%)
**Net Primary: +406 → +259** (range +259 to +406, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 60.3% |
| T2108 max | 65.9% |
| T2108 avg | 62.5% |
| 5d ratio min | 1.78 |
| 5d ratio max | 2.22 |
| 5d ratio avg | 1.97 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.27 |
| Classification | Normal |

### Period 16: BULL — 2024-03-25 to 2024-03-28

**T2108: 60.3% → 68.9%** (rise of 8.6 points; max 68.9%)
**Net Primary: +259 → +459** (range +207 to +459, trend: improving)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 58.5% |
| T2108 max | 68.9% |
| T2108 avg | 63.7% |
| 5d ratio min | 1.57 |
| 5d ratio max | 1.78 |
| 5d ratio avg | 1.65 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.65 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.22 |
| Pre-period days 5d ≥ 2.0 | 1 |

### Period 17: CORRECTION — 2024-03-28 to 2024-04-04

**T2108: 68.9% → 53.0%** (drop of 15.9 points; min 53.0%)
**Net Primary: +459 → +283** (range +270 to +459, trend: deteriorating)
**Duration: 5 trading days**

| Metric | Value |
|---|---|
| T2108 min | 53.0% |
| T2108 max | 68.9% |
| T2108 avg | 60.3% |
| 5d ratio min | 0.97 |
| 5d ratio max | 1.65 |
| 5d ratio avg | 1.41 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.17 |
| Classification | Normal |

### Period 18: BULL — 2024-04-04 to 2024-04-08

**T2108: 53.0% → 58.1%** (rise of 5.1 points; max 58.1%)
**Net Primary: +283 → +386** (range +283 to +386, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 53.0% |
| T2108 max | 58.1% |
| T2108 avg | 55.2% |
| 5d ratio min | 0.87 |
| 5d ratio max | 0.97 |
| 5d ratio avg | 0.94 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.32 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.65 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 19: CORRECTION — 2024-04-08 to 2024-04-17

**T2108: 58.1% → 21.6%** (drop of 36.5 points; min 21.6%)
**Net Primary: +386 → -294** (range -294 to +400, trend: deteriorating)
**Duration: 8 trading days**

| Metric | Value |
|---|---|
| T2108 min | 21.6% |
| T2108 max | 58.1% |
| T2108 avg | 38.4% |
| 5d ratio min | 0.27 |
| 5d ratio max | 1.41 |
| 5d ratio avg | 0.67 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 3 |
| BO:BD avg ratio | 0.81 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |

### Period 20: BULL — 2024-04-17 to 2024-04-23

**T2108: 21.6% → 40.0%** (rise of 18.4 points; max 40.0%)
**Net Primary: -294 → -131** (range -315 to -131, trend: improving)
**Duration: 5 trading days**

| Metric | Value |
|---|---|
| T2108 min | 21.6% |
| T2108 max | 40.0% |
| T2108 avg | 29.3% |
| 5d ratio min | 0.35 |
| 5d ratio max | 1.20 |
| 5d ratio avg | 0.63 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 5 |
| BO:BD avg ratio | 1.66 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 0.75 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 21: CORRECTION — 2024-04-23 to 2024-04-25

**T2108: 40.0% → 34.8%** (drop of 5.2 points; min 34.8%)
**Net Primary: -131 → -233** (range -233 to -131, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 34.8% |
| T2108 max | 40.0% |
| T2108 avg | 37.7% |
| 5d ratio min | 1.20 |
| 5d ratio max | 1.35 |
| 5d ratio avg | 1.27 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 3 |
| BO:BD avg ratio | 2.11 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |

### Period 22: BULL — 2024-04-25 to 2024-04-29

**T2108: 34.8% → 40.5%** (rise of 5.7 points; max 40.5%)
**Net Primary: -233 → -81** (range -233 to -81, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 34.8% |
| T2108 max | 40.5% |
| T2108 avg | 37.6% |
| 5d ratio min | 1.27 |
| 5d ratio max | 1.76 |
| 5d ratio avg | 1.53 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 3 |
| BO:BD avg ratio | 1.89 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.35 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 23: CORRECTION — 2024-04-29 to 2024-04-30

**T2108: 40.5% → 31.8%** (drop of 8.6 points; min 31.8%)
**Net Primary: -81 → -224** (range -224 to -81, trend: deteriorating)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 31.8% |
| T2108 max | 40.5% |
| T2108 avg | 36.1% |
| 5d ratio min | 1.04 |
| 5d ratio max | 1.76 |
| 5d ratio avg | 1.40 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 2 |
| BO:BD avg ratio | 1.50 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |

### Period 24: BULL — 2024-04-30 to 2024-05-15

**T2108: 31.8% → 57.9%** (rise of 26.1 points; max 57.9%)
**Net Primary: -224 → +324** (range -224 to +324, trend: improving)
**Duration: 12 trading days**

| Metric | Value |
|---|---|
| T2108 min | 31.8% |
| T2108 max | 57.9% |
| T2108 avg | 47.2% |
| 5d ratio min | 1.04 |
| 5d ratio max | 1.94 |
| 5d ratio avg | 1.42 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 3 |
| BO:BD avg ratio | 1.77 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.76 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 25: CORRECTION — 2024-05-15 to 2024-05-22

**T2108: 57.9% → 51.3%** (drop of 6.5 points; min 51.3%)
**Net Primary: +324 → +232** (range +232 to +324, trend: deteriorating)
**Duration: 6 trading days**

| Metric | Value |
|---|---|
| T2108 min | 51.3% |
| T2108 max | 57.9% |
| T2108 avg | 55.7% |
| 5d ratio min | 1.20 |
| 5d ratio max | 2.03 |
| 5d ratio avg | 1.63 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.38 |
| Classification | Normal |

### Period 26: BULL — 2024-05-22 to 2024-05-22

**T2108: 51.3% → 51.3%** (rise of 0.0 points; max 51.3%)
**Net Primary: +232 → +232** (range +232 to +232, trend: deteriorating)
**Duration: 1 trading days**

| Metric | Value |
|---|---|
| T2108 min | 51.3% |
| T2108 max | 51.3% |
| T2108 avg | 51.3% |
| 5d ratio min | 1.20 |
| 5d ratio max | 1.20 |
| 5d ratio avg | 1.20 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 0.95 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.03 |
| Pre-period days 5d ≥ 2.0 | 1 |

### Period 27: CORRECTION — 2024-05-22 to 2024-05-29

**T2108: 51.3% → 36.6%** (drop of 14.7 points; min 36.6%)
**Net Primary: +232 → -14** (range -14 to +232, trend: deteriorating)
**Duration: 5 trading days**

| Metric | Value |
|---|---|
| T2108 min | 36.6% |
| T2108 max | 51.3% |
| T2108 avg | 43.8% |
| 5d ratio min | 0.78 |
| 5d ratio max | 1.20 |
| 5d ratio avg | 0.91 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 1.15 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |

### Period 28: BULL — 2024-05-29 to 2024-05-31

**T2108: 36.6% → 51.4%** (rise of 14.8 points; max 51.4%)
**Net Primary: -14 → +88** (range -14 to +88, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 36.6% |
| T2108 max | 51.4% |
| T2108 avg | 43.4% |
| 5d ratio min | 0.83 |
| 5d ratio max | 1.37 |
| 5d ratio avg | 1.04 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 1.26 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.43 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 29: CORRECTION — 2024-05-31 to 2024-06-04

**T2108: 51.4% → 43.4%** (drop of 8.0 points; min 43.4%)
**Net Primary: +88 → -52** (range -52 to +88, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 43.4% |
| T2108 max | 51.4% |
| T2108 avg | 47.7% |
| 5d ratio min | 0.92 |
| 5d ratio max | 1.37 |
| 5d ratio avg | 1.15 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 1.05 |
| Classification | Normal |

### Period 30: BULL — 2024-06-04 to 2024-06-05

**T2108: 43.4% → 47.3%** (rise of 3.9 points; max 47.3%)
**Net Primary: -52 → +92** (range -52 to +92, trend: improving)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 43.4% |
| T2108 max | 47.3% |
| T2108 avg | 45.3% |
| 5d ratio min | 0.92 |
| 5d ratio max | 1.27 |
| 5d ratio avg | 1.09 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 1.64 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.37 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 31: CORRECTION — 2024-06-05 to 2024-06-11

**T2108: 47.3% → 35.9%** (drop of 11.4 points; min 35.9%)
**Net Primary: +92 → -45** (range -108 to +92, trend: deteriorating)
**Duration: 5 trading days**

| Metric | Value |
|---|---|
| T2108 min | 35.9% |
| T2108 max | 47.3% |
| T2108 avg | 41.6% |
| 5d ratio min | 0.89 |
| 5d ratio max | 1.27 |
| 5d ratio avg | 1.10 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 3 |
| BO:BD avg ratio | 1.41 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |

### Period 32: BULL — 2024-06-11 to 2024-06-12

**T2108: 35.9% → 42.1%** (rise of 6.2 points; max 42.1%)
**Net Primary: -45 → +30** (range -45 to +30, trend: improving)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 35.9% |
| T2108 max | 42.1% |
| T2108 avg | 39.0% |
| 5d ratio min | 1.19 |
| 5d ratio max | 1.20 |
| 5d ratio avg | 1.19 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 2.20 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.27 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 33: CORRECTION — 2024-06-12 to 2024-06-14

**T2108: 42.1% → 30.7%** (drop of 11.4 points; min 30.7%)
**Net Primary: +30 → -204** (range -204 to +30, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 30.7% |
| T2108 max | 42.1% |
| T2108 avg | 36.9% |
| 5d ratio min | 1.08 |
| 5d ratio max | 1.20 |
| 5d ratio avg | 1.14 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 2 |
| BO:BD avg ratio | 1.34 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |

### Period 34: BULL — 2024-06-14 to 2024-06-24

**T2108: 30.7% → 39.0%** (rise of 8.3 points; max 39.0%)
**Net Primary: -204 → -288** (range -328 to -204, trend: deteriorating)
**Duration: 6 trading days**

| Metric | Value |
|---|---|
| T2108 min | 30.7% |
| T2108 max | 39.0% |
| T2108 avg | 34.1% |
| 5d ratio min | 0.56 |
| 5d ratio max | 1.08 |
| 5d ratio avg | 0.80 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 6 |
| BO:BD avg ratio | 0.85 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.20 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 35: CORRECTION — 2024-06-24 to 2024-07-01

**T2108: 39.0% → 31.1%** (drop of 7.9 points; min 31.1%)
**Net Primary: -288 → -323** (range -360 to -259, trend: deteriorating)
**Duration: 6 trading days**

| Metric | Value |
|---|---|
| T2108 min | 31.1% |
| T2108 max | 39.0% |
| T2108 avg | 34.2% |
| 5d ratio min | 0.85 |
| 5d ratio max | 1.31 |
| 5d ratio avg | 1.08 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 6 |
| BO:BD avg ratio | 1.37 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |

### Period 36: BULL — 2024-07-01 to 2024-07-16

**T2108: 31.1% → 70.7%** (rise of 39.5 points; max 70.7%)
**Net Primary: -323 → +1022** (range -323 to +1022, trend: improving)
**Duration: 11 trading days**

| Metric | Value |
|---|---|
| T2108 min | 31.1% |
| T2108 max | 70.7% |
| T2108 avg | 45.1% |
| 5d ratio min | 1.09 |
| 5d ratio max | 7.36 |
| 5d ratio avg | 2.48 |
| Days 5d ratio ≥ 2.0 | 4 |
| Days Net Primary < 0 | 7 |
| BO:BD avg ratio | 5.18 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.31 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 37: CORRECTION — 2024-07-16 to 2024-07-18

**T2108: 70.7% → 65.0%** (drop of 5.6 points; min 65.0%)
**Net Primary: +1022 → +635** (range +635 to +1022, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 65.0% |
| T2108 max | 70.7% |
| T2108 avg | 68.7% |
| 5d ratio min | 2.08 |
| 5d ratio max | 7.36 |
| 5d ratio avg | 4.73 |
| Days 5d ratio ≥ 2.0 | 3 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 7.28 |
| Classification | Normal |

### Period 38: BULL — 2024-07-18 to 2024-07-22

**T2108: 65.0% → 66.4%** (rise of 1.4 points; max 66.4%)
**Net Primary: +635 → +711** (range +517 to +711, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 61.1% |
| T2108 max | 66.4% |
| T2108 avg | 64.2% |
| 5d ratio min | 1.65 |
| 5d ratio max | 2.08 |
| 5d ratio avg | 1.79 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.38 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 7.36 |
| Pre-period days 5d ≥ 2.0 | 5 |

### Period 39: CORRECTION — 2024-07-22 to 2024-07-24

**T2108: 66.4% → 57.4%** (drop of 9.1 points; min 57.4%)
**Net Primary: +711 → +502** (range +502 to +792, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 57.4% |
| T2108 max | 66.4% |
| T2108 avg | 63.1% |
| 5d ratio min | 0.75 |
| 5d ratio max | 1.65 |
| 5d ratio avg | 1.09 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.96 |
| Classification | Normal |

### Period 40: BULL — 2024-07-24 to 2024-07-26

**T2108: 57.4% → 67.0%** (rise of 9.6 points; max 67.0%)
**Net Primary: +502 → +797** (range +502 to +797, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 57.4% |
| T2108 max | 67.0% |
| T2108 avg | 61.9% |
| 5d ratio min | 0.75 |
| 5d ratio max | 1.60 |
| 5d ratio avg | 1.20 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.26 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 4.75 |
| Pre-period days 5d ≥ 2.0 | 2 |

### Period 41: CORRECTION — 2024-07-26 to 2024-08-05

**T2108: 67.0% → 31.4%** (drop of 35.5 points; min 31.4%)
**Net Primary: +797 → -500** (range -500 to +797, trend: deteriorating)
**Duration: 7 trading days**

| Metric | Value |
|---|---|
| T2108 min | 31.4% |
| T2108 max | 67.0% |
| T2108 avg | 56.5% |
| 5d ratio min | 0.25 |
| 5d ratio max | 1.60 |
| 5d ratio avg | 0.93 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 2 |
| BO:BD avg ratio | 1.04 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |

### Period 42: BULL — 2024-08-05 to 2024-08-26

**T2108: 31.4% → 63.4%** (rise of 31.9 points; max 63.4%)
**Net Primary: -500 → +533** (range -572 to +533, trend: improving)
**Duration: 16 trading days**

| Metric | Value |
|---|---|
| T2108 min | 31.4% |
| T2108 max | 63.4% |
| T2108 avg | 47.5% |
| 5d ratio min | 0.20 |
| 5d ratio max | 3.27 |
| 5d ratio avg | 1.56 |
| Days 5d ratio ≥ 2.0 | 6 |
| Days Net Primary < 0 | 10 |
| BO:BD avg ratio | 3.00 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.52 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 43: CORRECTION — 2024-08-26 to 2024-09-03

**T2108: 63.4% → 51.4%** (drop of 11.9 points; min 51.4%)
**Net Primary: +533 → +104** (range +104 to +533, trend: deteriorating)
**Duration: 6 trading days**

| Metric | Value |
|---|---|
| T2108 min | 51.4% |
| T2108 max | 63.4% |
| T2108 avg | 59.7% |
| 5d ratio min | 0.37 |
| 5d ratio max | 2.65 |
| 5d ratio avg | 1.61 |
| Days 5d ratio ≥ 2.0 | 2 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 0.99 |
| Classification | Normal |

### Period 44: BULL — 2024-09-03 to 2024-09-03

**T2108: 51.4% → 51.4%** (rise of 0.0 points; max 51.4%)
**Net Primary: +104 → +104** (range +104 to +104, trend: deteriorating)
**Duration: 1 trading days**

| Metric | Value |
|---|---|
| T2108 min | 51.4% |
| T2108 max | 51.4% |
| T2108 avg | 51.4% |
| 5d ratio min | 0.37 |
| 5d ratio max | 0.37 |
| 5d ratio avg | 0.37 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 0.09 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.65 |
| Pre-period days 5d ≥ 2.0 | 2 |

### Period 45: CORRECTION — 2024-09-03 to 2024-09-06

**T2108: 51.4% → 37.5%** (drop of 14.0 points; min 37.5%)
**Net Primary: +104 → -174** (range -174 to +104, trend: deteriorating)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 37.5% |
| T2108 max | 51.4% |
| T2108 avg | 45.9% |
| 5d ratio min | 0.34 |
| 5d ratio max | 0.50 |
| 5d ratio avg | 0.40 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 0.53 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |

### Period 46: BULL — 2024-09-06 to 2024-09-19

**T2108: 37.5% → 68.8%** (rise of 31.3 points; max 68.8%)
**Net Primary: -174 → +650** (range -174 to +650, trend: improving)
**Duration: 10 trading days**

| Metric | Value |
|---|---|
| T2108 min | 37.5% |
| T2108 max | 68.8% |
| T2108 avg | 50.8% |
| 5d ratio min | 0.34 |
| 5d ratio max | 2.74 |
| 5d ratio avg | 1.63 |
| Days 5d ratio ≥ 2.0 | 5 |
| Days Net Primary < 0 | 3 |
| BO:BD avg ratio | 2.43 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.78 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 47: CORRECTION — 2024-09-19 to 2024-09-20

**T2108: 68.8% → 63.4%** (drop of 5.4 points; min 63.4%)
**Net Primary: +650 → +518** (range +518 to +650, trend: deteriorating)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 63.4% |
| T2108 max | 68.8% |
| T2108 avg | 66.1% |
| 5d ratio min | 1.31 |
| 5d ratio max | 2.54 |
| 5d ratio avg | 1.93 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.18 |
| Classification | Normal |

### Period 48: BULL — 2024-09-20 to 2024-09-24

**T2108: 63.4% → 65.7%** (rise of 2.4 points; max 65.7%)
**Net Primary: +518 → +525** (range +461 to +525, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 63.4% |
| T2108 max | 65.7% |
| T2108 avg | 64.5% |
| 5d ratio min | 1.28 |
| 5d ratio max | 1.31 |
| 5d ratio avg | 1.30 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.26 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.74 |
| Pre-period days 5d ≥ 2.0 | 5 |

### Period 49: CORRECTION — 2024-09-24 to 2024-09-25

**T2108: 65.7% → 59.7%** (drop of 6.0 points; min 59.7%)
**Net Primary: +525 → +371** (range +371 to +525, trend: deteriorating)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 59.7% |
| T2108 max | 65.7% |
| T2108 avg | 62.7% |
| 5d ratio min | 1.14 |
| 5d ratio max | 1.31 |
| 5d ratio avg | 1.23 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.52 |
| Classification | Normal |

### Period 50: BULL — 2024-09-25 to 2024-09-27

**T2108: 59.7% → 66.9%** (rise of 7.2 points; max 66.9%)
**Net Primary: +371 → +560** (range +371 to +560, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 59.7% |
| T2108 max | 66.9% |
| T2108 avg | 63.3% |
| 5d ratio min | 1.10 |
| 5d ratio max | 1.64 |
| 5d ratio avg | 1.29 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.08 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.54 |
| Pre-period days 5d ≥ 2.0 | 2 |

### Period 51: CORRECTION — 2024-09-27 to 2024-10-10

**T2108: 66.9% → 48.4%** (drop of 18.5 points; min 48.4%)
**Net Primary: +560 → +100** (range +100 to +560, trend: deteriorating)
**Duration: 10 trading days**

| Metric | Value |
|---|---|
| T2108 min | 48.4% |
| T2108 max | 66.9% |
| T2108 avg | 56.8% |
| 5d ratio min | 1.05 |
| 5d ratio max | 1.69 |
| 5d ratio avg | 1.28 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.49 |
| Classification | Normal |

### Period 52: BULL — 2024-10-10 to 2024-10-16

**T2108: 48.4% → 63.6%** (rise of 15.2 points; max 63.6%)
**Net Primary: +100 → +522** (range +100 to +522, trend: improving)
**Duration: 5 trading days**

| Metric | Value |
|---|---|
| T2108 min | 48.4% |
| T2108 max | 63.6% |
| T2108 avg | 57.1% |
| 5d ratio min | 1.17 |
| 5d ratio max | 2.04 |
| 5d ratio avg | 1.51 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 3.38 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.35 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 53: CORRECTION — 2024-10-16 to 2024-10-31

**T2108: 63.6% → 38.1%** (drop of 25.5 points; min 38.1%)
**Net Primary: +522 → +373** (range +338 to +618, trend: deteriorating)
**Duration: 12 trading days**

| Metric | Value |
|---|---|
| T2108 min | 38.1% |
| T2108 max | 63.6% |
| T2108 avg | 50.4% |
| 5d ratio min | 0.99 |
| 5d ratio max | 2.17 |
| 5d ratio avg | 1.56 |
| Days 5d ratio ≥ 2.0 | 3 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.09 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |

### Period 54: BULL — 2024-10-31 to 2024-11-11

**T2108: 38.1% → 58.3%** (rise of 20.2 points; max 58.3%)
**Net Primary: +373 → +1054** (range +373 to +1054, trend: improving)
**Duration: 8 trading days**

| Metric | Value |
|---|---|
| T2108 min | 38.1% |
| T2108 max | 58.3% |
| T2108 avg | 49.1% |
| 5d ratio min | 0.86 |
| 5d ratio max | 3.06 |
| 5d ratio avg | 1.89 |
| Days 5d ratio ≥ 2.0 | 4 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.18 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.62 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 55: CORRECTION — 2024-11-11 to 2024-11-13

**T2108: 58.3% → 52.0%** (drop of 6.3 points; min 52.0%)
**Net Primary: +1054 → +644** (range +644 to +1054, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 52.0% |
| T2108 max | 58.3% |
| T2108 avg | 54.6% |
| 5d ratio min | 1.08 |
| 5d ratio max | 3.06 |
| 5d ratio avg | 2.15 |
| Days 5d ratio ≥ 2.0 | 2 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.17 |
| Classification | Normal |

### Period 56: BULL — 2024-11-13 to 2024-11-29

**T2108: 52.0% → 61.8%** (rise of 9.8 points; max 61.8%)
**Net Primary: +644 → +874** (range +198 to +874, trend: improving)
**Duration: 12 trading days**

| Metric | Value |
|---|---|
| T2108 min | 47.6% |
| T2108 max | 61.8% |
| T2108 avg | 54.2% |
| 5d ratio min | 0.46 |
| 5d ratio max | 3.12 |
| 5d ratio avg | 1.57 |
| Days 5d ratio ≥ 2.0 | 5 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.11 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 3.06 |
| Pre-period days 5d ≥ 2.0 | 5 |

### Period 57: CORRECTION — 2024-11-29 to 2024-12-05

**T2108: 61.8% → 54.8%** (drop of 7.0 points; min 54.8%)
**Net Primary: +874 → +701** (range +701 to +930, trend: deteriorating)
**Duration: 5 trading days**

| Metric | Value |
|---|---|
| T2108 min | 54.8% |
| T2108 max | 61.8% |
| T2108 avg | 58.9% |
| 5d ratio min | 1.12 |
| 5d ratio max | 3.12 |
| 5d ratio avg | 1.89 |
| Days 5d ratio ≥ 2.0 | 2 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.64 |
| Classification | Normal |

### Period 58: BULL — 2024-12-05 to 2024-12-05

**T2108: 54.8% → 54.8%** (rise of 0.0 points; max 54.8%)
**Net Primary: +701 → +701** (range +701 to +701, trend: deteriorating)
**Duration: 1 trading days**

| Metric | Value |
|---|---|
| T2108 min | 54.8% |
| T2108 max | 54.8% |
| T2108 avg | 54.8% |
| 5d ratio min | 1.12 |
| 5d ratio max | 1.12 |
| 5d ratio avg | 1.12 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 0.49 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 3.12 |
| Pre-period days 5d ≥ 2.0 | 3 |

### Period 59: CORRECTION — 2024-12-05 to 2024-12-18

**T2108: 54.8% → 18.1%** (drop of 36.6 points; min 18.1%)
**Net Primary: +701 → -141** (range -141 to +763, trend: deteriorating)
**Duration: 10 trading days**

| Metric | Value |
|---|---|
| T2108 min | 18.1% |
| T2108 max | 54.8% |
| T2108 avg | 43.7% |
| 5d ratio min | 0.09 |
| 5d ratio max | 1.28 |
| 5d ratio avg | 0.97 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 0.98 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |

### Period 60: BULL — 2024-12-18 to 2024-12-26

**T2108: 18.1% → 26.2%** (rise of 8.0 points; max 26.2%)
**Net Primary: -141 → +185** (range -193 to +185, trend: improving)
**Duration: 6 trading days**

| Metric | Value |
|---|---|
| T2108 min | 18.1% |
| T2108 max | 26.2% |
| T2108 avg | 21.5% |
| 5d ratio min | 0.09 |
| 5d ratio max | 3.07 |
| 5d ratio avg | 0.82 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 4 |
| BO:BD avg ratio | 3.39 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |
| Pre-period 5d max (5d before) | 1.21 |
| Pre-period days 5d ≥ 2.0 | 0 |

### Period 61: CORRECTION — 2024-12-26 to 2024-12-30

**T2108: 26.2% → 18.7%** (drop of 7.5 points; min 18.7%)
**Net Primary: +185 → +69** (range +69 to +185, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 18.7% |
| T2108 max | 26.2% |
| T2108 avg | 22.0% |
| 5d ratio min | 2.39 |
| 5d ratio max | 3.09 |
| 5d ratio avg | 2.85 |
| Days 5d ratio ≥ 2.0 | 3 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 3.86 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |

### Period 62: BULL — 2024-12-30 to 2025-01-21

**T2108: 18.7% → 47.8%** (rise of 29.2 points; max 47.8%)
**Net Primary: +69 → +180** (range -197 to +339, trend: improving)
**Duration: 14 trading days**

| Metric | Value |
|---|---|
| T2108 min | 18.7% |
| T2108 max | 47.8% |
| T2108 avg | 26.8% |
| 5d ratio min | 0.59 |
| 5d ratio max | 2.58 |
| 5d ratio avg | 1.74 |
| Days 5d ratio ≥ 2.0 | 7 |
| Days Net Primary < 0 | 5 |
| BO:BD avg ratio | 2.36 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |
| Pre-period 5d max (5d before) | 3.09 |
| Pre-period days 5d ≥ 2.0 | 2 |

### Period 63: CORRECTION — 2025-01-21 to 2025-01-22

**T2108: 47.8% → 42.6%** (drop of 5.2 points; min 42.6%)
**Net Primary: +180 → +142** (range +142 to +180, trend: deteriorating)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 42.6% |
| T2108 max | 47.8% |
| T2108 avg | 45.2% |
| 5d ratio min | 2.15 |
| 5d ratio max | 2.18 |
| 5d ratio avg | 2.17 |
| Days 5d ratio ≥ 2.0 | 2 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.68 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +1.6% |
| Pre-period cyclical ETF ret (30d) | +1.7% |
| Pre-period leading sector | Cyclical |

### Period 64: BULL — 2025-01-22 to 2025-01-30

**T2108: 42.6% → 50.6%** (rise of 8.0 points; max 50.6%)
**Net Primary: +142 → +146** (range -4 to +190, trend: improving)
**Duration: 7 trading days**

| Metric | Value |
|---|---|
| T2108 min | 42.6% |
| T2108 max | 50.6% |
| T2108 avg | 45.4% |
| 5d ratio min | 0.86 |
| 5d ratio max | 2.15 |
| 5d ratio avg | 1.36 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 1.32 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.18 |
| Pre-period days 5d ≥ 2.0 | 1 |
| Pre-period defensive ETF ret (30d) | +3.3% |
| Pre-period cyclical ETF ret (30d) | +2.8% |
| Pre-period leading sector | Defensive |

### Period 65: CORRECTION — 2025-01-30 to 2025-02-03

**T2108: 50.6% → 39.8%** (drop of 10.8 points; min 39.8%)
**Net Primary: +146 → -128** (range -128 to +146, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 39.8% |
| T2108 max | 50.6% |
| T2108 avg | 45.2% |
| 5d ratio min | 0.77 |
| 5d ratio max | 0.93 |
| 5d ratio avg | 0.86 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 1.08 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |
| Pre-period defensive ETF ret (30d) | +4.9% |
| Pre-period cyclical ETF ret (30d) | +3.6% |
| Pre-period leading sector | Defensive |

### Period 66: BULL — 2025-02-03 to 2025-02-05

**T2108: 39.8% → 50.6%** (rise of 10.9 points; max 50.6%)
**Net Primary: -128 → +197** (range -128 to +197, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 39.8% |
| T2108 max | 50.6% |
| T2108 avg | 45.5% |
| 5d ratio min | 0.89 |
| 5d ratio max | 1.34 |
| 5d ratio avg | 1.10 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 2.00 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.11 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | +4.9% |
| Pre-period cyclical ETF ret (30d) | +2.3% |
| Pre-period leading sector | Defensive |

### Period 67: CORRECTION — 2025-02-05 to 2025-02-12

**T2108: 50.6% → 45.0%** (drop of 5.6 points; min 45.0%)
**Net Primary: +197 → -149** (range -149 to +197, trend: deteriorating)
**Duration: 6 trading days**

| Metric | Value |
|---|---|
| T2108 min | 45.0% |
| T2108 max | 50.6% |
| T2108 avg | 48.7% |
| 5d ratio min | 0.87 |
| 5d ratio max | 1.34 |
| 5d ratio avg | 1.12 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 3 |
| BO:BD avg ratio | 1.22 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +4.9% |
| Pre-period cyclical ETF ret (30d) | +2.5% |
| Pre-period leading sector | Defensive |

### Period 68: BULL — 2025-02-12 to 2025-02-18

**T2108: 45.0% → 51.5%** (rise of 6.5 points; max 51.5%)
**Net Primary: -149 → +29** (range -149 to +29, trend: improving)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 45.0% |
| T2108 max | 51.5% |
| T2108 avg | 48.9% |
| 5d ratio min | 0.87 |
| 5d ratio max | 1.30 |
| 5d ratio avg | 1.13 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 3 |
| BO:BD avg ratio | 1.61 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.34 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | +3.9% |
| Pre-period cyclical ETF ret (30d) | +4.3% |
| Pre-period leading sector | Cyclical |

### Period 69: CORRECTION — 2025-02-18 to 2025-03-13

**T2108: 51.5% → 17.2%** (drop of 34.4 points; min 17.2%)
**Net Primary: +29 → -1286** (range -1289 to +29, trend: deteriorating)
**Duration: 18 trading days**

| Metric | Value |
|---|---|
| T2108 min | 17.2% |
| T2108 max | 51.5% |
| T2108 avg | 33.1% |
| 5d ratio min | 0.34 |
| 5d ratio max | 1.40 |
| 5d ratio avg | 0.63 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 17 |
| BO:BD avg ratio | 0.92 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |
| Pre-period defensive ETF ret (30d) | +1.0% |
| Pre-period cyclical ETF ret (30d) | +0.6% |
| Pre-period leading sector | Defensive |

### Period 70: BULL — 2025-03-13 to 2025-03-19

**T2108: 17.2% → 29.2%** (rise of 12.0 points; max 29.2%)
**Net Primary: -1286 → -800** (range -1286 to -800, trend: improving)
**Duration: 5 trading days**

| Metric | Value |
|---|---|
| T2108 min | 17.2% |
| T2108 max | 29.2% |
| T2108 avg | 24.3% |
| 5d ratio min | 0.55 |
| 5d ratio max | 1.63 |
| 5d ratio avg | 1.19 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 5 |
| BO:BD avg ratio | 2.97 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |
| Pre-period 5d max (5d before) | 0.59 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | -1.4% |
| Pre-period cyclical ETF ret (30d) | -7.9% |
| Pre-period leading sector | Defensive |

### Period 71: CORRECTION — 2025-03-19 to 2025-03-21

**T2108: 29.2% → 24.1%** (drop of 5.2 points; min 24.1%)
**Net Primary: -800 → -832** (range -832 to -799, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 24.1% |
| T2108 max | 29.2% |
| T2108 avg | 27.1% |
| 5d ratio min | 1.52 |
| 5d ratio max | 2.25 |
| 5d ratio avg | 1.80 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 3 |
| BO:BD avg ratio | 2.09 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |
| Pre-period defensive ETF ret (30d) | +0.9% |
| Pre-period cyclical ETF ret (30d) | -8.4% |
| Pre-period leading sector | Defensive |

### Period 72: BULL — 2025-03-21 to 2025-03-24

**T2108: 24.1% → 31.1%** (rise of 7.1 points; max 31.1%)
**Net Primary: -832 → -636** (range -832 to -636, trend: improving)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 24.1% |
| T2108 max | 31.1% |
| T2108 avg | 27.6% |
| 5d ratio min | 1.37 |
| 5d ratio max | 1.52 |
| 5d ratio avg | 1.45 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 2 |
| BO:BD avg ratio | 1.96 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.25 |
| Pre-period days 5d ≥ 2.0 | 1 |
| Pre-period defensive ETF ret (30d) | +0.1% |
| Pre-period cyclical ETF ret (30d) | -7.5% |
| Pre-period leading sector | Defensive |

### Period 73: CORRECTION — 2025-03-24 to 2025-03-28

**T2108: 31.1% → 24.2%** (drop of 6.9 points; min 24.2%)
**Net Primary: -636 → -1045** (range -1045 to -636, trend: deteriorating)
**Duration: 5 trading days**

| Metric | Value |
|---|---|
| T2108 min | 24.2% |
| T2108 max | 31.1% |
| T2108 avg | 28.6% |
| 5d ratio min | 0.49 |
| 5d ratio max | 1.37 |
| 5d ratio avg | 0.97 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 5 |
| BO:BD avg ratio | 0.93 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |
| Pre-period defensive ETF ret (30d) | -0.8% |
| Pre-period cyclical ETF ret (30d) | -4.7% |
| Pre-period leading sector | Defensive |

### Period 74: BULL — 2025-03-28 to 2025-04-02

**T2108: 24.2% → 30.9%** (rise of 6.7 points; max 30.9%)
**Net Primary: -1045 → -974** (range -1127 to -974, trend: improving)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 24.2% |
| T2108 max | 30.9% |
| T2108 avg | 26.9% |
| 5d ratio min | 0.30 |
| 5d ratio max | 0.49 |
| 5d ratio avg | 0.40 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 4 |
| BO:BD avg ratio | 1.09 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.52 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | -2.2% |
| Pre-period cyclical ETF ret (30d) | -3.4% |
| Pre-period leading sector | Defensive |

### Period 75: CORRECTION — 2025-04-02 to 2025-04-08

**T2108: 30.9% → 4.1%** (drop of 26.8 points; min 4.1%)
**Net Primary: -974 → -2245** (range -2245 to -974, trend: deteriorating)
**Duration: 5 trading days**

| Metric | Value |
|---|---|
| T2108 min | 4.1% |
| T2108 max | 30.9% |
| T2108 avg | 13.0% |
| 5d ratio min | 0.15 |
| 5d ratio max | 0.49 |
| 5d ratio avg | 0.23 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 5 |
| BO:BD avg ratio | 0.84 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |
| Pre-period defensive ETF ret (30d) | -3.4% |
| Pre-period cyclical ETF ret (30d) | -3.0% |
| Pre-period leading sector | Cyclical |

### Period 76: BULL — 2025-04-08 to 2025-04-17

**T2108: 4.1% → 18.4%** (rise of 14.3 points; max 18.4%)
**Net Primary: -2245 → -1467** (range -2245 to -1467, trend: improving)
**Duration: 8 trading days**

| Metric | Value |
|---|---|
| T2108 min | 4.1% |
| T2108 max | 18.4% |
| T2108 avg | 12.9% |
| 5d ratio min | 0.16 |
| 5d ratio max | 6.42 |
| 5d ratio avg | 2.30 |
| Days 5d ratio ≥ 2.0 | 4 |
| Days Net Primary < 0 | 8 |
| BO:BD avg ratio | 7.02 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |
| Pre-period 5d max (5d before) | 0.49 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | -8.3% |
| Pre-period cyclical ETF ret (30d) | -10.6% |
| Pre-period leading sector | Defensive |

### Period 77: CORRECTION — 2025-04-17 to 2025-04-21

**T2108: 18.4% → 13.2%** (drop of 5.2 points; min 13.2%)
**Net Primary: -1467 → -1592** (range -1592 to -1467, trend: deteriorating)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 13.2% |
| T2108 max | 18.4% |
| T2108 avg | 15.8% |
| 5d ratio min | 1.17 |
| 5d ratio max | 2.01 |
| 5d ratio avg | 1.59 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 2 |
| BO:BD avg ratio | 1.87 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |
| Pre-period defensive ETF ret (30d) | -6.1% |
| Pre-period cyclical ETF ret (30d) | -6.9% |
| Pre-period leading sector | Defensive |

### Period 78: BULL — 2025-04-21 to 2025-05-02

**T2108: 13.2% → 50.0%** (rise of 36.8 points; max 50.0%)
**Net Primary: -1592 → -221** (range -1592 to -221, trend: improving)
**Duration: 10 trading days**

| Metric | Value |
|---|---|
| T2108 min | 13.2% |
| T2108 max | 50.0% |
| T2108 avg | 31.6% |
| 5d ratio min | 1.17 |
| 5d ratio max | 4.30 |
| 5d ratio avg | 2.28 |
| Days 5d ratio ≥ 2.0 | 4 |
| Days Net Primary < 0 | 10 |
| BO:BD avg ratio | 3.63 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |
| Pre-period 5d max (5d before) | 6.42 |
| Pre-period days 5d ≥ 2.0 | 4 |
| Pre-period defensive ETF ret (30d) | -6.4% |
| Pre-period cyclical ETF ret (30d) | -8.8% |
| Pre-period leading sector | Defensive |

### Period 79: CORRECTION — 2025-05-02 to 2025-05-06

**T2108: 50.0% → 44.8%** (drop of 5.2 points; min 44.8%)
**Net Primary: -221 → -499** (range -499 to -221, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 44.8% |
| T2108 max | 50.0% |
| T2108 avg | 47.4% |
| 5d ratio min | 1.10 |
| 5d ratio max | 1.84 |
| 5d ratio avg | 1.51 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 3 |
| BO:BD avg ratio | 1.82 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | -4.2% |
| Pre-period cyclical ETF ret (30d) | -2.1% |
| Pre-period leading sector | Cyclical |

### Period 80: BULL — 2025-05-06 to 2025-05-19

**T2108: 44.8% → 67.3%** (rise of 22.5 points; max 67.3%)
**Net Primary: -499 → +697** (range -499 to +705, trend: improving)
**Duration: 10 trading days**

| Metric | Value |
|---|---|
| T2108 min | 44.8% |
| T2108 max | 67.3% |
| T2108 avg | 59.0% |
| 5d ratio min | 1.10 |
| 5d ratio max | 2.95 |
| 5d ratio avg | 1.94 |
| Days 5d ratio ≥ 2.0 | 5 |
| Days Net Primary < 0 | 4 |
| BO:BD avg ratio | 2.34 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 3.08 |
| Pre-period days 5d ≥ 2.0 | 1 |
| Pre-period defensive ETF ret (30d) | +3.9% |
| Pre-period cyclical ETF ret (30d) | +12.4% |
| Pre-period leading sector | Cyclical |

### Period 81: CORRECTION — 2025-05-19 to 2025-05-21

**T2108: 67.3% → 55.1%** (drop of 12.3 points; min 55.1%)
**Net Primary: +697 → +367** (range +367 to +750, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 55.1% |
| T2108 max | 67.3% |
| T2108 avg | 62.9% |
| 5d ratio min | 0.95 |
| 5d ratio max | 1.62 |
| 5d ratio avg | 1.39 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.32 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +2.1% |
| Pre-period cyclical ETF ret (30d) | +17.3% |
| Pre-period leading sector | Cyclical |

### Period 82: BULL — 2025-05-21 to 2025-06-10

**T2108: 55.1% → 69.0%** (rise of 13.9 points; max 69.0%)
**Net Primary: +367 → +1424** (range +367 to +1424, trend: improving)
**Duration: 14 trading days**

| Metric | Value |
|---|---|
| T2108 min | 53.3% |
| T2108 max | 69.0% |
| T2108 avg | 62.4% |
| 5d ratio min | 0.78 |
| 5d ratio max | 2.91 |
| 5d ratio avg | 1.81 |
| Days 5d ratio ≥ 2.0 | 7 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.51 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.76 |
| Pre-period days 5d ≥ 2.0 | 3 |
| Pre-period defensive ETF ret (30d) | +3.3% |
| Pre-period cyclical ETF ret (30d) | +16.7% |
| Pre-period leading sector | Cyclical |

### Period 83: CORRECTION — 2025-06-10 to 2025-06-20

**T2108: 69.0% → 50.6%** (drop of 18.3 points; min 50.6%)
**Net Primary: +1424 → +1042** (range +1028 to +1424, trend: deteriorating)
**Duration: 8 trading days**

| Metric | Value |
|---|---|
| T2108 min | 50.6% |
| T2108 max | 69.0% |
| T2108 avg | 58.2% |
| 5d ratio min | 0.82 |
| 5d ratio max | 2.41 |
| 5d ratio avg | 1.40 |
| Days 5d ratio ≥ 2.0 | 3 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.41 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | -0.8% |
| Pre-period cyclical ETF ret (30d) | +2.7% |
| Pre-period leading sector | Cyclical |

### Period 84: BULL — 2025-06-20 to 2025-06-24

**T2108: 50.6% → 61.2%** (rise of 10.6 points; max 61.2%)
**Net Primary: +1042 → +1229** (range +1042 to +1229, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 50.6% |
| T2108 max | 61.2% |
| T2108 avg | 56.5% |
| 5d ratio min | 0.87 |
| 5d ratio max | 1.23 |
| 5d ratio avg | 1.09 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.69 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.11 |
| Pre-period days 5d ≥ 2.0 | 1 |
| Pre-period defensive ETF ret (30d) | +0.8% |
| Pre-period cyclical ETF ret (30d) | +2.1% |
| Pre-period leading sector | Cyclical |

### Period 85: CORRECTION — 2025-06-24 to 2025-06-25

**T2108: 61.2% → 53.5%** (drop of 7.8 points; min 53.5%)
**Net Primary: +1229 → +1115** (range +1115 to +1229, trend: deteriorating)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 53.5% |
| T2108 max | 61.2% |
| T2108 avg | 57.4% |
| 5d ratio min | 1.23 |
| 5d ratio max | 1.33 |
| 5d ratio avg | 1.28 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 3.57 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | -0.1% |
| Pre-period cyclical ETF ret (30d) | +1.3% |
| Pre-period leading sector | Cyclical |

### Period 86: BULL — 2025-06-25 to 2025-07-03

**T2108: 53.5% → 69.3%** (rise of 15.8 points; max 69.3%)
**Net Primary: +1115 → +1740** (range +1115 to +1740, trend: improving)
**Duration: 7 trading days**

| Metric | Value |
|---|---|
| T2108 min | 53.5% |
| T2108 max | 69.3% |
| T2108 avg | 61.9% |
| 5d ratio min | 1.33 |
| 5d ratio max | 2.05 |
| 5d ratio avg | 1.59 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.70 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.23 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | +0.9% |
| Pre-period cyclical ETF ret (30d) | +2.3% |
| Pre-period leading sector | Cyclical |

### Period 87: CORRECTION — 2025-07-03 to 2025-07-07

**T2108: 69.3% → 62.8%** (drop of 6.5 points; min 62.8%)
**Net Primary: +1740 → +1566** (range +1566 to +1740, trend: deteriorating)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 62.8% |
| T2108 max | 69.3% |
| T2108 avg | 66.0% |
| 5d ratio min | 1.77 |
| 5d ratio max | 1.96 |
| 5d ratio avg | 1.86 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.17 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +1.0% |
| Pre-period cyclical ETF ret (30d) | +4.3% |
| Pre-period leading sector | Cyclical |

### Period 88: BULL — 2025-07-07 to 2025-07-10

**T2108: 62.8% → 66.9%** (rise of 4.1 points; max 66.9%)
**Net Primary: +1566 → +1903** (range +1566 to +1903, trend: improving)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 62.8% |
| T2108 max | 66.9% |
| T2108 avg | 64.7% |
| 5d ratio min | 1.77 |
| 5d ratio max | 2.16 |
| 5d ratio avg | 1.95 |
| Days 5d ratio ≥ 2.0 | 2 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.79 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.05 |
| Pre-period days 5d ≥ 2.0 | 1 |
| Pre-period defensive ETF ret (30d) | +1.1% |
| Pre-period cyclical ETF ret (30d) | +4.4% |
| Pre-period leading sector | Cyclical |

### Period 89: CORRECTION — 2025-07-10 to 2025-07-15

**T2108: 66.9% → 53.4%** (drop of 13.5 points; min 53.4%)
**Net Primary: +1903 → +1332** (range +1332 to +1903, trend: deteriorating)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 53.4% |
| T2108 max | 66.9% |
| T2108 avg | 61.9% |
| 5d ratio min | 1.29 |
| 5d ratio max | 2.17 |
| 5d ratio avg | 1.71 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.32 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +0.2% |
| Pre-period cyclical ETF ret (30d) | +3.6% |
| Pre-period leading sector | Cyclical |

### Period 90: BULL — 2025-07-15 to 2025-07-23

**T2108: 53.4% → 67.6%** (rise of 14.2 points; max 67.6%)
**Net Primary: +1332 → +1677** (range +1332 to +1677, trend: improving)
**Duration: 7 trading days**

| Metric | Value |
|---|---|
| T2108 min | 53.4% |
| T2108 max | 67.6% |
| T2108 avg | 59.1% |
| 5d ratio min | 1.20 |
| 5d ratio max | 3.28 |
| 5d ratio avg | 1.84 |
| Days 5d ratio ≥ 2.0 | 2 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 3.49 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.17 |
| Pre-period days 5d ≥ 2.0 | 3 |
| Pre-period defensive ETF ret (30d) | +0.1% |
| Pre-period cyclical ETF ret (30d) | +3.9% |
| Pre-period leading sector | Cyclical |

### Period 91: CORRECTION — 2025-07-23 to 2025-07-28

**T2108: 67.6% → 59.5%** (drop of 8.1 points; min 59.5%)
**Net Primary: +1677 → +1201** (range +1201 to +1677, trend: deteriorating)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 59.5% |
| T2108 max | 67.6% |
| T2108 avg | 63.2% |
| 5d ratio min | 1.96 |
| 5d ratio max | 3.28 |
| 5d ratio avg | 2.42 |
| Days 5d ratio ≥ 2.0 | 3 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.72 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +1.9% |
| Pre-period cyclical ETF ret (30d) | +4.7% |
| Pre-period leading sector | Cyclical |

### Period 92: BULL — 2025-07-28 to 2025-07-28

**T2108: 59.5% → 59.5%** (rise of 0.0 points; max 59.5%)
**Net Primary: +1201 → +1201** (range +1201 to +1201, trend: deteriorating)
**Duration: 1 trading days**

| Metric | Value |
|---|---|
| T2108 min | 59.5% |
| T2108 max | 59.5% |
| T2108 avg | 59.5% |
| 5d ratio min | 1.96 |
| 5d ratio max | 1.96 |
| 5d ratio avg | 1.96 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 0.81 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 3.28 |
| Pre-period days 5d ≥ 2.0 | 4 |
| Pre-period defensive ETF ret (30d) | +1.8% |
| Pre-period cyclical ETF ret (30d) | +3.0% |
| Pre-period leading sector | Cyclical |

### Period 93: CORRECTION — 2025-07-28 to 2025-08-01

**T2108: 59.5% → 37.0%** (drop of 22.5 points; min 37.0%)
**Net Primary: +1201 → +474** (range +474 to +1201, trend: deteriorating)
**Duration: 5 trading days**

| Metric | Value |
|---|---|
| T2108 min | 37.0% |
| T2108 max | 59.5% |
| T2108 avg | 49.8% |
| 5d ratio min | 0.43 |
| 5d ratio max | 1.96 |
| 5d ratio avg | 0.92 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 0.49 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |
| Pre-period defensive ETF ret (30d) | +1.8% |
| Pre-period cyclical ETF ret (30d) | +3.0% |
| Pre-period leading sector | Cyclical |

### Period 94: BULL — 2025-08-01 to 2025-08-13

**T2108: 37.0% → 57.7%** (rise of 20.7 points; max 57.7%)
**Net Primary: +474 → +747** (range +345 to +747, trend: improving)
**Duration: 9 trading days**

| Metric | Value |
|---|---|
| T2108 min | 37.0% |
| T2108 max | 57.7% |
| T2108 avg | 45.8% |
| 5d ratio min | 0.43 |
| 5d ratio max | 1.96 |
| 5d ratio avg | 1.03 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.39 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.23 |
| Pre-period days 5d ≥ 2.0 | 1 |
| Pre-period defensive ETF ret (30d) | -1.5% |
| Pre-period cyclical ETF ret (30d) | +1.1% |
| Pre-period leading sector | Cyclical |

### Period 95: CORRECTION — 2025-08-13 to 2025-08-15

**T2108: 57.7% → 50.0%** (drop of 7.6 points; min 50.0%)
**Net Primary: +747 → +641** (range +641 to +747, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 50.0% |
| T2108 max | 57.7% |
| T2108 avg | 53.6% |
| 5d ratio min | 1.96 |
| 5d ratio max | 2.25 |
| 5d ratio avg | 2.12 |
| Days 5d ratio ≥ 2.0 | 2 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.45 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | -1.2% |
| Pre-period cyclical ETF ret (30d) | +1.6% |
| Pre-period leading sector | Cyclical |

### Period 96: BULL — 2025-08-15 to 2025-08-22

**T2108: 50.0% → 62.8%** (rise of 12.8 points; max 62.8%)
**Net Primary: +641 → +861** (range +468 to +861, trend: improving)
**Duration: 6 trading days**

| Metric | Value |
|---|---|
| T2108 min | 49.5% |
| T2108 max | 62.8% |
| T2108 avg | 52.5% |
| 5d ratio min | 0.88 |
| 5d ratio max | 2.74 |
| 5d ratio avg | 1.83 |
| Days 5d ratio ≥ 2.0 | 3 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 8.74 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.16 |
| Pre-period days 5d ≥ 2.0 | 1 |
| Pre-period defensive ETF ret (30d) | +0.9% |
| Pre-period cyclical ETF ret (30d) | +2.6% |
| Pre-period leading sector | Cyclical |

### Period 97: CORRECTION — 2025-08-22 to 2025-09-02

**T2108: 62.8% → 56.7%** (drop of 6.1 points; min 56.7%)
**Net Primary: +861 → +692** (range +692 to +861, trend: deteriorating)
**Duration: 7 trading days**

| Metric | Value |
|---|---|
| T2108 min | 56.7% |
| T2108 max | 62.8% |
| T2108 avg | 60.4% |
| 5d ratio min | 1.44 |
| 5d ratio max | 5.04 |
| 5d ratio avg | 3.20 |
| Days 5d ratio ≥ 2.0 | 5 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 7.80 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +0.8% |
| Pre-period cyclical ETF ret (30d) | -0.6% |
| Pre-period leading sector | Defensive |

### Period 98: BULL — 2025-09-02 to 2025-09-11

**T2108: 56.7% → 63.2%** (rise of 6.6 points; max 63.2%)
**Net Primary: +692 → +881** (range +671 to +881, trend: improving)
**Duration: 8 trading days**

| Metric | Value |
|---|---|
| T2108 min | 55.9% |
| T2108 max | 63.2% |
| T2108 avg | 58.6% |
| 5d ratio min | 1.15 |
| 5d ratio max | 2.48 |
| 5d ratio avg | 1.57 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.41 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 5.04 |
| Pre-period days 5d ≥ 2.0 | 4 |
| Pre-period defensive ETF ret (30d) | +1.7% |
| Pre-period cyclical ETF ret (30d) | +2.7% |
| Pre-period leading sector | Cyclical |

### Period 99: CORRECTION — 2025-09-11 to 2025-09-17

**T2108: 63.2% → 54.3%** (drop of 9.0 points; min 54.3%)
**Net Primary: +881 → +763** (range +763 to +881, trend: deteriorating)
**Duration: 5 trading days**

| Metric | Value |
|---|---|
| T2108 min | 54.3% |
| T2108 max | 63.2% |
| T2108 avg | 57.6% |
| 5d ratio min | 2.09 |
| 5d ratio max | 2.48 |
| 5d ratio avg | 2.21 |
| Days 5d ratio ≥ 2.0 | 5 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.77 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +3.0% |
| Pre-period cyclical ETF ret (30d) | +1.8% |
| Pre-period leading sector | Defensive |

### Period 100: BULL — 2025-09-17 to 2025-09-18

**T2108: 54.3% → 59.8%** (rise of 5.5 points; max 59.8%)
**Net Primary: +763 → +1029** (range +763 to +1029, trend: improving)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 54.3% |
| T2108 max | 59.8% |
| T2108 avg | 57.0% |
| 5d ratio min | 2.07 |
| 5d ratio max | 2.11 |
| 5d ratio avg | 2.09 |
| Days 5d ratio ≥ 2.0 | 2 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 3.66 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.48 |
| Pre-period days 5d ≥ 2.0 | 4 |
| Pre-period defensive ETF ret (30d) | +0.3% |
| Pre-period cyclical ETF ret (30d) | +3.3% |
| Pre-period leading sector | Cyclical |

### Period 101: CORRECTION — 2025-09-18 to 2025-10-10

**T2108: 59.8% → 25.5%** (drop of 34.3 points; min 25.5%)
**Net Primary: +1029 → +387** (range +387 to +1029, trend: deteriorating)
**Duration: 17 trading days**

| Metric | Value |
|---|---|
| T2108 min | 25.5% |
| T2108 max | 59.8% |
| T2108 avg | 47.1% |
| 5d ratio min | 0.70 |
| 5d ratio max | 2.26 |
| 5d ratio avg | 1.72 |
| Days 5d ratio ≥ 2.0 | 5 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.27 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |
| Pre-period defensive ETF ret (30d) | -0.2% |
| Pre-period cyclical ETF ret (30d) | +3.6% |
| Pre-period leading sector | Cyclical |

### Period 102: BULL — 2025-10-10 to 2025-10-14

**T2108: 25.5% → 35.6%** (rise of 10.1 points; max 35.6%)
**Net Primary: +387 → +708** (range +387 to +708, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 25.5% |
| T2108 max | 35.6% |
| T2108 avg | 30.3% |
| 5d ratio min | 0.69 |
| 5d ratio max | 0.91 |
| 5d ratio avg | 0.77 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.67 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.26 |
| Pre-period days 5d ≥ 2.0 | 3 |
| Pre-period defensive ETF ret (30d) | +5.5% |
| Pre-period cyclical ETF ret (30d) | +1.8% |
| Pre-period leading sector | Defensive |

### Period 103: CORRECTION — 2025-10-14 to 2025-10-16

**T2108: 35.6% → 29.4%** (drop of 6.2 points; min 29.4%)
**Net Primary: +708 → +525** (range +525 to +756, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 29.4% |
| T2108 max | 35.6% |
| T2108 avg | 33.4% |
| 5d ratio min | 0.68 |
| 5d ratio max | 0.91 |
| 5d ratio avg | 0.82 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.39 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |
| Pre-period defensive ETF ret (30d) | +4.2% |
| Pre-period cyclical ETF ret (30d) | -1.0% |
| Pre-period leading sector | Defensive |

### Period 104: BULL — 2025-10-16 to 2025-10-27

**T2108: 29.4% → 43.0%** (rise of 13.6 points; max 43.0%)
**Net Primary: +525 → +643** (range +377 to +643, trend: improving)
**Duration: 8 trading days**

| Metric | Value |
|---|---|
| T2108 min | 29.4% |
| T2108 max | 43.0% |
| T2108 avg | 37.0% |
| 5d ratio min | 0.63 |
| 5d ratio max | 1.43 |
| 5d ratio avg | 1.07 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.02 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.87 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | +5.6% |
| Pre-period cyclical ETF ret (30d) | -0.5% |
| Pre-period leading sector | Defensive |

### Period 105: CORRECTION — 2025-10-27 to 2025-11-04

**T2108: 43.0% → 27.7%** (drop of 15.3 points; min 27.7%)
**Net Primary: +643 → -94** (range -94 to +643, trend: deteriorating)
**Duration: 7 trading days**

| Metric | Value |
|---|---|
| T2108 min | 27.7% |
| T2108 max | 43.0% |
| T2108 avg | 33.7% |
| 5d ratio min | 0.49 |
| 5d ratio max | 1.27 |
| 5d ratio avg | 0.92 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 0.84 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |
| Pre-period defensive ETF ret (30d) | +6.9% |
| Pre-period cyclical ETF ret (30d) | +0.3% |
| Pre-period leading sector | Defensive |

### Period 106: BULL — 2025-11-04 to 2025-11-12

**T2108: 27.7% → 42.6%** (rise of 14.9 points; max 42.6%)
**Net Primary: -94 → -65** (range -203 to +19, trend: improving)
**Duration: 7 trading days**

| Metric | Value |
|---|---|
| T2108 min | 27.7% |
| T2108 max | 42.6% |
| T2108 avg | 35.7% |
| 5d ratio min | 0.49 |
| 5d ratio max | 1.12 |
| 5d ratio avg | 0.74 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 6 |
| BO:BD avg ratio | 1.33 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.27 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | +0.0% |
| Pre-period cyclical ETF ret (30d) | +0.0% |
| Pre-period leading sector | Cyclical |

### Period 107: CORRECTION — 2025-11-12 to 2025-11-13

**T2108: 42.6% → 37.2%** (drop of 5.4 points; min 37.2%)
**Net Primary: -65 → -278** (range -278 to -65, trend: deteriorating)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 37.2% |
| T2108 max | 42.6% |
| T2108 avg | 39.9% |
| 5d ratio min | 0.90 |
| 5d ratio max | 1.07 |
| 5d ratio avg | 0.99 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 2 |
| BO:BD avg ratio | 0.76 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |
| Pre-period defensive ETF ret (30d) | +4.3% |
| Pre-period cyclical ETF ret (30d) | +1.9% |
| Pre-period leading sector | Defensive |

### Period 108: BULL — 2025-11-13 to 2025-11-13

**T2108: 37.2% → 37.2%** (rise of 0.0 points; max 37.2%)
**Net Primary: -278 → -278** (range -278 to -278, trend: deteriorating)
**Duration: 1 trading days**

| Metric | Value |
|---|---|
| T2108 min | 37.2% |
| T2108 max | 37.2% |
| T2108 avg | 37.2% |
| 5d ratio min | 0.90 |
| 5d ratio max | 0.90 |
| 5d ratio avg | 0.90 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 0.13 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.12 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | +5.1% |
| Pre-period cyclical ETF ret (30d) | +1.5% |
| Pre-period leading sector | Defensive |

### Period 109: CORRECTION — 2025-11-13 to 2025-11-20

**T2108: 37.2% → 25.4%** (drop of 11.8 points; min 25.4%)
**Net Primary: -278 → -751** (range -751 to -278, trend: deteriorating)
**Duration: 6 trading days**

| Metric | Value |
|---|---|
| T2108 min | 25.4% |
| T2108 max | 37.2% |
| T2108 avg | 30.9% |
| 5d ratio min | 0.40 |
| 5d ratio max | 0.90 |
| 5d ratio avg | 0.59 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 6 |
| BO:BD avg ratio | 0.54 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |
| Pre-period defensive ETF ret (30d) | +5.1% |
| Pre-period cyclical ETF ret (30d) | +1.5% |
| Pre-period leading sector | Defensive |

### Period 110: BULL — 2025-11-20 to 2025-12-03

**T2108: 25.4% → 53.4%** (rise of 28.1 points; max 53.4%)
**Net Primary: -751 → +65** (range -751 to +65, trend: improving)
**Duration: 9 trading days**

| Metric | Value |
|---|---|
| T2108 min | 25.4% |
| T2108 max | 53.4% |
| T2108 avg | 43.6% |
| 5d ratio min | 0.40 |
| 5d ratio max | 5.76 |
| 5d ratio avg | 1.75 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 7 |
| BO:BD avg ratio | 3.96 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 0.90 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | +3.2% |
| Pre-period cyclical ETF ret (30d) | -3.3% |
| Pre-period leading sector | Defensive |

### Period 111: CORRECTION — 2025-12-03 to 2025-12-08

**T2108: 53.4% → 47.3%** (drop of 6.1 points; min 47.3%)
**Net Primary: +65 → +76** (range +65 to +187, trend: improving)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 47.3% |
| T2108 max | 53.4% |
| T2108 avg | 51.0% |
| 5d ratio min | 1.26 |
| 5d ratio max | 2.05 |
| 5d ratio avg | 1.54 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 3.18 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +4.9% |
| Pre-period cyclical ETF ret (30d) | -0.9% |
| Pre-period leading sector | Defensive |

### Period 112: BULL — 2025-12-08 to 2025-12-11

**T2108: 47.3% → 57.2%** (rise of 9.9 points; max 57.2%)
**Net Primary: +76 → +411** (range +76 to +411, trend: improving)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 47.3% |
| T2108 max | 57.2% |
| T2108 avg | 51.3% |
| 5d ratio min | 1.72 |
| 5d ratio max | 2.52 |
| 5d ratio avg | 2.11 |
| Days 5d ratio ≥ 2.0 | 3 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.07 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.70 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | +2.3% |
| Pre-period cyclical ETF ret (30d) | +0.8% |
| Pre-period leading sector | Defensive |

### Period 113: CORRECTION — 2025-12-11 to 2025-12-31

**T2108: 57.2% → 46.3%** (drop of 10.9 points; min 46.3%)
**Net Primary: +411 → -81** (range -81 to +411, trend: deteriorating)
**Duration: 14 trading days**

| Metric | Value |
|---|---|
| T2108 min | 46.3% |
| T2108 max | 57.2% |
| T2108 avg | 51.7% |
| 5d ratio min | 0.45 |
| 5d ratio max | 2.03 |
| 5d ratio avg | 1.20 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 4 |
| BO:BD avg ratio | 1.01 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | -0.3% |
| Pre-period cyclical ETF ret (30d) | +1.2% |
| Pre-period leading sector | Cyclical |

### Period 114: BULL — 2025-12-31 to 2026-01-15

**T2108: 46.3% → 66.9%** (rise of 20.6 points; max 66.9%)
**Net Primary: -81 → +676** (range -81 to +676, trend: improving)
**Duration: 11 trading days**

| Metric | Value |
|---|---|
| T2108 min | 46.3% |
| T2108 max | 66.9% |
| T2108 avg | 58.3% |
| 5d ratio min | 0.57 |
| 5d ratio max | 2.74 |
| 5d ratio avg | 1.83 |
| Days 5d ratio ≥ 2.0 | 5 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 2.09 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.56 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | -0.5% |
| Pre-period cyclical ETF ret (30d) | +2.3% |
| Pre-period leading sector | Cyclical |

### Period 115: CORRECTION — 2026-01-15 to 2026-01-20

**T2108: 66.9% → 58.6%** (drop of 8.3 points; min 58.6%)
**Net Primary: +676 → +425** (range +425 to +676, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 58.6% |
| T2108 max | 66.9% |
| T2108 avg | 63.6% |
| 5d ratio min | 1.03 |
| 5d ratio max | 1.57 |
| 5d ratio avg | 1.34 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.04 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +2.0% |
| Pre-period cyclical ETF ret (30d) | +2.7% |
| Pre-period leading sector | Cyclical |

### Period 116: BULL — 2026-01-20 to 2026-01-22

**T2108: 58.6% → 64.9%** (rise of 6.2 points; max 64.9%)
**Net Primary: +425 → +769** (range +425 to +769, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 58.6% |
| T2108 max | 64.9% |
| T2108 avg | 62.7% |
| 5d ratio min | 1.03 |
| 5d ratio max | 1.61 |
| 5d ratio avg | 1.34 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 3.21 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.22 |
| Pre-period days 5d ≥ 2.0 | 1 |
| Pre-period defensive ETF ret (30d) | +0.7% |
| Pre-period cyclical ETF ret (30d) | +2.1% |
| Pre-period leading sector | Cyclical |

### Period 117: CORRECTION — 2026-01-22 to 2026-02-05

**T2108: 64.9% → 53.5%** (drop of 11.4 points; min 53.5%)
**Net Primary: +769 → -53** (range -53 to +769, trend: deteriorating)
**Duration: 11 trading days**

| Metric | Value |
|---|---|
| T2108 min | 53.5% |
| T2108 max | 64.9% |
| T2108 avg | 58.0% |
| 5d ratio min | 0.46 |
| 5d ratio max | 1.77 |
| 5d ratio avg | 1.00 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 1.12 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +1.9% |
| Pre-period cyclical ETF ret (30d) | +1.4% |
| Pre-period leading sector | Defensive |

### Period 118: BULL — 2026-02-05 to 2026-02-10

**T2108: 53.5% → 61.6%** (rise of 8.1 points; max 61.6%)
**Net Primary: -53 → +390** (range -53 to +428, trend: improving)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 53.5% |
| T2108 max | 61.6% |
| T2108 avg | 58.7% |
| 5d ratio min | 0.46 |
| 5d ratio max | 0.92 |
| 5d ratio avg | 0.74 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 2.83 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 0.71 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | -0.9% |
| Pre-period cyclical ETF ret (30d) | +0.9% |
| Pre-period leading sector | Cyclical |

### Period 119: CORRECTION — 2026-02-10 to 2026-03-20

**T2108: 61.6% → 16.7%** (drop of 44.8 points; min 16.7%)
**Net Primary: +390 → -743** (range -743 to +390, trend: deteriorating)
**Duration: 28 trading days**

| Metric | Value |
|---|---|
| T2108 min | 16.7% |
| T2108 max | 61.6% |
| T2108 avg | 42.3% |
| 5d ratio min | 0.57 |
| 5d ratio max | 1.64 |
| 5d ratio avg | 0.93 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 11 |
| BO:BD avg ratio | 1.43 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |
| Pre-period defensive ETF ret (30d) | -0.1% |
| Pre-period cyclical ETF ret (30d) | +1.3% |
| Pre-period leading sector | Cyclical |

### Period 120: BULL — 2026-03-20 to 2026-03-25

**T2108: 16.7% → 24.5%** (rise of 7.8 points; max 24.5%)
**Net Primary: -743 → -397** (range -743 to -397, trend: improving)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 16.7% |
| T2108 max | 24.5% |
| T2108 avg | 21.3% |
| 5d ratio min | 0.50 |
| 5d ratio max | 0.79 |
| 5d ratio avg | 0.62 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 4 |
| BO:BD avg ratio | 1.65 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |
| Pre-period 5d max (5d before) | 0.79 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | -5.0% |
| Pre-period cyclical ETF ret (30d) | -3.7% |
| Pre-period leading sector | Cyclical |

### Period 121: CORRECTION — 2026-03-25 to 2026-03-27

**T2108: 24.5% → 19.2%** (drop of 5.3 points; min 19.2%)
**Net Primary: -397 → -778** (range -778 to -397, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 19.2% |
| T2108 max | 24.5% |
| T2108 avg | 22.0% |
| 5d ratio min | 0.72 |
| 5d ratio max | 0.79 |
| 5d ratio avg | 0.74 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 3 |
| BO:BD avg ratio | 1.15 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |
| Pre-period defensive ETF ret (30d) | -7.5% |
| Pre-period cyclical ETF ret (30d) | -3.3% |
| Pre-period leading sector | Cyclical |

### Period 122: BULL — 2026-03-27 to 2026-04-20

**T2108: 19.2% → 63.0%** (rise of 43.8 points; max 63.0%)
**Net Primary: -778 → +718** (range -880 to +718, trend: improving)
**Duration: 16 trading days**

| Metric | Value |
|---|---|
| T2108 min | 19.2% |
| T2108 max | 63.0% |
| T2108 avg | 40.8% |
| 5d ratio min | 0.52 |
| 5d ratio max | 3.84 |
| 5d ratio avg | 2.02 |
| Days 5d ratio ≥ 2.0 | 10 |
| Days Net Primary < 0 | 10 |
| BO:BD avg ratio | 3.01 |
| Classification | 🔴 DEEP CORRECTION (T2108 < 20%) |
| Pre-period 5d max (5d before) | 0.79 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | -6.9% |
| Pre-period cyclical ETF ret (30d) | -5.7% |
| Pre-period leading sector | Cyclical |

### Period 123: CORRECTION — 2026-04-20 to 2026-04-29

**T2108: 63.0% → 54.9%** (drop of 8.1 points; min 54.9%)
**Net Primary: +718 → +215** (range +215 to +718, trend: deteriorating)
**Duration: 8 trading days**

| Metric | Value |
|---|---|
| T2108 min | 54.9% |
| T2108 max | 63.0% |
| T2108 avg | 59.5% |
| 5d ratio min | 0.60 |
| 5d ratio max | 3.23 |
| 5d ratio avg | 1.47 |
| Days 5d ratio ≥ 2.0 | 2 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.19 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +2.9% |
| Pre-period cyclical ETF ret (30d) | +7.0% |
| Pre-period leading sector | Cyclical |

### Period 124: BULL — 2026-04-29 to 2026-05-06

**T2108: 54.9% → 60.6%** (rise of 5.8 points; max 60.6%)
**Net Primary: +215 → +782** (range +215 to +782, trend: improving)
**Duration: 6 trading days**

| Metric | Value |
|---|---|
| T2108 min | 54.9% |
| T2108 max | 60.6% |
| T2108 avg | 57.8% |
| 5d ratio min | 0.60 |
| 5d ratio max | 2.05 |
| 5d ratio avg | 1.30 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.13 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.92 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | +0.2% |
| Pre-period cyclical ETF ret (30d) | +10.0% |
| Pre-period leading sector | Cyclical |

### Period 125: CORRECTION — 2026-05-06 to 2026-05-19

**T2108: 60.6% → 38.9%** (drop of 21.8 points; min 38.9%)
**Net Primary: +782 → +73** (range +73 to +782, trend: deteriorating)
**Duration: 10 trading days**

| Metric | Value |
|---|---|
| T2108 min | 38.9% |
| T2108 max | 60.6% |
| T2108 avg | 49.4% |
| 5d ratio min | 0.69 |
| 5d ratio max | 2.05 |
| 5d ratio avg | 1.15 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 0.98 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |
| Pre-period defensive ETF ret (30d) | -0.4% |
| Pre-period cyclical ETF ret (30d) | +7.7% |
| Pre-period leading sector | Cyclical |

### Period 126: BULL — 2026-05-19 to 2026-05-20

**T2108: 38.9% → 53.0%** (rise of 14.1 points; max 53.0%)
**Net Primary: +73 → +43** (range +43 to +73, trend: deteriorating)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 38.9% |
| T2108 max | 53.0% |
| T2108 avg | 45.9% |
| 5d ratio min | 0.66 |
| 5d ratio max | 0.69 |
| 5d ratio avg | 0.68 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 0.66 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.16 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | -1.8% |
| Pre-period cyclical ETF ret (30d) | +1.9% |
| Pre-period leading sector | Cyclical |

### Period 127: CORRECTION — 2026-05-20 to 2026-05-21

**T2108: 53.0% → 46.5%** (drop of 6.5 points; min 46.5%)
**Net Primary: +43 → +399** (range +43 to +399, trend: improving)
**Duration: 2 trading days**

| Metric | Value |
|---|---|
| T2108 min | 46.5% |
| T2108 max | 53.0% |
| T2108 avg | 49.7% |
| 5d ratio min | 0.66 |
| 5d ratio max | 0.74 |
| 5d ratio avg | 0.70 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.12 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | -0.8% |
| Pre-period cyclical ETF ret (30d) | +1.0% |
| Pre-period leading sector | Cyclical |

### Period 128: BULL — 2026-05-21 to 2026-05-26

**T2108: 46.5% → 50.1%** (rise of 3.6 points; max 50.1%)
**Net Primary: +399 → +590** (range +399 to +590, trend: improving)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 46.5% |
| T2108 max | 50.1% |
| T2108 avg | 48.1% |
| 5d ratio min | 0.74 |
| 5d ratio max | 1.79 |
| 5d ratio avg | 1.24 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 3.03 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.06 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | +0.4% |
| Pre-period cyclical ETF ret (30d) | +2.9% |
| Pre-period leading sector | Cyclical |

### Period 129: CORRECTION — 2026-05-26 to 2026-06-03

**T2108: 50.1% → 39.3%** (drop of 10.8 points; min 39.3%)
**Net Primary: +590 → +502** (range +502 to +777, trend: deteriorating)
**Duration: 7 trading days**

| Metric | Value |
|---|---|
| T2108 min | 39.3% |
| T2108 max | 50.1% |
| T2108 avg | 46.0% |
| 5d ratio min | 1.29 |
| 5d ratio max | 2.94 |
| 5d ratio avg | 2.12 |
| Days 5d ratio ≥ 2.0 | 4 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 2.00 |
| Classification | 🟡 SHALLOW CORRECTION (T2108 20-40%) |
| Pre-period defensive ETF ret (30d) | +2.9% |
| Pre-period cyclical ETF ret (30d) | +2.9% |
| Pre-period leading sector | Defensive |

### Period 130: BULL — 2026-06-03 to 2026-06-12

**T2108: 39.3% → 50.2%** (rise of 10.9 points; max 50.2%)
**Net Primary: +502 → +535** (range +232 to +642, trend: improving)
**Duration: 8 trading days**

| Metric | Value |
|---|---|
| T2108 min | 39.3% |
| T2108 max | 50.2% |
| T2108 avg | 43.4% |
| 5d ratio min | 0.59 |
| 5d ratio max | 1.63 |
| 5d ratio avg | 0.94 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.81 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 2.94 |
| Pre-period days 5d ≥ 2.0 | 4 |
| Pre-period defensive ETF ret (30d) | -0.4% |
| Pre-period cyclical ETF ret (30d) | +4.9% |
| Pre-period leading sector | Cyclical |

### Period 131: CORRECTION — 2026-06-12 to 2026-06-17

**T2108: 50.2% → 42.9%** (drop of 7.3 points; min 42.9%)
**Net Primary: +535 → +452** (range +452 to +572, trend: deteriorating)
**Duration: 4 trading days**

| Metric | Value |
|---|---|
| T2108 min | 42.9% |
| T2108 max | 50.2% |
| T2108 avg | 47.8% |
| 5d ratio min | 1.60 |
| 5d ratio max | 1.68 |
| 5d ratio avg | 1.64 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.12 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +3.5% |
| Pre-period cyclical ETF ret (30d) | +0.1% |
| Pre-period leading sector | Defensive |

### Period 132: BULL — 2026-06-17 to 2026-07-16

**T2108: 42.9% → 56.6%** (rise of 13.6 points; max 56.6%)
**Net Primary: +452 → +143** (range +143 to +686, trend: deteriorating)
**Duration: 20 trading days**

| Metric | Value |
|---|---|
| T2108 min | 42.9% |
| T2108 max | 56.6% |
| T2108 avg | 50.0% |
| 5d ratio min | 0.63 |
| 5d ratio max | 2.03 |
| 5d ratio avg | 1.20 |
| Days 5d ratio ≥ 2.0 | 1 |
| Days Net Primary < 0 | 0 |
| BO:BD avg ratio | 1.32 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 1.68 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | +4.4% |
| Pre-period cyclical ETF ret (30d) | +2.5% |
| Pre-period leading sector | Defensive |

### Period 133: CORRECTION — 2026-07-16 to 2026-07-20

**T2108: 56.6% → 49.4%** (drop of 7.2 points; min 49.4%)
**Net Primary: +143 → -55** (range -55 to +143, trend: deteriorating)
**Duration: 3 trading days**

| Metric | Value |
|---|---|
| T2108 min | 49.4% |
| T2108 max | 56.6% |
| T2108 avg | 53.1% |
| 5d ratio min | 0.68 |
| 5d ratio max | 0.77 |
| 5d ratio avg | 0.72 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 1 |
| BO:BD avg ratio | 0.65 |
| Classification | Normal |
| Pre-period defensive ETF ret (30d) | +2.8% |
| Pre-period cyclical ETF ret (30d) | -0.5% |
| Pre-period leading sector | Defensive |

### Period 134: BULL — 2026-07-20 to 2026-07-24

**T2108: 49.4% → 51.0%** (rise of 1.6 points; max 51.4%)
**Net Primary: -55 → -199** (range -199 to +75, trend: deteriorating)
**Duration: 5 trading days**

| Metric | Value |
|---|---|
| T2108 min | 47.2% |
| T2108 max | 51.4% |
| T2108 avg | 50.0% |
| 5d ratio min | 0.77 |
| 5d ratio max | 1.00 |
| 5d ratio avg | 0.90 |
| Days 5d ratio ≥ 2.0 | 0 |
| Days Net Primary < 0 | 4 |
| BO:BD avg ratio | 1.14 |
| Classification | Normal |
| Pre-period 5d max (5d before) | 0.93 |
| Pre-period days 5d ≥ 2.0 | 0 |
| Pre-period defensive ETF ret (30d) | +5.9% |
| Pre-period cyclical ETF ret (30d) | -1.3% |
| Pre-period leading sector | Defensive |

## Limitations

1. **2024 OHLCV gap**: daily_ohlcv has only ~19 dates in 2024 (backfill was ~500 days from Jul 2026 ≈ Feb 2025). For 2024 periods, T2108/Net Primary/BO/BD/5d ratio are available from MM data, but 20% study, follow-through, and per-ticker scans are NOT.
2. **ETF sector RS**: Only available from Dec 4, 2024. Periods starting before this date have no sector RS analysis.
3. **T2108 swing threshold**: 5-point threshold is heuristic. Smaller swings (<5 points) are not counted as full corrections/bull trends.
4. **Peak/trough detection**: Uses running high/low with reset on new period. This may merge adjacent small swings into one period or split one large move if there is a counter-trend bounce >5 points.
5. **No LLM judge for 2024**: The LLM judge was only run on Jan-Jul 2026 sessions. 2024 periods are identified by T2108 alone, not cross-validated against regime labels.

## Cross-Reference

- [[Market Regime Validation - Jan-Jul 2026]] — detailed Jan-Jul 2026 analysis with LLM judge validation
- [[Market Monitor]] — T2108, Net Primary, BO/BD definitions
- [[Calibration - Definitions and Gaps]] — calibration methodology
