---
title: "Trade Ideas Multi-Day Validation — July 15-20 Radar vs Pradeep Meetings"
date: 2026-07-21
tags: [analysis, validation, trade-ideas, comparison, stockbee, pradeep-bonde, multi-day, market-regime]
---

# Trade Ideas Multi-Day Validation — July 15-20 Radar vs Pradeep Meetings

A four-day head-to-head audit of the Daily Trading Radar engine against Pradeep Bonde's actual meeting commentary (AM + PM) for July 15, 16, 17, and 20, 2026 — the radar called FULL_BULL on Day 1-2 while Pradeep said "my wallet is closed," and the radar's structural blind spots (no SIPs, no 20% study suppression, DEP/ANTS over-generation) persisted across all four sessions.

---

## Day 1 — Tuesday, July 15, 2026

### Radar Regime vs Pradeep SA

| Dimension | Radar (for Jul 15) | Pradeep (Jul 15 AM + PM) | Match? |
|-----------|-------------------|--------------------------|--------|
| **Regime** | FULL_BULL → FULL_LONG (60% conf.) | Range-bound, "breakouts unlikely to follow through" | ❌ Wildly wrong |
| **T2108** | 52.25% — "stable bullish range" | Referenced 20% study readings (~25 bullish / 15 bearish), said market "gone into sleep" after 18% move in 2 months | ❌ Radar read T2108 as bullish; Pradeep read 20% study as sleep/chop |
| **Breadth** | Net Primary +334, "stable positive" | "Funds are not aggressively buying, and funds are not aggressively selling" — stalemate | ❌ Radar interpreted positive breadth as bullish; Pradeep saw it as no-man's-land |
| **Action** | "Full playbook — 5 SOS with 6/6 TL" | "My wallet is closed." "I just don't see any need to open my wallet." | ❌ Opposite |

> "Breakouts unlikely to follow through. I have a big follow through, which is my main situational awareness."
> — Pradeep, Jul 15 AM [01:11]

> "The funds are not aggressively buying, and the funds are not aggressively selling. When do you make money? You make money when the funds are aggressively buying."
> — Pradeep, Jul 15 AM [02:23]

> "My wallet is closed."
> — Pradeep, Jul 15 AM [68:15]

### SOS Breakout Validation

| Radar SOS Pick | Two Lynch | Pradeep Mentioned? | Verdict |
|---------------|-----------|---------------------|---------|
| [[GOOGL]] | 6/6 | ✅ Mentioned in PM as "second day of a breakout" — said "My method does not involve buying second day of the breakout" | ❌ Rejected (wrong day) |
| [[GOOG]] | 6/6 | ✅ Same as GOOGL | ❌ Rejected |
| [[GS]] | 6/6 | ✅ Mentioned next day (Jul 16) — "Goldman Sachs... may follow through, but almost ended up giving you" | ❌ Rejected (failed follow-through) |
| [[AFRM]] | 6/6 | ❌ Not mentioned | — |
| [[HWM]] | 6/6 | ❌ Not mentioned | — |

**Radar said:** "All 5 top SOS candidates have perfect 6/6 Two Lynch scores — very high quality breakout day!"

**Pradeep said:** "Just see what happened to breakouts from yesterday, and did they follow through." (PM) — He was systematically skeptical of all breakouts.

**Score: 0/5 endorsed.** The radar's SOS module generated 50 candidates; Pradeep endorsed zero. The 6/6 Two Lynch score was meaningless in this market.

### DEP Validation

| Radar DEP Pick | Width | Pradeep Mentioned? | Verdict |
|----------------|-------|---------------------|---------|
| [[AAPL]] | 5.36% | ✅ Mentioned as "continuation setup... for some reason" — not as DEP | ❌ Not endorsed as DEP |
| [[NKE]] | 7.65% | ❌ Not mentioned | — |
| [[TECH]] | 1.28% | ❌ Not mentioned | — |
| [[APGE]] | 1.0% | ❌ Not mentioned | — |
| [[ABBV]] | 6.96% | ❌ Not mentioned this day (mentioned Jul 16 as "will fit/chop") | — |

**Radar said:** 10 DEP candidates found. Placed limit orders.

**Pradeep said:** "I don't see anything which is actionable here." (PM) — No DEP discussion at all.

