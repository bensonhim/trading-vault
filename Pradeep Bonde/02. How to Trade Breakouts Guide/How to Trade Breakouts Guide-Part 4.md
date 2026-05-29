---
title: How to Trade Breakouts Guide — Part 4
date: 2026-05-28
tags:
- trading-process
- volume-breakouts
- institutional-footprints
- breakout-filtering
- long-term-hold
- watchlist-trading
- sacrificial-filter
- tc2000
---

# How to Trade Breakouts Guide — Part 4

### The Three Breakout Types (Recap)

Before introducing volume, Pradeep recaps the three price-action breakouts from prior sessions:

1. **Bottom Bounce** — stock hits a low and reverses with a range-expansion bar
2. **Continuation** — 3–5 day up-move, followed by 3–10 day pause, then breakout
3. **Consolidation** — stock goes up and spends a long time in zigzag basing before breaking out

Across all three, **price is the primary variable** — specifically a bar that is bigger than any bar in the last 2–3 days. Volume may or may not be present and the breakout can still work.

---

### Volume as a Filter, Not a Requirement

Pradeep makes a critical distinction:

> "Primarily we are concerned with the price as a variable... the volume may or may not be present and still this breakout works."

Volume is **additive** — it does not replace price analysis. It is a filter for those who want:
- **Longer holding periods**
- **Fewer opportunities to research deeply**
- **Evidence of institutional participation**

---

### Four Ways to Define "Abnormal Volume"

#### 1. Multiple of 50-Day Average Volume
The simplest definition: **V ≥ 2 × average(V50.1)**

- Uses **V50.1** (50-day average *excluding today*) so today's abnormal volume doesn't inflate its own average
- Can be tuned: 2×, 3×, etc.
- Kelvin Wong's scan (shown in the attached PDF) used 3× average volume — Pradeep notes it should have been `avg(V50.1) × 3`, not `avg(V50) × 3`

#### 2. Highest Volume in a Timeframe
- **Highest in 252 days** (1 year)
- **Highest in 126 days** (6 months) → more opportunities, slightly less significance
- **Highest in 63 days** (quarter)

In TC2000, this is expressed as a sort column: `V / max(V252.1)` — anything > 1 means today is the highest volume in that period.

#### 3. All-Time High Volume
The strongest signal — when a stock trades more shares today than *ever before*. Example: Cardlytics traded 71M shares vs. a 25M float — the float turned over ~3× in one day.

#### 4. The "9M+" Twist
Pradeep's personal method: look for breakouts with **9,000,000+ shares traded**. This is an absolute volume threshold that acts as a standalone method, not just a filter.

---

### The 50.1 Trick: Why Exclude Today's Volume?

> "If you include today's volume in the average, the abnormal volume is going to change the average itself, especially if you have really small volumes before that."

Using `V50.1` (or `V252.1`, etc.) ensures the comparison baseline is *before* the breakout day. Otherwise a single spike artificially lowers the multiple.

---

### Reading Institutional Footprints

The core thesis of Part 4:

> "These are the footprints of the elephants."

High volume on larger, established stocks (not $1–2 penny stocks) is almost always **institutional buying**. Examples Pradeep walked through:

| Stock | Volume Signal | What Happened After |
|---|---|---|
| First Solar | 7.7M → 9.6M two-day cumulative | Fund ownership jumped from ~900 to 1,595 mutual funds |
| Onon (ONON) | Highest volume in its lifetime | Three days of continuous buying after earnings |
| AHR | Massive volume spike | Clear institutional footprint |
| NFI | Significant volume increase | Fund ownership jumped dramatically |
| PDD | Volume spikes at $60–$110 | Ownership increased from 1,100 to 1,300 funds |
| FICO | Volume spike at breakout | Institutional accumulation visible |

The key insight: **mutual fund ownership data is released 3–6 months late**. By the time you see the filings, the funds already bought — on the high-volume breakout day.

---

### Who Should Use Volume Breakouts?

Pradeep is explicit about the target audience:

> "Somebody who's full time job... He wants to make money trading. And the way to make money trading then is to focus on few things rather than focusing on thousand things."

Volume breakouts are for:
- **Working people** who can't monitor 200–300 breakouts daily
- **Longer-term position holders** — these breakouts "are likely to persist for a longer period of time"
- Anyone who wants to **reduce effort while increasing quality**

---

### The Sacrifice

Adding volume filters always trades quantity for quality:

> "That is always the sacrifice which you have to be willing to do."

A standard breakout scan might yield 50–100 stocks. Adding a volume filter (e.g., highest in 1 year) might reduce that to **5–10 stocks**, or even **1–2**.

The flip side: these fewer breakouts are more likely to be driven by real catalysts and institutional money, making them better candidates for multi-week or multi-month holds.

---

### What NOT to Use: ETFs

Pradeep explicitly excludes ETFs — especially leveraged/triple ETFs:

> "Triple ETFs are a very different animal... because the price has dropped, people are forced to buy more shares."

In ETFs like BOIL, high volume reflects the same dollar amount buying more shares at lower prices, not increased institutional interest. After a reverse split, volume "normalizes" again.

---

### Practical Implementation Summary

| Goal | Volume Filter | Expected Output |
|---|---|---|
| Reduce daily workload | V ≥ 2–3 × avg(V50.1) | 10–30 candidates |
| Find significant catalyst | Highest V in 252 days | 5–10 candidates |
| Extreme conviction | Highest V in 126 days | More candidates, slightly less significance |
| All-time participation | All-time high volume | Very few, very powerful |
| Pradeep's method | 9M+ absolute volume | Standalone signal |

---

### Key Insight

> "Volume breakouts... allow you to find breakouts that can be held for longer duration. Those are the signatures — those are the footprints of the elephants."

Volume is not about confirming whether a breakout will work today. It's about identifying which breakouts have **big-money backing** that makes them worth researching deeply and holding longer.

---

See: [[../../transcripts/Pradeep Bonde - How to Trade Breakouts Guide-Part 4_deepgram|Transcript]]
