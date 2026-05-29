---
title: TI65 Guide — Trend Intensity 65 Momentum Indicator
source:
  - https://stockbee-videos.b-cdn.net/TI65%20Guide%20Part%201/TI65%20Guide%20Part%201.mp4
  - https://stockbee-videos.b-cdn.net/TI65%20Guide%20Part%202/TI65%20Guide%20Part%202.mp4
  - https://stockbee-videos.b-cdn.net/TI65%20Guide%20Part%203/TI65%20Guide%20Part%203.mp4
  - https://stockbee-videos.b-cdn.net/TI65%20Guide%20Part%204/TI65%20Guide%20Part%204.mp4
  - https://stockbee-videos.b-cdn.net/TI65%20Guide%20Part%205/TI65%20Guide%20Part%205.mp4
  - https://stockbee-videos.b-cdn.net/TI65%20Guide%20Part%206/TI65%20Guide%20Part%206.mp4
  - https://stockbee-videos.b-cdn.net/2023-03-30-how-to-use-ti65/2023-03-30-how-to-use-ti65.mp4
language: en
backend: deepgram
date: 2026-05-29
tags:
- momentum
- trend-intensity
- TI65
- momentum-indicator
- absolute-momentum
- relative-momentum
- anticipation
- continuation-setup
- pullback-trading
- short-selling
- scan-setup
- TC2000
- combo-list
- young-momentum
- days-in-ti65
- experienced-traders
---

# TI65 Guide — Trend Intensity 65 Momentum Indicator

> This guide covers both the **mechanics** of setting up the TI65 indicator (Parts 1–6) and the **advanced applications** for finding young momentum, continuation setups, pullback entries, and shorting opportunities ("How to Profit from TI65").
> 
> **Prerequisite:** Understanding of momentum burst concepts from the [[How to Get Started In Trading Guide|Getting Started Guide]] and [[How to Trade Breakouts Guide|Breakouts Guide]] is assumed.

---

## 1. What Is TI65?

TI65 (Trend Intensity 65) is a **momentum indicator** that measures the **velocity** of a stock's trend.

> "What TI65 essentially tells you is it tells you the **velocity of move**. Higher the trend intensity, faster is the stock moving."

It is computed as the ratio of two moving averages:

| Formula | Interpretation |
|---|---|
| `Average(C, 7) / Average(C, 65)` | Ratio of 7-day MA to 65-day MA |
| **> 1.05** | Bullish trend intensity — stock is trending up with speed |
| **< 0.95** | Bearish trend intensity — stock is trending down with speed |
| **0.95 – 1.05** | Neutral — no clear trend intensity |

> "If a stock has TI65 of 1.05, it is definitely in a positive trend. But we don't just want positive trend — we want positive trend with **a certain speed**."

---

## 2. Relative Momentum vs. Absolute Momentum

Pradeep introduces a critical distinction that most momentum tools fail to capture:

| | Relative Momentum | Absolute Momentum |
|---|---|---|
| **What it measures** | How a stock ranks vs. all other stocks (percentile) | A stock's own velocity, independent of others |
| **Example** | IBD RS Rating of 97 — ranked #3 among all stocks | TI65 of 1.05 — 7-day MA is 5% above 65-day MA |
| **Problem** | Tells you a stock is strong, but **not when momentum started** | Tells you **exactly when momentum began** and its speed |
| **Trading use** | Often leads to buying extended stocks | Finds early entry points, avoids overextended stocks |

Pradeep calls this the difference between knowing *"Brian has $5M"* (absolute wealth) and knowing *"Brian is in the top 5% of Americans"* (relative wealth). Both are useful, but only absolute momentum tells you where the trend began.

> "Relative strength is good to know — it means you're ranked #3 amongst all stocks in momentum — but it is **perfectly useless** because you don't know where this momentum started."

> "If you select stocks based on relative momentum, you're going to be buying stocks which are way extended. **Absolute momentum is a trader's friend.**"

---

## 3. Setting Up TI65 in TC2000 (Parts 1–3)

### Part 1 — Chart Setup

The TI65 is displayed as a **colored area plot** on the chart:
- **Green area** = Bullish trend intensity (price above 1.05)
- **Red area** = Bearish trend intensity (price below 0.95)

This gives you **visual trend intensity** — you can see at a glance when a stock entered a strong trend and when it exited.

> "Unlike other momentum indicators, TI65 tells you the **exact day** when trend intensity turned positive. It tells you the **exact day** when it turned negative."

