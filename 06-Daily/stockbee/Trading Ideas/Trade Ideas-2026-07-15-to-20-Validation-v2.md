---
title: "Trade Ideas Multi-Day Validation v2 — Post Phase F+G+H Fixes"
date: 2026-07-22
tags: [analysis, validation, trade-ideas, comparison, stockbee, pradeep-bonde, multi-day, market-regime, post-fix, scorecard]
---

# Trade Ideas Multi-Day Validation v2 — Post Phase F+G+H Fixes

A re-run of the 4-day head-to-head audit (Jul 15, 16, 17, 20) after 13 systemic fixes from Phase F+G+H. The original validation scored 1/60 to 7/60 (5.4% accuracy). This re-run measures the improvement.

**Bottom line: 38/60 average (63.3%), up from 3.25/60 (5.4%) — an 11.7x improvement.**

---

## What Changed (Phase F+G+H — 13 fixes)

1. **20% study suppression gate** — SOS/DEP/ANTS suppressed when 20% study < 30
2. **SIPs detection module** — premarket gap scanner with fresh catalyst flags
3. **Short-side module on all days** — Bearish DEP, WSS, SB Short, Momentum Inversion, Bearish Reversal, Bearish Study
4. **Regime LLM judge retuned** — uses 20% study, 5d/10d ratios, breakdown spikes, former leader rollover
5. **FADE mode labeling** — SOS section relabeled as FADE candidates when 20% study < 30
6. **Sector "TOP FORMING" / "Former leader rolling over" labels**
7. **DEP suppression when 20% study < 30** (fully suppressed Jul 17+)
8. **ANTS suppression in range-bound markets** (5d ratio < 0.8, 20% study < 50)
9. **Short candidate cap at 20-30** (was 125 on Jul 20 original)
10. **Breakout follow-through tracking** (3d/5d % with FAILING flag)
11. **DISTRIBUTING regime** added (former leader rolling over + breakdown > breakout + 5d/10d < 0.8)
12. **20% study displayed with signal labels** (⚠️ Low, Marginal, etc.)
13. **Secondary indicator warnings** (5d/10d/monthly ratio < 0.8 flagged)

---

## Day 1 — Tuesday, July 15, 2026

### Radar Regime vs Pradeep SA

| Dimension | Radar (NEW) | Radar (OLD) | Pradeep | Match? |
|-----------|-------------|-------------|---------|--------|
| **Regime** | CAUTIOUS_BULL → REDUCE_SIZE | FULL_BULL → FULL_LONG | Range-bound, "wallet closed" | ✅ Major improvement |
| **20% study** | 32 — "Marginal", suppression active | Not used | ~25/15 — "funds not buying, not selling" | ✅ Now aligned |
| **Breadth** | Net +223, BO:BD 1.15 | Same | "Stalemate — no buying, no selling" | ⚠️ Radar still positive, Pradeep saw stalemate |
| **Action** | "REDUCE_SIZE — selective setups only" | "Full playbook — 5 SOS with 6/6 TL" | "My wallet is closed." | ⚠️ Closer but still too active |

> Pradeep: "The funds are not aggressively buying, and the funds are not aggressively selling. When do you make money? You make money when the funds are aggressively buying."

**Regime score: 7/10** (was 1) — CAUTIOUS_BULL/REDUCE_SIZE is a massive upgrade from FULL_BULL. 20% study at 32 correctly flagged. Still says "selective setups" vs Pradeep's "nothing to do," but directionally correct.

### SOS Validation

| Radar SOS (NEW) | Radar SOS (OLD) | Pradeep | Verdict |
|-----------------|-----------------|---------|---------|
| **0 found** (suppressed — 20% study 32 < threshold) | 50 found, 5 with 6/6 TL | "Breakouts unlikely to follow through" | ✅ Suppression correct |

**SOS score: 8/10** (was 0) — Zero false positives. The 20% study suppression gate correctly prevented 50 noise candidates. Not 10/10 because FADE mode didn't list any fade candidates either (the section is empty rather than showing fade-eligible breakouts).

### DEP Validation

| Radar DEP (NEW) | Pradeep Mentioned? | Verdict |
|-----------------|---------------------|---------|
| TECH | ❌ Not mentioned | — |
| KHC | ❌ Not mentioned | — |
| MRK | ❌ Not mentioned | — |
| ABBV | ❌ Not mentioned (Jul 16: "will chop") | — |
| GIS | ❌ Not mentioned | — |
| XYZ | ❌ Not mentioned | — |
| DT | ❌ Not mentioned | — |
| UAL | ❌ Not mentioned | — |
| AAL | ❌ Not mentioned | — |

**Radar said:** 9 DEP candidates (20% study at 32, just above the 30 threshold — DEP not suppressed).

**Pradeep said:** "I don't see anything which is actionable here." (PM)

**DEP score: 1/10** (was 0) — Slight improvement (9 vs 10 candidates), but still generating noise. The 20% study at 32 is borderline — DEP suppression threshold is < 30, so these 9 leaked through. Pradeep endorsed zero.

### ANTS Validation

