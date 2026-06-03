---
title: DT Guide — Double Trouble (Darvas-Style Momentum Scan)
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
  - darvas-box
  - continuation-setup
  - breakout
  - anticipation
  - scan-setup
  - TC2000
  - combo-list
  - bucket-zero
  - position-trading
  - pradeep-bonde
  - stockbee
---

# DT Guide — Double Trouble (Darvas-Style Momentum Scan)

> **Double Trouble (DT)** is a momentum scan inspired by Nicolas Darvas's box theory: find stocks that have risen at least **80% from their 52-week low**, then look for a consolidation "box" near the high. When the stock breaks out of the box, you buy. If it breaks below the box, it's in trouble — hence the name.
>
> **Important caveat:** Pradeep says "I don't use it anymore" but created it after reading Darvas's book. It is best suited for **position trading and longer-term holding**, not swing trading.

---

## Series Overview

| Part | Theme | Key Question Answered |
|---|---|---|
| **Part 1** | What Is Double Trouble? | Darvas's original concept, the 80%/box theory, why "trouble" |
| **Part 2** | Chart Setup | Adding DT indicator as area plot in TC2000 |
| **Part 3** | Building the Scan | Combo list, DT column, liquidity filters, ranking |
| **Part 4** | Who Is This For? | Darvas's full criteria, bucket zero, the funnel from 351→3–5 |

---

### 1. What Is Double Trouble?

**Double Trouble** is a momentum method based on Nicolas Darvas's observation from his book *How I Made $2,000,000 In The Stock Market*:

> Darvas would look through Barron's tables at the 52-week high and 52-week low columns. He was looking for a stock whose 52-week high was **double** the 52-week low. That told him the stock had something in it intrinsically — and had the potential to double again.

Pradeep formalizes this insight into a quantitative scan. The threshold is **1.8x** (not 2.0x) because Darvas was willing to accept stocks within 20% of the doubling point — they didn't have to have literally doubled yet.

| Attribute | Value |
|---|---|
| **Core condition** | Price is at least **1.8x** the 52-week low (i.e., up 80%+) |
| **TC2000 formula** | `C / MINL252 >= 1.8` |
| **Why 1.8, not 2.0?** | Darvas accepted stocks within 20% of the doubling; room for the "box" |
| **Core insight** | Stocks that have already moved significantly from their lows have **proven institutional interest** |
| **Best used for** | Position trading, longer-term holds (NOT swing trading) |
| **Name meaning** | After doubling, the stock either **doubles again** or **gets into trouble** |

> "Either it is going to double, or it is going to get into trouble. That is why the name double trouble came in."

---

### 2. The Darvas Box — The Core Concept

The entire DT methodology revolves around what Darvas called the **box**. This is the most important concept in the guide, and it's what differentiates DT from a simple momentum scan.

#### What Is a Box?

After a stock doubles from its 52-week low, it doesn't go straight up forever. It **consolidates** near the high for days or weeks. This consolidation range is the "box."

```
Stock doubles from low → Forms a box (consolidation) → Breaks out of box → Next leg up
```

**Real examples from the transcript:**

| Stock | What Happened |
|---|---|
| **Rhythm (RTHM)** | Stock doubled, then showed on DT indicator. Formed a box, broke out, made a move. |
| **TRVI** | Doubled from low, formed a Darvas box. When it broke out of the box, Darvas would buy. |
| **Revlon** | Doubled, formed a box, then the stock went up from the box breakout. |
| **TH** | Near all-time high, forming a good Darvas box — ideal candidate |
| **TMNTX** | Forming a box, another candidate meeting Darvas criteria |

#### Darvas's Buy and Sell Rules

| Action | Rule |
|---|---|
| **Buy stop** | Place a **buy stop order 20¢–50¢ above the high of the box** (e.g., box high $15.67 → buy stop at $15.87–$15.92; box high $314.90 → buy stop at $315.40) |
| **Stop loss** | Place at the **low of the box** |
| **If stock breaks below box** | "It is no more a good stock and it is going to get into trouble" — exit |
| **If stock breaks above box** | Hold for the next leg — it may double or triple from there |

