---
title: "Lesson 2: The 4% Breakout + 9M Volume — The Foundational Pattern"
date: 2026-06-04
tags: [class, lesson-02, breakout, 4-percent, 9M, volume, foundational-pattern]
---

# Lesson 2: The 4% Breakout + 9M Volume

> **Core Question:** What pattern starts every explosive move in the market?
> **Answer:** A 4%+ price move on 9M+ volume. This is the atom of the entire system — everything is built on top of this.

---

## The Discovery

Pradeep studied all stocks that made 25%+ in a month for the **last 40 years**. The finding:

> **Almost every explosive move starts with a 4%+ day on high volume.**

This is not opinion. It's data from 40 years of market history. The 4% breakout is the **universal starting signal** — the grammar of the market.

---

## The Two Pillars

| Pillar | What It Measures | Threshold | Why It Matters |
|--------|-----------------|-----------|----------------|
| **4% price move** | Price conviction — "something real happened" | Close ≥ 1.04 × Previous Close | Only stocks where something *structural* changed |
| **9M volume** | Institutional participation | Volume ≥ 9,000,000 | Only stocks where *institutions* are involved |

**Both must be present.** This is not optional.

- **4% without volume** = noise. A stock moved 4% on 500K shares. Nobody cares.
- **Volume without price** = accumulation. Institutions are buying, but the move hasn't started yet. Might start tomorrow, might start next month.
- **4% + 9M** = **the market noticed something, and institutions are participating.** This is where follow-through comes from.

---

## Why 4%, Not 2% or 5%?

| Threshold | Problem |
|-----------|---------|
| **1–2%** | Too much noise. Many stocks move 1–2% on any given day for no structural reason. False positives everywhere. |
| **4%** | The data shows this threshold is where something *structural* has changed. Earnings, analyst action, sector rotation — 4% means the market noticed. |
| **8–10%** | Too high. Misses many valid breakouts that start at 4–5% and accelerate later. You'd skip MSFT on a 4.2% earnings gap that goes on to make 60%. |

---

## Why 9M Volume?

**9M is an empirical threshold, not a magic number.** Pradeep arrived at it through years of observation: the biggest EP moves ALL started with 9M+ volume. The "9M" in "EP 9M" literally stands for 9 million.

Volume separates **institutional participation** from **retail noise**:

| Volume Level | Who's There                      | Implication                                               |
| ------------ | -------------------------------- | --------------------------------------------------------- |
| **< 1M**     | Retail day traders, thin float   | Manipulation risk; no follow-through                      |
| **1–5M**     | Some institutional interest      | Decent; might work                                        |
| **5–9M**     | Growing institutional interest   | Good; watch for follow-through                            |
| **≥ 9M**     | Full institutional participation | This is where the big money flows; follow-through is real |

> *"Volume tells you how good the catalyst is. Volume tells you whether this is a significant catalyst or not."*

### Is 9M a Hard Cutoff or a Guideline?

**It's a practical threshold, not a cliff.** A stock with 8.5M volume isn't fundamentally different from one with 9.1M. The principle is:

> **A breakout without institutional volume has no follow-through.**

| Context | Volume Threshold | Why Adjusted |
|---------|-----------------|-------------|
| **Standard EP 9M** | 9M+ | Default — where institutional follow-through is confirmed |
| **Dollar breakout (FHP)** | 100K+ | High-priced stocks ($100+) are always liquid; 9M is unnecessary |
| **Small cap scan** | 5M+ | Relaxed for smaller caps with lower float |
| **Very thin names** | 1M+ | Only for experienced traders who know the risk |

**The number (9M) matters less than the principle (institutional volume confirms the move).** Use 5M for small caps, 100K for FHPs, but always ensure "sufficient volume for follow-through."

---

## The Scan Formula

### TC2000 (TradeStation)

```
C/C1 >= 1.04           // Close today ≥ 4% above yesterday's close
AND V >= V1             // Volume ≥ yesterday's volume (optional refinement)
AND V >= 8900000        // Volume ≥ 9 million
```

### FMP API (Python Scanner)

```
GET /stable/biggest-gainers  →  filter changePercentage >= 4%, volume >= 9M
GET /stable/biggest-losers   →  filter changePercentage <= -4%, volume >= 9M
```

### What the Scan Produces

| Time | Number of Stocks |
|------|-----------------|
| **9:30 AM** | 10–20 stocks |
| **9:45 AM** | 20–30 stocks |
| **10:00 AM** | 30–40 stocks |
| **11:00 AM** | 60–70 stocks |
| **End of day** | 200–300 stocks (on a normal day) |

At 9:30, you're looking for **1–2** SOS setups from the 10–20 stocks. Not 50. Not 10. **1–2.**

---

## The Sugar Baby Connection

Pradeep asked a simple question:

> *"Which stocks do this 4%+ 9M+ breakout REPEATEDLY?"*

That question gave birth to **Sugar Babies**. You count how many times a stock has a 4%+ day with 9M+ volume across multiple timeframes (5, 10, 20, 50, 126, 252, 504, 756, 1,450 days). The top 20–30 per timeframe form your master list of ~90 stocks that are "madly in love" with the market.

**These are your universe.** You don't scan 8,000 stocks. You trade SOS/DEP/ANTS **only on Sugar Babies** when possible.

==The logic:==
- ==A stock that breaks out 4%+ on 9M+ volume **4 times a year** has proven institutional interest==
- ==When that stock gives a setup again, it's far more likely to produce a 30–40% move in 2–3 days==
- ==Ordinary stocks make 8–20% in the same timeframe; Sugar Babies make 40–50%==

---

## The 4% Breakout Happens in Real-Time