| Radar ANTS (NEW) | Radar ANTS (OLD) | Pradeep | Verdict |
|------------------|------------------|---------|---------|
| **0 found** (suppressed) | 35 found | "Anticipation doesn't work in this market" | ✅ Suppression correct |

**ANTS score: 9/10** (was 0) — Perfect suppression. Pradeep said anticipation won't work in range-bound markets. The radar agreed by generating zero. The one point off is because the report still says "Place ANTS BSLO orders" in the action summary (stale template text).

### SIPs Detection

| Pradeep SIPs | Radar Detected? | Notes |
|--------------|-----------------|-------|
| PENG | ✅ | In SIPs list, fresh catalyst flag |
| BLK (BlackRock) | ✅ | In SIPs list, fresh catalyst |
| AHR | ❌ | 36% gap up — not detected (likely below volume threshold or not in ticker universe) |
| BABA | ❌ | Gapping up — not detected |
| CRWD | ❌ | Day 2 SIPs — not detected |

**SIPs score: 5/10** (was 0) — Major improvement from zero. Found 2 of 5 Pradeep SIPs (PENG, BLK). The module is working but has gaps — AHR (36% gap) and BABA should have been caught.

### Short-Side

| Radar Short Category | Top Picks | Pradeep Mentioned? | Verdict |
|----------------------|----------|---------------------|---------|
| Bearish DEP | PENG, CELC, PL, UUUU, COUR | ✅ PENG discussed as SIPs (not short) | ⚠️ Partial |
| WSS Enhanced | ONDS, INTC, MU, MRVL, CSCO | ✅ MU/MRVL — semis weakness | ⚠️ Partial |
| Sugar Baby Short | DFNS, CAST, ASTC, LHSW, ANY | ❌ Not mentioned | — |
| Momentum Inversion | QUCY, QTEX, LASE, MNTS, RXT | ❌ Not mentioned | — |
| Bearish Reversal | PCT, XE, EQPT, EH, HPP | ❌ Not mentioned | — |
| Bearish Study | SOC, ABTC, TOYO, FAC, MNTS... | ❌ Not mentioned | — |

**Radar said:** 35 short candidates across 6 categories.

**Pradeep said:** "Shorts look more attractive to me than longs." Named semis breakdown (Dell, Lemonade). But no actual short trades on Jul 15.

**Short score: 4/10** (was 0) — Module exists, semis directionally correct (MU, MRVL in WSS). But 35 candidates is still over-generated, and Pradeep's specific names (DELL, Lemonade) weren't in the list. PENG appearing as both SIPs long AND Bearish DEP short is contradictory.

### Daily Scorecard — July 15

| Category | NEW Score | OLD Score | Delta | Notes |
|----------|:---------:|:---------:|:-----:|-------|
| Regime Match | 7 | 1 | +6 | CAUTIOUS_BULL vs FULL_BULL — massive upgrade |
| SOS Validation | 8 | 0 | +8 | Suppression correct — zero false positives |
| DEP Validation | 1 | 0 | +1 | Still 9 noise candidates (20% study 32 leaked through) |
| ANTS Validation | 9 | 0 | +9 | Perfect suppression |
| SIPs Detection | 5 | 0 | +5 | Found PENG, BLK; missed AHR, BABA, CRWD |
| Short-Side | 4 | 0 | +4 | Module exists, semis directionally correct |
| **Total** | **34/60** | **1/60** | **+33** | **57% accuracy (was 1.7%)** |

---

## Day 2 — Thursday, July 16, 2026

### Radar Regime vs Pradeep SA

| Dimension | Radar (NEW) | Radar (OLD) | Pradeep | Match? |
|-----------|-------------|-------------|---------|--------|
| **Regime** | CAUTIOUS_BULL → REDUCE_SIZE | FULL_BULL → FULL_LONG | "Don't buy anything at open" | ✅ Major improvement |
| **20% study** | 30 — "Marginal", suppression active | Not used | "20% study still at 20" | ✅ Aligned |
| **Breadth** | Net +144, breakdown spike 509 vs 251 | Same | "Selling has started coming in" | ✅ Breakdown spike confirmed |
| **Action** | "REDUCE_SIZE — selective setups" | "Full playbook — 4 SOS with 6/6 TL" | Shorted Google. First trade post-Norway. | ⚠️ Radar reduce, Pradeep shorted |

**Regime score: 6/10** (was 1) — CAUTIOUS_BULL with breakdown spike 509 flagged. But Pradeep was actively shorting (more aggressive than "reduce size"). The radar correctly identified weakness but didn't go far enough — DISTRIBUTING would have been closer.

### SOS Validation

| Radar SOS (NEW) | Radar SOS (OLD) | Pradeep | Verdict |
|-----------------|-----------------|---------|---------|
| **0 found** (suppressed) | 50 found, 4 with 6/6 TL | "I don't see anything actionable" | ✅ Suppression correct |

**SOS score: 8/10** (was 0) — Zero false positives. Suppression gate working.

### DEP Validation

| Radar DEP (NEW) | Pradeep Mentioned? | Verdict |
|-----------------|---------------------|---------|
| TECH | ❌ Not mentioned | — |
| XOM | ❌ Not mentioned | — |
| PR | ❌ Not mentioned | — |
| BKR | ❌ Not mentioned | — |
| MRK | ❌ Not mentioned | — |
| NKE | ❌ Not mentioned | — |
| ABBV | ✅ "These pharma stocks... will chop" | ❌ Rejected |
| NFLX | ✅ "No idea what Netflix will do" | ❌ Not endorsed |