**Score: 0/5 validated.** The radar's DEP module generated 10 candidates; Pradeep validated zero. Key issue: the radar didn't check whether these stocks had genuine catalysts (Pradeep's DEP definition requires 1,000+ fund ownership + $10B+ market cap + positive earnings reaction + genuine catalyst).

### Anticipation

**Radar:** 35 ANTS candidates. Top 5: AAPL, AMZN, NFLX, CPRX, HBAN. Placed BSLO orders.

**Pradeep:**

> "In this market condition, anticipation, if you're trying to work, it is not going to work... For anticipation to work, you need to be in a market which is where buyers are falling all over and just little pause and buying is going to come in. Otherwise, it just doesn't work."
> — Pradeep, Jul 16 AM [69:06]

(Said on Jul 16, but the principle was the same on Jul 15 — he said "I don't really see anything which is, like, to me personally" on anticipation in the Jul 15 PM.)

**Score: 0/5.** Anticipation is the worst setup in a range-bound market. The radar generated 35 candidates — all noise.

### Short-Side

**Radar:** No short-side module for July 15. Zero short candidates.

**Pradeep:** Mentioned short-side interest: "This party on the semiconductor is over" (PM). Named [[DELL]] breakdown, "lemonade" (likely a stock). Said "shorts look more attracted to me than lungs because most of the lungs don't have [follow through]. But, like, shorts are also not having really, much of a follow through."

**Score: 0/10.** Complete blind spot. The radar had no short-side capability.

### SIPs Gap

| Pradeep SIPs / Day Trade | Radar Detected? | Notes |
|--------------------------|-----------------|-------|
| [[AHR]] | ❌ | Pradeep analyzed extensively using Grok — 36% gap up, 272 funds, target $100 already priced in. "Just a SIPs." |
| ELVA | ❌ | "Might work as a delayed reaction" (Jul 16 AM) |
| [[PENN]] | ❌ | "Everybody was excited... I was in Oslo that day... nothing happened." |
| [[SNDK]] / [[MU]] / [[WDC]] | ❌ | "Whatever I'm watching, like, SNDK, Mo, these are all, like, Western Digital" — semis in play |
| Amazon / Apple | ❌ | Mentioned as continuation setups for "if you're inclined to chop yourself" |

**Score: 0/5.** The radar has NO SIPs detection module — the single biggest gap.

### Daily Scorecard — July 15

| Category | Score (0-10) | Notes |
|----------|:------------:|-------|
| Regime Match | 1 | FULL_BULL vs range-bound — nearly opposite |
| SOS Validation | 0 | 0 of 5 endorsed |
| DEP Validation | 0 | 0 of 5 validated |
| Anticipation | 0 | 35 ANTS, all noise |
| Short-Side | 0 | No module |
| SIPs Gap | 0 | No detection — biggest blind spot |
| **Total** | **1/60** | Catastrophic mismatch |

---

## Day 2 — Thursday, July 16, 2026

### Radar Regime vs Pradeep SA

| Dimension | Radar (for Jul 16) | Pradeep (Jul 16 AM + PM) | Match? |
|-----------|-------------------|--------------------------|--------|
| **Regime** | FULL_BULL → FULL_LONG (60% conf.) | "At the open, you don't buy anything." Breakouts "likely to chop." | ❌ Still wrong |
| **T2108** | 53.83% — "rising slightly, bullish" | "20% study is still at 20" — low readings, not confirming | ❌ |
| **Breadth** | Net +223, breakouts 235, "market stabilizing" | "We have reached a stalemate. There is no buying and there is no selling." Selling accelerating. | ❌ |
| **Action** | "Full playbook — 4 SOS with 6/6 TL" | "I'm not going to take a trade till I get a good read on the market." Then SHORTED Google. | ❌ Opposite direction |

> "At the open, you don't buy anything."
> — Pradeep, Jul 16 AM [01:35]

> "Ultimately, at some stage, all traders learn, by sheer experience that essay is greater than setup."
> — Pradeep, Jul 16 AM [03:25]

> "Situational awareness is that breakouts are unlikely to work. But what we have seen is that selling has accelerated."
> — Pradeep, Jul 16 PM [00:31]

### SOS Breakout Validation

| Radar SOS Pick | Two Lynch | Pradeep Mentioned? | Verdict |
|---------------|-----------|---------------------|---------|
| [[URBN]] | 6/6 | ❌ Not mentioned | — |
| [[NMRK]] | 6/6 | ❌ Not mentioned | — |
| [[MGA]] | 6/6 | ❌ Not mentioned | — |
| [[MMI]] | 6/6 | ❌ Not mentioned | — |
| [[GOOGL]] | 5/6 | ✅ **SHORTED Google** — "I took a Google, like, whenever when I saw today as a short." | ❌ Radar said BUY, Pradeep SHORTED |
| [[GOOG]] | 5/6 | ✅ Same as GOOGL — shorted | ❌ |
| [[PENN]] | 5/6 | ✅ Mentioned Jul 15 as a failed breakout ("nothing happened") | ❌ Already rejected |
| [[AAPL]] | 5/6 (2nd leg) | ✅ "Apple, for some reason" mentioned as continuation — not endorsed | ❌ |
| [[AMZN]] | 5/6 | ✅ "Amazon is where the money is flowing" — but as day trade observation, not SOS buy | ⚠️ Partial |

**Radar said:** "Full playbook — 4 SOS with 6/6 Two Lynch scores (URBN, NMRK, MGA, MMI)."

**Pradeep said:** "I don't see anything which is actionable." (AM) And he shorted the radar's #5-6 SOS pick (Google).

**Score: 0/5 endorsed.** The radar's top 6/6 picks were never mentioned. Google — which the radar ranked #5-6 for long — was shorted by Pradeep.

### DEP Validation

| Radar DEP Pick | Width | Pradeep Mentioned? | Verdict |
|----------------|-------|---------------------|---------|
| [[XOM]] | 2.80% | ❌ Not mentioned | — |
| [[BKR]] | 5.68% | ❌ Not mentioned | — |
| [[BTE]] | 8.98% | ❌ Not mentioned | — |
| [[CRNX]] | 0.67% | ❌ Not mentioned | — |
| [[TECH]] | 1.28% | ❌ Not mentioned | — |
| [[KHC]] | 5.31% | ❌ Not mentioned | — |
| [[NKE]] | 7.65% | ❌ Not mentioned | — |
| [[ABBV]] | 6.96% | ✅ "These kind of pharma company stocks are attracting some buying. But, again... same problem. Is it a good setup? Yes. But what is likely to happen? It will fit." | ❌ Rejected (will chop) |

**Radar said:** 20 DEP candidates. Placed 10 limit orders.

**Pradeep said:** "I don't see a DEP on a bullish side here." (said Jul 17 AM, but same stance). On ABBV specifically: "it will fit" (chop/fade).

**Score: 0/5 validated.** 20 DEP candidates generated; Pradeep validated zero. The one he mentioned (ABBV), he explicitly said would fail.

### Anticipation

**Radar:** 35 ANTS. Top: T (super-tight 3T), LCID (ultra-tight), PFE, CMCSA, HIMS, AMZN, NFLX, GOOGL, GOOG, PLTR.

**Pradeep:**

> "In this market condition, anticipation, if you're trying to work, it is not going to work... These are not going to work in this market condition, my friend."
> — Pradeep, Jul 16 AM [67:59]

> "Anticipation is the worst setup to focus on here, even worse than breakouts."
> — Pradeep, Jul 16 AM (context of range-bound)

**Score: 0/5.** 35 ANTS candidates, all rejected. Pradeep called anticipation "the worst setup" in this market.

### Short-Side

**Radar:** Still no short-side module for July 16.

**Pradeep:** SHORTED [[GOOGL]] and [[BB]] (Blackberry). Both were EP 9,000,000 on the downside.

> "I shorted Google yesterday. Why? Because that was the EP 9,000,000... I shorted BB yesterday. Why? Because it was an EP 9,000,000."
> — Pradeep, Jul 17 AM [16:14]

> "Google... selling might accelerate even more. It's been straight down."
> — Pradeep, Jul 16 PM [05:27]

Google catalyst: Gemini launch postponed. BB: "clear range expansion... this is where people were hiding, funds were hiding."

**Score: 0/10.** Radar generated zero shorts. Pradeep made two EP 9M short trades.

### SIPs Gap

| Pradeep SIPs / Day Trade | Radar Detected? | Notes |
|--------------------------|-----------------|-------|
| [[UNH]] (UnitedHealth) | ❌ | "UnitedHealth will be a day trade today" — catalyst in premarket |
| [[ABT]] (Abbott Labs) | ❌ | Abbott catalyst — CGM competitor, continuous glucose monitors |
| [[DXCM]] | ❌ | "DXCM is also going up because of Abbott Laboratories" |
| ELVA | ❌ | "might work as a delayed reaction" — on watch list |
| [[TSM]] (Taiwan Semi) | ❌ | "very choppy" — mentioned but not traded |

**Score: 0/5.** Radar missed all SIPs. UnitedHealth and Abbott were the day's primary catalyst stocks.

### Daily Scorecard — July 16

| Category | Score (0-10) | Notes |
|----------|:------------:|-------|
| Regime Match | 1 | FULL_BULL vs "don't buy anything" — still opposite |
| SOS Validation | 0 | 0 of 5 endorsed; Google was shorted instead |
| DEP Validation | 0 | 0 of 5 validated; ABBV explicitly called a chop |
| Anticipation | 0 | 35 ANTS — "worst setup" per Pradeep |
| Short-Side | 0 | No module; Pradeep shorted GOOGL + BB |
| SIPs Gap | 0 | Missed UNH, ABT, DXCM, ELVA |
| **Total** | **1/60** | No improvement from Day 1 |

---

## Day 3 — Friday, July 17, 2026

### Radar Regime vs Pradeep SA

| Dimension | Radar (for Jul 17) | Pradeep (Jul 17 AM + PM) | Match? |
|-----------|-------------------|--------------------------|--------|
| **Regime** | CAUTIOUS_BULL → REDUCE_SIZE (65% conf.) | Range-bound, selling spreading, "I just don't see anything" | ⚠️ Closer but still too bullish |
| **T2108** | 56.29% — "rising" | "20% study is still at, like, in a some fourteen, fifteen currently" — low | ❌ Radar saw T2108 rising as neutral; Pradeep saw 20% study as sleep |
| **Breadth** | Net +144 (declining), breakdown spike 509 | "Selling is going to spread to the other stocks which are holding up" — confirming radar's breakdown spike concern | ✅ First alignment |
| **Action** | "REDUCE_SIZE — selective setups only" | "I just don't see anything." "There is nothing I can see." | ⚠️ Radar said reduce; Pradeep said nothing to do |

> "Situational awareness remains same... tight range for the time being result into selling in select AI themed stock. The selling is restricted."
> — Pradeep, Jul 17 AM [01:31]

> "The implication is very clear that most likely, what is going to happen is selling is going to spread to the other stocks which are holding up."
> — Pradeep, Jul 17 PM [01:34]

**Notable improvement:** The radar downgraded from FULL_BULL to CAUTIOUS_BULL/REDUCE_SIZE — its first regime correction. The breakdown spike (509 vs 251) was correctly flagged.

### SOS Breakout Validation

| Radar SOS Pick | Two Lynch | Pradeep Mentioned? | Verdict |
|---------------|-----------|---------------------|---------|
| [[NKE]] | 6/6 | ❌ Not mentioned as SOS | — |
| [[MDLZ]] | 6/6 | ❌ Not mentioned | — |
| [[CTRE]] | 6/6 | ❌ Not mentioned | — |
| [[AHR]] | 6/6 | ✅ "AHR... I told you on the day of the earning itself... it's just a sips" (Jul 20 ref) | ❌ Rejected as SOS |
| [[CCEP]] | 6/6 | ❌ Not mentioned | — |
| [[ITW]] | 6/6 | ❌ Not mentioned | — |
| [[XPO]] | 6/6 | ❌ Not mentioned | — |

**Radar said:** "10 SOS candidates with perfect 6/6 Two Lynch scores! Real Estate has 5 of the top 10."

**Pradeep said:** "I don't see anything which is actionable here." "Most breakouts are not likely to work till I see a contrary evidence to it." (PM)

The radar's Real Estate sector call (12 breakouts) was specifically wrong — Pradeep said selling would spread to "stocks which are holding up" (i.e., Real Estate was where people were hiding, and it would break down next).

**Score: 0/5 endorsed.** 50 SOS candidates, zero endorsed.

### DEP Validation

| Radar DEP Pick | Width | Pradeep Mentioned? | Verdict |
|----------------|-------|---------------------|---------|
| [[XOM]] | 3.39% | ❌ Not mentioned | — |
| [[BKR]] | 5.68% | ❌ Not mentioned | — |
| [[PTEN]] | 8.64% | ❌ Not mentioned | — |
| [[CRNX]] | 0.67% | ❌ Not mentioned | — |
| [[TECH]] | 1.28% | ❌ Not mentioned | — |
| [[NKE]] | 7.65% | ❌ Not mentioned | — |

**Radar said:** 20 DEP candidates.

**Pradeep said:**

> "I don't see a DEP on a bullish side here... There is no DEP I see."
> — Pradeep, Jul 17 AM [52:01]

**Score: 0/5 validated.** 20 DEP candidates; Pradeep explicitly said "no DEP I see." Total contradiction.

### Anticipation

**Radar:** 35 ANTS. Top: NU (super-tight), T (super-tight), GOOGL (super-tight), BAC (super-tight), NFLX (tight).

**Pradeep:**

> "I don't really see any anticipation set up also which was setting up."
> — Pradeep, Jul 17 PM [24:29]

**Score: 0/5.** 35 ANTS; Pradeep saw zero. The "super-tight" tier the radar introduced was irrelevant — tight days don't matter when breakouts don't follow through.

### Short-Side

**Radar:** Still no short-side module for July 17.

**Pradeep:** Continued holding Google and BB shorts from Jul 16. Mentioned selling spreading:

> "It might be that the selling in the semiconductors and AI team might have, for the time being, stopped. But what is most likely to happen is that it might spread to other thing."
> — Pradeep, Jul 17 PM [03:46]

> "Look for something which is already weak rather than trying to short something which is already strong."
> — Pradeep, Jul 17 AM [38:08]

Mentioned [[DDOG]] (Datadog) and [[CRWD]] (Crowd) as next candidates to break down — "33 insiders selling... it's almost like they're telling you, we don't believe in our own company."

**Score: 0/10.** No short module. Pradeep was actively short and identifying next short candidates.

### SIPs Gap

| Pradeep SIPs / Day Trade | Radar Detected? | Notes |
|--------------------------|-----------------|-------|
| [[TSM]] (Taiwan Semi) | ❌ | "Taiwan Semi, yesterday, had a very good earnings" |
| ORCA | ❌ | One of only two stocks Pradeep saw (PM) |
| [[CADL]] | ❌ | Second of only two stocks Pradeep saw (PM) |
| [[SNDK]] / [[MU]] / [[SOXL]] | ❌ | Semis in play for day trading |
| [[NFLX]] | ❌ | Mentioned but "I have no way to know what Netflix catalyst is going to be" |

**Score: 0/5.** ORCA and CADL were the only two stocks Pradeep found actionable — neither appeared anywhere in the radar.

### Daily Scorecard — July 17

| Category | Score (0-10) | Notes |
|----------|:------------:|-------|
| Regime Match | 4 | CAUTIOUS_BULL/REDUCE_SIZE — closer, but still too bullish. First downgrade. |
| SOS Validation | 0 | 0 of 5 endorsed; Real Estate call was wrong |
| DEP Validation | 0 | 20 DEPs; Pradeep said "no DEP I see" |
| Anticipation | 0 | 35 ANTS; Pradeep saw zero |
| Short-Side | 0 | No module; Pradeep holding shorts + finding new candidates |
| SIPs Gap | 0 | Missed ORCA, CADL, TSM, SNDK/MU |
| **Total** | **4/60** | Slight improvement (regime downgrade) |

---

## Day 4 — Monday, July 20, 2026

### Radar Regime vs Pradeep SA

| Dimension | Radar (for Jul 20) | Pradeep (Jul 20 AM + PM) | Match? |
|-----------|-------------------|--------------------------|--------|
| **Regime** | CAUTIOUS_BULL → REDUCE_SIZE | "Range bound market... nothing to do. Literally, like, nothing to do." | ⚠️ Radar said reduce; Pradeep said nothing |
| **T2108** | 53.50% — stable | "20% study on bullish size is at 15" — used for bounce assessment | ❌ Radar didn't use 20% study |
| **Breadth** | Net +44 (very low), 5d ratio 0.70, 10d 0.75 | "Selling is going to spread... both sides, shots as well as lungs are not really working" | ✅ Breadth deterioration confirmed |
| **Action** | "REDUCE_SIZE — selective setups only" | "Nothing really on the short side. Nothing really on the long side. Nothing really on, reversal." | ⚠️ Radar said selective; Pradeep said nothing |

> "Short term, I say we remain in a range bound market. 20% study on bullish size is at 15."
> — Pradeep, Jul 20 AM [02:41]

> "There is nothing which you can do here about the market except for a day trade. Otherwise, like, in a most of the time, if you take anything overnight, probability of that working is not."
> — Pradeep, Jul 20 PM [01:10]

> "Nothing to do. Literally, like, nothing to do."
> — Pradeep, Jul 20 PM [06:25]

> "Both sides, shots as well as lungs are not really, like, working."
> — Pradeep, Jul 20 PM [06:36]

### SOS Breakout Validation

| Radar SOS Pick | Two Lynch | Pradeep Mentioned? | Verdict |
|---------------|-----------|---------------------|---------|
| [[DRS]] | 6/6 | ❌ Not mentioned | — |
| [[RHP]] | 6/6 | ❌ Not mentioned | — |
| [[AQST]] | 5/6 | ❌ Not mentioned | — |
| [[ETON]] | 5/6 | ❌ Not mentioned | — |
| [[AIRS]] | 5/6 | ❌ Not mentioned | — |
| [[NFLX]] | 4/6 | ✅ Mentioned — "I have no way to know what Netflix catalyst is going to be" (Jul 16). Not endorsed. | ❌ |

**Radar said:** 50 SOS candidates. Healthcare sector precursor (18 breakouts).

**Pradeep said:** "I don't see anything which I would like and take as a swing." (AM) "Nothing really on the long side." (PM)

**Score: 0/5 endorsed.** 50 SOS candidates, zero endorsed.

### DEP Validation

| Radar DEP Pick | Width | Pradeep Mentioned? | Verdict |
|----------------|-------|---------------------|---------|
| [[CRNX]] | 0.67% | ❌ Not mentioned | — |
| [[APGE]] | 1.0% | ❌ Not mentioned | — |
| [[TECH]] | 1.28% | ❌ Not mentioned | — |
| [[PYPL]] | 4.32% | ✅ Mentioned Jul 15 — "rumor of a buyout by Stripe... not something which I have expertise trading" | ❌ Rejected |
| [[XOM]] | 5.61% | ❌ Not mentioned | — |
| [[MRK]] | 6.01% | ❌ Not mentioned | — |
| [[NFLX]] | 10.48% | ✅ "I have no way to know what Netflix catalyst is going to be" — not a DEP | ❌ |

**Radar said:** 20 DEP candidates, top: CRNX, APGE, TECH, PYPL, XOM.

**Pradeep said:** "I don't see anything which I would like and take as a swing." (AM)

**Score: 0/5 validated.** 20 DEPs; Pradeep endorsed zero. PYPL was explicitly rejected days earlier as a buyout rumor trade.

### Anticipation

**Radar:** 35 ANTS. Top: NU, PATH, SOFI, T, AMZN, CMCSA, PLTR, VZ, RIVN, WMT.

**Pradeep:**

> "Anticipation is the worst setup to focus on here, even worse than, like, any breakouts. Because you're guaranteed you're going to get chopped."
> — Pradeep, Jul 20 PM [13:09]

**Score: 0/5.** 35 ANTS; Pradeep called anticipation "the worst setup" — guaranteed to get chopped.

### Short-Side

**Radar:** NEW — 125 short candidates! Bearish DEP (20), WSS Enhanced (20), Sugar Baby Short (20), Bearish Reversal (15), Bearish Study (50).

| Radar Short Category | Top Picks | Pradeep Mentioned? | Verdict |
|----------------------|----------|---------------------|---------|
| Bearish DEP | [[SMH]], [[PSKY]], [[ARRY]], [[ISRG]], [[LUMN]], [[AMAT]], [[TXN]], [[APH]], [[VRT]] | ✅ [[AMAT]] mentioned as sector breakdown; semis mentioned broadly | ⚠️ Partial |
| WSS Enhanced | [[MARA]], [[GRAB]], [[QXO]], [[AA]], [[ISRG]], [[AMAT]], [[OPI]], [[BFLY]], [[AVEX]] | ❌ Not specifically mentioned | — |
| Sugar Baby Short | [[CAST]], [[ASTC]], [[LHSW]], [[ANY]], [[AXTI]], [[SIDU]], [[LUNR]], [[SPCE]] | ❌ Not mentioned | — |
| Bearish Reversal | [[SNDK]], [[ANNX]], [[REZI]], [[CRNC]], [[ELTX]], [[QTRX]], [[CHPT]], [[QXO]] | ✅ [[SNDK]] mentioned as stock in play | ⚠️ Partial |

**Radar said:** 125 short candidates across 5 categories.

**Pradeep said:** "Nothing really on the short side." (PM) — But this was because the easy shorts (Google, BB) had already been taken and the market was range-bound on both sides. He had been short Google from Jul 16 and was getting stopped out on Jul 20:

> "I'm getting stopped out on this Google. This is what happens even on the short side."
> — Pradeep, Jul 20 AM [15:23]

**Score: 3/10.** The radar added a short-side module — a structural improvement. 125 candidates was massive over-generation, but SMH/semis and SNDK were directionally correct. Pradeep wasn't adding new shorts (range-bound both sides), but the radar's short picks were more aligned with Pradeep's actual prior trades than any prior day.

### SIPs Gap

| Pradeep SIPs / Day Trade | Radar Detected? | Notes |
|--------------------------|-----------------|-------|
| [[SNDK]] / [[MU]] / [[SOXL]] | ❌ | "Saksal, Delhi, semi con, bull three x" — stocks in play |
| [[GOOGL]] | ❌ | Google catalyst — Gemini postponed. Day trade. |
| [[IREN]] | ❌ | "You should be on Irene" for SIPs |
| [[ACHR]] (Archer Aviation) | ❌ | Partnership announcement — but "history of dilution" |
| [[CLSK]] (Cipher Mining) | ❌ | "Data center 6,000,000,000 deal... same problem... dilution" |
| [[BMNR]] (BitMiner) | ❌ | Breakout failing example |

**Score: 0/5.** The radar still has no SIPs module. Pradeep's "stocks in play" methodology (SNDK, MU, SOXL, GOOGL, IREN) was entirely absent.

### Daily Scorecard — July 20

| Category | Score (0-10) | Notes |
|----------|:------------:|-------|
| Regime Match | 4 | CAUTIOUS_BULL/REDUCE_SIZE — stable but still too bullish vs "nothing to do" |
| SOS Validation | 0 | 0 of 5 endorsed; 50 candidates all noise |
| DEP Validation | 0 | 0 of 5 validated; PYPL rejected days earlier |
| Anticipation | 0 | 35 ANTS; "worst setup, guaranteed chop" |
| Short-Side | 3 | NEW module — 125 candidates (over-generated) but SMH/SNDK directionally correct |
| SIPs Gap | 0 | Still no module; missed SNDK, MU, GOOGL, IREN, CLSK |
| **Total** | **7/60** | Best day — short-side module added points |

---

## Trend Analysis

### Errors Persisting Across All 4 Days

| Error | Jul 15 | Jul 16 | Jul 17 | Jul 20 | Frequency |
|-------|:------:|:------:|:------:|:------:|:---------:|
| Regime too bullish (FULL_BULL when range-bound) | ✅ | ✅ | ⚠️ (downgraded) | ⚠️ (downgraded) | 4/4 |
| SOS over-generation (50/day, 0 endorsed) | ✅ | ✅ | ✅ | ✅ | 4/4 |
| DEP over-generation (10-20/day, 0 validated) | ✅ | ✅ | ✅ | ✅ | 4/4 |
| ANTS over-generation (35/day, 0 endorsed) | ✅ | ✅ | ✅ | ✅ | 4/4 |
| No SIPs detection module | ✅ | ✅ | ✅ | ✅ | 4/4 |
| 20% study not used for suppression | ✅ | ✅ | ✅ | ✅ | 4/4 |
| No short-side module (Days 1-3) | ✅ | ✅ | ✅ | ❌ (added) | 3/4 |
| Sector rotation mismatch (radar finds breakouts, Pradeep finds hiding spots) | ✅ | ✅ | ✅ | ✅ | 4/4 |

### Radar Improvement/ Degradation Over 4 Days

| Metric | Jul 15 | Jul 16 | Jul 17 | Jul 20 | Trend |
|--------|:------:|:------:|:------:|:------:|-------|
| Regime score | 1 | 1 | 4 | 4 | ↑ Improving (downgraded Jul 17) |
| Short-side score | 0 | 0 | 0 | 3 | ↑ Improving (module added Jul 20) |
| SOS score | 0 | 0 | 0 | 0 | → Flat (no improvement) |
| DEP score | 0 | 0 | 0 | 0 | → Flat (no improvement) |
| ANTS score | 0 | 0 | 0 | 0 | → Flat (no improvement) |
| SIPs score | 0 | 0 | 0 | 0 | → Flat (no improvement) |
| **Total** | **1** | **1** | **4** | **7** | ↑ Slowly improving |

The radar improved from 1/60 to 7/60 — driven entirely by the regime downgrade (Jul 17) and the short-side module addition (Jul 20). But the core problems (SOS, DEP, ANTS over-generation, no SIPs, no 20% study) showed zero improvement.

### Consistently Wrong Radar Calls

1. **FULL_BULL regime (Jul 15-16):** Pradeep said "my wallet is closed" and "don't buy anything." The radar's LLM Judge was 2 days late in downgrading.

2. **SOS 6/6 Two Lynch = "high quality breakout day" (all 4 days):** Pradeep endorsed zero SOS picks across 4 days. The Two Lynch score was noise in a range-bound market. 200 SOS candidates generated; 0 endorsed.

3. **DEP candidates without catalyst validation (all 4 days):** 70 DEP candidates total (10+20+20+20); Pradeep validated zero. The radar doesn't check for genuine catalyst (Pradeep's DEP definition: 1,000+ funds + $10B+ market cap + positive earnings reaction + genuine catalyst).