> "Darvas would put a buy stop limit order at 20¢ or 25¢ above this particular high point. If the order was executed, his stop used to be at the low of the box. His theory was that if the stock comes back and breaches the low of this box, then it is no more a good stock and it is going to get into trouble."

---

### 3. The Full Darvas Criteria — Not Just Doubling

This is where most people misunderstand DT. Darvas didn't just look for stocks that doubled. He had **four additional criteria** that most traders skip:

| # | Criterion | Why It Matters |
|---|---|---|
| **1** | **Near all-time high** | The stock must be making new highs, not just recovering from a crash |
| **2** | **Infant industry** | New, rapidly growing sector (rocket fuel in the 1950s, contraceptives when new, biotech today) |
| **3** | **Low capitalization** | Small-cap stocks have more room to multiply |
| **4** | **Rapid sales/earnings growth** | The fundamental catalyst driving the move |
| **5** | **Forming a box** | Must be consolidating near the high, not just running |

> "He was not looking for any stock which doesn't have a catalyst. He was looking for a lot of things beside just the box."

**Real examples of what Darvas would SKIP:**

| Stock | Why Skip |
|---|---|
| **Utility stocks (AMPS)** | Not an infant industry |
| **Oil & gas (High Peak Energy)** | Not an infant industry, been around for decades |
| **Shipping stocks (ASC)** | Not an infant industry, not near all-time high |
| **Any stock not making all-time high** | Darvas only traded stocks breaking into new high ground |

> "If you go through these 48 stocks which are meeting the definition of Darvas, you're going to find only probably four or five stocks. And that is what Darvas was doing, and that is why he was very selective."

---

### 4. Building the DT Scan (TC2000)

#### Step 1: Create a Combo List

| Setting | Value |
|---|---|
| **Name** | DT (Double Trouble) |
| **Universe** | US stocks + ADRs |
| **Liquidity** | `MINV3.1 >= 100,000` (100K shares/day last 3 days) |
| **Price** | `C >= 3` (eliminate penny stocks) |
| **Core condition** | `C / MINL252 >= 1.8` |

Result: approximately **351 stocks** at any given time with standard liquidity.

#### Step 2: Add the DT Column for Ranking

| Column Name | Formula | Purpose |
|---|---|---|
| `DT` | `C / MINL252` | Shows how much the stock has risen from 52w low |

Sort by DT to find:
- **Descending** → stocks that have run the most (strongest)
- **Ascending** → stocks that have just crossed 1.8 (youngest momentum)

**Example:** A stock trading at $26 with a 52w low of $0.09 has a DT value of ~289 (extreme). A stock just crossing 1.8 has only risen 80%.

> "The higher the value, the bigger the move. But you also find stocks like this one which has made a 697% move from its 52-week low."

**Buyout warning:** Many extreme DT values are buyouts or acquisitions. Always visually verify.

> "All of these stocks were, like, kind of, basically some sort of a buyout or things like that."

---

### 5. The Recommended Approach: Run on Bucket Zero

Instead of running DT on all US stocks, Pradeep recommends running it on **Bucket Zero** stocks only.

Bucket Zero is a pre-filtered universe with:
- **IPO'd in the last 10 years** (young stocks — Darvas's "infant industry")
- **Back-to-back quarters of 39%+ sales growth** (the fundamental catalyst)
- **Market capitalization under $10 billion** (low cap — more room to grow)

> "Instead of running this scan on a universe of stock, what you can do is you should run this scan on bucket zero. Bucket zero is a set of stocks which have two quarters back-to-back of sales growth of 39% plus, and they've IPO'd in the last ten years, which is what Darvas was looking for."

By running DT on Bucket Zero, you automatically satisfy 3 of Darvas's 5 criteria (infant industry, low cap, sales growth). Then you only need to check:
- Is the stock near all-time high?
- Is it forming a good box?