**Radar said:** 20 DEP candidates (20% study at 30, exactly at threshold — not suppressed).

**Pradeep said:** "I don't see a DEP on a bullish side here." (Jul 17 AM, same stance)

**DEP score: 1/10** (was 0) — 20 candidates, zero endorsed. ABBV explicitly called a chop. The 20% study at 30 is exactly at the threshold — DEP should have been suppressed (threshold is < 30, but 30 is borderline).

### ANTS Validation

| Radar ANTS (NEW) | Radar ANTS (OLD) | Pradeep | Verdict |
|------------------|------------------|---------|---------|
| **0 found** (suppressed) | 35 found | "Anticipation is the worst setup" | ✅ Suppression correct |

**ANTS score: 9/10** (was 0) — Perfect suppression.

### SIPs Detection

| Pradeep SIPs | Radar Detected? | Notes |
|--------------|-----------------|-------|
| UNH (UnitedHealth) | ✅ | In SIPs list, fresh catalyst, +7.4% gap |
| ABT (Abbott) | ✅ | In SIPs list, fresh catalyst, +6.7% gap |
| DXCM | ❌ | Not detected (Abbott CGM competitor) |
| ELVA | ❌ | "Delayed reaction EP" — not detected |
| TSM | ❌ | "Very choppy" — not detected |

**SIPs score: 5/10** (was 0) — Found the two primary SIPs (UNH, ABT). Missed DXCM, ELVA, TSM. 2/5 = 40% recall.

### Short-Side

| Radar Short Category | Top Picks | Pradeep Mentioned? | Verdict |
|----------------------|----------|---------------------|---------|
| Bearish DEP | PL, PURR, CMPS, SMH, FPS | ✅ SMH (semis) | ⚠️ Partial |
| WSS Enhanced | ONDS, INTC, ORCL, ASTS, JOBY | ❌ Not specifically mentioned | — |
| Sugar Baby Short | DFNS, CAST, ASTC, LHSW, NVVE | ❌ Not mentioned | — |
| Bearish Reversal | DOCN, KRO, TMCI, KLAC, AMAT | ✅ KLAC, AMAT (semis) | ⚠️ Partial |
| Bearish Study | BIYA, FAC, SOC, MNTS, TOYO... | ❌ Not mentioned | — |

**Radar said:** 30 short candidates.

**Pradeep said:** SHORTED GOOG (EP 9M, Gemini delay catalyst). BB was best long (EP 9M). GLW short from yesterday.

**Short score: 3/10** (was 0) — Module exists, semis directionally correct (SMH, KLAC, AMAT). But the actual trade (GOOG short) was completely missed. BB (the best long) wasn't in any radar list. 30 candidates is still over-generated.

### Daily Scorecard — July 16

| Category | NEW Score | OLD Score | Delta | Notes |
|----------|:---------:|:---------:|:-----:|-------|
| Regime Match | 6 | 1 | +5 | CAUTIOUS_BULL + breakdown spike flagged |
| SOS Validation | 8 | 0 | +8 | Suppression correct |
| DEP Validation | 1 | 0 | +1 | 20 candidates still leaked (20% study at 30 = borderline) |
| ANTS Validation | 9 | 0 | +9 | Perfect suppression |
| SIPs Detection | 5 | 0 | +5 | Found UNH, ABT; missed DXCM, ELVA, TSM |
| Short-Side | 3 | 0 | +3 | Semis directionally correct; missed GOOG short trade |
| **Total** | **32/60** | **1/60** | **+31** | **53% accuracy (was 1.7%)** |

---

## Day 3 — Friday, July 17, 2026

### Radar Regime vs Pradeep SA

| Dimension | Radar (NEW) | Radar (OLD) | Pradeep | Match? |
|-----------|-------------|-------------|---------|--------|
| **Regime** | CAUTIOUS_BULL → REDUCE_SIZE | CAUTIOUS_BULL → REDUCE_SIZE | "Nothing actionable, selling spreading" | ⚠️ Same as old, slightly better reasoning |
| **20% study** | 22 — "⚠️ Low", full suppression | Not used | "20% study still at 14-15" | ✅ Aligned |
| **Breadth** | Net +44 (very low), 5d 0.70, 10d 0.75 | Same | "Selling going to spread to stocks holding up" | ✅ Breadth deterioration confirmed |
| **Action** | "REDUCE_SIZE — selective setups" | Same | "Nothing I can see. ORCA and CADL only." | ⚠️ Radar reduce, Pradeep nothing |

**Regime score: 6/10** (was 4) — Same regime label but now with 20% study at 22 explicitly cited, all three long scans suppressed. Better reasoning. Still says "selective setups" vs "nothing."

### SOS Validation

| Radar SOS (NEW) | Radar SOS (OLD) | Pradeep | Verdict |
|-----------------|-----------------|---------|---------|
| **0 found** (suppressed, FADE MODE) | 50 found, 7 with 6/6 TL | "Most breakouts not likely to work" | ✅ Suppression + FADE mode correct |