4. **ANTS in range-bound market (all 4 days):** 140 ANTS candidates total (35×4); Pradeep said "anticipation is the worst setup" and "guaranteed to get chopped." The radar's tight-day tiers (super-tight, ultra-tight) were irrelevant — tight days don't matter when breakouts don't follow through.

5. **Sector precursor = "group move" (all 4 days):** The radar identified Real Estate (12 breakouts on Jul 17), Industrials (11), Consumer Cyclical (13 on Jul 16) as sector precursors. Pradeep said these were where "people were hiding" and would break down next — the opposite interpretation.

### Consistently Right Radar Calls

1. **Breadth deterioration (Jul 17):** The radar correctly flagged the breakdown spike (509 vs 251) and declining net primary (+144). Pradeep confirmed: "selling is going to spread."

2. **Short-side semis (Jul 20):** The radar's Bearish DEP included SMH, AMAT, TXN, APH — Pradeep had been shorting the AI/semi complex since Jul 16. Directionally correct, though over-generated.

3. **Regime downgrade (Jul 17-20):** The radar downgraded from FULL_BULL to CAUTIOUS_BULL/REDUCE_SIZE on Jul 17. Late, but directionally correct.

4. **Sugar Baby identification:** IREN, WULF, OKLO consistently appeared. Pradeep mentioned IREN as a SIPs candidate — partial alignment.

