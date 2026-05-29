---
title: DT Guide — Double Trouble Methodology (Darvas-Style Momentum Scan)
source:
  - https://stockbee-videos.b-cdn.net/DT%20Guide%20Part%201/DT%20Guide%20Part%201.mp4
  - https://stockbee-videos.b-cdn.net/DT%20Guide%20Part%202/DT%20Guide%20Part%202.mp4
  - https://stockbee-videos.b-cdn.net/DT%20Guide%20Part%203/DT%20Guide%20Part%203.mp4
  - https://stockbee-videos.b-cdn.net/DT%20Guide%20Part%204/DT%20Guide%20Part%204.mp4
language: en
backend: deepgram
date: 2026-05-29
tags:
- momentum
- darvas
- double-trouble
- DT
- 52-week-low
- continuation-setup
- breakout
- anticipation
- scan-setup
- TC2000
- combo-list
- momentum-burst
- pradeep-bonde
- stockbee
---

# DT Guide — Double Trouble Methodology

> The **Double Trouble (DT)** methodology is a momentum scan inspired by Nicolas Darvas: find stocks that have risen at least **80% from their 52-week low** and are now setting up for their next leg. This is not a breakout scan — it is a **continuation-setup and anticipation scan** that operates on the premise that stocks which have already doubled from their lows are statistically more likely to continue trending.
> 
> **Series:** 4 parts (Introduction → Scan Setup → Advanced Use → Anticipation)

---

## 1. What Is Double Trouble?

**Double Trouble** is a momentum method based on a principle Nicolas Darvas observed: stocks that have **doubled from their 52-week low** are in powerful uptrends and worth monitoring for the next move.

Pradeep adapts this insight into a quantitative scan:

| Attribute | Value |
|---|---|
| **Core condition** | Price is at least **1.8x** the 52-week low |
| **TC2000 formula** | `C / MINL252 >= 1.8` |
| **Why 1.8, not 2.0?** | Darvas used "double" loosely; 1.8 captures strong momentum while still leaving room for the next leg |
| **Core insight** | Stocks that have already moved significantly from their lows have **proven institutional interest** |
| **Best used for** | Continuation setups, anticipation, swing trading |

---

## 2. Why "Doubled from Low" Matters

Darvas noticed that stocks making big moves often start from a **deep base** and then double before the public notices. The psychology:

- Stocks near 52-week lows are ignored or hated
- Once they begin moving up, early accumulation happens quietly
- By the time they've **doubled from the low**, the trend is visible but **not yet exhausted**
- These stocks are now on radars but still have room to run

> "If a stock has gone from $10 to $20, it's already doubled. That tells you something is happening. But has it topped? Not necessarily. The next leg is what you want."

This is fundamentally a **confirmation of trend strength** — not a raw breakout signal.

---

## 3. Building the Double Trouble Scan (TC2000)

### Step 1: Create a Combo List (or EasyScan)

| Tab | Condition | Purpose |
|---|---|---|
| **Universe** | US stocks + ADRs + ETFs | Broad coverage |
| **Liquidity** | `MINV3.1 >= 100000` | Minimum 100K shares/day |
| **Price** | `C >= 3` | Avoid sub-$3 penny stocks |
| **DT Core** | `C / MINL252 >= 1.8` | **Has risen 80%+ from 52w low** |

**Alternative formula (TC2000 EasyScan):**
```
C >= 1.8 * MINL252
```

Result with standard liquidity: ~400–800 stocks at any given time.

### Step 2: Rank by DT Strength

Create a **column** for the DT value:

| Column Name | Formula | Display |
|---|---|---|
| `DT` | `C / MINL252` | Decimal value (e.g., 2.34 = up 134% from low) |

Sort the list by DT in **ascending** or **descending** order depending on your goal:

- **Descending** → find the stocks that have run the most (strongest relative to their lows)
- **Ascending** → find stocks that have *just* crossed the 1.8 threshold (younger momentum)

---

## 4. Three Ways to Use Double Trouble

### 4.1 — Rank the Strongest Stocks (Momentum Leaders)

This is the simplest use: find the stocks that have already proven they can move.

1. Run the DT scan daily
2. Sort by `DT` column descending
3. Focus on the **top 50–100**
4. Look for:
   - Pullbacks to a rising MA (8-day, 21-day)
   - Tight consolidation near highs
   - Low-volume contraction before expansion

> "If you're going to swing trade, you want to trade the strongest stocks. Double Trouble IS the list of the strongest stocks."

### 4.2 — Anticipation Setups (Before the Breakout)

This is Pradeep's primary use. The DT list becomes your **anticipation universe**.

**Single-day anticipation scan from DT universe:**

| Condition | Value | Purpose |
|---|---|---|
| DT universe | Base list | Already up 80%+ from low |
| `AVGC7 / AVGC65 >= 1.05` | TI65 bullish | Has momentum |
| `Price Percent Change Today` | Between `-0.4%` and `+0.4%` | Very narrow range = resting |
| NC column | `ABS(C - C1)` near **0** | Flat day |

Same logic as the TI65 anticipation scan, but now the **universe is filtered to Darvas-style momentum leaders**.