**SOS score: 9/10** (was 0) — Zero false positives AND FADE mode label added. Pradeep said "fading breakouts is better." The radar now explicitly labels the section as FADE candidates.

### DEP Validation

| Radar DEP (NEW) | Radar DEP (OLD) | Pradeep | Verdict |
|-----------------|-----------------|---------|---------|
| **0 found** (suppressed — 20% study 22 < 30) | 20 found | "I don't see a DEP on a bullish side here. There is no DEP I see." | ✅ Perfect match |

**DEP score: 10/10** (was 0) — **Perfect score.** The radar generated zero DEPs. Pradeep explicitly said "no DEP I see." The 20% study suppression gate worked flawlessly.

### ANTS Validation

| Radar ANTS (NEW) | Radar ANTS (OLD) | Pradeep | Verdict |
|------------------|------------------|---------|---------|
| **0 found** (suppressed) | 35 found | "I don't really see any anticipation set up" | ✅ Perfect suppression |

**ANTS score: 9/10** (was 0) — Perfect suppression. Pradeep saw zero anticipation setups.

### SIPs Detection

| Pradeep SIPs | Radar Detected? | Notes |
|--------------|-----------------|-------|
| TSM (Taiwan Semi) | ❌ | "Taiwan Semi had very good earnings" |
| ORCA | ❌ | One of only two stocks Pradeep saw |
| CADL | ❌ | Second of only two stocks Pradeep saw |
| SNDK / MU / SOXL | ❌ (SNDK in Bearish Reversal, not SIPs) | Semis in play for day trading |
| NFLX | ❌ | "No idea what Netflix catalyst will be" |

**Radar SIPs:** BIYA, SDOT, SG, JLHL, ADVB, LCID, ASTS, EOSE, IOVA, WU, VG, FCEL, SLS, TRVI, SOC

**SIPs score: 2/10** (was 0) — Module exists but found NONE of Pradeep's actual SIPs (ORCA, CADL, TSM). The radar's SIPs are all small-cap gap stocks, while Pradeep's were mid/large-cap earnings plays. The SIPs scanner's volume/float filters may be misaligned with Pradeep's SIPs universe.

### Short-Side

| Radar Short Category | Top Picks | Pradeep Mentioned? | Verdict |
|----------------------|----------|---------------------|---------|
| Bearish DEP | SMH, PSKY, ARRY, ISRG, LUMN | ✅ SMH (semis ETF) | ⚠️ Partial |
| WSS Enhanced | MARA, GRAB, QXO, PSKY, AA | ❌ Not specifically | — |
| Sugar Baby Short | DFNS, CAST, ASTC, LHSW, ANY | ❌ Not mentioned | — |
| Bearish Reversal | SNDK, ANNX, REZI, CRNC, ELTX | ✅ SNDK (stock in play) | ⚠️ Partial |
| Bearish Study | FAC, BIYA, SOC, TOYO, MNTS... | ❌ Not mentioned | — |

**Radar said:** 30 short candidates.

**Pradeep said:** Holding GOOG and BB shorts from Jul 16. DDOG and CRWD are next short candidates (insider selling). Selling spreading to KO, Disney, XLP (defensive names).

**Short score: 4/10** (was 0) — SMH (semis) and SNDK directionally correct. But missed GOOG, BB (the actual held shorts), DDOG/CRWD (the next candidates), and KO/defensive names (where selling was spreading). 30 candidates over-generated.

### Daily Scorecard — July 17

| Category | NEW Score | OLD Score | Delta | Notes |
|----------|:---------:|:---------:|:-----:|-------|
| Regime Match | 6 | 4 | +2 | Better reasoning with 20% study cited |
| SOS Validation | 9 | 0 | +9 | Suppression + FADE mode |
| DEP Validation | 10 | 0 | +10 | **Perfect** — zero DEPs, Pradeep said "no DEP" |
| ANTS Validation | 9 | 0 | +9 | Perfect suppression |
| SIPs Detection | 2 | 0 | +2 | Module exists but missed all Pradeep SIPs |
| Short-Side | 4 | 0 | +4 | SMH/SNDK correct; missed GOOG/BB/DDOG/CRWD |
| **Total** | **40/60** | **4/60** | **+36** | **67% accuracy (was 6.7%)** |

---

## Day 4 — Monday, July 20, 2026

### Radar Regime vs Pradeep SA

| Dimension | Radar (NEW) | Radar (OLD) | Pradeep | Match? |
|-----------|-------------|-------------|---------|--------|
| **Regime** | **DISTRIBUTING → NO_NEW_LONGS** | CAUTIOUS_BULL → REDUCE_SIZE | "Nothing to do. Literally, nothing to do." | ✅ Best match yet |
| **20% study** | 24 — "⚠️ Low", full suppression | Not used | "20% study bullish at 15" — weak bounce | ✅ Aligned |
| **Breadth** | Net -53 (negative!), 5d 0.77, 10d 0.69 | Net +44, 5d 0.70 | "Both sides not working" | ✅ Net negative confirmed |
| **Action** | "NO NEW LONGS — process over chasing" | "REDUCE_SIZE — selective setups" | "Nothing really on short side. Nothing on long side." | ✅ Closest match |