This narrows 351 stocks → **3–5 candidates**.

---

### 6. Chart Setup (TC2000)

To visualize DT on a chart:

1. **Left click chart** → Add Plot → Custom PCF True Indicator
2. **Formula:** `C / MINL252 >= 1.8`
3. **Style:** Area
4. **Color:** Dark color (to distinguish from other indicators)
5. **Name:** `DT`

When the indicator shows, it highlights the exact date the stock crossed 80% above its 52-week low. From that point on, you look for the Darvas box formation.

> "As soon as the stock goes up 80% from the 52-week low, you will see the stock showing up on your chart."

---

### 7. The 351 → 3–5 Funnel

The power of DT combined with Darvas's criteria:

| Step | Filter | Stocks Remaining |
|---|---|---|
| 1 | DT scan (C/MINL252 >= 1.8 + liquidity) | ~351 |
| 2 | Run on Bucket Zero instead of all US stocks | ~48 |
| 3 | Near all-time high? | ~10–15 |
| 4 | Forming a good Darvas box? | ~3–5 |
| 5 | Infant industry + sales growth catalyst? | **2–4** |

> "Only stocks which are near all-time high is what he was looking for. If you use that logic, you're going to find very few stocks."

> "In fact, the only stocks which you would be interested in is these three stocks — out of which you have to look at which one is forming a good box."

---

### 8. Market Phase Dependency

Darvas explicitly stated his method works in **rising markets**:

> "Darvas was very clearly saying that Darvas's method works in rising market. He was using his double trouble kind of a scan in situational awareness where the market was bullish."

| Market Phase | DT Effectiveness |
|---|---|
| **Bullish / Rising** | Best — many stocks doubling from lows, forming boxes |
| **Recovery from correction** | Good — beaten-down stocks turning up |
| **Bearish / Downtrend** | Poor — stocks form boxes but break down instead of up |
| **Choppy / Sideways** | Mixed — fewer reliable setups |

---

### 9. Who Is This For?

> "This whole double trouble methodology is more suitable, not really for people who want to do swing trading. This is more suitable for people who want to do longer term holding or who are looking for position trading on stocks which have doubled, then they form a nice base, they also have some catalyst, and then from there, when they break out, they might make multi-month moves."

> "I don't use it anymore, but I created this whole thing once I read the Darvas's method."

| Trader Type | Recommended Use |
|---|---|
| **Position trader** | Best fit — hold for multi-month moves, buy box breakouts |
| **Investor** | Good fit — use DT to find catalyst-driven stocks with momentum |
| **Swing trader** | Less ideal — DT setups can take weeks to develop |
| **Day trader** | Not recommended — time horizon mismatch |

---

### 10. Key Principles

#### Principle 1: "Doubled from Low" = Trend Confirmation
A stock that has doubled from its 52-week low has survived selling pressure, built a base, and attracted buyers. It is no longer a "hope" stock.

#### Principle 2: The Box Is Everything
Finding a stock that doubled is only step 1. The box (consolidation near the high) is where the real trade is. No box = no trade.

#### Principle 3: Buy Above the Box, Stop Below the Box
- Buy stop: 25¢–50¢ above the high of the box
- Stop loss: at the low of the box
- If the stock breaks below the box, it's in trouble — exit

#### Principle 4: Catalyst Matters
Darvas didn't trade random doubles. He wanted **infant industries** with **rapid sales growth**. The fundamental catalyst gives the move staying power.

#### Principle 5: Selectivity Is Key
From 351 DT stocks → 48 on Bucket Zero → 3–5 meeting all Darvas criteria. The power is in the filtering, not the scan.

#### Principle 6: Rising Markets Only
DT works best in bull markets. In bear markets, boxes break down instead of up.

---

### 11. Scan Formula Summary (TC2000)

