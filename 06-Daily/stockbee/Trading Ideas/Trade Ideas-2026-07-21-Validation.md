---
title: "Trade Ideas Validation — July 21 Market vs July 21 Radar"
date: 2026-07-21
tags: [analysis, validation, trade-ideas, comparison, stockbee, pradeep-bonde, market-regime]
---

# Trade Ideas Validation — July 21 Market vs July 21 Radar

Radar called CAUTIOUS_BULL / REDUCE_SIZE; Pradeep called range-bound chop with breakouts failing — the radar was too bullish, over-generated swing setups, and entirely missed SIPs, the only setup consistently making money on July 21.

---

## 1. Market Regime Comparison

| Dimension | Radar Verdict | Pradeep's SA | Match? |
|-----------|---------------|--------------|--------|
| Regime label | CAUTIOUS_BULL | Range-bound / choppy / "London Calling" range | **No** — "bull" label wrong |
| Action | REDUCE_SIZE | Do not buy breakouts; intraday/SIPs only | Partial — both reduce, but Pradeep says *no* swing buys |
| Primary breadth | Net +75, BO:BD 3.54 (positive day) | "Primary breadth turned negative"; 8 of 12 days negative, 5 were 300+ selling | **No** — radar used single-day snapshot; Pradeep used 12-day trend |
| T2108 | 50.19% | Not cited directly, but wants T2108 in single digits for bottom fishing | Neutral |
| EP 9M follow-through | Not tracked | "Only 2-3 followed through positive in last 5 days, more on bearish side" | **Missing** — radar has no EP 9M follow-through study |
| 20% study | Not cited as SA input | "20% study only at 14-15" — used as evidence of no momentum | **Missing** — radar has the data but doesn't use it as regime signal |
| 3-5 day follow-through | Not tracked | "None of these moves have had 2-3 day follow through" — core thesis | **Missing** — critical regime input absent |

> "We are in a tight range bound market… if you are trading to momentum, then there has to be a inherent momentum in the market. If there is no momentum… none of these moves have had two or three days follow through."
> — Pradeep, AM [03:23]

> "Failure to acknowledge that will cost you money if you keep buying breakouts."
> — Pradeep, AM [05:31]

**Verdict:** Radar's REDUCE_SIZE action was directionally correct (acknowledging weakness), but the CAUTIOUS_BULL label is wrong. Pradeep's SA is RANGE_BOUND / NO_BREAKOUTS. The radar's regime engine relies on single-day breadth snapshots and monthly 25% ratio, but ignores the 12-day breadth trend, EP 9M follow-through rate, and 3-5 day follow-through — the three signals Pradeep actually uses.

---

## 2. SOS Breakout Candidates

Radar generated **50 SOS candidates** (top 20 shown). Pradeep explicitly endorsed **zero**.