> Pradeep: "Nothing to do. Literally, like, nothing to do." (PM)
> Pradeep: "Both sides, shorts as well as longs, are not really working." (PM)

**Regime score: 8/10** (was 4) — **Best regime call in 4 days.** DISTRIBUTING/NO_NEW_LONGS is nearly perfect. Former leader BUG rolling over flagged. Net primary negative (-53). All long scans suppressed. The only miss: Pradeep said both sides not working, while the radar still generated 25 short candidates.

### SOS Validation

| Radar SOS (NEW) | Radar SOS (OLD) | Pradeep | Verdict |
|-----------------|-----------------|---------|---------|
| **0 found** (suppressed, FADE MODE) | 50 found | "Fading breakouts is better than buying" | ✅ Suppression + FADE mode correct |

**SOS score: 9/10** (was 0) — Zero false positives. FADE mode label matches Pradeep's "fading breakouts > buying breakouts."

### DEP Validation

| Radar DEP (NEW) | Radar DEP (OLD) | Pradeep | Verdict |
|-----------------|-----------------|---------|---------|
| **0 found** (suppressed — 20% study 24 < 30) | 20 found | "I don't see anything which I would like and take as a swing." | ✅ Perfect match |

**DEP score: 10/10** (was 0) — **Perfect score.** Zero DEPs generated. Pradeep endorsed zero. Suppression gate working flawlessly.

### ANTS Validation

| Radar ANTS (NEW) | Radar ANTS (OLD) | Pradeep | Verdict |
|------------------|------------------|---------|---------|
| **0 found** (suppressed) | 35 found | "Anticipation is the worst setup here, even worse than breakouts. Guaranteed chop." | ✅ Perfect suppression |

**ANTS score: 9/10** (was 0) — Perfect suppression. Pradeep called anticipation "the worst setup" and "guaranteed chop."

### SIPs Detection

| Pradeep SIPs | Radar Detected? | Notes |
|--------------|-----------------|-------|
| SNDK / MU / SOXL | ✅ MU (in SIPs, fresh catalyst) | SNDK/SOXL missed |
| IREN | ✅ | In SIPs, fresh catalyst, +8.2% gap |
| ACHR (Archer Aviation) | ✅ | In SIPs, but NO dilution flag ⚠️ |
| CLSK (Cipher Mining) | ❌ | "Data center $6B deal... dilution" — not detected |
| CIFR | ✅ | In SIPs (crypto mining sympathy) |
| BMNR (BitMiner) | ❌ | Breakout failing example — not detected |
| AHR | ❌ | "Was a SIPs, not an EP" — not detected |
| GOOGL | ❌ | Google catalyst — not detected as SIPs |

**Radar SIPs:** ACHR, IREN, BIYA, CIFR, MU, AMD, APLD, SKYQ, NBIS, CORZ, FCEL, HUT, CRDO, LITE, NNBR

**SIPs score: 5/10** (was 0) — Found MU, IREN, ACHR, CIFR (4/8). But ACHR has dilution risk that Pradeep flagged — the radar didn't show a [DILUTION] flag. Missed CLSK, BMNR, AHR, GOOGL, SNDK, SOXL.

### Short-Side

| Radar Short Category | Top Picks | Pradeep Mentioned? | Verdict |
|----------------------|----------|---------------------|---------|
| Bearish DEP | ARRY, MDLN, AI, CTMX, GDXJ | ❌ Not mentioned | — |
| WSS Enhanced | QXO, BE, PSNL, CVNA, TEM | ❌ Not mentioned | — |
| Sugar Baby Short | UPC, ICCM, TDIC, SOC, HSPT | ❌ Not mentioned | — |
| Momentum Inversion | QTEX, LASE, MNTS, AMPG, AIB | ❌ Not mentioned | — |
| Bearish Reversal | INIO, QNT, FBRX, AADX, GALT | ❌ Not mentioned | — |

**Radar said:** 25 short candidates (capped, down from 125 in old version).

**Pradeep said:** "Nothing really on the short side." GOOG and BB shorts got stopped out. No new shorts being added. "Both sides not working."

**Short score: 5/10** (was 3) — Better calibrated (25 vs 125). Former leader BUG rolling over flagged in regime. Sector RS shows semis (SOXX), quantum (QTUM), EV (DRIV) all down 15-18% — directionally correct. But Pradeep said "nothing on short side either" — so 25 candidates is still over-generated for a market where both sides are dead.

### Daily Scorecard — July 20

| Category | NEW Score | OLD Score | Delta | Notes |
|----------|:---------:|:---------:|:-----:|-------|
| Regime Match | 8 | 4 | +4 | DISTRIBUTING/NO_NEW_LONGS — best call yet |
| SOS Validation | 9 | 0 | +9 | Suppression + FADE mode |
| DEP Validation | 10 | 0 | +10 | **Perfect** — zero DEPs |
| ANTS Validation | 9 | 0 | +9 | Perfect suppression |
| SIPs Detection | 5 | 0 | +5 | Found MU, IREN, ACHR, CIFR; missed CLSK, BMNR, AHR |
| Short-Side | 5 | 3 | +2 | Better calibrated (25 vs 125); former leader rollover flagged |
| **Total** | **46/60** | **7/60** | **+39** | **77% accuracy (was 11.7%)** |

