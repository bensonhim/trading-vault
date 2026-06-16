---
title: Bullish Momentum Burst Guide — Section 6
date: 2026-05-29
source: https://stockbee-videos.b-cdn.net/2023-04-01-how-to-trade-breakouts/2023-04-01-how-to-trade-breakouts.mp4
language: en
backend: deepgram
duration_seconds: 0.0
tags:
  - dollar-breakout
  - higher-priced-stocks
  - low-risk-setup
  - tc2000-template
  - combination-scan
  - two-lynch-dollar
  - dollar-breakout-scan
  - position-size
  - capital-efficiency
---

# Bullish Momentum Burst Guide — Section 6

**Source:** Section 6 (Parts 51–60)
**Language:** en
**Backend:** deepgram
**Duration:** 00:00.000

## Summary

Section 6 introduces the **dollar breakout** method — Pradeep's favorite setup and complement to 4% breakout. Higher-priced stocks ($40+) often don't achieve a 4% move on breakout day, but a $1–$3 move can be the start of a 6–12 day swing. Dollar breakout solves this: scan for stocks up $0.90+ from open with volume > 100K. The same Two Lynch framework applies. The key advantage: **much tighter stops** (1–2.5% vs. 5–10%), enabling much larger position sizes and faster account growth. This section covers scan setup, chart template, Two Lynch application, and real examples.

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

### 1. Why Dollar Breakout? The Problem with 4% on Higher-Priced Stocks

Higher-priced stocks ($100, $200, $300+) have a different behavior pattern:
- They often move $2–$5 on a breakout day — which is only **1–2%**
- This 1–2% move will NEVER show up in a 4% breakout scan
- But that $2–$5 move is the start of a **6–12 day swing** worth $30–$100+

Examples:
- **Booking.com:** Up $96 in 3 days without a single 4% breakout
- **MELI:** Up $46 in a swing — breakout was only 1.5%
- **AutoZone:** Up $100+ over 6–7 days — breakout was only 2%
- **BlackRock:** Down $64 in a breakdown — no 4% breakdown visible

> "The higher priced stocks need to be treated differently. And the dollar breakout is a very good setup for trading higher priced stocks."

---

### 2. Dollar Breakout vs. 4% Breakout: Key Differences

| Attribute | 4% Breakout | Dollar Breakout |
|---|---|---|
| **Breakout magnitude** | 4%+ | $0.90+ (often only 1–3%) |
| **Best for** | Stocks under $40 | Stocks above $40 |
| **Typical stop (half-range)** | 2.5–5% | **1–2.5%** |
| **Typical stop (low of day)** | 5–10% | 2–5% |
| **Hold period** | 3–5 days | **6–12+ days** |
| **Volatility** | Higher | Lower |
| **Entry timing** | Must be Day 1 | Next-day entry possible |
| **Position size** | 10–30% of account | **30–50%+** of account |
| **Crowd** | Many traders chase | Few traders focus here |

**The origin:** Dan Zenger's approach of scanning for stocks above $40 that are up $1+. Pradeep adapted and refined it.

---

### 3. Dollar Breakout Scan Setup

**Bullish Dollar Breakout:**
```
C - O >= 0.90       // Stock up $0.90+ from open to close
V >= 100,000         // Minimum liquidity
```

**Bearish Dollar Breakdown:**
```
O - C >= 0.90        // Stock down $0.90+ from open to close
V >= 100,000
```

**TC2000 setup:**
1. New → Combo List → "Dollar Bullish"
2. Add list: US stocks, ADRs, ETFs
3. Add condition: `C-O >= 0.90 AND V >= 100000`
4. (Optional) Add price filter: `C >= 40` for pure dollar breakout focus

**Eliminating 4% overlap (pure dollar breakouts only):**
1. Run dollar breakout scan → copy all symbols to "Bullish Working" watchlist
2. Run 4% breakout scan → flag all symbols
3. In "Bullish Working", remove all flagged symbols
4. What remains = pure dollar breakouts (stock up $1+ but less than 4%)

**Combination approach (recommended):**
1. Copy 4% breakout bullish results to "Bullish Working"
2. Copy dollar breakout bullish results to same "Bullish Working"
3. You now have ~120 candidates (duplicates removed)
4. Apply Two Lynch to the combined list

---

### 4. Dollar Breakout Chart Template

Use the same template as 4% breakout, but change the indicator conditions:

- **Dollar bullish:** Custom PCF True Indicator → `C-O >= 0.90 AND V >= 100000` → green area fill
- **Dollar bearish:** Custom PCF True Indicator → `O-C >= 0.90 AND V >= 100000` → red area fill

**Practical tip:** Use different background colors for 4% vs. dollar chart tabs so you always know which method you're looking at.

> "I color these things with a different color so that you know quickly this is a different tab."

**Pradeep's actual use:** On a normal day, he only uses the 4% template. The dollar template is for deep dives and studying setups, not daily scanning.

---

### 5. Two Lynch Applies Equally to Dollar Breakout

The exact same selection framework applies:

| Check | Dollar Breakout Application |
|---|---|
| **Not up two days in a row** | Yes — stock should not have 2 consecutive up days before breakout |
| **Linearity** | Yes — first leg shows strong, persistent buying |
| **Young setup** | Yes — first or second leg only |
| **Narrow/negative day prior** | Yes — ideally a small-range or down day before breakout |
| **Consolidation quality** | Yes — compact, orderly, no big breakdowns, low volume |
| **Close near high** | Yes — stock holds most of its gains |

**The only difference:** the breakout magnitude is 1–3% instead of 4%+. The pattern and selection criteria are identical.

---

### 6. Dollar Breakout Examples

#### Example: EME (Emcor Group)
- First leg established
- Very compact, orderly consolidation
- Breakout day up only **$2.63** (2.47%)
- Stop at half-range: ~1.25% risk
- With 1% account risk: can put over 100% of account into one trade
- In practice: 0.25% risk → 25–30% position size
- Stock went on to make **$6–8** more

#### Example: O'Reilly (ORLY)
- Very orderly pullback after first leg
- Breakout: up **$2.60** (2.68%)
- Half-range stop: ~$2.13
- Risk: ~1% of account
- Stock made **$25** in follow-through

#### Example: Clean Harbors
- First leg established, small consolidation
- Breakout: up only **1.89%**
- These setups are what Pradeep hunts for daily
- Stock went up $25+ over multiple days

#### Example: Copart (CPRT)
- Two separate breakouts: up $2.66 (2.66%) and up $1.63 (1.63%)
- Both yielded $7 moves in 5–6 days
- Dollar breakouts = same stock can set up again and again

#### Example: Zebra Technologies (ZBRA) — Pradeep's template setup
- Breakout: up $1.60 (only **0.49%**!)
- First leg established, very orderly consolidation
- Result: **30%+ move** in 3–4 days
- Extremely low risk for extremely high reward

> "These are the kind of setups which can make your week or they can make your days."

---

### 7. The Capital Efficiency Advantage

This is the single most important concept in dollar breakout:

| Scenario | 4% Breakout | Dollar Breakout |
|---|---|---|
| Breakout magnitude | 6–8% | 1–3% |
| Half-range stop | 3–4% | **1–1.5%** |
| Risk 1% of account | Can deploy 10–25% of account | Can deploy **30–60%** of account |
| Total risk across positions | Hard to have 3+ positions | **3–4 positions with 3–4% total risk** |
| Account velocity | Moderate | **Fast** |

> "You can have four setups like this open, and your risk on that setup cumulatively on all four positions still can be less than 3%."

**This means:** With dollar breakout, you can be fully invested (3–4 positions, 100%+ of account) while risking only 3–4% total. That's extraordinary.

---

### 8. Duration Advantage

| Method | Typical Hold | Behavior |
|---|---|---|
| 4% Breakout | 3–5 days | Explosive, then done |
| Dollar Breakout | **8–12+ days** | Slow, persistent, keeps climbing |

> "Many times dollar breakouts will move for 8, 10, 12 days. They may not move very rapidly. They'll move very slowly, but they'll move for eight to ten days."

**Example: AutoZone**
- 2% breakout
- Moved very slowly but made **$120+** over 7–8 days
- Not exciting for retail traders → less competition

---

### 9. Next-Day Entry Is Possible

Unlike 4% breakout (where next-day entry is a cardinal sin), dollar breakout CAN be entered on Day 2:

- The stock is only up 1–2% — no gap-up scramble
- No mass retail excitement
- Higher-priced stocks don't have the same urgency
- This makes dollar breakout ideal for **working professionals**

> "If you're a working person or if you want to trade a method where you're holding for more than three to four days, dollar breakout is a very good way to do it."

---

### Key Takeaways

1. **Dollar breakout captures what 4% misses** — higher-priced stocks moving 1–3% with $2–$10 dollar ranges
2. **Two Lynch framework applies exactly the same** — only the breakout magnitude differs
3. **Stops are dramatically tighter** — 1–2.5% vs. 5–10% for 4% breakout
4. **Position sizes are dramatically larger** — 30–60% of account per trade
5. **Duration is longer** — 8–12 days vs. 3–5 days
6. **Next-day entry is viable** — working professionals can trade this
7. **Same stock can set up multiple times** — AutoZone, O'Reilly, Copart all offered repeat setups
8. **This is Pradeep's personal favorite setup** — he focuses exclusively on dollar breakout for his own trading

---

### Cross-References

- [[../../transcripts/03. Bullish Momentum Burst/Pradeep Bonde - Bullish Momentum Burst Guide-Section 6_deepgram|Full Transcript]]
- [[Bullish Momentum Burst Guide-Section 5|Section 5: Win Rate & Market Phase]]
- [[Bullish Momentum Burst Guide-Section 7|Section 7: Dollar Breakout Examples & Capital Efficiency]]

---

### Key Quotes

> "Dollar breakout is something which is a very good method, and it is more suitable for people who have larger accounts and people who are working."

> "These are the kind of setups which can make your week or they can make your days. Because from a very low risk, in three, four days, the stock made 30% kind of a move."