---
title: Bullish Momentum Burst Guide — Section 5
date: 2026-05-29
source: https://stockbee-videos.b-cdn.net/2023-04-01-how-to-trade-breakouts/2023-04-01-how-to-trade-breakouts.mp4
language: en
backend: deepgram
duration_seconds: 0.0
tags:
  - win-rate
  - market-monitor
  - sector-selection
  - capitalization
  - position-size
  - trade-frequency
  - ti-65
  - m20
  - mdt-filter
  - index-components
  - top-25
---

# Bullish Momentum Burst Guide — Section 5

**Source:** Section 5 (Parts 41–50)
**Language:** en
**Backend:** deepgram
**Duration:** 00:00.000

## Summary

Section 5 addresses two practical questions: "What determines my win rate?" and "How do I reduce the overwhelming number of scan results?" The answer to both is **market phase**. Pradeep explains how the Market Monitor's primary indicator (number of stocks up 25%+ in a quarter) determines when breakouts work and when they fail. The section also covers average stop sizes by price point, the three sectors that produce the biggest moves, capitalization as the single biggest predictor of move size, and multiple filters (TI-65, M20, MDT, Top 25, Index Components) to reduce scan results for beginners.

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

### 1. Average Stop Size by Price Point

| Stock Price | Typical Breakout Size | Half-Range Stop | Low-of-Day Stop |
|---|---|---|---|
| **Below $5** | 10–20% | 5–10% | 10–20% |
| **$10–$40** | 4–10% | 2.5–5% | 5–10% |
| **Above $40** | 4–6% | 2.5–3% | 4–6% |

> "Your price point is going to determine what kind of stop you can get."

**How to get 2.5–3% stops on 4% breakout:**
1. Focus on breakouts that are only 5–6% up (not 15–20%)
2. Enter early in the day
3. Use half-of-day-range stops
4. Trade higher-priced stocks
5. **Combine with dollar breakout** for even tighter stops

Pradeep's average stop evolution: Started at ~8% (early years) → now 2.5–3% (using dollar breakout + early entry + half-range stops).

---

### 2. Win Rate: Market Phase Is Everything

The single most important factor in your win rate is **whether money is flowing into or out of the market.**

#### Green Light: Trade Aggressively
- Market Monitor primary indicator is **green** (lots of stocks up 25%+ in a quarter)
- Money is flowing INTO the market
- 300+ up days on 4% breadth
- Breakouts follow through consistently

#### Caution: Reduce Exposure
- Distribution days start appearing (300+ down days)
- Same high-quality setups that worked last week suddenly fail
- This is the first sign something has changed

#### Red Light: Stop Trading Breakouts
- Market Monitor primary indicator is **red**
- 300+ down days accumulating
- Breakouts fail one after another

> "If you continue to buy breakouts when the primary indicator is red, you're going to get stopped out one after the other."

#### Special Bullish Window
- Market turning from extremely oversold to bullish
- This is when **bottom bounce** breakouts appear — stocks making first legs from lows
- These can be the highest-probability setups of the year

#### Study 20%+ as Exhaustion Signal
- When the "20%+ in 5 days" study shows 200+ stocks → peak has been reached
- Breakouts start failing after this signal
- Good time to buy breakouts: when 20%+ readings are **low** + you get a 300+ up day

---

### 3. Capitalization: The Single Biggest Predictor of Move Size

| Market Cap | Move Potential | Notes |
|---|---|---|
| **Below $1B** | Most explosive | 20–40%+ moves common |
| **$1B–$10B** | Large moves | 15–30% moves |
| **Above $10B** | Small moves (percentage) | 5–10% typical |

> "Lower the capitalization, more explosive the move is likely to be."

**Practical advice:** When you have 5–7 good Two Lynch setups, **always pick the lower capitalization one.** A $2.4B market cap stock will make you more money than a $112B stock that breaks out with the same setup.

Pradeep's data: On a recent day with 430 stocks up 20%+, only 75 had market cap above $10B. The vast majority of explosive movers are small-cap.

---

### 4. Sector Selection: The Big Three

| Sector | Why It Works | Key Examples |
|---|---|---|
| **Healthcare / Biotech** | Most explosive movers year after year | AXSM, Rhythm, biotech runners |
| **Technology** | Consistent follow-through, larger moves | New tech, new innovation |
| **Consumer Discretionary / Fashion** | Emotional buying drives big moves | Lululemon, shoes, luxury goods |

**Avoid:**
- Utilities — slow, no burst potential
- Defense — methodical, institutional ownership suppresses volatility
- Staples (P&G, Colgate) — defensive, low ADR

