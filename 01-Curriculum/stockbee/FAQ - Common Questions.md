---
title: "Q&A — Common Questions and Confusions"
date: 2026-06-04
tags: [class, q-a, faq, clarifications, common-questions]
---

# Q&A — Common Questions and Confusions

> Quick-reference for the most common points of confusion. Each answer ties back to the lesson and KB notes for deeper study.

---

## Q1: Primary Indicator — What Exactly Is the Reading?

**Question:** The reading ">400 = strong bull market" — is this the net difference (stocks up 25% minus stocks down 25%)?

**Answer:** **Yes.** The primary indicator is a **net number**:

```
Primary Reading = (Stocks up 25%+ in 65 days) − (Stocks down 25%+ in 65 days)
```

**Example (2026-06-02 StockBee data):**
- Primary Up = 1,582
- Primary Down = 902
- **Net = 1,582 − 902 = 680** → Strong bull (above 400 threshold)

Both raw counts are tracked separately, but the net is what you use for classification.

| Net Reading | Classification |
|-----------|---------------|
| **> 400** | Strong bull — most breakouts work |
| **200–400** | Normal bull |
| **0–200** | Weak bull / transition |
| **< 0** | Bear market |
| **< −200** | Severe bear / capitulation |

**See also:** [[01 - Market Monitor#The Primary Indicator]]

---

## Q2: 4% Breakout — Timing Confusion

**Question:** We won't know whether a stock will have a 4% breakout "today" until it happens. Does the scan use yesterday's data? If I enter the next day, won't the stop be too large?

**Answer:** The 4% breakout is detected **in real-time during the trading day.** You don't predict it — you react to it.

**The correct workflow:**
1. At **9:30 AM**, run the EP 9M scan
2. Stocks that are **already up 4%+ today** appear on the scan
3. Enter within the **first 15–30 minutes** (SOS entry)
4. Stop at **low of the day**

**If you miss day 1, your options:**

| What Happened | What to Do | Stop | Size |
|---------------|-----------|------|------|
| Stock broke out 4%+ yesterday | Add to DEP watchlist, wait for pullback (days 3–10) | 0.5–2.5% | 25–50%+ |
| Stock in tight consolidation | ANTS entry with BSLO at 2:58 PM | <1% | Large |
| You just missed it | Skip it — another setup comes tomorrow | No risk | N/A |

**You NEVER buy day 2 or 3 after a breakout.** The move is typically 3–5 days; most of it happens on day 1. Buying day 2 means your stop is now 8–10% wide (too far from entry) and most of the move is done.

**The only way to "predict" a breakout is ANTS** — placing a Buy Stop Limit Order at 2:58 PM the day before, based on tight consolidation patterns (3T/2T). If it triggers, you're in with a <1% stop. If it doesn't, the order never activates.

**See also:** [[02 - The 4% Breakout#The 4% Breakout Happens in Real-Time]], [[03 - Entries#Entry #2: SOS (Start of a Swing)]], [[03 - Entries#Entry #3: DEP (Delayed Entry After Pullback)]], [[03 - Entries#Entry #4: ANTS (Anticipation)]]

---

## Q3: T2108 — Can It Be Used Alone?

**Question:** Does T2108 alone tell us anything? At >90%, should we still trade bullish?

**Answer:** T2108 is most powerful **when combined with the primary indicator.** Alone, it's useful at extremes but can mislead in the middle range.

**T2108 > 90% → Still trade bullish!**

> *"It's not that T2108 goes above 90 and then the market has topped. No. That tells you that there has been just a start of a new bull market."*

T2108 > 90% means **the bull has just started**, not that it's over. This is the most common misunderstanding.

**Where T2108 alone fails:**

| Scenario | T2108 | Primary | Correct Interpretation |
|----------|-------|---------|----------------------|
| Bear bounce | 85% (high!) | < 0 (bear) | 85% is just a bounce in a bear market — do NOT trust it |
| Bull pullback | 30% (low) | > 200 (bull) | 30% is a pullback in a bull market — buy the dip |
| New bull start | > 90% | > 200 | Full bull — size up on longs |
| Capitulation | < 10% | < −200 | Generational bottom — deploy capital |

**The rule: Primary = structural trend (quarterly). T2108 = momentum within that trend (short-term).** Always check primary first.

**See also:** [[01 - Market Monitor#The T2108 Indicator]]

---

## Q5 (Q4 Skipped): Is 9M a Magic Number?

**Question:** Is 9M just a round number? Do I need exactly 9M, or can I use 8M or 10M?

**Answer:** 9M is an **empirical threshold, not a magic number.** It's grounded in Pradeep's 40+ years of observation that the biggest moves ALL started with 9M+ volume. But the exact number matters less than the principle it represents.

**The principle:**

> **A breakout without institutional volume has no follow-through.**

Whether you use 5M, 9M, or 10M depends on context:

| Context | Volume Threshold | Why |
|---------|-----------------|-----|
| Standard EP 9M | 9M+ | Default — institutional follow-through confirmed |
| Dollar breakout (FHP) | 100K+ | High-priced stocks ($100+) are always liquid |
| Small cap scan | 5M+ | Relaxed for smaller caps with lower float |
| Very thin names | 1M+ | Only for experienced traders who know the risk |

A stock with 8.5M volume isn't fundamentally different from one with 9.1M. The principle is: **sufficient volume to confirm institutional participation.** 9M is the sweet spot Pradeep arrived at empirically.

> **Think of it like a speed limit:** 55 mph isn't magical either, but it's a practical threshold that separates safe from dangerous. The exact number matters less than the principle it represents.

**See also:** [[02 - The 4% Breakout#Why 9M Volume?]]

---

## Q6: Why Not Buy Day 2 or 3?

**Question:** If I miss day 1, can't I buy day 2 with a slightly wider stop?

**Answer:** No. This is one of the most common and costly mistakes.

> *"There is nothing in this trading which works by buying on a third day."*

**The move is typically 3–5 days.** If you buy on day 2:
- You've already missed 50–70% of the move (most of it is day 1)
- Your stop is now 8–10% wide (far from entry)
- Risk/reward is terrible: risking 10% to make 10% (1:1 at best)

**Instead of buying day 2, use one of these options:**
1. **DEP** — wait for pullback (days 3–10), enter with 0.5–2.5% stop
2. **ANTS** — if stock enters tight consolidation, buy before the NEXT breakout
3. **Skip it** — another setup comes tomorrow

**See also:** [[03 - Entries#What NOT to Do]], [[04 - Stops#The Fundamental Rule]]

---

## Q7: What's the Difference Between DEP and Buying Day 2?

**Question:** If DEP enters on day 3–5, isn't that the same as buying day 2 or 3?

**Answer:** No. The key difference is **where you enter relative to the price action.**

| Scenario | Entry Price | Stop | Stop Width | Position Size |
|----------|-----------|------|-----------|---------------|
| **Day 2 chase** | Near the top | Low of day 2 | 8–10% | Small |
| **DEP (day 3–10)** | After pullback, near support | Below consolidation | 0.5–2.5% | **Large** |

DEP enters **after the stock pulls back to support**, not when it's still near the top. The pullback is the structural signal: institutional quality stocks gap up, pull back, shakeout weak hands, and THEN go. DEP buys at the shakeout, not the top.

**See also:** [[03 - Entries#Entry #3: DEP (Delayed Entry After Pullback)]]

---

## Q8: What If Market Monitor Is Green but I'm Scared?

**Question:** Market Monitor says green, but I'm hesitant to trade. What should I do?

**Answer:** This is a process problem, not a market problem.

> *"Cognitive dissonance leads to process error. Cognitive dissonance leads to fumbling. Cognitive dissonance leads to second guessing yourself. Cognitive dissonance leads to FOMO."*

The fix:
1. **Have a checklist** — if all boxes are checked (Market Monitor green, catalyst, institutional stock, defined stop, calculated size), you trade.
2. **If you can't check all boxes, you don't trade.** End of story.
3. **If you CAN check all boxes but still hesitate**, the problem is lack of conviction from insufficient study. Do the Deep Work exercise: study 5,000 examples of the setup.

> *"You don't need discipline. You need process orientation."*

**See also:** [[10 - The Daily Process#The Process Mindset]], [[Mentality]]

---

## Q9: Can I Use Market Monitor to Call Tops?

**Question:** If T2108 is above 90%, doesn't that mean the market is overbought and I should go short?

**Answer:** **No.** This is the #1 mistake with Market Monitor.

> *"Excessive bullishness is NOT bearish. Excessive bearishness IS bullish."*

T2108 > 90% means a new bull has started — this is when you want to be most aggressive on the long side. It does NOT mean a top is imminent.

Market Monitor finds **bottoms** reliably (primary < 200 + T2108 single digits). It does **NOT** find tops. "Excessive bullishness can persist for years."

**If you try to call tops using Market Monitor, you will get out too early and miss the biggest moves.**

**See also:** [[01 - Market Monitor#Critical Asymmetry: Breadth Finds Bottoms, NOT Tops]]

---

## Q10: Why Is DEP the "Non-FOMO" Setup?

**Question:** Why does Pradeep say DEP is the anti-FOMO setup?

**Answer:** Because DEP gives you **hours to decide, not seconds.**

| Setup | Decision Time | Stop Width | Size |
|-------|--------------|-----------|------|
| **EP Day 1** | Seconds at market open | 8–20% | Small |
| **DEP** | Hours or days (watchlist, wait for pullback) | 0.5–2.5% | **Large** |

EP forces you to decide at 9:30 AM with seconds to think. DEP lets you:
1. Add the stock to your watchlist during morning scan
2. Study the catalyst, check fund ownership, verify institutional quality
3. Wait for the pullback (3–10 days)
4. Enter when it "shows life" near support with a tiny stop

**DEP is specifically designed for working people** who can only trade 9:30–11:00 AM and need time to make decisions.

> *"90% of your problems in trading can be solved if you have mental clarity about what really are you doing, why are you doing, and when you want to do it."*

**See also:** [[03 - Entries#Entry #3: DEP (Delayed Entry After Pullback)]], [[Mentality]]

---

## Quick Reference: Most Common Mistakes

| # | Mistake | Correct | Lesson |
|---|---------|---------|--------|
| 1 | Buying day 2 or 3 after breakout | Buy day 1 (SOS) or wait for DEP (pullback) | [[03 - Entries]] |
| 2 | Using Market Monitor to call tops | Market Monitor finds bottoms only | [[01 - Market Monitor]] |
| 3 | Treating 9M as magic number | It's a practical threshold for institutional volume | [[02 - The 4% Breakout]] |
| 4 | Thinking T2108 > 90% = overbought | T2108 > 90% = new bull started | [[01 - Market Monitor]] |
| 5 | Predicting 4% breakouts | React in real-time at 9:30 AM | [[02 - The 4% Breakout]] |
| 6 | Ignoring primary indicator | Always check primary first; T2108 is tactical | [[01 - Market Monitor]] |
| 7 | Using mental stops | Hard stops, market hours only | [[04 - Stops]] |
| 8 | Same position size regardless of setup | Scale size with stop width and conviction | [[05 - Position Sizing]] |
| 9 | Trading without catalyst | If you can't explain it in 10 min, skip it | [[06 - Catalysts]] |
| 10 | No defined process | Build checklist; decide everything before 9:30 AM | [[10 - The Daily Process]] |

---

*Last updated: 2026-06-04 | Based on 23 curated guides, 12 KB notes, 170+ transcripts*