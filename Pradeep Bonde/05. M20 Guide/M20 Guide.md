---
title: M20 Guide — Anchored Momentum Indicator (Momentum 20)
source:
  - https://stockbee-videos.b-cdn.net/M20%20Guide%20Part%201/M20%20Guide%20Part%201.mp4
  - https://stockbee-videos.b-cdn.net/M20%20Guide%20Part%202/M20%20Guide%20Part%202.mp4
  - https://stockbee-videos.b-cdn.net/M20%20Guide%20Part%203/M20%20Guide%20Part%203.mp4
  - https://stockbee-videos.b-cdn.net/M20%20Guide%20Part%204/M20%20Guide%20Part%204.mp4
  - https://stockbee-videos.b-cdn.net/M20%20Guide%20Part%205/M20%20Guide%20Part%205.mp4
  - https://stockbee-videos.b-cdn.net/M20%20Guide%20Part%206/M20%20Guide%20Part%206.mp4
language: en
backend: deepgram
date: 2026-05-29
tags:
- momentum
- anchored-momentum
- M20
- momentum-20
- anticipation
- continuation-setup
- pullback
- weak-structure-short
- waterfall-decline
- bottom-bounce
- market-correction
- scan-setup
- TC2000
- combo-list
- pradeep-bonde
- stockbee
---

# M20 Guide — Anchored Momentum Indicator (Momentum 20)

> **M20** is an **anchored momentum indicator** designed to find stocks the moment they change direction. It calculates momentum not from a fixed lookback, but from a **30-day anchored low (or high)** — making it ideal for catching trend changes early, especially after market corrections.
> 
> **Series:** 6 parts (Concept → Scan Formulas → Chart Setup → Step-by-Step Use → Anticipation Trick → Short Side)

---

## 1. What Is M20?

M20 (Momentum 20) is an **absolute momentum indicator** that measures a stock's move from its **30-day extreme** — either the lowest close (for bullish) or highest close (for bearish).

| Attribute | Value |
|---|---|
| **Core idea** | Find stocks immediately after they change direction |
| **Bullish trigger** | Stock up **20%** or **$20** from the **30-day minimum close** |
| **Bearish trigger** | Stock down **20%** or **$20** from the **30-day maximum close** |
| **Why "anchored"** | The reference point is the **last 30 days' low or high** — not a fixed MA |
| **Best used when** | Market coming out of a **correction** or after a **bottom** |
| **Primary use** | **Anticipation setups** — catch the first leg, then the next setup |

> "M20 is like a red light / green light — it tells you when you should go long, when to look for a continuation setup, and when to look for a short trade."

---

## 2. Why Anchored Momentum Is Different

Most momentum indicators (like TI65) use fixed-period moving averages. M20 uses a **floating anchor** — the lowest (or highest) close of the last 30 days.

| | TI65 | M20 |
|---|---|---|
| **Anchor** | Fixed 65-day MA | Floating 30-day min/max close |
| **What it measures** | Trend velocity vs. past average | Change from recent extreme |
| **Best for** | Stocks already trending | Stocks **just turning** from bottom or top |
| **Market phase** | All phases | Especially after corrections |
| **Signal speed** | Lagging (momentum already established) | Leading (catches turns immediately) |

> "The advantage of M20 is it finds trends very early. Other momentum indicators will catch it 5–10 days later."

---

## 3. The Formulas (TC2000)

### Bullish M20 Scan

```
C >= 1.2 * MINC30
```

Or equivalently:

```
C >= MINC30 + 20
```

**Meaning:** Price is at least 20% above (or $20 above) the lowest closing price in the last 30 days.

### Bearish M20 Scan

```
C <= 0.8 * MAXC30
```

Or equivalently:

```
C <= MAXC30 - 20
```

**Meaning:** Price is at least 20% below (or $20 below) the highest closing price in the last 30 days.

### Base Liquidity Filters