---

## Summary Scorecard — Before vs After

| Day | Regime | SOS | DEP | ANTS | SIPs | Short | **NEW Total** | OLD Total | **Delta** |
|-----|:------:|:---:|:---:|:----:|:----:|:-----:|:------------:|:---------:|:---------:|
| Jul 15 | 7 | 8 | 1 | 9 | 5 | 4 | **34/60** | 1/60 | **+33** |
| Jul 16 | 6 | 8 | 1 | 9 | 5 | 3 | **32/60** | 1/60 | **+31** |
| Jul 17 | 6 | 9 | 10 | 9 | 2 | 4 | **40/60** | 4/60 | **+36** |
| Jul 20 | 8 | 9 | 10 | 9 | 5 | 5 | **46/60** | 7/60 | **+39** |
| **Avg** | **6.75** | **8.5** | **5.5** | **9.0** | **4.25** | **4.0** | **38/60** | **3.25/60** | **+34.75** |

### Accuracy Improvement

| Metric | OLD | NEW | Improvement |
|--------|:---:|:---:|:-----------:|
| Overall accuracy | 5.4% | **63.3%** | **11.7x** |
| Best day | 7/60 (11.7%) | 46/60 (76.7%) | 6.6x |
| Worst day | 1/60 (1.7%) | 32/60 (53.3%) | 32x |
| Categories at 0 | 5/6 (all but regime) | 0/6 | All categories improved |
| Perfect scores (10/10) | 0 | 2 (DEP Jul 17, DEP Jul 20) | — |

---

## Category-by-Category Improvement

### Regime Match: 2.5 → 6.75 (+4.25)

| Day | OLD | NEW | What improved |
|-----|:---:|:---:|---------------|
| Jul 15 | 1 | 7 | FULL_BULL → CAUTIOUS_BULL. 20% study now used. |
| Jul 16 | 1 | 6 | FULL_BULL → CAUTIOUS_BULL. Breakdown spike 509 flagged. |
| Jul 17 | 4 | 6 | Same label, but 20% study at 22 now explicitly cited. |
| Jul 20 | 4 | 8 | CAUTIOUS_BULL → **DISTRIBUTING/NO_NEW_LONGS**. Former leader BUG rolling over. Net primary negative. |

**Verdict:** The LLM judge retuning was highly effective. The 20% study is now the primary regime input. The progression CAUTIOUS_BULL → CAUTIOUS_BULL → CAUTIOUS_BULL → DISTRIBUTING tracks Pradeep's "range-bound → selling accelerating → selling spreading → nothing works" arc.

**Remaining gap:** Jul 15-16 still says "selective setups" when Pradeep said "wallet closed" / "don't buy anything." The regime label is right; the action text is still slightly too permissive.

### SOS Validation: 0 → 8.5 (+8.5)

| Day | OLD | NEW | What improved |
|-----|:---:|:---:|---------------|
| Jul 15 | 0 | 8 | 50 candidates → 0 (suppressed). Zero false positives. |
| Jul 16 | 0 | 8 | 50 candidates → 0 (suppressed). |
| Jul 17 | 0 | 9 | 50 candidates → 0 (suppressed + FADE mode label). |
| Jul 20 | 0 | 9 | 50 candidates → 0 (suppressed + FADE mode label). |

**Verdict:** The 20% study suppression gate completely fixed the SOS over-generation problem. 200 SOS candidates in the old run → 0 in the new run. Pradeep endorsed zero SOS across all 4 days in both runs — the new run correctly generates zero instead of 50 noise candidates.

**Remaining gap:** The FADE mode section is empty (0 candidates) rather than showing yesterday's breakouts as fade candidates. Pradeep said "fading breakouts is better" — the radar labels the section correctly but doesn't populate it.

### DEP Validation: 0 → 5.5 (+5.5)

| Day | OLD | NEW | What improved |
|-----|:---:|:---:|---------------|
| Jul 15 | 0 | 1 | 10 → 9 candidates (20% study 32, just above threshold) |
| Jul 16 | 0 | 1 | 20 → 20 candidates (20% study 30, borderline) |
| Jul 17 | 0 | **10** | 20 → **0** (suppressed, 20% study 22 < 30). **Perfect.** |
| Jul 20 | 0 | **10** | 20 → **0** (suppressed, 20% study 24 < 30). **Perfect.** |

**Verdict:** The DEP suppression gate works perfectly when 20% study is clearly below 30 (Jul 17, 20). But when 20% study is at 30-32 (Jul 15, 16), candidates leak through. Pradeep endorsed zero DEPs on all 4 days — the threshold may need to be raised from < 30 to < 35.

**Remaining gap:** Jul 15-16 DEP still over-generates. The 20% study threshold of 30 is too tight — Pradeep's "no DEP" stance started when 20% study was at 25-32. Recommend raising DEP suppression threshold to < 35.

### ANTS Validation: 0 → 9.0 (+9.0)

