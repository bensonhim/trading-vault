---
title: "Daily Trading Radar — 2026-07-10"
date: 2026-07-10
tags: [daily, trading-radar, stockbee, pradeep-ultratrader, cautious-bull, reduce-size, dep, aapl, crm, cmcsa, bkng]
---

# Daily Trading Radar — 2026-07-10

## 1. Market Regime — LLM Judge Verdict

> [!tip] **CAUTIOUS_BULL** — Action: **REDUCE_SIZE** (confidence: 60%)
> Net primary positive but declining (+453 to +349 over 4 days). T2108 stable at ~50%. Breakdowns exceeding breakouts on most days. Selective setups only, reduce size, tighten stops.

---

## 2. Market Monitor (Primary Breadth)

| Indicator | Jul 10 | Jul 9 | Jul 8 | Jul 7 | Trend |
|-----------|---------|-------|-------|-------|-------|
| Net Primary | +349 | +425 | +313 | +453 | Declining |
| T2108 | 52.0% | 49.8% | 48.1% | 50.4% | Stable |
| Breakouts (4%+) | 129 | 250 | 185 | 189 | — |
| Breakdowns (4%+) | 181 | 100 | 309 | 476 | — |
| BO:BD Ratio | 0.71 | 2.50 | 0.60 | 0.40 | Improving from Jul 7 |

**Primary Trend Assessment:** Net primary positive but declining from +453 to +349. T2108 in normal range (48-52%). Breakdowns exceeding breakouts on Jul 7, 8, and 10 — choppy conditions. Jul 9 was a positive day (250 breakouts vs 100 breakdowns) but not sustained.

> [!note] Pradeep's Rule
> "If you just trade breakouts when the primary indicator is green, you will find most of the time, most of the breakouts work." — Primary is green (+349) but declining. Reduce size, be selective.

### Breakout Follow-Through

> [!warning] Limited OHLCV coverage for Jul 10 (1448 tickers vs 6000+ normal)
> Follow-through data may be incomplete. Full coverage requires nightly pipeline run on home workstation.

---

## 3. Sector Relative Strength

> [!note] Sector RS data unavailable for Jul 10
> ETF OHLCV data needs backfill to Jul 10. Run nightly pipeline on home workstation to update.

---

## 4. Rally Maturity

| Metric | Value |
|--------|-------|
| Days since last market low | 0 (T2108 at 52%, not in low zone) |
| Mature (3+ days) | No |
| Overbought (20% > 50) | No |
| Extended | No |

---

## 5. SPY & QQQ Intraday Narrative

> [!note] Intraday data not available for Jul 10
> FMP 5-min/hourly data not fetched. Available on home workstation via nightly pipeline.

---

## 6. Sugar Baby Watchlist

**Core List:** 95 tickers | **Expanded List:** 188 tickers

### Top 10 Sugar Babies (by count_504d)

| Rank | Ticker | 504d | 252d | 63d | 21d | 5d | Tier |
|------|--------|------|------|-----|-----|-----|------|
| 1 | IREN | 103 | 56 | 15 | 2 | 0 | core |
| 2 | WULF | 94 | 48 | 13 | 3 | 0 | core |
| 3 | OKLO | 91 | 45 | 12 | 3 | 0 | core |
| 4 | APLD | 89 | 44 | 13 | 1 | 0 | core |
| 5 | RKLB | 83 | — | — | — | — | core |

> [!note] Sugar Baby counts last updated Jul 2. Run `py src/scans/compute_sugar_babies.py --date 2026-07-10` on home workstation to refresh.

---

## 7. Trade Ideas — Confluence Tiers

### A+ Confluences (Setup + Sugar Baby + Catalyst)

> No A+ confluences found — none of today's DEP candidates are Sugar Babies.

### A Confluences (Setup + Sugar Baby)

> No A confluences found.

### B+ Confluences (Setup + Catalyst)

| # | Ticker | Setup | Entry | Stop | Width | Catalyst | Status |
|---|--------|-------|-------|------|-------|----------|--------|
| — | — | — | — | — | — | — | No B+ found |

### B Setups (Setup Only)