| Purpose | Formula |
|---|---|
| **DT core scan** | `C / MINL252 >= 1.8` |
| **DT value column** | `C / MINL252` |
| **Liquidity filter** | `MINV3.1 >= 100000` |
| **Price filter** | `C >= 3` |
| **Chart indicator** | `C / MINL252 >= 1.8` (area, dark color) |

**Recommended:** Run DT on **Bucket Zero** (IPO'd last 10 years + 39%+ sales growth + market cap < $10B) instead of all US stocks.

---

### 12. Relationship to Other Guides

| Guide | Relationship |
|---|---|
| [[../../04. TI65 Guide/TI65 Guide|TI65]] | Use the DT list as the **base universe** for TI65 anticipation scans — DT confirms the stock has proven strength; TI65 confirms the trend velocity |
| [[../../05. M20 Guide/M20 Guide|M20]] | M20 catches stocks **turning** from bottoms; DT confirms they have **already doubled** from those bottoms |
| [[../../03. Bullish Momentum Burst Guide/Bullish Momentum Burst Guide-Section 1|BMB Section 1]] | DT stocks that form a box and break out are classic momentum burst setups — the box is the consolidation, the breakout is the burst |
| [[../../03. Bullish Momentum Burst Guide/Bullish Momentum Burst Guide-Section 2|BMB Section 2]] | A DT stock breaking out of its box with a 4% move and Two-Lynch setup is a high-probability trade |

---

### Key Takeaways

1. **DT finds stocks that have doubled from their 52-week low** — they have proven institutional interest
2. **The Darvas box is the core concept** — a stock doubles, consolidates near the high (the box), then breaks out
3. **Buy above the box, stop below the box** — 25¢ above the high for entry, low of the box for stop loss
4. **The name "Double Trouble"** — after doubling, either the stock doubles again or it gets into trouble
5. **Darvas had 5 criteria, not just 1** — near all-time high, infant industry, low cap, sales growth, AND a box
6. **Run DT on Bucket Zero** — automatically satisfies infant industry, low cap, and sales growth criteria
7. **The funnel goes from 351 → 3–5 stocks** — selectivity is the power
8. **Works best in rising markets** — Darvas explicitly stated this
9. **Position trading, not swing trading** — holds are multi-week to multi-month
10. **Pradeep doesn't use it anymore** — but it's in the toolkit for those who want Darvas-style position trading

---

## See Also

- [[../../KB/Scans and Filters|Scans and Filters]] — PCF formulas, combo lists, liquidity filters, FMP API mapping
- [[../../KB/Entries|Entries]] — all entry types compared: EP, DEP, SOS, ANT, Reversal, MB

---

### Cross-References

- [[../../transcripts/06. DT/Pradeep Bonde - DT Guide-Part 1_deepgram|Part 1 Transcript]]
- [[../../transcripts/06. DT/Pradeep Bonde - DT Guide-Part 2_deepgram|Part 2 Transcript]]
- [[../../transcripts/06. DT/Pradeep Bonde - DT Guide-Part 3_deepgram|Part 3 Transcript]]
- [[../../transcripts/06. DT/Pradeep Bonde - DT Guide-Part 4_deepgram|Part 4 Transcript]]
- [[../../04. TI65 Guide/TI65 Guide|TI65 Guide]]
- [[../../05. M20 Guide/M20 Guide|M20 Guide]]
- [[../../03. Bullish Momentum Burst Guide/Bullish Momentum Burst Guide-Section 1|BMB Section 1]]

---

### Key Quotes

> "Either it is going to double, or it is going to get into trouble. That is why the name double trouble came in."

> "He was not looking for any stock which doesn't have a catalyst. He was looking for a lot of things beside just the box."

> "If you go through these 48 stocks which are meeting the definition of Darvas, you're going to find only probably four or five stocks. And that is what Darvas was doing, and that is why he was very selective."

> "This whole double trouble methodology is more suitable for people who want to do longer term holding or who are looking for position trading."

> "I don't use it anymore, but I created this whole thing once I read the Darvas's method."

> "Darvas was very clearly saying that Darvas's method works in rising market."