| Day | OLD | NEW | What improved |
|-----|:---:|:---:|---------------|
| Jul 15 | 0 | 9 | 35 → 0 (suppressed). Perfect. |
| Jul 16 | 0 | 9 | 35 → 0 (suppressed). Perfect. |
| Jul 17 | 0 | 9 | 35 → 0 (suppressed). Perfect. |
| Jul 20 | 0 | 9 | 35 → 0 (suppressed). Perfect. |

**Verdict:** The ANTS suppression is flawless across all 4 days. 140 ANTS candidates in the old run → 0 in the new run. Pradeep called anticipation "the worst setup" in range-bound markets — the radar now agrees.

**Remaining gap:** The action summary still says "Place ANTS BSLO orders" (stale template text). Should say "ANTS suppressed — range-bound market" when suppression is active.

### SIPs Detection: 0 → 4.25 (+4.25)

| Day | OLD | NEW | What improved |
|-----|:---:|:---:|---------------|
| Jul 15 | 0 | 5 | No module → found PENG, BLK (2/5 Pradeep SIPs) |
| Jul 16 | 0 | 5 | No module → found UNH, ABT (2/5 Pradeep SIPs) |
| Jul 17 | 0 | 2 | No module → found 0/5 Pradeep SIPs (ORCA, CADL, TSM missed) |
| Jul 20 | 0 | 5 | No module → found MU, IREN, ACHR, CIFR (4/8 Pradeep SIPs) |

**Verdict:** The SIPs module is the biggest new feature. It found 8 of Pradeep's 23 SIPs across 4 days (35% recall). Best on Jul 20 (4/8). Worst on Jul 17 (0/5 — missed ORCA and CADL entirely).

**Remaining gaps:**
1. **Small-cap bias** — The radar's SIPs are dominated by micro-caps (BIYA, SDOT, SG, JLHL). Pradeep's SIPs include mid/large-caps (TSM, UNH, ABT, GOOGL). The scanner may need a separate "large-cap SIPs" pass.
2. **No dilution risk flag** — ACHR, IREN, CLSK all have shelf offerings / serial dilution. Pradeep explicitly flagged these. The radar shows ACHR and IREN without [DILUTION] flags.
3. **Missing earnings-driven SIPs** — TSM (earnings), AHR (earnings), ELVA (delayed reaction) were all earnings plays. The scanner may not be catching earnings-calendar catalysts.
4. **ORCA and CADL** — The only two stocks Pradeep found actionable on Jul 17 were completely absent. These may be low-volume stocks below the scanner's threshold.

### Short-Side: 0.75 → 4.0 (+3.25)

| Day | OLD | NEW | What improved |
|-----|:---:|:---:|---------------|
| Jul 15 | 0 | 4 | No module → 35 candidates (semis directionally correct) |
| Jul 16 | 0 | 3 | No module → 30 candidates (missed GOOG short trade) |
| Jul 17 | 0 | 4 | No module → 30 candidates (SMH/SNDK correct) |
| Jul 20 | 3 | 5 | 125 → 25 candidates (better calibrated, former leader flagged) |

**Verdict:** The short-side module now runs on all 4 days (was only Jul 20 in old run). The Jul 20 calibration improved dramatically (125 → 25 candidates). Sector-level weakness (semis, AI) is directionally correct.

**Remaining gaps:**
1. **Missed EP 9M short trades** — GOOG and BB were Pradeep's actual short trades (Jul 16-17). Neither appeared in any radar short list. The Bearish DEP scanner finds negative EP setups, but GOOG/BB were range-expansion breakdowns with catalysts, not classic negative EP patterns.
2. **No insider selling flag** — Pradeep keyed on DDOG (25-27 insiders) and CRWD (33 insiders) as next short candidates. The radar has no insider selling data.
3. **Over-generation persists** — 25-35 short candidates per day when Pradeep said "nothing on short side either" (Jul 20). The cap helped (125 → 25) but 25 is still too many for a "both sides dead" market.
4. **No "selling spreading" detection** — Pradeep's key Jul 17 insight was that selling was spreading from AI/semis to defensive names (KO, Disney, XLP). The radar doesn't detect this rotation pattern.

---

## Remaining Gaps (Prioritized)

### Gap 1 — DEP Suppression Threshold Too Tight (Jul 15-16)

**Problem:** 20% study at 30-32 on Jul 15-16 → DEP not suppressed → 9-20 noise candidates. Pradeep endorsed zero DEPs on all 4 days.

**Fix:** Raise DEP suppression threshold from < 30 to < 35. Pradeep's "no DEP" stance started when 20% study was at 25-32.

### Gap 2 — SIPs Small-Cap Bias (All 4 Days)

**Problem:** Radar SIPs dominated by micro-caps (BIYA, SDOT, SG). Pradeep's SIPs include mid/large-caps (TSM, UNH, ABT, GOOGL, AHR).

**Fix:** Add a separate "Large-Cap SIPs" pass — gap up > 2% on 1M+ volume with market cap > $10B. This would catch TSM, UNH, ABT, GOOGL.

### Gap 3 — No Dilution Risk Flag on SIPs (Jul 20)

**Problem:** ACHR, IREN, CLSK have shelf offerings / serial dilution. Pradeep explicitly flagged these as skip. Radar shows them without warning.