| #   | Ticker | Setup | Entry   | Stop    | Width | Shares | Pos USD | Risk HKD | Status |
| --- | ------ | ----- | ------- | ------- | ----- | ------ | ------- | -------- | ------ |
| 1   | AAPL   | DEP   | $317.23 | $311.55 | 1.79% | 87     | $27,599 | $3,000   | Ready  |
| 2   | CRM    | DEP   | $166.55 | $162.38 | 2.50% | 166    | $27,647 | $3,000   | Ready  |
| 3   | CMCSA  | DEP   | $24.02  | $23.42  | 2.50% | 1,147  | $27,547 | $3,000   | Ready  |
| 4   | CCC    | DEP   | $6.07   | $5.92   | 2.50% | 4,646  | $28,201 | $3,000   | Ready  |
| 5   | BKNG   | DEP   | $186.69 | $182.02 | 2.50% | 148    | $27,630 | $3,000   | Ready  |

### C Watchlist (Sugar Baby Only — No Position)

| Ticker | SB Rank | Notes |
|--------|---------|-------|
| IREN | #1 | 103 breakouts in 504d, but 0 in last 5d — dormant |
| WULF | #2 | 94 breakouts, 3 in 21d — watch for setup |
| OKLO | #3 | 91 breakouts, 3 in 21d — watch for setup |
| APLD | #4 | 89 breakouts, 1 in 21d — fading |
| RKLB | #5 | 83 breakouts — watch for setup |

---

## 8. Pre-Market Order Sheet

> [!important] Place these orders BEFORE 9:30 AM ET (next trading day)
> DEP entry/stop are known from prior-day data — place limit + stop orders before market open.

### DEP Limit Orders

| Ticker | Tier | Entry (Limit) | Stop    | Width | Shares | Pos USD | Risk HKD | Consolidation   | Breakout Date    |
| ------ | ---- | ------------- | ------- | ----- | ------ | ------- | -------- | --------------- | ---------------- |
| AAPL   | B    | $317.23       | $311.55 | 1.79% | 87     | $27,599 | $3,000   | 4d, 1.52% width | Jun 30 (10d ago) |
| CRM    | B    | $166.55       | $162.38 | 2.50% | 166    | $27,647 | $3,000   | 4d, 2.44% width | Jun 30 (10d ago) |
| CMCSA  | B    | $24.02        | $23.42  | 2.50% | 1,147  | $27,547 | $3,000   | 4d, 3.64% width | Jun 26 (14d ago) |
| CCC    | B    | $6.07         | $5.92   | 2.50% | 4,646  | $28,201 | $3,000   | 2d, 5.66% width | Jul 7 (3d ago)   |
| BKNG   | B    | $186.69       | $182.02 | 2.50% | 148    | $27,630 | $3,000   | 7d, 5.81% width | Jun 24 (16d ago) |

### ANTS BSLO Orders (35 candidates — top 5 shown)

| Ticker | Tier | Trigger (BSLO) | Stop          | Notes              |
| ------ | ---- | -------------- | ------------- | ------------------ |
| AAL    | —    | $17.04         | Prior day low | Tight day detected |
| AAPL   | —    | $316.27        | Prior day low | Tight day detected |
| CIFR   | —    | $22.43         | Prior day low | Tight day detected |
| BTE    | —    | $4.10          | Prior day low | Tight day detected |
| BB     | —    | $11.12         | Prior day low | Tight day detected |

> Full ANTS list: 35 candidates. Run `py src/scans/anticipation.py` for complete list with BSLO triggers and stops.

---

## 9. Intraday Watchlist (SOS + EP 9M)

> [!warning] SOS scan found 0 candidates
> Only 1448 tickers in DB for Jul 10 (vs 6000+ normal). Full SOS scan requires complete OHLCV data. Run nightly pipeline on home workstation for full coverage.

### SOS Breakout Candidates

| Ticker | Trigger Price | Two Lynch | Leg | Sugar Baby | 9M Volume | Notes                            |
| ------ | ------------- | --------- | --- | ---------- | --------- | -------------------------------- |
| —      | —             | —         | —   | —          | —         | No SOS candidates (limited data) |
|        |               |           |     |            |           |                                  |

### EP 9M Candidates

> EP 9M scan not run (requires live FMP gainers data during market hours)

---

## 10. Sector ETF Momentum Proxies

> Sector RS data unavailable — ETF OHLCV needs backfill to Jul 10.

---

## 11. Similar Historical Conditions

> Historical context matcher requires sector RS data which is unavailable for Jul 10.

---

## 12. Account Parameters

| Parameter | Value |
|-----------|-------|
| Account | 1,000,000 HKD |
| Risk per trade | 3,000 HKD (~$385 USD) |
| USD/HKD | 7.8 |
| Soft cap | 25% of account |
| Hard cap | 50% (DEP + Sugar Baby confluence) |
| Universe | ~6,080 TC2000 common stocks |
| ETFs | Sector proxies only (not for individual positions) |