| Radar SOS Pick | Pradeep Mentioned? | Pradeep's Verdict |
|----------------|-------------------|-------------------|
| GM (#1) | Yes — "General Motors. Wow." AM [42:43] | Not endorsed as buy; observation only |
| CDE, BTG, AG, PAAS, FSM, SSRM, EGO, AGI, SVM, WPM (gold miners) | SSRM, AG mentioned PM [16:20] | "Gold is very choppy… most of the time doesn't work"; showing "near bottom" |
| DHR (#4, –11% change) | Not mentioned as buy | Negative-change stock in SOS list = **misclassified** |
| ALSN, APH, CLOV, AMLX, WFRD, DHC, GTES, HRMY | Not mentioned | — |

**Key rejection:**

> "I don't see anything here to get excited about… do you see any clean breakout or you just see some really loose, choppy action… there's no tight action, there is no linear moves."
> — Pradeep, AM [30:34]

> "Are breakouts working? No. Are they having follow through? No."
> — Pradeep, AM [57:57]

**AHR — the one stock Pradeep liked — was NOT in the radar's SOS list.** Pradeep said:

> "If I had to, gun to head, AHR is the only thing I would look at."
> — Pradeep, AM [60:06]

**Misclassification:** DHR appears as SOS #4 with a **–11%** change. A stock down 11% should not be a breakout candidate — this is a WSS/short candidate, and indeed the radar also lists DHR in WSS Enhanced as sector_breakdown short. Contradictory classification.

**Score: 2/10** — 50 picks, zero endorsed, one liked stock (AHR) missed entirely, one internal contradiction (DHR).

---

## 3. DEP Candidates

Radar generated **20 DEP candidates**. Pradeep validated **zero** and explicitly rejected the loose definition.

| Radar DEP | Market Cap | 1000+ Funds? | Pradeep Validated? |
|-----------|-----------|-------------|-------------------|
| CRNX | $8.9B | Yes | Not mentioned |
| ABT | $173.6B | Yes (5000+) | Not mentioned |
| PYPL | $49.3B | Yes (2500+) | Not mentioned |
| WU | $2.6B | Speculative | **Fails Pradeep's DEP definition** |
| NKE | $63.6B | Yes | Not mentioned |
| NVDA | — | Yes | Mentioned as SIPs/day trade fade, NOT DEP |
| SNAP | small | — | **Fails DEP definition** |
| BTE | small | — | **Fails DEP definition** |
| CCC | small | — | **Fails DEP definition** |
| BKR | — | — | Mentioned PM as oil & gas — "not convinced" |

Pradeep's DEP definition (PM [25:36]):

> "For a DEP, what is the condition required? Institutional quality, 1000+ funds. The stock should react positively on the day of the earnings. Market cap 10 billion+. Genuine catalyst plus institutional quality. That's the setup definition. Nowadays, everything is a DEP."

The radar's DEP scanner includes sub-$10B stocks (WU $2.6B, SNAP, BTE, CCC) that **fail Pradeep's institutional-quality filter**. In a choppy market with no follow-through, generating 20 DEPs is over-generation — Pradeep's bar is far higher.

**Score: 2/10** — 20 DEPs, zero validated, multiple sub-10B stocks that fail the definition, no earnings-reaction filter.

---

## 4. Anticipation (ANTS)

| Metric | Radar | Pradeep |
|--------|-------|---------|
| ANTS count | 35 | 50 (on ANTS 15 scan) |
| Normal baseline | Not tracked | 400–500 |
| Quality assessment | 35 candidates, all prioritized "highest" | "There is nothing which is setting up as anticipation" |

Pradeep used the ANTS 15 count as a **situational awareness signal** — 50 vs normal 400-500 tells him the market has no first-leg momentum. The radar treats ANTS as actionable trade ideas and assigns "highest" priority to all 35.

> "What number do you see on ANTS 15? 50. Normally, how many do you see? That tells you that first leg moves — there are very few first leg moves."
> — Pradeep, PM [21:35]

> "There is nothing which is setting up as anticipation also."
> — Pradeep, PM [26:53]

**Score: 4/10** — count is in the right direction (low), but radar should use ANTS count as a *regime signal* (50 vs 400 baseline = no momentum), not as a trade-idea list. All "highest" priority in a market Pradeep says has no setups is misleading.

---

## 5. Short-Side Setups

Radar generated **95 short candidates** across 5 categories. Pradeep's actual short picks were narrow.

| Pradeep Short Pick | Radar Category | Match? |
|-------------------|----------------|--------|
| FIG (EP 9M struggling, earnings rate 5) | WSS Enhanced — sector_breakdown | **Yes** — correctly identified |
| CrowdStrike (CRWD) — "matter of time" | Not in short list | **Missed** |
| AEHR fade (later in day) | Not in short list | **Missed** — radar had AEHR nowhere |
| CLSK (faded after catalyst) | Not in short list | **Missed** — classic failed breakout fade |
| Gold miners (choppy, not short) | Not shorted | Correct — radar had them as SOS longs |

Radar's WSS Enhanced caught FIG. But the 95-candidate short list is massively over-generated — Pradeep only singled out 2-3 shorts. The Momentum Inversion list (VCIG, QUCY, AIIO — stocks that went up 900% and crashed 90%) is not actionable; those are already destroyed.

> "If you are so inclined to look at FIG as a short EP 9M… this has been struggling for quite some time. There's some rally here is failing."
> — Pradeep, PM [01:46]

**Score: 5/10** — FIG correctly caught; CRWD, AEHR, CLSK missed; 95 candidates is noise, not signal.

---

## 6. SIPs Detection

**This is the radar's biggest failure.** The radar has **no SIPs category**. SIPs were the #1 working setup on July 21.

| Pradeep SIPs/Day Trade | Catalyst | Radar Detected? |
|------------------------|----------|-----------------|
| TSLA | Robotaxis in Tampa announcement | **No** — not in any radar list |
| NBIS | "Today's SIPs" (AM [16:53]) | **No** |
| AMD | SIPs, gapping up | **No** — radar had AMD as Sugar Baby only |
| ACHR | Archer Aviation story (AM [48:08]) | **No** — appeared in Bearish Reversal list (misclassified) |
| VIVACORE | Water-to-oil fugazi story | **No** |
| Zibot | Veterinary China, +516% | **No** |

> "SIPs is what is working… SIPs doesn't care about [market conditions]. SIPs work every day."
> — Pradeep, AM [07:56]

> "The best SIPs are the one which has zero earnings, zero sales, and no probability of even making [revenue]. It's all stories. It's all fugazi."
> — Pradeep, AM [49:21]

Pradeep's SIPs criteria:
- Morning catalyst / news (any news, not just earnings)
- Small float (often <1M shares)
- Low market cap
- Gap up premarket
- Story-driven (fugazi is fine)

The radar scans for institutional swing setups (EP, DEP, SOS) and entirely misses the micro-cap catalyst-driven day-trade universe. In a choppy market where Pradeep says only SIPs and intraday work, this is a **critical gap**.

**Score: 0/10** — no SIPs detection exists. The single most profitable setup class in this regime is invisible to the radar.

---

## 7. Sector Analysis

| Radar Sector Call | Pradeep Commentary | Match? |
|-------------------|-------------------|--------|
| Leading: BUG (cybersecurity, RS_20d 34.18) | BUG mentioned in PM ticker pass [10:33], no endorsement | Weak — radar identifies RS leader but Pradeep doesn't act on it |
| Precursor: Basic Materials (15 breakouts, gold miners) | "Gold stocks showing up near bottom… SSRM, AG… but gold is very choppy, most of time doesn't work" PM [15:54] | **Partial** — sector activity confirmed but not actionable |
| Precursor: Industrials (11 breakouts) | Not mentioned | — |
| Precursor: Healthcare (7 breakouts) | ABT, DHR in DEP/SOS but not endorsed | — |
| Precursor: Technology (7 breakouts) | Not mentioned as sector | — |
| Oil & Gas | Baker Hughes, Schlumberger mentioned PM [19:21] — "not convinced… geopolitical catalyst but choppy" | Radar had XOP as #2 RS but no oil precursor |
| Semiconductors | Cerebras, SK Hynix, Intel, NVDA mentioned as fading | Radar had SMH as weakest sector (RS_20d –24.27) — **correct** |

> "If you're into gold kind of stocks, they are showing up here near the bottom. Gold tends to work from bottom."
> — Pradeep, PM [15:54]

**Score: 4/10** — Basic Materials precursor partially valid; semiconductor weakness correctly detected; but sector RS leaders (BUG) don't translate to actionable setups in Pradeep's framework.

---

## 8. Summary Scorecard

| Category | Score | One-Line Verdict |
|----------|-------|-----------------|
| Market Regime | 4/10 | REDUCE_SIZE directionally right; CAUTIOUS_BULL label wrong — should be RANGE_BOUND |
| SOS Breakouts | 2/10 | 50 picks, zero endorsed; AHR (only liked stock) missed; DHR misclassified |
| DEP Candidates | 2/10 | 20 DEPs, zero validated; sub-10B stocks fail definition; no earnings-reaction filter |
| Anticipation | 4/10 | Count low (correct direction) but used as trade list not SA signal; all "highest" priority |
| Short-Side | 5/10 | FIG caught; CRWD/AEHR/CLSK missed; 95 candidates = noise |
| SIPs Detection | 0/10 | No SIPs category — complete blind spot; #1 working setup invisible |
| Sector Analysis | 4/10 | Basic Materials partial; semis weakness correct; BUG leader not actionable |
| **Overall** | **3/10** | Radar over-generates swing setups in a no-follow-through market and misses SIPs entirely |

---

## 9. Key Improvements

1. **Add SIPs detection module** — premarket gap scan with catalyst/news flag, float <2M, market cap <$500M, gap >5%. This is the #1 gap. Without it, the radar is useless in choppy markets where Pradeep says only SIPs work.

2. **Downgrade regime to RANGE_BOUND** when: primary breadth negative for 8+ of 12 days, EP 9M follow-through <30%, 3-5 day follow-through absent. Current engine uses single-day snapshots; Pradeep uses 12-day trends.

3. **Track EP 9M follow-through rate** as a core regime input. Pradeep explicitly checks "how many EP 9M followed through in last 5 days." Radar has EP data but no follow-through study.

4. **Use 20% study and ANTS 15 count as SA signals**, not just trade lists. ANTS 15 at 50 vs 400-500 baseline = "no momentum" signal that should suppress all swing trade generation.

5. **Tighten DEP filter**: market cap ≥$10B, 1000+ fund ownership, positive earnings-day reaction required. Remove WU, SNAP, BTE, CCC-class stocks from DEP.

6. **Suppress SOS generation when 3-5 day follow-through = 0**. In Pradeep's words, breakouts "show up" but "don't follow through" — generating 50 SOS picks in this environment is actively harmful.

7. **Add failed-breakout fade / EP 9M short scan**. AEHR, CLSK, CRWD patterns — stocks with catalyst that gap and fade — are Pradeep's short-side bread and butter in choppy markets.

8. **Fix DHR contradiction** — a stock down 11% should not appear as SOS #4 and WSS short simultaneously. Add change% sign check to SOS filter.

9. **Add 3-5 day follow-through tracker** — for every EP/SOS in last 5 days, track whether it closed higher 2, 3, 5 days later. This is Pradeep's core momentum confirmation.

10. **Reduce short-side from 95 to ≤15 actionable candidates**. Filter Momentum Inversion to stocks still liquid and not yet destroyed. Focus on failed-breakout fades and EP 9M breakdowns.