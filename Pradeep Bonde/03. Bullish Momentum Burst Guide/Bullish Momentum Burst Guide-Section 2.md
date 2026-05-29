---
title: Bullish Momentum Burst Guide — Section 2
date: 2026-05-29
source: https://stockbee-videos.b-cdn.net/2023-04-01-how-to-trade-breakouts-part-2/2023-04-01-how-to-trade-breakouts-part-2.mp4
language: en
backend: deepgram
duration_seconds: 0.0
tags:
  - 4-percent-breakout
  - momentum-burst-scan
  - tc2000-setup
  - two-lynch-setup
  - filter
  - deep-dive
  - dollar-breakout
  - combination-scan
  - low-threshold-breakout
  - v-by-v1
  - volume-confirmation
  - close-near-high
---

# Bullish Momentum Burst Guide — Section 2

**Source:** Section 2 (Parts 11–20)
**Language:** en
**Backend:** deepgram
**Duration:** 00:00.000

## Summary

Section 2 covers the practical implementation of momentum burst trading: how to find setups (4% breakout scan), how to configure TC2000, and the complete **Two Lynch** framework for setup selection. Pradeep walks through the 4% breakout scan conditions in detail, demonstrates a real-time walkthrough filtering 73 candidates down to 2–3 quality setups, and explains why each rejection criterion matters. The section is the operational core of the method — everything builds on finding good setups through Two Lynch.

---

## Series Overview

| Section | Theme | Key Question Answered |
|---------|-------|----------------------|
| **Section 1** | What Is a Momentum Burst? | Definition, duration, magnitude, myth-busting, anticipation limitations |
| **Section 2** | 4% Breakout Method & Two Lynch | Scanning setup, setup selection framework, TC2000 configuration |
| **Section 3** | Two Lynch Examples | Visual deep-dive into ideal and failed setups, pattern recognition |
| **Section 4** | Entry, Stops & Trade Management | When to enter, stop placement, position sizing, intraday management |
| **Section 5** | Win Rate, Market Phase & Filters | Market Monitor, sector selection, capitalization, TI-65/M20 filters |
| **Section 6** | Dollar Breakout Method | Higher-priced stocks, lower risk, TC2000 setup, Two Lynch application |
| **Section 7** | Dollar Breakout Examples & Capital Efficiency | Live examples, position sizing math, risk/reward advantage |

---

### 1. Universal Applicability & Deep Dive

Momentum burst methods work in every liquid market worldwide (US, UK, Europe, Korea, China, Singapore, Malaysia). The only exception is markets with price filters (circuit breakers that halt trading after 5% moves).

**Before trading, Pradeep mandates a deep dive:**

1. Study **2,000–3,000 historical momentum bursts** across all stocks
2. Mark the first leg, consolidation, breakout, and Day 3 result on each chart
3. Observe: Do they work near 52-week highs? Lows? In bear markets? How does ADR affect them?
4. Only after this immersion should you start trading

> "Deep dive of at least 3,000 examples is the starting point for you getting a deeper understanding of momentum burst."

This builds **pattern recognition**, not just theory. Multiple deep dives are recommended: the first to understand the phenomenon, subsequent ones to understand setup quality.

---

### 2. Methods Under the Momentum Burst Umbrella

| Method | Condition | Best For |
|---|---|---|
| **4% breakout** | Stock up 4%+ with volume > yesterday AND volume > 100,000 | Lower-priced stocks ($3–$40), broad scanning |
| **Dollar breakout** | Stock up $0.90+ (closing minus opening) with volume > 100,000 | Higher-priced stocks ($40+), tighter stops |
| **Combination scan** | 4% OR dollar breakout together | Maximum coverage |
| **Low threshold breakout** | Similar logic with lower percentage thresholds | Beginners or conservative approaches |

All four are based on the same underlying phenomenon — range expansion starting a momentum burst.

---