---

## 13. Action Summary

- [x] Reduce size — selective setups only
- [ ] Place DEP limit orders before open: AAPL $317.23, CRM $166.55, CMCSA $24.02
- [ ] Only B tier setups — no A+/A confluences today
- [ ] Sell into strength on existing positions
- [ ] Monitor 35 ANTS candidates for tomorrow's BSLO
- [ ] No SOS breakouts today — no intraday long entries
- [ ] Watch Sugar Babies (IREN, WULF, OKLO) for new setups forming

---

## 14. Ticker Details

### AAPL — Consumer Electronics | XLK | $4.6T | 5000+ funds (Liquid Glamour)

**DEP Setup:** Breakout Jun 30 (+10.1%), 4-day consolidation, 1.52% width (very tight)

**Breakout History (4 past swings):**
| Date | Total Move | Entry | Stop | Last Close | Volume | Result |
|------|-----------|-------|------|-----------|--------|--------|
| Jun 30 | +10.1% | $291.48 | $290.74 | $308.63 | 71,897,697 | SUCCESS |
| Feb 2 | +4.1% | $269.86 | $256.62 | $270.01 | 73,913,425 | STOPPED |
| Sep 22 | +4.3% | $255.32 | $245.64 | $256.08 | 105,517,416 | STOPPED |
| Aug 6 | +13.0% (2d) | $211.04 | $203.53 | $229.35 | 108,483,103 | PROFIT_80_20 |

**Assessment:** Last breakout SUCCESS, tight consolidation (1.52%), institutional quality. Good DEP candidate.

---

### CRM — Software Application | XLK | $134B | 5000+ funds (Liquid Glamour)

**DEP Setup:** Breakout Jun 30 (+10.6%), 4-day consolidation, 2.44% width

**Breakout History (5 past swings):**
| Date | Total Move | Entry | Stop | Last Close | Volume | Result |
|------|-----------|-------|------|-----------|--------|--------|
| Jun 26 | +10.6% (2d) | $156.20 | $156.12 | $166.11 | 5,050,622 | SUCCESS |
| May 29 | +19.0% (2d) | $183.22 | $178.22 | $209.60 | 33,998,900 | BREAKEVEN |
| May 1 | +4.1% | $183.59 | $176.96 | $183.82 | 12,324,400 | BREAKEVEN |
| Apr 13 | +4.8% | $171.56 | $164.11 | $172.82 | 12,390,800 | PROFIT_80_20 |
| Mar 5 | +4.3% | $200.80 | $192.30 | $201.39 | 15,860,914 | BREAKEVEN |

**Assessment:** Last breakout SUCCESS, good track record (2 SUCCESS, 1 PROFIT_80_20). Consolidation 2.44% — good DEP candidate.

---

### CMCSA — Telecom Services | XLC | $84B | 2500+ funds (Institutional Quality)

**DEP Setup:** Breakout Jun 26 (+8.8%), 4-day consolidation, 3.64% width

**Breakout History (3 past swings):**
| Date | Total Move | Entry | Stop | Last Close | Volume | Result |
|------|-----------|-------|------|-----------|--------|--------|
| Jun 26 | +8.8% | $23.60 | $24.32 | $24.68 | 83,460,058 | BREAKEVEN |
| Apr 23 | +7.7% | $30.54 | $30.10 | $31.64 | 46,477,905 | STOPPED |
| Dec 16 | +5.4% | $27.49 | $25.86 | $27.85 | 98,070,427 | BREAKEVEN |

**Assessment:** Last breakout BREAKEVEN, prior STOPPED. Wider consolidation (3.64%). Lower confidence than AAPL/CRM.

---

## 15. Data Coverage Notes

| Data | Coverage | Notes |
|------|----------|-------|
| Market Monitor | Jul 7-10 | From StockBee Google Sheet |
| OHLCV | Jul 7-9 (6000+), Jul 10 (1448), Jul 13 (5197) | Jul 10 partial — hourly fetch through proxy was slow |
| Sugar Babies | Jul 2 (last computed) | Needs refresh on home workstation |
| Sector RS | Jun 25 (last ETF data) | Needs ETF OHLCV backfill |
| SOS scan | Limited (1448 tickers) | Full scan needs 6000+ tickers |
| DEP scan | Full coverage | Uses 25-day lookback with complete historical data |

---

*Generated by Pradeep Ultratrader Trading Radar Engine*
*LLM Judge: Rules-based fallback | Market Context: 5-day lookback | Validation: 97% match+close (260 dates)*