| Condition | Value | Purpose |
|---|---|---|
| Universe | US stocks + ADRs + ETFs | Coverage |
| Price | `C >= 3` | Eliminate penny stocks |
| Volume | `MINV3.1 >= 100000` | Minimum liquidity |

**Note:** The `$20` version is preferred for **high-priced stocks** (e.g., AutoZone, Tesla, Berkshire) because 20% of a $500 stock is $100 — too large a move. The `$20` version captures these quickly.

---

## 4. Chart Setup (Visual Indicator)

M20 is displayed as a **red/green histogram** on the price chart:

- **Green histogram** above zero = bullish momentum (price at least 20% above 30-day low)
- **Red histogram** below zero = bearish momentum (price at least 20% below 30-day high)

### How to Add in TC2000

1. **Left click** on the chart → **Add Plot** → **Custom PCF True Indicator**

2. **Bearish formula (make red histogram):**
   ```
   C <= 0.8 * MAXC30
   ```
   - Set color: **Red**
   - Style: **Histogram**

3. **Bullish formula (make green histogram):** — add another plot, overlay on same panel
   ```
   C >= 1.2 * MINC30
   ```
   - Set color: **Green**
   - Style: **Histogram**

4. **Overlay both** onto the same panel to create the red/green histogram effect

> "When the momentum was negative, it shows red. When momentum turned positive here, it indicates momentum has turned positive. And then you can find the stock when it is setting up."

---

## 5. Primary Use: Anticipation Setups

The main purpose of M20 is **anticipation** — not chasing breakouts, but finding stocks that have just turned and are resting before the next move.

### Step-by-Step Workflow (Bullish Side)

1. **Create the M20 bullish scan** as a Combo List
2. **Run it daily** (or 2–3 hours before market close)
3. **Add the NC column**:

| Column | Formula | Purpose |
|---|---|---|
| `NC` | `ABS(C - C1)` | Net Change — how much price moved today |

4. **Sort by NC ascending** (lowest first)
5. **Look for stocks with NC ≈ 0** (flat day)
6. **Review charts for:**
   - A stock that was going down
   - Then momentum turned positive (first green bar)
   - Now resting / flat with low NC (orderly pullback, bull flag)

7. **Enter in anticipation before the next breakout**

> "The primary use of M20 is to find anticipation setups which have had the first leg up, and they are forming a very orderly thing."

---

## 6. The NC Trick — Prioritizing Flat Stocks

The **NC trick** is a simple but powerful filter:

| NC Value | Interpretation | Action |
|---|---|---|
| **0.00 – 0.50** | Very flat day — stock is resting after first leg | **Top candidates** |
| **0.50 – 1.50** | Small move — still acceptable | Review chart pattern |
| **> 2.00** | Significant move — likely extended or volatile | Usually skip |

> "Lower the NC value, the better the anticipation setup. Once NC increases, these are not — most of the time — good stocks."

### Example Workflow with NC

```
1. Run M20 bullish scan
2. Add column: NC = ABS(C - C1)
3. Sort by NC ascending
4. Go through top 10–20 stocks
5. Look for charts showing:
   - First leg up (green M20 bar appears)
   - Then flat / slightly down day (NC ≈ 0)
   - Forming a tight consolidation or bull flag
6. Add to watch list
```

> "If you run this at 2:00 or 3:00 during the day, you can create a watch list and enter some in anticipation before the close."

---

## 7. Short Side: Weak Structure Shorts

M20 bearish works just as well for **shorting**:

1. Create M20 **bearish** Combo List
2. Sort by **positive NC** (or dollar change / percentage change ascending)
3. Look for:
   - **Waterfall decline** (3–4 down days in a row)
   - Then a **weak bounce** (< 2–2.5%)
   - This is the first leg down, now resting before the next drop

4. Add to watch list as a **weak structure short candidate**

> "You want a stock which had a waterfall decline, and which is having a weak bounce. If that bounce fails, that's a short."

> "Four days in a row the stock is down. This is a weak bounce of 1.53%. So it goes into your watch list."

### Waterfall Decline + Weak Bounce Pattern