> "Healthcare, especially biotechnology, technology, and consumer discretionary — these three sectors make the biggest moves any given normal year."

Pradeep's internal mnemonic: "Focus on plastics" (biotech, tech, consumer discretionary).

---

### 5. Trade Frequency: How Many Trades Per Year?

| Market Condition | A-Quality Setups Only | With All Setups |
|---|---|---|
| **Normal/bull year** | 200–250 | 250+ |
| **With position sizing limits** | 150–200 (3–4 positions at a time) | — |

> "Realistically, aim for 150 to 200 trades using 4% breakout."

Even though 200+ setups may appear, your actual trade count is limited by capital allocation (3–4 positions fully invested).

---

### 6. Filters to Reduce Scan Results

When 100–300+ stocks appear in your 4% scan, you need filters. Pradeep covers five options:

#### Filter 1: TI-65 (Trend Intensity)

```
AVGC7 / AVGC65 >= 1.05
```

- Reduces 73 → 24 stocks
- Selects stocks with established momentum
- **Good for established bull markets**
- **Misses early-stage stocks** — stocks just starting a trend won't have 65-day average above 7-day

> "I used this kind of a filter for many years and subsequently decided not to put this kind of filter because you miss out on some very good trades, especially in the beginning of a bull market."

**Pradeep's current use:** Does NOT use TI-65 as a hard filter. But it's valid for overwhelmed beginners.

#### Filter 2: TI-65 Stricter (1.19)

```
AVGC7 / AVGC65 >= 1.19
```

- Even more restrictive
- Only stocks with very strong established momentum
- Very small universe = very few trades
- Good for busy people who want 5–10 setups max

#### Filter 3: M20 (Absolute Momentum from 30-Day Low)

```
C / MIN(C, 20) >= 1.20
OR
C - MIN(C, 20) >= 20
```

- Finds stocks up 20% or $20 from their 20-day low
- **Best for:** early-stage breakouts after market corrections
- Stocks emerging from bottoms that won't show up in TI-65
- Reduces 73 → 34 stocks

> "M20 is a good filter to find younger trend. It will not show up in a TI-65 filter."

**Combine:** Use TI-65 during established trends, switch to M20 when markets are coming off lows.

#### Filter 4: Top 25 by TI-65

- Run 4% breakout scan
- Add TI-65 as a column
- Sort by TI-65 descending
- **Only look at the top 25**
- This ensures you focus on the highest-momentum setups

> "If you go through those 25, you're going to only find one or two good ideas. You're not going to get overwhelmed with 10 breakouts."

#### Filter 5: MDT (6-Month Momentum)

```
AVGC21 / AVGC126 >= 1.18
```

- Finds stocks with established 6-month momentum
- Good for longer-term holding
- Very restrictive
- Pradeep does NOT personally use this

#### Filter 6: Index Components (For Working Professionals)

- Instead of 6,000–9,000 stocks, scan only:
  - NASDAQ 100
  - S&P 500
  - (Dow 30 is already member of S&P 500)
- Drastically reduces universe
- Lower returns per trade, but easier to manage
- Suitable for people who can't babysit positions during the day

---

### Key Takeaways

1. **Market phase determines your win rate** — only trade breakouts when money is flowing into the market (Market Monitor green)
2. **Average stop size depends on price point** — below $5 stocks = 5–20% stops; $10–40 stocks = 2.5–5% stops
3. **Lower capitalization = bigger moves** — when choosing between similar setups, always pick the lower market cap
4. **Three sectors dominate:** Healthcare/Biotech, Technology, Consumer Discretionary
5. **Aim for 150–200 trades/year** with A-quality setups only
6. **Use filters when overwhelmed** — TI-65 (1.05 or 1.19), M20, Top 25, MDT, or Index Components
7. **Pradeep personally uses NO filters** but they are valid for beginners

---

### Cross-References

- [[../../transcripts/03. Bullish Momentum Burst/Pradeep Bonde - Bullish Momentum Burst Guide-Section 5_deepgram|Full Transcript]]
- [[Bullish Momentum Burst Guide-Section 4|Section 4: Entry & Stops]]
- [[Bullish Momentum Burst Guide-Section 6|Section 6: Dollar Breakout Method]]

---

### Key Quotes

> "If you continue to buy breakouts when the primary indicator is red, you're going to get stopped out one after the other."

> "Lower the capitalization, more explosive the move is likely to be."

> "Healthcare, especially biotechnology, technology, and consumer discretionary — these three sectors make the biggest moves."