### Part 2 — Custom Indicator Formula

To add TI65 as a **custom PCF True Indicator**:

| Side | Formula | Color | Style |
|---|---|---|---|
| **Bullish** | `AVGC7 / AVGC65 >= 1.05` | Green | Area |
| **Bearish** | `AVGC7 / AVGC65 <= 0.95` | Red | Area |

> **Note for European keyboards**: Use `105 / 100` instead of `1.05`, and `95 / 100` instead of `0.95`.

### Part 3 — Adding the Numeric Value to Toolbar

To see the actual TI65 ratio value on every chart:

1. Create a new **Indicator** called `65T`
2. Formula: `AVGC7 / AVGC65`
3. Add to toolbar via **Edit Toolbar → Plus sign → Select 65T**

This shows the ratio (e.g., **TI 1.82**) so you can instantly gauge trend speed.

---

## 4. Building Bullish & Bearish Universe Scans (Part 4)

Create two **Combo Lists** (scan universes):

### Bullish TI65

| Condition | Purpose |
|---|---|
| US stocks + ADRs + ETFs | Universe |
| `MINV3.1 >= 100,000` | Liquidity: minimum 100K shares traded last 3 days |
| `C >= 3` | Price filter: eliminate sub-$3 stocks |
| `AVGC7 / AVGC65 >= 1.05` | **Trend intensity bullish** |

Result: ~870 stocks (with 100K min volume) currently in bullish trend intensity.

### Bearish TI65

Same conditions, but:

| Condition | Value |
|---|---|
| `AVGC7 / AVGC65 <= 0.95` | **Trend intensity bearish** |

Result: ~832 stocks currently in bearish trend intensity.

> "This itself gives you information about the underlying buying or selling pressure in the market."

---

## 5. Practical Applications (Part 5 & "How to Profit")

Once the two universes are built, there are **multiple ways to use TI65** depending on your trading style:

### 5.1 Rank & Isolate Strongest / Weakest Stocks

Sort the bullish list by TI65. Focus only on the **top 25, 50, or 100** strongest stocks.

> "If they are setting up for a possible bounce or having a pullback, just focus on the first 25 ranked stocks — these are the strongest stocks."

Similarly, sort the bearish list and look at the **weakest stocks** for short candidates or oversold bounces.

### 5.2 Anticipation Scan (Part 6)

Create a **narrow-range anticipation scan** from the bullish TI65 universe:

| Condition | Value |
|---|---|
| Bullish TI65 universe | Base |
| `AVGC7 / AVGC65 >= 1.05` | Already has momentum |
| `Price Percent Change Today` between **-0.4% and +0.4%** | Very narrow range day |

Add a column:
- **NC** (Net Change) = `ABS(C - C1)` — lower = more flat

Sort by lowest NC. Stocks with **NC near 0** and existing TI65 momentum are setting up for a breakout.

> "These are stocks which are having a very orderly low-and-limp pullback. You can find them, create a watch list, and you're ready for when they break out."

### 5.3 Finding Young Momentum — The "Days In" Column (Advanced)

This is the most powerful application, but **only for experienced traders**.

The problem: You want the **first** breakout or pullback after momentum turns positive. Not the third or fourth.

**Solution:** Create a column tracking **how many days the stock has had positive TI65 in the last N days**.

| Column | Formula | Purpose |
|---|---|---|
| `C65` | `COUNTTRUE(AVGC7 / AVGC65 >= 1.05, 100)` | Count of days with bullish TI65 in last 100 days |
| `D65` | `COUNTTRUE(AVGC7 / AVGC65 <= 0.95, 100)` | Count of days with bearish TI65 in last 100 days |

**Sort by C65 (ascending)** to find stocks that **just entered** bullish trend intensity.

> "If this stock went into positive TI65 **yesterday**, and we ran this scan yesterday, we would have bought it. We don't need a breakout — as long as there's sufficient liquidity."

> "We want to find **young setups**. What we want is the **first good pullback or the first good breakout after TI65 goes above 1.05**."

**Why young momentum matters for holding period:**

| Entry Timing | Can You Hold for Second Leg? |
|---|---|
| First breakout after TI65 turns positive | **Yes** — room to run |
| Second or third leg | **No** — extended, higher risk |

> "If you want to hold for longer term, you have to find **younger setups**."

---

## 6. Matching TI65 to the Three Setup Types

TI65 maps directly to the three momentum burst setups:

