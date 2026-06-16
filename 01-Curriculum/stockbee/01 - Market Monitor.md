---
title: "Lesson 1: Market Monitor — The Traffic Light"
date: 2026-06-04
tags: [class, lesson-01, market-monitor, breadth, timing, process]
---

# Lesson 1: Market Monitor — The Traffic Light

> **Core Question:** *When* do I trade, and in *which direction*?
> **Answer:** Breadth tells you the regime. Green = trade long. Red = trade short. Choppy = reduce size or sit out.

---

## The Core Idea

The market is not random. The number of stocks participating in a move — called **breadth** — tells you whether breakouts will work or fail.

Think of it as a traffic light:

| Signal | Primary Indicator | What It Means | What You Do |
|--------|-------------------|---------------|-------------|
| 🟢 **Green** | Stocks up 25% in 65 days > Stocks down 25% | Bull market. Breakouts work. | Trade long — full size on A+ setups |
| 🔴 **Red** | Stocks down 25% > Stocks up 25% | Bear market. Breakouts fail. | Trade short — WSS, DEP short broken business |
| 🟡 **Choppy** | Green but low counts (breakouts < 200) | Transition. Breakouts fail often. | Only ANTS in confirmed bullish; reduce size |

---

## The Primary Indicator

The **primary indicator** is a **net number** — the difference between stocks up 25%+ and stocks down 25%+ over 65 trading days (roughly one quarter):

```
Primary Reading = (Stocks up 25%+ in 65 days) − (Stocks down 25%+ in 65 days)
```

**Example (2026-06-02 StockBee data):**
- Primary Up = 1,582
- Primary Down = 902
- **Net = 1,582 − 902 = 680** → Strong bull (above 400 threshold)

Both raw counts (1582 and 902) are tracked separately in the spreadsheet, but the **net** is what you use for the traffic light classification.

**When net > 0** → green (more stocks up than down = bullish).
**When net < 0** → red (more stocks down than up = bearish).

### Key Readings

| Net Reading | Interpretation                                   | Action                                     |
| ----------- | ------------------------------------------------ | ------------------------------------------ |
| **> 400**   | Strong bull — most breakouts work                | Full size; all long setups                 |
| **200–400** | Normal bull — trade breakouts with standard size | Standard DEP, SOS, ANTS                    |
| **0–200**   | Weak bull / transition — breakouts start failing | Reduce size; only A+ setups                |
| **< 0**     | Bear market — more stocks down than up           | Trade shorts; prepare for reversal         |
| **< −200**  | Severe bear / capitulation                       | Generational buying opportunity; reversals |

## The T2108 Indicator

T2108 = percentage of stocks trading **above their 40-day simple moving average**. It measures the **breadth of participation** in the current trend.

### T2108 Alone — What It Tells You

| Reading           | Standalone Meaning                            | Action                      |
| ----------------- | --------------------------------------------- | --------------------------- |
| **> 90%**         | Start of a new bull market (NOT a top signal) | Size up on longs            |
| **70–90%**        | Healthy bull market                           | Standard long trading       |
| **40–70%**        | Neutral / mixed                               | Be selective; check primary |
| **< 20%**         | Capitation — extremely bullish (bottoming)    | Prepare for reversal longs  |
| **Single digits** | Generational buying opportunity               | Deploy long-term capital    |

### ⚠️ T2108 Is Most Powerful When Combined With Primary

T2108 is a **shorter-term** momentum indicator (40-day) that can mislead in the middle range. The **primary indicator** is a **longer-term** structural signal (65-day). Always cross-check:

| Signal                  | T2108         | Primary | Meaning                                       |
| ----------------------- | ------------- | ------- | --------------------------------------------- |
| **Generational bottom** | Single digits | < −200  | Both at extremes → maximum buy signal         |
| **New bull confirmed**  | > 90%         | > 200   | Full-bull trading; size up                    |
| **Bull pullback**       | 30–50%        | > 200   | Buy the dip — structure is still bullish      |
| **Bear bounce**         | 70–80%        | < 0     | Do NOT trust it — still a bear market bounce  |
| **Capitulation**        | < 20%         | < −200  | Prepare for reversal longs                    |
| **Overbought?**         | > 90%         | > 400   | NOT a top — bull is strong; keep trading long |
| **Bull fatigue**        | 40–70%        | 200–400 | Mixed signal; reduce size; be selective       |

**Key insight:** T2108 above 90% does NOT mean "overbought, time to sell." It means **a new bull has started** — this is when you want to be most aggressive on the long side.

> *"It's not that T2108 goes above 90 and then the market has topped. No. That tells you that there has been just a start of a new bull market."*

**Where T2108 alone fails:**
- If T2108 = 85% but primary is < 0 (bear), the 85% is just a bounce within a bear market — not a reliable buy signal
- If T2108 = 30% but primary is > 200 (bull), the 30% is just a pullback in a bull market — a buying opportunity
- **Always check primary first.** Primary = structural trend. T2108 = momentum within that trend.

## The Daily Numbers You Track

Every night, run these scans and record:

| Column            | What It Measures                      | How to Compute                              |
| ----------------- | ------------------------------------- | ------------------------------------------- |
| **Breakouts**     | Stocks up 4%+ today with 9M+ volume   | TC2000 scan / FMP screener                  |
| **Breakdowns**    | Stocks down 4%+ today with 9M+ volume | TC2000 scan / FMP screener                  |
| **Primary (65d)** | Stocks up 25% vs. down 25% in 65 days | TC2000: `C/C65 >= 1.25` and `C/C65 <= 0.75` |
| **Monthly (22d)** | Stocks up 50% vs. down 50% in 22 days | Short-term breadth                          |
| **T2108**         | % above 40-day MA                     | TC2000 built-in                             |
| **Universe**      | Total stocks in the market            | Watch for IPO surges                        |

### Additional Columns

| Column | Purpose |
|--------|---------|
| **Fibonacci (34d)** | 34-day window; earlier signal but more false positives |
| **5/10d ratios** | Short-term breadth momentum |
| **Turn days** | Abnormally high 4% counts (1,000+); often at market turns |

---

## Critical Asymmetry: Breadth Finds Bottoms, NOT Tops

⚠️ **This is the #1 mistake people make with Market Monitor.**

|            | Bottoms                                                 | Tops                                            |
| ---------- | ------------------------------------------------------- | ----------------------------------------------- |
| **Signal** | Primary < 200 + T2108 single digits = extremely bullish | No reliable top signal                          |
| **Works?** | ✅ Almost every major bottom                             | ❌ "Excessive bullishness can persist for years" |
| **Why**    | Forced selling exhausts itself                          | Greed has no natural limit                      |

> *"Whenever the reading goes below 200, that's extremely bullish... that tells you that there is a capitulation kind of selling."*

**Do NOT use Market Monitor to call tops.** You will get out too early and miss the rest of the move.

> *"Excessive bearishness is bullish. Excessive bullishness is NOT bearish."*

---

## Post-COVID Caveat

After COVID, retail traders created persistent high breadth readings that didn't lead to pullbacks. The monthly 50% > 20 predictor no longer works reliably. Monitor it, but don't trade it blindly until the retail-driven regime changes.

Also: when the total number of stocks jumps dramatically (e.g., 5,000 → 7,000 in 2021), an IPO surge signals a **duration bear market** (18–24 months) follows. Every historical instance confirms this.

---

## The Weekend Process

| Task | Duration | Tool |
|------|----------|------|
| Run Market Monitor scans | 10 min | TC2000 or FMP nightly runner |
| Update spreadsheet | 5 min | Manual entry (edge: the process itself) |
| Review primary indicator | 2 min | Green/red/yellow classification |
| Check T2108 | 1 min | Built-in TC2000 |
| Note turn days (1,000+ breakouts) | 1 min | Flag in notes |

> *"The manual process is part of the edge."* — The discipline of running scans nightly and entering data is itself a process commitment.

---

## What Market Monitor Gates

```
Market Monitor GREEN  →  Trade breakouts (SOS, DEP, ANTS, EP)
                        →  Full size on A+ setups
                        →  Sugar Babies long

Market Monitor RED     →  Trade shorts (WSS, DEP short broken business)
                        →  Sector-focused shorts in weak sectors
                        →  Reversals bullish only at capitulation

Market Monitor YELLOW →  Only ANTS in confirmed bullish
                        →  Reduce position size 50%
                        →  "Death by thousand cuts" if you trade breakouts
```

---

## Key Rules Summary

| # | Rule | Source |
|---|------|--------|
| 1 | Primary < 200 = generational buying opportunity | [[Market Monitor]] |
| 2 | T2108 single digits = capitulation bottom | [[Market Monitor]] |
| 3 | Excessive bearishness = bullish; excessive bullishness ≠ bearish | [[Market Monitor]] |
| 4 | Only trade breakouts when primary is green | [[Market Monitor]] |
| 5 | Only trade shorts when primary is red | [[Market Monitor]] |
| 6 | In choppy markets, only ANTS in confirmed bullish | [[Market Monitor]] |
| 7 | 1,000+ breakout day = turn day; often at market bottoms | [[Market Monitor]] |
| 8 | IPO surge in total universe = duration bear market coming | [[Market Monitor]] |
| 9 | Don't use Market Monitor to call tops | [[Market Monitor]] |
| 10 | Primary green = most breakouts work; fight that at your peril | [[Market Monitor]] |

---

## Homework

1. **Understand the primary indicator formula:** Stocks up 25% in 65 days vs. stocks down 25% in 65 days. Calculate it for today's market using TC2000 or your screener.
2. **Check T2108** today and classify the market: green, red, or yellow.
3. **Read the full guide:** [[11. Market Monitor Guide]] — all 8 parts for the complete breadth methodology.

---

## Next Lesson

→ [[02 - The 4% Breakout]] — What pattern starts every explosive move?

---

## Cross-References

- **KB Notes:** [[Market Monitor]], [[Mentality]], [[Common Mistakes]]
- **Curated Guides:** [[11. Market Monitor Guide]], [[12. Situational Awareness Guide]], [[21. Process Guide]]
- **Transcripts:** `transcripts/11. Market Monitor Guide/`