| Phase | Chart | Action |
|---|---|---|
| **Waterfall** | 3–4 consecutive down days, high volume | M20 turns red |
| **Weak bounce** | 1–2 up days, < 2–2.5% gain, low volume | Add to watch list |
| **Failure** | Next day back down, breaks bounce low | **Enter short** |

---

## 8. Key Principles

### Principle 1: "Young Trend"
M20 finds stocks that have **just changed direction**. The momentum arc is young — there's room for a second leg.

### Principle 2: Market Phase Matters
M20 is **especially powerful** after a market correction:
- Scans find hundreds of stocks turning from bottom
- Many of these have been beaten down and are now bouncing
- Other momentum methods miss these because they're anchored to old highs

> "If you run it when the market is coming out of a correction, it's going to find you a lot of stocks which have been beaten down and they turn."

### Principle 3: Dual Purpose
Unlike some scans that only work on one side:
| Side | M20 Signal | Strategy |
|---|---|---|
| **Bullish** | M20 turns green after bottom | Buy anticipation / continuation |
| **Bearish** | M20 turns red after top | Short weak structure |

### Principle 4: Anticipation, Not Breakouts
M20's value is **not breakouts** — it helps you find stocks *before* they break out:
> "You don't want a stock which is breaking out today. You want a stock which had the first leg, and now it's going sideways."

---

## 9. Relationship to Other Guides

| Guide | How They Connect |
|---|---|
| [[01.How to Get Started\|Getting Started]] | Understand what "anticipation" and "continuation" mean |
| [[02. How to Trade Breakouts Guide\|Breakouts]] | M20 finds the stocks for the *next* breakout, not the first |
| [[03. Bullish Momentum Burst Guide\|Momentum Burst]] | M20 signals are often followed by a momentum burst after the anticipation entry |
| [[04. TI65 Guide\|TI65]] | TI65 measures trend velocity; M20 measures turning points. Use M20 to find the turn, TI65 to gauge the trend strength |
| [[05. DT Guide\|DT Guide]] | DT finds stocks up 80%+ from 52w low. M20 finds stocks up 20% from 30d low. M20 catches the turn earlier; DT confirms the larger trend |

---

## 10. Practical Tips

| Tip | Why |
|---|---|
| Run M20 at **2:00–3:00 PM** | Gives you time to create a watch list before market close |
| Use both **M20 bullish + bearish** daily | Be ready for trend changes in either direction |
| Combine M20 with **volume analysis** | Volume contraction on the pullback = higher probability |
| Don't take anticipation setups in a **downtrend** market | "If the market is in a downtrend, you want to wait" |
| Prioritize stocks with **NC < 0.50** | These are the most orderly and likely to continue |
| For **shorts**, look for **3–4 down days + < 2.5% bounce** | This is the classic weak structure short |

---

## Bottom Line

M20 is an **early detection system** for trend changes. Anchored to the last 30 days' extreme, it finds stocks the moment they recover (or start breaking down). Combined with the NC trick for prioritization and the anticipation framework, M20 is a core tool for catching young trends — both long and short — before the broader momentum crowd arrives.

---

## Full Transcripts

See:
- [[../../transcripts/Pradeep Bonde - M20 Guide-Part 1_deepgram|Part 1 — Introduction]]
- [[../../transcripts/Pradeep Bonde - M20 Guide-Part 2_deepgram|Part 2 — Scan Setup]]
- [[../../transcripts/Pradeep Bonde - M20 Guide-Part 3_deepgram|Part 3 — Chart Setup]]
- [[../../transcripts/Pradeep Bonde - M20 Guide-Part 4_deepgram|Part 4 — Step-by-Step Use]]
- [[../../transcripts/Pradeep Bonde - M20 Guide-Part 5_deepgram|Part 5 — Anticipation Trick (NC)]]
- [[../../transcripts/Pradeep Bonde - M20 Guide-Part 6_deepgram|Part 6 — Short Side (Weak Structure)]]