### 4.3 — Continuation After First Breakout

After a stock has already doubled from its low, the **first continuation setup** is often the safest and most profitable entry:

- Stock breaks out on Day 1 (range expansion)
- Pulls back for 3–10 days in low volume
- The pullback holds above the breakout level or the rising 8-day MA
- Entry: when it breaks out of the pullback

These are "Two-Leg" momentum burst setups:

| Phase | Description | TI65 State |
|---|---|---|
| **Leg 1** | Stock moves from low, doubles | TI65 crosses above 1.05 |
| **Consolidation** | Flat/pullback for 3–10 days | TI65 stays > 1.05 |
| **Leg 2** | Breakout from consolidation | TI65 rises further |

---

## 5. Combining DT with Other Tools

The DT method is **not a standalone system** — it is a **momentum universe** that feeds into other setups:

| Tool | How It Combines with DT |
|---|---|
| **TI65** | Use the **DT list as the base universe** for TI65 anticipation scans |
| **4% Breakout Scan** | The stocks that show up on 4% breakouts are often already on the DT list |
| **EP (Episodic Pivot) Scan** | EP stocks frequently have strong DT values |
| **Combination Scan** | Run breakouts and EPs, but **cross-reference against DT** — DT stocks have better follow-through |

---

## 6. Key Principles from the Guide

### Principle 1: "Doubled from Low" = Trend Confirmation
A stock that has doubled from its low has already passed a test: it survived selling pressure, built a base, and attracted buyers. It is no longer a "hope" stock.

### Principle 2: The Best Entries Are After the First Breakout

the most reliable setup on a DT stock is the **first pullback** after the initial move. Stocks that have doubled and then rest are coiling for the next leg.

### Principle 3: DT + Volume Pattern
When a DT stock consolidates, watch for:
- **Declining volume during the consolidation** (contraction)
- **Range expansion on the next breakout** (explosion)

This volume-contraction-to-expansion pattern is a high-probability setup.

### Principle 4: Don't Chase the Extremes
If a stock has a DT value of 5.0x (up 400% from low), the risk is higher. Pradeep prefers stocks in the **1.8–3.0x range** — they have momentum but are not yet parabolic.

---

## 7. Darvas Context

Nicolas Darvas, in his book *How I Made $2,000,000 In The Stock Market*, used the "box theory" but also paid attention to stocks that had risen significantly from their lows. He believed these stocks had "proven" themselves and were more likely to continue. Pradeep formalizes that intuition into a scan.

> "Darvas didn't have TC2000. He did this by reading the newspaper and looking at stocks that had doubled. We can do it in two seconds with a scan."

---

## 8. Scan Formula Summary (TC2000)

| Purpose | Formula |
|---|---|
| **Double Trouble core** | `C / MINL252 >= 1.8` |
| **Double Trouble column** | `C / MINL252` |
| **Liquidity filter** | `MINV3.1 >= 100000` |
| **Price filter** | `C >= 3` |
| **DT + TI65 bullish** | `C / MINL252 >= 1.8` + `AVGC7 / AVGC65 >= 1.05` |
| **DT anticipation** | `C / MINL252 >= 1.8` + `Price Percent Change Today` between `-0.4` and `+0.4` |
| **DT + narrow range** | `C / MINL252 >= 1.8` + `ABS(C - C1) <= (H - L) * 0.3` |

---

## 9. Who Is This For?

| Skill Level | Best Use |
|---|---|
| **Beginner** | Run the scan daily and just **look at the top 25** to understand which stocks are strong |
| **Intermediate** | Combine DT with TI65 for **anticipation scans** |
| **Advanced** | Use DT as a **base universe** for all breakout/continuation setups; filter further with volume, float, or catalyst data |

---

## 10. Relationship to Other Guides

| Guide | Relationship |
|---|---|
| [[01.How to Get Started\|Getting Started]] | DT is a **momentum layer** you add once you understand the basics |
| [[02. How to Trade Breakouts Guide\|Breakouts]] | DT stocks often produce the **best breakout setups** |
| [[03. Bullish Momentum Burst Guide\|Bullish Momentum Burst]] | DT + momentum burst = **continuation after the first leg** |
| [[04. TI65 Guide\|TI65]] | Use **DT list as the TI65 universe** for rank and anticipation |

---

## Bottom Line

Double Trouble is a **momentum filter**: it answers the question "which stocks have already proven they can move?" By restricting your trading universe to stocks that have doubled from their 52-week lows, you tilt the odds in your favor. Combined with TI65, anticipation scans, and volume analysis, DT becomes a core pillar of a momentum-based trading system.

---

## Full Transcripts

See:
- [[../../transcripts/Pradeep Bonde - DT Guide-Part 1_deepgram|Part 1]]
- [[../../transcripts/Pradeep Bonde - DT Guide-Part 2_deepgram|Part 2]]
- [[../../transcripts/Pradeep Bonde - DT Guide-Part 3_deepgram|Part 3]]
- [[../../transcripts/Pradeep Bonde - DT Guide-Part 4_deepgram|Part 4]]