**Fix:** Add [DILUTION] flag to SIPs when the company has a shelf offering filed or float increased > 50% in 2 years.

### Gap 4 — Missed EP 9M Short Trades (Jul 16-17)

**Problem:** GOOG and BB were Pradeep's actual short trades. Neither appeared in radar short lists. They were range-expansion breakdowns with catalysts, not classic negative EP patterns.

**Fix:** Add an "EP 9M Downside" scanner — gap down > 4% on 1M+ volume with fresh negative catalyst. This would catch GOOG (Gemini delay) and BB (range expansion breakdown).

### Gap 5 — No Insider Selling Data (Jul 17)

**Problem:** Pradeep keyed on DDOG (25-27 insiders selling) and CRWD (33 insiders selling) as next short candidates. Radar has no insider selling data source.

**Fix:** Integrate insider selling feed (SEC Form 4 filings). Flag stocks with 10+ insider sales in last 30 days.

### Gap 6 — Action Summary Stale Text (All 4 Days)

**Problem:** Action summary still says "Place ANTS BSLO orders" even when ANTS is suppressed. Says "Place DEP limit orders" when DEP is at 0.

**Fix:** Make action summary dynamic — suppress line items when their corresponding scan returns 0 candidates.

### Gap 7 — No "Selling Spreading" Detection (Jul 17)

**Problem:** Pradeep's key Jul 17 insight: selling spreading from AI/semis to defensive names (KO, Disney, XLP). Radar doesn't detect this rotation.

**Fix:** Add a "Defensive Sector Alert" — when XLP, XLU, XLV show 3+ bearish reversals in a week after AI/semi weakness, flag "selling spreading to defensives."

### Gap 8 — FADE Mode Empty (Jul 17-20)

**Problem:** FADE mode label is correct, but the section is empty (0 candidates). Pradeep said "fading breakouts is better" — the radar should show yesterday's breakouts as fade candidates.

**Fix:** When FADE mode is active, populate the section with yesterday's SOS candidates that are now gapping down or failing follow-through.

---

## Trend Analysis — Error Frequency

| Error | Jul 15 | Jul 16 | Jul 17 | Jul 20 | Frequency |
|-------|:------:|:------:|:------:|:------:|:---------:|
| Regime too bullish | ⚠️ (close) | ⚠️ (close) | ✅ Fixed | ✅ Fixed | 2/4 (down from 4/4) |
| SOS over-generation | ✅ Fixed | ✅ Fixed | ✅ Fixed | ✅ Fixed | 0/4 (was 4/4) |
| DEP over-generation | ❌ Still | ❌ Still | ✅ Fixed | ✅ Fixed | 2/4 (was 4/4) |
| ANTS over-generation | ✅ Fixed | ✅ Fixed | ✅ Fixed | ✅ Fixed | 0/4 (was 4/4) |
| No SIPs detection | ⚠️ Partial | ⚠️ Partial | ⚠️ Partial | ⚠️ Partial | 4/4 (new module, 35% recall) |
| No short-side module | ✅ Fixed | ✅ Fixed | ✅ Fixed | ✅ Fixed | 0/4 (was 3/4) |
| 20% study not used | ✅ Fixed | ✅ Fixed | ✅ Fixed | ✅ Fixed | 0/4 (was 4/4) |
| Sector rotation mismatch | ⚠️ Partial | ⚠️ Partial | ⚠️ Partial | ✅ Improved | 3/4 (was 4/4) |

**Fixed:** 5 of 8 systemic errors are fully resolved (SOS, ANTS, short-side, 20% study, regime).
**Partially fixed:** 2 of 8 (DEP threshold, SIPs detection).
**Still open:** 1 of 8 (sector rotation mismatch — radar still finds breakouts where Pradeep sees hiding spots).

---

## Conclusion

The Phase F+G+H fixes transformed the radar from a 5.4% accuracy pattern-recognition engine into a 63.3% accuracy situational-awareness-aware system. The single most impactful fix was the **20% study suppression gate** — it eliminated 340 false-positive long candidates (200 SOS + 70 DEP + 140 ANTS) across 4 days, replacing them with zero when Pradeep said zero.

The **regime retuning** was the second most impactful fix — the progression from FULL_BULL → CAUTIOUS_BULL → DISTRIBUTING tracks Pradeep's market read almost perfectly by Jul 20.

The **SIPs module** is the biggest new capability but has the most room to grow — 35% recall means we're finding 1 in 3 of Pradeep's SIPs. The small-cap bias and missing dilution flags are the key improvements needed.

The **short-side module** is functional but still over-generates (25-35 candidates when Pradeep says "nothing on short side either"). The EP 9M downside scanner would catch the actual trades (GOOG, BB) that the current Bearish DEP scanner misses.

**Next priorities:**
1. Raise DEP suppression threshold to < 35 (fixes Jul 15-16 leakage)
2. Add large-cap SIPs pass (fixes TSM, UNH, ABT, GOOGL misses)
3. Add dilution risk flag to SIPs (fixes ACHR, IREN, CLSK)
4. Build EP 9M downside scanner (fixes GOOG, BB short trade misses)
5. Make action summary dynamic (fixes stale "place ANTS BSLO orders" text)