### 3. 4% Breakout Scan: The Three Conditions

The 4% breakout scan has exactly three conditions that a stock must meet:

| Condition | Formula | Purpose |
|---|---|---|
| **1. Price up 4%+** | `C/C1 >= 1.04` | Range expansion confirmed |
| **2. Volume > yesterday** | `V >= V1` | Institutional buying confirmation |
| **3. Volume ≥ 100,000** | `V >= 100,000` | Minimum liquidity |

**Bullish scan:** `C/C1 >= 1.04 AND V >= V1 AND V >= 100000`
**Bearish scan:** `C/C1 <= 0.96 AND V >= V1 AND V >= 100000`

**Why V ≥ V1 matters:** It confirms that today's volume exceeds yesterday's. This is the "elephants' footprint" — institutional money creates volume expansion alongside price expansion. Without it, you may be buying something that has momentum without conviction.

> "Buying a stock which doesn't meet v by v1 condition and doesn't meet 100,000 condition, you're going to buy something which doesn't have momentum, which doesn't have range expansion, which doesn't have volume expansion, and the probability of that working may not be very high."

**Why 100,000 volume:** It ensures minimum liquidity so you can enter and exit.

---

### 4. Setting Up the Scan in TC2000

**Step-by-step for 4% breakout bullish:**
1. New → Combo List → Name: "4% breakout Bullish"
2. Add list: US stocks, ADRs, ETFs
3. Add condition → Write formula: `C/C1 >= 1.04 AND V >= V1 AND V >= 100000`
4. Optional filter: Price > $3 (reduces from ~127 to ~73 stocks on a typical day)

**4% breakdown bearish:**
1. Same setup, formula: `C/C1 <= 0.96 AND V >= V1 AND V >= 100000`

**Chart template setup (4% breakout + breakdown visual):**
- Add price (candlestick, black)
- Add volume (black/red, no MA)
- Add "Custom PCF True Indicator" for 4% bullish: `C/C1 >= 1.04 AND V >= V1 AND V >= 100000` → green area fill
- Add "Custom PCF True Indicator" for 4% bearish: `C/C1 <= 0.96 AND V >= V1 AND V >= 100000` → red area fill
- Overlay both indicators on the same panel
- Add TI-65 indicator: `AVGC7/AVGC65 >= 1.05` (green) and `AVGC7/AVGC65 <= 0.95` (red) → overlay on volume

Save the chart template with a memorable name (e.g., "4p").

---

### 5. When to Run the Scan

| Time | What Happens |
|---|---|
| **Market open (9:30)** | Scan starts populating immediately |
| **First 30 minutes** | Best candidates appear — most explosive bursts start here |
| **First hour** | Still strong — genuine bursts keep going |
| **Afternoon** | Some bursts appear on afternoon buying |
| **End of day** | Less ideal but still possible |

> "Most of the stocks which break out with 4% breakout, which go on to make a big move, they typically show up in the first half an hour or first one hour."

**Common objection:** "By the time the stock shows up in 4%, it's already up 4–5%, isn't that too late?"

**Answer:** No. The 4% is the confirmation that momentum burst has started. Entering before 4% means buying without confirmation — the probability of that working is lower.

---

### 6. The Two Lynch Framework: Setup Selection

Two Lynch is the **complete checklist** for filtering scan results. Every letter matters:

| Letter | Stands For | Detail |
|---|---|---|
| **T** | **Two** | Stock should NOT be up two days in a row before breakout. (A very minor up of 0.1–0.5% is tolerated, but ideally flat or down.) |
| **L** | **Linearity** | First leg shows clean, persistent buying. No big selling candles. Orderly advance. Choppiness = wider stops needed, lower probability. |
| **Y** | **Young** | First or second leg of the move only. NOT 3rd, 4th, 5th. Later legs have higher failure rates because the setup is obvious. Pradeep: "There's a reason why 60-year-old hedge fund managers date 20-year-old girls." |
| **N** | **Narrow/negative day** | Day before breakout should be a small-range or down day. Narrow range = volatility compressed before explosion. Up days before breakout = energy already spent. |
| **C** | **Consolidation quality** | Compact, orderly, low-volatility pause. No 4% breakdowns during consolidation. Low volume during consolidation = sellers absent. Choppy consolidation = avoid. |
| **H** | **High close** | Stock should close as near the day's high as possible. Up to 30% giveback from intraday high is acceptable. More than that = fading momentum, not worth trading. |

