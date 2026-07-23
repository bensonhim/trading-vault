---
title: "Trade Ideas Validation — Pre-Fix Baseline (2024-2025)"
date: 2026-07-23
tags: [analysis, validation, trade-ideas, comparison, pre-fix, baseline, stockbee]
---

# Trade Ideas Validation — Pre-Fix Baseline (2024-2025)

Systematic comparison of 6 pre-fix Daily Trading Radar files against Pradeep Bonde's corresponding StockBee session notes. The radars were generated before the 7 fixes (tighten 20% study suppression, DEP market cap filter, SIPs fallback, RANGE_BOUND regime, follow-through as regime input, Cat/Dog/Liquid Lava, callout box enrichment). This establishes the baseline the fixes should improve upon.

---

## 2024-07-11

### Radar Regime vs Pradeep SA

| Source | Call |
|---|---|
| **Radar** | CAUTIOUS_BULL — REDUCE_SIZE. 20% study at 12, TI65 bullish 92, young momentum 11. SOS/DEP/ANTS suppressed. |
| **Pradeep** | Selective slow grinding bull. Breakouts working selectively. Focus on 9M breakout, delayed reaction, sugar babies. 20% study went 20→47 — buying came in. Biotech/solar/oil field leading. |

The radar called CAUTIOUS_BULL while Pradeep called "selective slow grinding bull." These are directionally aligned — both recognize selectivity is required. **However, the radar missed the key inflection**: the 20% study tripled (20→47) in 3 days, which Pradeep flagged as "buying came in." The radar treated 20% study at 12 (yesterday's reading) as the suppression trigger, but the live number had surged to 47. The pre-fix suppression logic was too rigid — it didn't account for rapid momentum shifts within the 5-day window.

> "The numbers were 20 just three days ago, and now they are 47. So buying came in."

### Setup Validation

| Setup | Radar | Pradeep | Match? |
|---|---|---|---|
| DEP | 0 candidates | Discussed delayed reaction as core focus | ❌ Missed — radar suppressed all DEP despite buying coming in |
| ANTS | 0 candidates | Not mentioned | N/A |
| SOS | Suppressed | 9M breakout = one of three core focuses | ❌ Suppressed wrong — 20% study was surging |
| SIPs | 30 found, 0 fresh catalyst | Not specifically discussed but AMD appeared | Partial — AMD was in radar SIPs |
| Sugar Babies | 20 listed | Discussed as core focus | ✅ Aligned |
| Shorts | 27 candidates (WSS, momentum inversion) | "Not much money on short side" | ❌ Radar over-generated shorts when Pradeep said shorts unattractive |

### Key Hits

- TI65 young momentum scan correct (11 stocks = few new trends, aligns with Pradeep's "selective" call)
- AMD appeared in both radar SIPs and Sugar Babies
- Breakout follow-through 3d=44.2% / 5d=41.8% = OK, consistent with Pradeep's "breakouts working selectively"

### Key Misses

- **20% study suppression too aggressive** — triggered on lagging data (12), ignored the live surge to 47
- **DEP/ANTS suppressed entirely** — Pradeep explicitly listed delayed reaction and 9M breakout as top 3 focuses
- **Short-side over-generation** — 27 short candidates when Pradeep said "not much money on short side"
- **No sector leadership call** — radar had empty Sector Relative Strength section; Pradeep identified biotech, solar, oil field as leaders

### Daily Scorecard

| Category | Score (0-10) | Notes |
|---|---|---|
| Regime | 5 | Direction right (selective bull) but missed the 20→47 inflection |
| Setups | 3 | Suppressed DEP/SOS when Pradeep wanted them; over-generated shorts |
| Overall | **4** | Radar was too defensive; Pradeep was more constructive |

---

## 2025-01-16

### Radar Regime vs Pradeep SA

| Source | Call |
|---|---|
| **Radar** | CAUTIOUS_BULL — REDUCE_SIZE. 20% study at 1, TI65 bullish 97, follow-through FAILING (5d=21.8%). SOS/DEP/ANTS suppressed. Selling spreading to 2 sectors. |
| **Pradeep** | Short-term bullish — tradable rally after positive CPI + strong bank earnings. T2108 25.51→30.94. "Will there be follow-through? And if there is, will it stick?" Chop year thesis. Very low conviction — "not a game changer." |

Directionally aligned again — both recognize a bounce with uncertain follow-through. The radar's CAUTIOUS_BULL is appropriate. **The radar correctly identified the follow-through problem** (5d=21.8% FAILING), which mirrors Pradeep's central question. However, the radar called REDUCE_SIZE while Pradeep was taking specific trades (DATS, AVGO, CRMD, Rumble). The radar was more defensive than Pradeep's actual behavior.

> "I have a very, very low expectation from the market currently."

> "It's not a game changer."

### Setup Validation

| Setup | Radar | Pradeep | Match? |
|---|---|---|---|
| DEP | 0 candidates | Rumble = "best-looking breakout of the day" (delayed reaction) | ❌ Missed delayed reaction entirely |
| ANTS | 0 candidates | Not discussed | N/A |
| SOS | Suppressed | DATS = EP 9M trade taken at $5.16 | ❌ Suppressed EP 9M when Pradeep was trading it |
| SIPs | 30 found, 30 fresh catalyst | Not the focus — Pradeep focused on specific setups | Partial |
| Sugar Babies | 20 listed | Not central to this session | N/A |
| Shorts | 29 candidates | Weak structure short (WSS) = primary strategy; SJM, UnitedHealth, Moderna | ✅ Aligned on short framework but radar didn't capture WSS methodology |
| FADE | 15 candidates | Pradeep said breakouts failing = "fading breakouts is a better strategy" | ✅ Good alignment |

### Key Hits

- **Follow-through FAILING call** — 5d=21.8% correctly identified systematic breakout failure
- **Selling spreading warning** — 2 sectors, aligns with Pradeep's "selling is going to spread"
- **FADE candidates** — 15 failing breakouts, Pradeep explicitly endorsed fading
- **Quantum stocks in SIPs** (RGTI, QBTS, IONQ) — Pradeep mentioned these as potential strong structure shorts

### Key Misses

- **EP 9M suppressed** — DATS was a live trade Pradeep took at $5.16 from the EP 9M scanner; radar had 0 candidates
- **Delayed reaction missed** — Rumble was "best breakout of the day" (delayed reaction), radar had 0 DEP
- **No Cat/Dog/Liquid Lava distinction** — Pradeep's 3-tier EP 9M framework (cats, dogs, liquid lava) not represented
- **WSS methodology absent** — Pradeep's Niagara fall criteria (3 days down 10%, weak bounce <3 days <2.5%) not in radar's short framework
- **Sector relative strength empty** — Pradeep identified banks (Citibank $20B buyback) as best sector; radar had no sector section

### Daily Scorecard

| Category | Score (0-10) | Notes |
|---|---|---|
| Regime | 7 | Good — follow-through FAILING call matched Pradeep's key question |
| Setups | 2 | Bad — missed DATS EP 9M trade, missed Rumble delayed reaction, suppressed everything |
| Overall | **4** | Regime was right but setup generation was almost completely wrong |

---

## 2025-04-16

### Radar Regime vs Pradeep SA

| Source | Call |
|---|---|
| **Radar** | CAUTIOUS_BULL — REDUCE_SIZE. 10-day ratio 0.78, monthly 25% ratio 0.12, TI65 bullish 204. ANTS suppressed. Selling spreading to 5 sectors. |
| **Pradeep** | Cautiously bullish, select breakouts working AM → **Bear market classification** by PM. Powell speech triggered range expansion down. T2108 flat 16.38. Three bull-market sectors (tech, biotech, consumer discretionary) ALL in purgatory. NOT a bull market start. |

This is the most significant regime miss. The radar called CAUTIOUS_BULL all day, but by the PM session Pradeep had classified it as a **bear market** (event-driven + cyclical). The radar's CAUTIOUS_BULL with REDUCE_SIZE was too optimistic. The correct call was RANGE_BOUND or BEARISH after Powell's range expansion down. The pre-fix regime logic had no RANGE_BOUND state and couldn't capture the intraday regime shift.

> "The three sectors that lead a bull market — technology, biotech, consumer discretionary — are ALL in purgatory."

> "This is a self-inflicted policy error bear market."

> "If you understand just one thing in trading — range expansion — you'll know."

### Setup Validation

| Setup | Radar | Pradeep | Match? |
|---|---|---|---|
| DEP | 4 candidates (NEM, B, UNH, CVS) | Not discussed — Pradeep focused on shorts and first-leg formations | Partial — DEP existed but Pradeep wasn't trading them |
| SOS | 5 candidates (ADMA, PM, CTGO, RAY, SXTP) | Not endorsed; first legs "not ready yet" | ❌ Pradeep said first legs need 2-3 more days |
| ANTS | Suppressed | Not discussed | N/A |
| SIPs | 30 found, 6 fresh catalyst | UAL, Hertz, MP Materials discussed as SIPs | ✅ MP appeared in both radar WSS short and Pradeep's SIPs |
| Shorts | 26 candidates (WSS, sugar baby short, momentum inversion) | **Excellent short setups**: Walmart ($91.85), BMY, Disney, AbbVie, TQQ/SQQ/SPXS | ✅ Short-side aligned — both identified short opportunity |
| Sugar Babies | 20 listed | Not central | N/A |

### Key Hits

- **Short-side setup generation** — 26 candidates; Pradeep said "some really good setups today" for shorts
- **Selling spreading to 5 sectors** — correctly identified deteriorating breadth
- **SOS ADMA** — appeared in radar; Pradeep mentioned healthcare precursor sector (ADMA, SXTP)
- **UNH in both DEP long and WSS short** — radar captured both sides; Pradeep shorted UNH
- **Breakout follow-through OK** (5d=43.3%) — consistent with "select breakouts working" in AM

### Key Misses

- **Regime too bullish** — CAUTIOUS_BULL all day; Pradeep classified bear market by PM
- **No range expansion signal** — Pradeep's #1 framework ("range expansion is the one thing") not captured
- **Gold/silver/mining leadership missed** — radar showed XOP as leading sector; Pradeep explicitly said gold, silver, mining, defense are the leaders
- **Tech/biotech/consumer "purgatory" not flagged** — radar had no way to identify that all 3 bull-market sectors were failing simultaneously
- **Walmart short ($91.85)** — Pradeep's "best setup of the day" not in radar's short candidates
- **DEP candidates questionable** — NEM, B, UNH, CVS as DEP longs while Pradeep was actively shorting UNH

### Daily Scorecard

| Category | Score (0-10) | Notes |
|---|---|---|
| Regime | 3 | Missed bear market classification; no RANGE_BOUND state |
| Setups | 5 | Short-side good, but missed Walmart and range expansion signal |
| Overall | **4** | Regime failure dragged down otherwise decent short-side work |

---

## 2025-05-16

### Radar Regime vs Pradeep SA

| Source | Call |
|---|---|
| **Radar** | CAUTIOUS_BULL — REDUCE_SIZE. Former leader rolling over: GNOM (genomics). 20% study 137 (elevated). T2108 64.99. ANTS active (35 candidates). |
| **Pradeep** | Bullish momentum but extended. Breakouts failing. "Not a good environment for breakouts." Focus on continuation setups and 9M EP. T2108 bounced to 65.08. Taking day off. All 3 positions stopped out. |

The radar's CAUTIOUS_BULL with REDUCE_SIZE is reasonable but slightly too cautious. Pradeep was "bullish but extended" — not cautious-bull. The key difference: Pradeep identified **breakout failures** as the primary signal, while the radar was still in REDUCE_SIZE mode with 35 ANTS candidates and 11 SOS candidates. The radar was generating bullish setups while Pradeep said breakouts are failing.

> "Not a good environment for breakouts."

> "Number of breakouts failing — something is there in the market."

> "9M EP and continuation setups — that's my focus."

### Setup Validation

| Setup | Radar | Pradeep | Match? |
|---|---|---|---|
| DEP | 2 candidates (CARR, CDE) | Not discussed — Pradeep focused on continuation + 9M EP | Partial |
| SOS | 11 candidates (NFG, WRB, STN, PSMT, CSV, ADUS, IBTA, CTAS, SAIC, ZBIO, FICO) | Not discussed; "not a good environment for breakouts" | ❌ Over-generated SOS when Pradeep said breakouts failing |
| ANTS | 35 candidates (NVDA, F, AMD, HBAN, MSFT, etc.) | Not discussed | ❌ Over-generated — 35 ANTS in a "breakouts failing" environment |
| SIPs | 30 found, 8 fresh catalyst (BIRK, NVNI, TIC, OSG, etc.) | DSSI, Kava, RKT, TTWO, EVLV, POOL discussed | ❌ No overlap — radar missed all of Pradeep's SIPs |
| Shorts | 31 candidates | Not discussed (Pradeep took day off) | N/A |
| Sugar Babies | 20 listed + hot sector table | Not discussed | N/A |

### Key Hits

- **20% study elevated** (137) — Pradeep said "20% study still extended" — aligned
- **T2108 ~65** — Pradeep said "T2108 bounced back to 65.08" — aligned
- **ANTS NVDA/AMD/AVGO** — semis in hot sector table, consistent with Pradeep's semi focus
- **Former leader rolling over: GNOM** — correct identification

### Key Misses

- **SIPs completely mismatched** — radar had BIRK, NVNI, TIC, OSG; Pradeep discussed DSSI, Kava, RKT, TTWO, EVLV, POOL. Zero overlap.
- **ANTS over-generation** — 35 candidates when Pradeep said "not a good environment for breakouts"
- **SOS over-generation** — 11 SOS candidates when Pradeep said breakouts are failing
- **No continuation setup framework** — Pradeep's focus was continuation setups and 9M EP; radar had neither as a distinct category
- **No "extended" warning** — Pradeep said market is "extended short term"; radar didn't flag this

### Daily Scorecard

| Category | Score (0-10) | Notes |
|---|---|---|
| Regime | 6 | Cautious-bull direction OK, but missed "breakouts failing" signal |
| Setups | 3 | Over-generated ANTS/SOS; missed all of Pradeep's SIPs; no continuation framework |
| Overall | **4** | Breadth data good, setup generation poor |

---

## 2025-06-23

### Radar Regime vs Pradeep SA

| Source | Call |
|---|---|
| **Radar** | DISTRIBUTING — NO_NEW_LONGS. Former leader rolling over: BLOK. Leading sector SIL top forming. Selling spreading to 11 sectors. |
| **Pradeep** | Cautious. Geopolitical fallout from US strike on Iranian nuclear facilities. T2108 flat at 50.64. 20% study bullish 3:1 but selling pressure in high-price stocks. Cautious positioning given geopolitical uncertainty. |

This is the **best regime call** in the sample. The radar called DISTRIBUTING/NO_NEW_LONGS, which aligns with Pradeep's "cautious" stance. The selling spreading to 11 sectors correctly captured the broad deterioration. The former leader rolling over (BLOK) and SIL top forming were both valid signals. Pradeep didn't explicitly say "distributing" but his tone ("cautious positioning given geopolitical uncertainty") is consistent with NO_NEW_LONGS.

### Setup Validation

| Setup | Radar | Pradeep | Match? |
|---|---|---|---|
| DEP | 0 candidates | Not discussed — brief session | N/A |
| SOS | 0 candidates | Not discussed | N/A |
| ANTS | 0 candidates | Not discussed | N/A |
| SIPs | 30 found, 23 fresh catalyst (KR, QUBT, IREN, GLXY, etc.) | HIMSS (negative catalyst), CDTX/EXEL (drug news), Bitcoin treasury theme | ❌ No overlap — radar missed HIMSS, CDTX, EXEL |
| Shorts | 31 candidates | Not specifically discussed but "negative catalysts as viable short setups" | Partial — radar had short candidates, Pradeep endorsed short approach |
| Sugar Babies | 20 listed | Bitcoin treasury theme (ECDA, EYEN) mentioned | Partial |

### Key Hits

- **Regime call: DISTRIBUTING/NO_NEW_LONGS** — aligned with Pradeep's cautious stance
- **Selling spreading to 11 sectors** — broad deterioration correctly identified
- **Former leader rolling over: BLOK** — valid signal
- **T2108 ~50.64** — exact match with Pradeep's reading
- **Short-side candidates** — 31 short setups, Pradeep endorsed "negative catalysts as viable short setups"

### Key Misses

- **SIPs mismatch** — radar had KR, QUBT, IREN, GLXY; Pradeep discussed HIMSS, CDTX, EXEL. Zero overlap.
- **HIMSS as negative catalyst** — Pradeep's key SIPs pick (negative catalyst, gapping down) not in radar
- **Bitcoin treasury theme** — Pradeep mentioned ECDA, EYEN; radar had GLXY in SIPs but not the treasury theme framing
- **Geopolitical context absent** — radar had no callout about US-Iran strike impact

### Daily Scorecard

| Category | Score (0-10) | Notes |
|---|---|---|
| Regime | 9 | Best in sample — DISTRIBUTING aligned with Pradeep's cautious stance |
| Setups | 4 | SIPs mismatched but shorts aligned; no setup generation for Pradeep's specific picks |
| Overall | **6** | Best overall score — regime was right, setups partially right |

---

## 2025-07-16

*Note: Session-2025-07-16 does not exist. Pradeep traveled to Germany on July 15 and held no meetings Wed-Fri. The radar uses `data_date: 2025-07-15`, so comparison is against Session-2025-07-15.*

### Radar Regime vs Pradeep SA

| Source | Call |
|---|---|
| **Radar** | CAUTIOUS_BULL — REDUCE_SIZE. Breakdown spike 377 vs 129. T2108 dropped 64.13→53.42. Selling spreading to 7 sectors. 20% study 63 (healthy). |
| **Pradeep (7/15)** | Bullish but likely to fade the gap. Semis overextended (18% above 200 SMA). "Sell the news" on NVDA. Breadth narrowing — only 67% above 200 DMA vs typical 84%. 940 bearish vs 88 bullish in combination scan. China theme emerging. |

The radar called CAUTIOUS_BULL — REDUCE_SIZE, but Pradeep's 7/15 session showed significant bearish divergence: 940 bearish vs 88 bullish, breadth narrowing, semis overextended. The T2108 drop from 64.13 to 53.42 (a 10-point collapse) is a major deterioration that CAUTIOUS_BULL understates. This should have been RANGE_BOUND or DISTRIBUTING.

> "940 stocks in combination bearish, 88 in combination bullish. What is the market telling you? Clearly, sellers are dominating."

> "Typically when the market makes big moves, you get 84% of stocks above 200 DMA. Right now, only 67%."

### Setup Validation

| Setup | Radar | Pradeep (7/15) | Match? |
|---|---|---|---|
| DEP | 16 candidates (LUV, CVE, GM, F, TGT, NEE, PR, APG, DELL, HPE, DVN, HL, MRNA, NKE, U, HUT) | Not discussed — Pradeep said "delayed reaction EP is the go-to after Germany" | ✅ Aligned — radar generated DEP, Pradeep endorses delayed reaction |
| SOS | 31 candidates (FSLR, BEPC, JRVR, LITE, C, YMM, NVDA, TTD, CRML, OUST, etc.) | NVDA = "sell the news"; FSLR/CRML = China rare earth theme | Partial — some overlap but Pradeep was cautious on breakouts |
| ANTS | 35 candidates (NU, INTC, F, PLTR, BAC, etc.) | Not discussed | ❌ Over-generated in deteriorating market |
| SIPs | 30 found, 25 fresh catalyst (NVDA, AMD, SMCI, TTD, NVTS, CRWV, etc.) | NVDA gap up = sell the news; SMCI = "no volume" | ✅ NVDA/SMCI appeared in both, but Pradeep's view was bearish |
| Shorts | 26 candidates (WSS: TSLL, WFC, WULF, QUBT, AMC) | WFC = "clear catalyst" best short; RCL = "selling, selling, selling" | ✅ WFC appeared in radar WSS short |
| Sugar Babies | 20 listed + hot sector table (ASTS, RKLB, INTC, NVTS, AVGO, MRVL, NVDA) | Semis setting up, NVDA/AVGO mentioned | ✅ Good alignment on hot sector table |

### Key Hits

- **WFC in WSS short** — Pradeep called WFC "clear catalyst" best short; radar had WFC in WSS enhanced
- **Sugar Babies hot sector table** — ASTS, RKLB, NVDA, AVGO in radar; Pradeep discussed semis setting up
- **NVDA in SOS + SIPs** — Pradeep discussed NVDA extensively (sell the news)
- **SOS volume** — 31 candidates; Pradeep said breakouts exist but are selective
- **Leading sector: UFO (space economy)** — Pradeep mentioned space/drone themes

### Key Misses

- **Regime too bullish** — CAUTIOUS_BULL understated the T2108 10-point collapse and 940:88 bearish/bullish ratio
- **ANTS over-generation** — 35 candidates when breadth is narrowing and sellers dominating
- **NVDA treatment** — radar had NVDA as SOS candidate (bullish); Pradeep said "sell the news" (bearish)
- **China theme absent** — Pradeep identified BABA, BIDU, JD as emerging theme; radar had no China sector callout
- **S&P 500 addition gaming** — Pradeep's insight about DDOG ("Goldman buys in anticipation, sells to retail") not captured
- **"Think in setups, not stocks"** — Pradeep's core lesson not reflected in radar's stock-list approach

### Daily Scorecard

| Category | Score (0-10) | Notes |
|---|---|---|
| Regime | 4 | Too bullish — missed T2108 collapse and bearish divergence |
| Setups | 6 | DEP generation good, WFC short hit, hot sector table aligned |
| Overall | **5** | Better setup generation but regime still too bullish |

---

## Trend Analysis

### What the Radar Was Consistently Good At

1. **Breadth data accuracy** — T2108, 20% study, breakout/breakdown counts matched Pradeep's readings every time
2. **Short-side generation** — When Pradeep identified short opportunity (Apr 16, Jun 23, Jul 16), radar had short candidates
3. **Sugar Baby tracking** — Consistent 20-stock list, hot sector table aligned with Pradeep's sector calls
4. **Selling spreading detection** — Correctly flagged sector-by-sector deterioration (2→5→7→11 sectors)
5. **Former leader rolling over** — GNOM (May 16), BLOK (Jun 23) both correctly identified

### What the Radar Was Consistently Bad At

1. **Regime classification** — Called CAUTIOUS_BULL in 5 of 6 sessions, including a bear market day (Apr 16) and a distributing day (Jul 16). No RANGE_BOUND state available.
2. **SIPs relevance** — Near-zero overlap with Pradeep's SIPs picks across all 6 sessions. Radar's SIPs scanner found different stocks than what Pradeep discussed.
3. **20% study suppression** — Too rigid. Suppressed DEP/SOS/ANTS based on lagging data (Jul 11: suppressed on 12 when live was 47). Didn't account for rapid momentum shifts.
4. **DEP/ANTS over-generation** — When not suppressed, generated too many candidates (May 16: 35 ANTS in a "breakouts failing" market; Jul 16: 35 ANTS in a narrowing market).
5. **Sector leadership** — Sector Relative Strength section was empty in 2024, partially filled in 2025. Missed Pradeep's sector calls (biotech/solar/oil Jul 11; banks Jan 16; gold/silver/mining Apr 16; China theme Jul 16).
6. **EP 9M Cat/Dog/Liquid Lava** — No 3-tier classification. Missed DATS as a "dogs" trade (Jan 16).
7. **Range expansion signal** — Pradeep's #1 framework ("range expansion is the one thing") not captured anywhere.
8. **Follow-through as regime input** — Follow-through data was present but not used in regime determination.

### Did the Radar Improve Over Time (2024 → 2025)?

| Dimension | 2024-07-11 | 2025-Q1 | 2025-Q2 | 2025-Q3 |
|---|---|---|---|---|
| Sector RS | Empty | Empty | Populated | Populated + group moves |
| Short-side | Basic WSS | WSS + sugar baby short | WSS + sugar baby short + momentum inversion | Full short suite |
| Sugar Babies | Basic 20 list | Basic 20 list | Hot sector table added | Hot sector table + recency scoring |
| Ticker details | None | None | Full details (EMA, breakout history, fund ownership) | Full details continued |
| Regime states | CAUTIOUS_BULL only | CAUTIOUS_BULL only | CAUTIOUS_BULL + DISTRIBUTING | CAUTIOUS_BULL (regressed) |

**Yes, incremental improvement** — sector RS, ticker details, and sugar baby hot sector table were added between Q1 and Q2 2025. The DISTRIBUTING regime appeared once (Jun 23) but wasn't consistently applied. The core problems (no RANGE_BOUND, SIPs mismatch, 20% suppression rigidity) persisted throughout.

### Average Scores

| Date | Regime | Setups | Overall |
|---|---|---|---|
| 2024-07-11 | 5 | 3 | 4 |
| 2025-01-16 | 7 | 2 | 4 |
| 2025-04-16 | 3 | 5 | 4 |
| 2025-05-16 | 6 | 3 | 4 |
| 2025-06-23 | 9 | 4 | 6 |
| 2025-07-16 | 4 | 6 | 5 |
| **Average** | **5.7** | **3.8** | **4.5** |

---

## Pre-Fix Baseline Summary

| Category | Pre-Fix Average (0-10) | Primary Weakness | Fix That Should Help |
|---|---|---|---|
| **Regime** | 5.7 | CAUTIOUS_BULL default; no RANGE_BOUND; missed bear market (Apr 16); missed T2108 collapse (Jul 16) | RANGE_BOUND regime + follow-through as regime input |
| **Setups** | 3.8 | SIPs near-zero overlap; DEP/ANTS over-generation; no Cat/Dog/Liquid Lava; 20% suppression too rigid | Tighten 20% study suppression + DEP market cap filter + SIPs fallback + Cat/Dog/Liquid Lava + callout box enrichment |
| **Overall** | 4.5 | Regime + setup generation both need work | All 7 fixes combined |

### Expected Post-Fix Improvements

1. **RANGE_BOUND regime** — should catch Apr 16 (bear market) and Jul 16 (T2108 collapse) that were wrongly called CAUTIOUS_BULL
2. **Follow-through as regime input** — 5d follow-through <30% should downgrade regime automatically (Jan 16 had 21.8% FAILING but still CAUTIOUS_BULL)
3. **Tighten 20% study suppression** — should prevent Jul 11 suppression (12 → 47 surge) and allow DEP/SOS when buying is coming in
4. **DEP market cap filter** — should reduce DEP candidates in low-quality environments (Apr 16 had UNH as both DEP long and WSS short)
5. **SIPs fallback** — should improve SIPs overlap with Pradeep's picks (currently near-zero)
6. **Cat/Dog/Liquid Lava** — should capture DATS-type "dogs" trades (Jan 16) that radar completely missed
7. **Callout box enrichment** — should surface range expansion signals, sector leadership, and geopolitical context that radar currently misses

**Target post-fix averages**: Regime ≥7.0, Setups ≥6.0, Overall ≥6.5.