| Setup Type | TI65 State at Setup | How to Use TI65 |
|---|---|---|
| **Bottom Bounce** | TI65 negative or just turning positive | Best bottom bounces happen when TI65 is deep in negative territory |
| **Continuation Breakout (Two-Leg)** | TI65 > 1.05 (momentum established) | Most good two-leg setups appear **after** TI65 > 1.05 |
| **Consolidation Breakout** | TI65 > 1.05, flat/sideways for 3–10 days | Sort by 7-day momentum (C7) ascending — find orderly pullbacks |

---

## 7. Short-Side Applications

The exact same logic applies to shorting:

1. **Bearish TI65 universe** — stocks with `AVGC7 / AVGC65 <= 0.95`
2. Prioritize very liquid stocks (Pradeep uses 1M+ volume for shorts, but 100K works for smaller accounts)
3. Add `D65` column (days in bearish TI65, last 100 days)
4. Sort ascending — find stocks that **just turned negative**

> "When do you want to short? You want to short **early in the breakdown**, not when the breakdown is so apparent."

> "Our scans are designed to find breakouts on Day 1. They won't show you the short the day after earnings recovers and then dumps. But if you do this TI65 work, you'll find the low-risk short **next day** after the bounce."

---

## 8. Why "Days In" Matters — The Long-Run Statistics

Pradeep emphasizes a statistical fact most newer traders miss:

> "Most stock moves happen in a **two-month period**. Even if a stock is going to make a bigger move, it happens all in two months."

This is why finding **young** momentum is so critical:

| Days in TI65 > 1.05 | Interpretation |
|---|---|
| 1–10 days | Very young trend, highest reward/risk |
| 50–100 days | Trend is maturing — still valid, but be selective |
| 120–150+ days | Rare. Most stocks can't maintain >1.05 velocity this long |

> "I've seen examples where stocks go up without getting extended — they go sideways, breakout, sideways again. But those are **very, very rare**. Most stocks have a very difficult time maintaining TI above 1.05 for more than 120–150 days."

---

## 9. Key Formulas Summary (TC2000)

| Purpose | Formula |
|---|---|
| Bullish TI65 indicator | `AVGC7 / AVGC65 >= 1.05` (green area) |
| Bearish TI65 indicator | `AVGC7 / AVGC65 <= 0.95` (red area) |
| TI65 value on toolbar | `AVGC7 / AVGC65` (display as 2 decimals) |
| Liquidity filter | `MINV3.1 >= 100000` |
| Price filter | `C >= 3` |
| Anticipation: narrow range | `Price Percent Change Today` between `-0.4` and `+0.4` |
| Net Change (flatness) | `ABS(C - C1)` |
| Days in bullish TI65 (100 days) | `COUNTTRUE(AVGC7 / AVGC65 >= 1.05, 100)` |
| Days in bearish TI65 (100 days) | `COUNTTRUE(AVGC7 / AVGC65 <= 0.95, 100)` |
| 7-day momentum (for pullback scan) | `C / C7` or simply `C7` |

---

## 10. Who Is This For?

> "This session is designed for people with **a little bit of experience** who already know what we are talking about, who have gone through the guide section, who understand what is momentum."

> "New traders are confused as it is. There is no guide for this, and I don't intend to make a guide for this. But for experienced people — if I open a window, it's enough to jump out and find opportunities."

| Skill Level | Recommended Use |
|---|---|
| **Beginner** | Focus on Parts 1–4: set up TI65, build scans, get familiar |
| **Intermediate** | Part 5: rank stocks, use anticipation scan |
| **Advanced** | "How to Profit" session: Days In column, pullback trading, short side |

---

## Full Transcripts

See:
- [[../../transcripts/Pradeep Bonde - TI65 Guide-Part 1_deepgram|Part 1]]
- [[../../transcripts/Pradeep Bonde - TI65 Guide-Part 2_deepgram|Part 2]]
- [[../../transcripts/Pradeep Bonde - TI65 Guide-Part 3_deepgram|Part 3]]
- [[../../transcripts/Pradeep Bonde - TI65 Guide-Part 4_deepgram|Part 4]]
- [[../../transcripts/Pradeep Bonde - TI65 Guide-Part 5_deepgram|Part 5]]
- [[../../transcripts/Pradeep Bonde - TI65 Guide-Part 6_deepgram|Part 6]]
- [[../../transcripts/Pradeep Bonde - TI65 Guide-How to profit from TI65_deepgram|How to Profit from TI65]]