> "The most important thing in trading this setup is your ability to select a setup which meets all the criteria."

**The three most important conditions (in order):**
1. **Linearity** — "Linearity is extremely important to me. I only select linear setups, and I avoid, under any circumstances, choppy setups."
2. **Not up two days in a row**
3. **Young setup**

---

### 7. Real-Time Two Lynch Walkthrough: 73 Candidates → 2–3 Good Ones

Pradeep walks through the Friday scan of 73 stocks meeting 4% breakout conditions and filters them one by one:

**Rejected (examples):**
- Stock up two days in a row → REJECTED
- Choppy first leg (no linearity) → REJECTED
- Consolidation has 2–4% breakdowns → REJECTED ("there is a 4% breakdown... this is not orderly")
- High volume selling during consolidation → REJECTED
- Stock not closing near the high → REJECTED
- Fourth/fifth leg of the move → REJECTED
- Stock in clear downtrend → REJECTED

**Accepted (examples):**
- First leg, orderly 3–4 day pullback, no 4% breakdown, closing near high → ACCEPTED
- First leg, very compact consolidation, low volume, clean breakout near high → ACCEPTED

> "The moment you start using Two Lynch, you can eliminate 80–90% of the stocks which are showing up in your scan."

---

### 8. Close Near High: The Misunderstood Criterion

Many traders ask: "If I need the stock to close near the high, doesn't that mean I can only buy at end of day?"

**No.** "Closing near the high" applies to **every minute of the market**. At 9:45 AM, the stock should be trading near its intraday high. At 10:00 AM, same thing. The "close" criterion is about confirming momentum, not about when you can buy.

> "Every minute of the market has a close. So at that time, the stock should be closing near the high."

If a stock is up 4% at 10:00 AM but has already given back 3% of its intraday range, that's a stock fading on Day 1 — the momentum is already dissipating.

---

### Key Takeaways

1. **Deep dive 3,000+ examples before trading** — pattern recognition is the foundation
2. **4% breakout has exactly 3 conditions** — price up 4%+, volume > yesterday, volume > 100K
3. **Two Lynch is the complete setup filter** — T(wo), L(inearity), Y(oung), N(arrow/negative), C(onsolidation quality), H(igh close)
4. **Linearity is the #1 criterion** — avoid choppy setups under any circumstances
5. **Youngness matters** — first/second leg only; fourth/fifth legs have declining win rates
6. **Run scans from market open** — the best candidates appear in the first 30 minutes
7. **Two Lynch eliminates 80–90% of scan results** — this is the quality filter

---

### Cross-References

- [[../../transcripts/03. Bullish Momentum Burst/Pradeep Bonde - Bullish Momentum Burst Guide-Section 2_deepgram|Full Transcript]]
- [[Bullish Momentum Burst Guide-Section 1|Section 1: Definition & Myth-Busting]]
- [[Bullish Momentum Burst Guide-Section 3|Section 3: Two Lynch Examples]]

---

### Key Quotes

> "Linearity is extremely important to me. I only select linear setups, and I avoid, under any circumstances, choppy setup."

> "The most important thing in trading this setup is your ability to select a setup which meets all the criteria."

> "Try and get into younger setup and understanding that youngness is extremely important to become good at trading Two Lynch kind of setups."

> "Stocks which have V ≥ V1 condition being met... are the ones which are being strongly bought."