---

## Consolidated Improvements

Prioritized by frequency of error across the 4 days (highest frequency first):

### Priority 1 — 20% Study Suppression (4/4 days)

**Problem:** The radar generates SOS, DEP, and ANTS candidates regardless of 20% study readings. Pradeep uses the 20% study as his primary regime filter — when readings are ~15-25, he says "breakouts unlikely to work" and "my wallet is closed."

**Fix:** Add a 20% study suppression layer:
- 20% study < 30 (bullish side): Suppress all SOS and DEP candidates. Only show SIPs and EP 9M.
- 20% study 30-50: Show DEP only if catalyst-validated. Suppress ANTS entirely.
- 20% study > 100: Full playbook (current behavior).
- 20% study > 200: Suppress all longs (extreme euphoria = top forming, per Pradeep's London Calling framework).

### Priority 2 — SIPs Detection Module (4/4 days)

**Problem:** The radar has zero SIPs detection. Pradeep's primary income source in range-bound markets is SIPs (stocks with immediate catalyst — earnings, news, partnerships). He traded AHR, UNH, ABT, DXCM, ELVA, SNDK, MU, GOOGL, IREN, CLSK as SIPs/day trades across these 4 days. The radar detected none.

**Fix:** Build a premarket gap scanner:
- Gap up > 4% on 100K+ volume (Pradeep's EP 9M trigger)
- News catalyst identification (earnings, FDA, contracts, partnerships)
- Dilution risk flag (Pradeep avoids stocks with shelf offerings — ACHR, IREN, CLSK)
- Fund ownership check (Pradeep's SIPs require catalyst + neglect analysis)
- Output as "Stocks in Play" — separate from SOS/DEP/ANTS pipeline

### Priority 3 — DEP Catalyst Validation (4/4 days)

**Problem:** 70 DEP candidates generated; 0 validated. The radar finds stocks that broke out N days ago and consolidated, but doesn't check whether they have a genuine catalyst. Pradeep's DEP definition: 1,000+ fund ownership + $10B+ market cap + positive earnings reaction + genuine catalyst.

**Fix:** Add DEP qualification filters:
- Fund ownership ≥ 1,000 (already partially implemented — verify enforcement)
- Market cap ≥ $10B (already partially implemented — verify enforcement)
- Catalyst present within last 30 days (earnings beat, contract win, FDA approval)
- Stock not already "priced in" (gap up < 10% on catalyst day — Pradeep rejected AHR at 36% gap, ELVA at 70% gap)
- If no catalyst detected → reclassify as "pattern-only breakout" (not DEP)

### Priority 4 — ANTS Suppression in Range-Bound Markets (4/4 days)

**Problem:** 140 ANTS candidates generated; 0 endorsed. Pradeep said anticipation is "the worst setup" in range-bound markets — "guaranteed to get chopped." The radar's tight-day tiers (super-tight, ultra-tight) are irrelevant when breakouts don't follow through.

**Fix:** Suppress ANTS entirely when:
- 5-day ratio < 0.8 (breakdowns > breakouts over 5 days)
- 10-day ratio < 0.8
- 20% study < 30
- Net primary declining (3-day trend)

Only show ANTS when 20% study > 50 AND 5-day ratio > 1.0.

### Priority 5 — Short-Side Refinement (3/4 days missing, 1/4 over-generated)

**Problem:** No short module for Jul 15-17. Added Jul 20 with 125 candidates — massive over-generation. Pradeep made 2 short trades (GOOGL, BB) across 4 days, both EP 9M on the downside.

**Fix:**
- EP 9M Downside scanner: gap down > 4% on 1M+ volume with fresh negative catalyst (like the upside EP 9M but reversed). This would have caught Google (Gemini postponed) and BB (range expansion breakdown).
- WSS should require 3+ EP 9M downside legs before triggering (Pradeep: "If there is a three plus EP 9,000,000 to the downside, fourth time it happens is when you short it").
- Sugar Baby Short: only show SBs in sectors with RS_20d < -5 (currently shows any SB that declined).
- Bearish Reversal: require 3:58 PM exhaustion on 1M+ volume stocks only.
- Cap total short candidates at 20 (not 125).

### Priority 6 — Regime LLM Judge Retuning (4/4 days)

**Problem:** The LLM Judge called FULL_BULL on Jul 15-16 when Pradeep said "wallet closed." It took 2 days to downgrade to CAUTIOUS_BULL. The judge over-weights T2108 (52-56% = "stable bullish") and net primary positive, but doesn't weight the 20% study or 5d/10d ratios sufficiently.

**Fix:** Retune the LLM Judge prompt:
- If 20% study < 30 → maximum regime is CAUTIOUS_BULL (never FULL_BULL)
- If 5d ratio < 0.8 AND 10d ratio < 0.8 → maximum regime is REDUCE_SIZE
- If 20% study < 15 AND net primary declining → NO_NEW_LONGS
- T2108 50-60% is NEUTRAL, not "bullish" — remove "stable bullish range" language for this zone
- Add 20% study as explicit input to the LLM Judge (currently absent from the prompt)

### Priority 7 — Sector Precursor Interpretation (4/4 days)

**Problem:** The radar identifies sectors with 3+ breakouts as "group moves" (bullish). Pradeep interprets the same data as "where people are hiding" — i.e., these sectors are the next to break down. The radar's Real Estate call (12 breakouts on Jul 17) was exactly wrong — Pradeep said selling would spread there next.

**Fix:** In range-bound markets (20% study < 50):
- Sector precursor with 3+ breakouts → label as "HIDING SPOT" (potential short target), not "group move"
- Only label as "group move" when 20% study > 50 AND sector RS_20d > 10
- Add insider selling flag (Pradeep checks insider sales — DDOG had 27, CRWD had 33)

### Priority 8 — Fading Breakout Mode (4/4 days)

**Problem:** Pradeep explicitly said "fading breakouts is a better strategy here than buying breakouts" (Jul 20 AM). The radar has no fade mode — it only generates long and short candidates.

**Fix:** Add a "Fade Mode" when 20% study < 30:
- Show SOS candidates as FADE candidates (short on gap up failure)
- Show DEP candidates as "likely to chop" warnings
- Add a "breakout failure rate" metric (track what % of yesterday's SOS followed through)

---

## Summary Scorecard

| Day | Regime | SOS | DEP | ANTS | Short | SIPs | **Total** |
|-----|:------:|:---:|:---:|:----:|:-----:|:----:|:--------:|
| Jul 15 | 1 | 0 | 0 | 0 | 0 | 0 | **1/60** |
| Jul 16 | 1 | 0 | 0 | 0 | 0 | 0 | **1/60** |
| Jul 17 | 4 | 0 | 0 | 0 | 0 | 0 | **4/60** |
| Jul 20 | 4 | 0 | 0 | 0 | 3 | 0 | **7/60** |
| **Avg** | **2.5** | **0** | **0** | **0** | **0.75** | **0** | **3.25/60** |

**Overall accuracy: 5.4%.** The radar's core long-side pipeline (SOS, DEP, ANTS) had 0% validation across all 4 days. The only points came from the regime downgrade (Jul 17+) and the short-side module addition (Jul 20). The SIPs gap — the biggest blind spot — contributed zero across all 4 days.

The radar's fundamental flaw: it generates setups unconditionally, treating every day as a pattern-recognition exercise. Pradeep's fundamental principle: **situational awareness > setup**. The radar has setups; it lacks situational awareness. The 20% study is the missing bridge.