⚠️ **Critical misunderstanding to avoid:** The 4% breakout is NOT a prediction of what will happen tomorrow. It is a **detection of what is happening RIGHT NOW, today, in real-time.**

You don't predict which stock will go 4%+. You **react** to stocks that are already moving 4%+ when the market opens.

### The Correct Workflow

```
9:30 AM → Run EP 9M scan
         → Stocks that are ALREADY up 4%+ today appear on the scan
         → This is happening RIGHT NOW, in real-time
         → Enter within the first 15–30 minutes (SOS entry)
         → Stop at low of the day
```

### What You Do NOT Do

| ❌ Wrong | Why Wrong | Source |
|----------|-----------|--------|
| Wait for yesterday's 4% breakout to buy today | That's buying day 2 — stop too wide, move mostly done | [[15. Start of a Swing Guide]] |
| Try to predict which stock will go 4%+ tomorrow | You can't predict; you REACT to what's happening now | [[08. Anticipation (ANTS) Guide]] |
| Buy the next day after a 4% breakout | Same as buying day 2 — the move is 3–5 days; most is day 1 | [[Mind Clarity Guide]] |

### If You Miss Day 1

| Option | What to Do | Stop Width | Position Size | Source |
|--------|-----------|-----------|---------------|--------|
| **Add to DEP watchlist** | Wait 3–10 days for pullback, then enter | 0.5–2.5% | **25–50%+** (biggest) | [[16. DEP Guide]] |
| **Check for ANTS setup** | If now in tight consolidation, enter via BSLO at 2:58 PM | <1% | Large | [[08. Anticipation (ANTS) Guide]] |
| **Skip it** | There will be another setup tomorrow | No risk | N/A | [[21. Process Guide]] |

**The only way to "predict" a 4% breakout is ANTS (Anticipation):**
1. Stock shows 3T tight days (3 consecutive days <1% change) with strong momentum
2. Place a Buy Stop Limit Order (BSLO) at close+1%, limit at trigger+0.25% at 2:58 PM the day before
3. Next morning, if stock breaks out 4%+, your BSLO is triggered and you're already in with a <1% stop
4. If it doesn't break out, the order never activates — no loss

---

## How to Use the Scan

| Time | What You Do |
|------|-------------|
| **9:30** | Run EP 9M scan (4%+ breakout + 9M+ volume) — stocks moving RIGHT NOW |
| **9:30–9:45** | Find 1–2 with SOS (Start of a Swing) |
| **9:45–10:00** | Enter early leaders with stop at low of day |
| **10:00+** | Classify: cat (real catalyst), dog (story), liquid lava (theme) |

---

## The $ Breakout Variant

For **high-priced stocks** ($60+), 4% may be too much volatility. Pradeep uses a **dollar breakout** instead:

```
C - O >= $0.90     // Close minus Open ≥ $0.90
AND V >= 100000    // Volume ≥ 100K (lower threshold; institutions dominate price)
```

**Why dollars instead of %?**
- A $100 stock moving 4% = $4 — that's huge noise for an institutional name
- A $100 stock moving $0.90 = less than 1% — this is how Goldman Sachs, NVDA, etc. start their swings
- Think in dollars for FHP (Full High-Priced) stocks: *"I'm risking $2 to make $10"*

---

## What the 4% Breakout Does NOT Do

| Myth | Reality |
|------|---------|
| Every 4% breakout is buyable | ❌ Most are not. You must **qualify** with catalyst, stock quality, and market regime |
| 4% breakout works on any stock | ❌ Institutional quality (1000+ funds) matters for follow-through |
| 4% breakout works in bear markets | ❌ In red Market Monitor, breakouts fail; go short instead |
| Wait for confirmation after 4% breakout | ❌ By ORB confirmation, your stop is 8–10%; you've missed the move |

> *"Just because it's a start of a swing doesn't mean you buy every start of a swing. You have to qualify... Without qualification, if you just buy a breakout, you will lose money. That's the skill."*

---

## Key Rules Summary

| # | Rule | Source |
|---|------|--------|
| 1 | 4%+ price + 9M+ volume = the atom of the system | [[How to Trade Breakouts Guide-Part 1]] |
| 2 | Both pillars required — 4% without volume is noise | [[Scans and Filters]] |
| 3 | 9M volume = institutional participation = follow-through | [[21. Process Guide]] |
| 4 | At 9:30, look for 1–2 setups, not 50 | [[21. Process Guide]] |
| 5 | Most 4% breakouts are NOT buyable without qualification | [[15. Start of a Swing Guide]] |
| 6 | Dollar breakout ($0.90+) for stocks >$60 | [[15. Start of a Swing Guide]] |
| 7 | Sugar Babies = stocks that repeatedly produce 4%+ 9M+ days | [[14. Sugar Babies Guide]] |
| 8 | 40 years of data confirms: explosive moves start with 4%+ days | [[How to Trade Breakouts Guide-Part 1]] |

---

## Homework

1. **Run the EP 9M scan** on TC2000 or your screener right now. Count how many stocks are up 4%+ on 9M+ volume today.
2. **Cross-reference with Sugar Babies list** — how many of today's breakouts are on the Sugar Baby master list?
3. **Classify each breakout:** Is there a clear catalyst? Is the stock institutional quality (1000+ funds)?
4. **Read the full guide:** [[How to Trade Breakouts Guide-Part 1]] — all 7 parts.

---

## Next Lesson

→ [[03 - Entries]] — The five ways to enter a trade.

---

## Cross-References

- **KB Notes:** [[Scans and Filters]], [[Entries]], [[Market Monitor]]
- **Curated Guides:** [[How to Trade Breakouts Guide-Part 1]], [[14. Sugar Babies Guide]], [[15. Start of a Swing Guide]]
- **Transcripts:** `transcripts/02. How to Trade Breakouts/`