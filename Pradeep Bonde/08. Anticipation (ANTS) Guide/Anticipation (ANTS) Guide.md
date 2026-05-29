---
title: Anticipation (ANTS) Guide
date: 2026-05-29
tags:
  - pradeep-bonde
  - anticipation
  - ants
  - momentum-pause
  - breakout-anticipation
  - buy-stop-limit-order
  - bslo
  - front-running
  - smart-scan
  - tight-consolidation
  - first-leg-only
  - volatility-compression
  - position-trading
  - swing-trading
  - ti65
  - m20
  - mdt
  - dt
  - market-condition
---

# Anticipation (ANTS) Guide

**Author:** Pradeep Bonde (StockBee)  
**Source:** [StockBee ANTS Guide](https://stockbee.biz/ants-guide/) — 12 parts  
**Transcripts:**
- [[../../transcripts/08. Anticipation (ANTS) Guide/Pradeep Bonde - ANTS Guide-Part 1_deepgram.md|Part 1]]
- [[../../transcripts/08. Anticipation (ANTS) Guide/Pradeep Bonde - ANTS Guide-Part 2_deepgram.md|Part 2]]
- [[../../transcripts/08. Anticipation (ANTS) Guide/Pradeep Bonde - ANTS Guide-Part 3_deepgram.md|Part 3]]
- [[../../transcripts/08. Anticipation (ANTS) Guide/Pradeep Bonde - ANTS Guide-Part 4_deepgram.md|Part 4]]
- [[../../transcripts/08. Anticipation (ANTS) Guide/Pradeep Bonde - ANTS Guide-Part 5_deepgram.md|Part 5]]
- [[../../transcripts/08. Anticipation (ANTS) Guide/Pradeep Bonde - ANTS Guide-Part 6_deepgram.md|Part 6]]
- [[../../transcripts/08. Anticipation (ANTS) Guide/Pradeep Bonde - ANTS Guide-Part 7_deepgram.md|Part 7]]
- [[../../transcripts/08. Anticipation (ANTS) Guide/Pradeep Bonde - ANTS Guide-Part 8_deepgram.md|Part 8]]
- [[../../transcripts/08. Anticipation (ANTS) Guide/Pradeep Bonde - ANTS Guide-Part 9_deepgram.md|Part 9]]
- [[../../transcripts/08. Anticipation (ANTS) Guide/Pradeep Bonde - ANTS Guide-Part 10_deepgram.md|Part 10]]
- [[../../transcripts/08. Anticipation (ANTS) Guide/Pradeep Bonde - ANTS Guide-Part 11_deepgram.md|Part 11]]
- [[../../transcripts/08. Anticipation (ANTS) Guide/Pradeep Bonde - ANTS Guide-Part 12_deepgram.md|Part 12]]

## Summary

Anticipation (ANTS) is a **momentum-pause entry strategy** that seeks to buy stocks *before* the formal breakout occurs, achieving tighter stops (often under 2.5%, ideally ~1%) and closer entries than waiting for a 4% or dollar breakout confirmation. It is not a standalone methodology—it requires prior mastery of the momentum-ranking frameworks (TI65, M20, MDT, DT) to identify the underlying universe of stocks that already have established momentum. The guide presents two versions: a labor-intensive "grunt work" approach (manual chart review of hundreds of stocks nightly) and a "smart" approach (scans that reduce the universe to 20–40 stocks in minutes). Pradeep’s personal edge comes from running scans at **3:30 PM and entering at 3:58 PM** on the same day, front-running the majority of traders who do their anticipation work at night.

| Part | Theme | Key Question Answered |
|------|-------|----------------------|
| 1 | Building the Watch List | How do you manually review every momentum stock to find setups? |
| 2 | Filtering for Quality | How do you remove weak setups and avoid long sideways traps? |
| 3 | Entry Execution | How do you enter before the breakout—active monitoring vs. BSLO? |
| 4 | Trade Management | Why do so many anticipation setups fail, and how do you protect profits? |
| 5 | Market Condition Filter | When should you trade anticipation vs. when must you stop? |
| 6 | Leg Count Rule | Why first-leg and second-leg setups work; why third+ legs fail |
| 7 | Method Recap & Advanced Preview | Summary of grunt-work approach; preview of smarter methods |
| 8 | Smart Scan — Tight Day Filter | How to use a ±1% (or ±0.5%) daily-move scan to reduce effort |
| 9 | Smart Scan — Tight Days in a Row | How to use 2T/3T (two/three tight days) to find explosive compression |
| 10 | Pradeep’s Personal Edge | The 3:30 PM scan / 3:58 PM entry tactic to front-run night traders |
| 11 | Stringent Visual Criteria | Detailed checklist for ideal anticipation chart patterns |
| 12 | Position Trading Variant | Using weekly charts and MDT/MDT25/MDT50 for multi-month holds |

---

## 1. Core Philosophy: Momentum Pause

> "In order to understand this, what you need to do is you need to first understand the guide section in which we talked about TI65, we talked about MDT, we talked about DT, all those kind of, or M20, all those kind of momentum based methodology to rank stocks or to determine whether stock has a momentum." — Part 1

Anticipation is **not** about predicting breakouts in random stocks. It is about finding stocks that:
1. **Already have proven momentum** (via M20, TI65, MDT, or DT)
2. **Have paused** in a tight, orderly consolidation or minor pullback
3. **Are likely to resume** the trend with the next range-expansion move

The core thesis: if you can identify the pause correctly and enter before the crowd, your stop is tighter and your risk/reward is superior to a formal breakout entry.

---

## 2. The Grunt-Work Approach (Parts 1–3)

### 2.1 Step 1: Build the Universe (Part 1)
Every evening after market close, run your momentum scans (M20, TI65, MDT, DT). In a bear market this might be 80 stocks; in a strong bull market it can be 800–1,500 stocks. Go through **every chart manually** and flag stocks that are:
- Holding up well after a momentum move
- Showing sideways consolidation or minor pullback
- Setting up for a possible breakout

Create an "Anticipation" watchlist in TC2000 (or your platform) and copy all flagged tickers into it.

### 2.2 Step 2: Filter for Quality (Part 2)
Go through the watchlist with a "fine-tooth comb" and **remove setups that look attractive but have high failure probability**:

| Remove | Keep |
|--------|------|
| Stocks with recent 4%+ breakdown days (distribution) | Stocks with orderly pullback after aggressive buying |
| Choppy, long sideways moves without momentum | First or second leg after clear breakout |
| High volume during selling | High volume during first leg, low volume during consolidation |
| Extended third/fourth/fifth legs | Stocks where the momentum pause is recent and shallow |
| Dull, low-volatility drift | Tight, compressing price action |

> "Whenever you see a stock which is going sideways for a long period of time, it looks very attractive. But, these are the stocks where you're going to have highest failure in anticipation. Because, whenever a stock goes sideways for such a long period of time, the momentum is not there." — Part 2

### 2.3 Step 3: Entry Execution (Part 3)
Once filtered to 3–5 high-quality ideas, execute in one of two ways:

**Method A — Active Morning Monitoring (Aggressive, Recommended)**
- Load the 3–5 stocks into your brokerage platform before market open
- Watch them like a hawk in the first 10–15 minutes
- Enter on any 1%+ positive move (range expansion to the upside)
- Immediately place a stop below the consolidation low

**Method B — Buy Stop Limit Order (BSLO)**
- Calculate your trigger (e.g., yesterday’s close + 1%)
- Set a BSLO: trigger activates the order; a limit cap prevents filling on a violent gap-up
- Example: stock at $26.00 → trigger at $26.25, limit at $26.50, stop at $25.80
- Place before market open; if the stock hits $26.25, you’re in automatically

> "If you wait for a stock to breakout like this 4% or $1 and then buy, you wasted all your effort because then why did you create this watch list?" — Part 3

---

## 3. Trade Management: Why Anticipation Fails (Part 4)

Anticipation setups have a **higher failure rate than formal breakouts** for a structural reason: there is no volume confirmation at entry. You are buying on the *hope* that follow-through buying will arrive.

### 3.1 The Crowded-Trade Problem
Because momentum trading is widely taught, many traders build similar watchlists. When a stock breaks out in the first 20 minutes:
- Anticipation traders enter early
- Breakout traders enter on the move
- Newsletter followers pile in
If genuine institutional follow-through does **not** arrive, the stock fades and gives back the morning spike.

> "Every single trader you know of, name a good trader and their trading anticipation set up. And many of these traders have a lot more followers. So they are sending out watch list. They are sending out newsletter with the same set of stock." — Part 4

### 3.2 The Golden Rule: Move Stop to Breakeven Fast
- If the stock moves 4–5% in the first 30 minutes, move your stop to **protect profit** (not just breakeven)
- If the setup works and follow-through arrives, manage it like a normal 3–5 day momentum burst (see [[03. Bullish Momentum Burst Guide/Bullish Momentum Burst Guide-Section 4|Momentum Burst Guide — Trade Management]])
- If it fails, your breakeven stop ensures you lose nothing

> "The first thing which you need to do once you are in this kind of a setup and it starts going up, is to try and move your stop to at least to break even. And if it makes four to 5% move immediately in the first half an hour, to at least move your stop to protect some of the profit." — Part 4

---

## 4. The Single Most Important Filter: Market Condition (Part 5)

> "The only time you should be trading anticipation setup is when the market is in a very confirmed and in a very wild bullish conditions. If you trade this setup in a choppy market conditions, you are going to have setups after setups trying to have a minor breakout and failing and you are going to get frustrated. You will have death by thousand cuts." — Part 5

| Market Condition | Action |
|-----------------|--------|
| **Confirmed bull** (Market Monitor green; 25%+ stocks > 25%− stocks) | Trade anticipation aggressively |
| **Choppy / uncertain** | Stop trading anticipation; expect false breakouts |
| **Bearish** | Do not trade anticipation; guaranteed losses on failed breakouts |

Pradeep is explicit: this one filter alone will **dramatically improve win rate**. Anticipation requires a continuous inflow of new buyers. Only a confirmed bull market provides that.

---

## 5. The Leg-Count Rule (Part 6)

Not all momentum pauses are equal. The highest-probability anticipation setups form after the **first leg** of a move. Second-leg setups are still viable. Third+ leg setups fail increasingly often.

| Leg | Probability | Rationale |
|-----|------------|-----------|
| **First leg** | Highest | Fresh momentum, early adopters still accumulating |
| **Second leg** | Good | Momentum confirmed, but not yet over-owned |
| **Third+ leg** | Declining | "Who is left to buy?" — exhausted move |

> "Ask yourself a question: Who is left to buy that particular stock? And that is where you're gonna get high failure rates." — Part 6

This is why early momentum identification (via TI65, M20) is critical: the sooner you catch a stock in its momentum cycle, the better your anticipation entries will perform.

---

## 6. The Smart Approach: Scans (Parts 8–9)

Instead of manually reviewing 1,500 charts nightly, use scans to pre-filter the universe.

### 6.1 Scan 1: Tight Day Filter (Part 8)
Build a scan with:
1. Liquidity condition (standard)
2. Price > $10
3. TI65 > 1.05 (or M20, MDT, DT condition)
4. **Price % change today between −1% and +1%** (or −0.5% to +0.5% for more restrictive)

Result: in a bear market, 415 TI65 stocks → 32 stocks with ±0.5% move. In a bull market, 1,800+ stocks → ~100 stocks. Review time drops from 2–3 hours to **10 minutes**.

> "If you look at every stock, which meets TI 65 bullish criteria, you'll be looking at 415 stocks versus if you use the smart approach, you're only looking at stocks which are going to be anticipations smart. Only 32 stocks." — Part 8

### 6.2 Scan 2: Tight Days in a Row (Part 9)
Further tighten by requiring **multiple consecutive tight days**:
- Change the daily-move filter to **"X bars in a row"**
- Set 3 bars in a row with price % change between −1% and +1% → "3T" (three tight days)
- Or 2 bars in a row → "2T" (two tight days)

Result: 415 stocks → 19 stocks (3T). This finds the most compressed, explosive setups.

> "So, if you want to find like two tight days, all that you need to do is to change this particular condition to two tight days." — Part 9

### 6.3 Pradeep’s Personal Settings
For his own trading, Pradeep uses **±0.4%** as the daily-move threshold—far tighter than the ±1% or ±2% examples given for beginners. This finds only the most explosive, lowest-risk compressions.

---

## 7. Pradeep’s Personal Edge: The 3:30 PM Tactic (Part 10)

This is the **advanced technique** that gives Pradeep an edge over traders who do anticipation work at night.

| Step | Time | Action |
|------|------|--------|
| 1 | 3:30 PM | Run the anticipation smart scan during market hours |
| 2 | 3:30–3:55 PM | Review the 20–30 stocks, identify 1–2 best setups |
| 3 | 3:58 PM | Enter the setup in anticipation of next-day breakout |
| 4 | Next morning | If it breaks out, stop is already in; move to breakeven quickly |

**Why this works:**
- All other anticipation traders do their work at night and place BSLO orders for the next morning
- By entering at 3:58 PM, Pradeep is **already in the stock** before they even start their analysis
- If the stock gaps up and breaks out at the open, he captures the full move while others are scrambling to enter

**Risk:** The stock can gap down overnight. Pradeep accepts this risk because in a confirmed bull market, well-setup stocks rarely gap down dramatically.

> "There is a generic age in the stock market of being first. If you can enter any move before other people enter you are always going to be in a better position." — Part 10

---

## 8. Stringent Visual Criteria for Ideal Setups (Part 11)

When reviewing charts, Pradeep applies a strict checklist:

### 8.1 Price and Volatility
- **Higher-price stocks preferred** ($10+; ideally $30–$300): tighter absolute-dollar stops
- **Daily move ≤ 0.4%** (±0.4% filter): extreme compression
- **Stop target: ~1% or less** on ideal setups

### 8.2 First Leg Characteristics
- **Unidirectional candles**: clear one-directional buying, candles closing near the high
- **No gap-up heavy legs**: continuous buying preferred over gap-and-go
- **Aggressive volume on the leg**: high volume during the up-move

### 8.3 Consolidation Characteristics
- **Volatility compression**: consolidation candles must be **smaller-bodied** than first-leg candles
- **Body of candle matters, not wicks**: ignore wick fascination; focus on body compression
- **Direction of consolidation**: slightly down or flat (not rising—rising wedge is not anticipation)
- **Duration**: 3–4 days ideal; < 7 days best; > 10–12 days = not a momentum pause, just stalemate
- **Volume dries up** during consolidation: lower volume than first leg

### 8.4 Momentum Strength
- Prioritize stocks with **highest TI65** (or highest momentum rank): more aggressive buying = better follow-through
- Avoid gap-up consolidations: less reliable than continuous-up consolidations

> "I want the body of the candles to be smaller, during this consolidation. I want the volatility to decrease in the direction of the breakout." — Part 11

---

## 9. Position Trading Variant: Weekly Charts (Part 12)

Anticipation is not limited to 3–5 day swing trades. It can also find **multi-month position trades** using longer-term momentum and weekly charts.

### 9.1 Methodology
1. Use **MDT, MDT25, or MDT50** (or DT) to build the momentum universe
2. Switch to **weekly charts**
3. Look for stocks that have:
   - Established a clear first leg
   - Formed a **4–10 week (or longer) sideways consolidation**
   - Volume drying up during the consolidation
4. Verify on the **daily chart** that the setup is also valid on the shorter timeframe
5. Create a watchlist with price alerts; wait for the breakout

### 9.2 Key Differences from Swing Trading

| Aspect | Swing ANTS | Position ANTS |
|--------|-----------|---------------|
| Timeframe | Daily | Weekly |
| Consolidation | 3–7 days | 4–10+ weeks |
| Hold duration | 3–5 days | 2–4+ months |
| Momentum tool | TI65, M20 | MDT, MDT25, MDT50, DT |
| Entry style | 3:58 PM or BSLO | Formal breakout with volume |
| Goal | 8–20% move | 40–100%+ move |

> "If you are using DT or MDT underlying assumption is that you are using it to find longer term hold positions because if it is a base of two to three months or four months then you are going to be holding it for three to four months." — Part 12

---

## 10. Common Pitfalls and How to Avoid Them

| Pitfall | Why It Happens | Fix |
|---------|--------------|-----|
| **Trading in wrong market** | FOMO; desire to trade every day | Only trade when Market Monitor is green |
| **Buying extended third+ legs** | Momentum scans show strong stocks late in cycle | Always ask: "Who is left to buy?" |
| **Long sideways traps** | Looks "ready" but lacks momentum | Remove if consolidation > 12 days or choppy |
| **Low-price stocks with wide stops** | Penny stocks have high volatility | Focus on $10+ stocks; adjust filters for sub-$10 |
| **Buyouts showing in scans** | Acquired stocks go sideways forever | Mark with "XXX"; skip all buyouts |
| **Not moving stop to breakeven** | Hope that breakout will continue | Move stop aggressively in first 30 min |
| **Entering on gap-up days** | BSLO triggers on gap-up, bad fill | Use limit cap on BSLO; monitor gap risk |

---

## Key Takeaways

1. **Anticipation is a momentum-pause strategy, not a standalone system.** Master TI65, M20, MDT, and DT first.
2. **Confirmed bull market only.** This one filter eliminates most anticipation losses.
3. **First and second leg only.** Third+ leg setups fail because the buying pool is exhausted.
4. **Two paths:** grunt-work (manual review, 2–3 hours) or smart (scans, 10–20 minutes).
5. **Pradeep’s edge:** 3:30 PM scan, 3:58 PM entry. Front-run the night traders.
6. **Tight consolidation = 3–7 days, ±0.4% daily move, volatility compressing, volume drying up.**
7. **Move stop to breakeven fast.** Anticipation setups fade quickly if genuine buying doesn't follow.
8. **Position-trading variant:** Weekly charts + MDT/MDT25 for multi-month holds.

---

## Cross-References

- [[01. How to Get Started/01. How to Get Started In Trading Guide-Part 1|How to Get Started — Market Monitor]] — confirmed bull market definition
- [[04. TI65 Guide/TI65 Guide|TI65 Guide]] — `AVGC7/AVGC65`, bullish threshold ≥ 1.05
- [[05. M20 Guide/M20 Guide|M20 Guide]] — anchored 20% or $20 from 30-day extreme
- [[06. DT Guide/DT Guide|DT Guide]] — Darvas box momentum (`C / AVGC126` variant)
- [[07. MDT Guide/MDT Guide|MDT Guide]] — absolute momentum ranking, MDT25/MDT50 variants
- [[03. Bullish Momentum Burst Guide/Bullish Momentum Burst Guide-Section 4|BMB Section 4]] — first 30-min entry and stop progression
- [[03. Bullish Momentum Burst Guide/Bullish Momentum Burst Guide-Section 5|BMB Section 5]] — 4% breakout scan setup (used as formal breakout alternative)

---

## Key Quotes

> "In order to understand this, what you need to do is you need to first understand the guide section in which we talked about TI65, we talked about MDT, we talked about DT, all those kind of, or M20, all those kind of momentum based methodology to rank stocks." — Part 1

> "Whenever you see a stock which is going sideways for a long period of time, it looks very attractive. But, these are the stocks where you're going to have highest failure in anticipation." — Part 2

> "If you wait for a stock to breakout like this 4% or $1 and then buy, you wasted all your effort because then why did you create this watch list?" — Part 3

> "A lot of anticipation fail compared to breakouts. Because in anticipation setup, when you're using a BSL order or you're entering in anticipation, there is no volume confirmation." — Part 4

> "The only time you should be trading anticipation setup is when the market is in a very confirmed and in a very wild bullish conditions." — Part 5

> "Ask yourself a question: Who is left to buy that particular stock? And that is where you're gonna get high failure rates." — Part 6

> "If you look at every stock, which meets TI 65 bullish criteria, you'll be looking at 415 stocks versus if you use the smart approach, you're only looking at stocks which are going to be anticipations smart. Only 32 stocks." — Part 8

> "There is a generic age in the stock market of being first. If you can enter any move before other people enter you are always going to be in a better position." — Part 10

> "I want the body of the candles to be smaller, during this consolidation. I want the volatility to decrease in the direction of the breakout." — Part 11

> "If you are using DT or MDT underlying assumption is that you are using it to find longer term hold positions because if it is a base of two to three months or four months then you are going to be holding it for three to four months." — Part 12
