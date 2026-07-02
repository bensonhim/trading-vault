# TC2000 Scan Formulas — StockBee Methodology

> **Date:** 2026-06-10
> **Purpose:** Replicate these scans in TC2000 to cross-validate our Python results
> **Source:** Pradeep Bonde's StockBee guides and M20 Guide

---

## 1. EP 9M (Episodic Pivots)

**What it finds:** Today's explosive movers (≥4% on ≥9M volume)

**TC2000 Formula:**
```
(changePercentage >= 4 OR changePercentage <= -4)
AND volume >= 9,000,000
AND price >= 3
```

**Notes:**
- Use FMP `biggest-gainers` + `biggest-losers` endpoints (our implementation)
- Sort by volume descending, then change descending
- Top 20 candidates max
- Entry: First 10-15 minutes if opens positive, stop 8-20%

---

## 2. SOS (Start of a Swing)

**What it finds:** First day of a new swing — range expansion breakout

**TC2000 Formula:**
```
C / C1 >= 1.04
AND V >= 9,000,000
AND price >= 3
```

**Notes:**
- `C1` = previous day close
- Volume must be above 9M (not just 9M on SOS day)
- For high-priced stocks ($60+): use $ breakout: `C - O >= 0.90 AND V >= 100,000`
- Entry: Buy immediately, stop at day low or breakeven
- Not every SOS is tradable — qualification is the skill

---

## 3. DEP (Delayed Reaction EP)

**What it finds:** Stocks that had an EP within last 25 days, now pulling back — first valid setup after catalyst

**TC2000 Formula:**
```
C / C1 >= 1.04
AND V >= 9,000,000
AND V > V1  (volume expansion)
Within last 25 days
```

**Notes:**
- Sort by max volume in 25 days (maxVol25)
- Our implementation uses: max volume in 25d window + V > V1 filter
- Entry: First 10-15 minutes if opens positive, stop 0.5-2.5%
- Position size: 3-4x normal (tight stop = larger size)
- DEP is NOT just any entry after catalyst — it's the FIRST valid pullback

---

## 4. Sugar Baby (Stock Selection)

**What it finds:** Stocks with most 4% + 9M breakouts over multiple timeframes

**TC2000 Formula (per timeframe):**
```
CountThrough(C / C1 >= 1.04 AND V >= 8,900,000, TF)
```
Where TF = 5, 10, 20, 50, 126, 252, 504, 756, 1450

**Selection rules:**
- Sort each timeframe column descending by count
- Select top 20–30 per timeframe
- For 5d, 10d, 20d: require minimum 3 hits (filter out one-hit wonders)
- Combine all flagged symbols into one master list (~87–90 names)
- Add ~30 "SugarMamas" (market cap >$10B) for balance → ~143 total

**Notes:**
- TC2000 `CountThrough` counts how many times condition was true over N days
- Our implementation: SQL query counting breakout days per ticker
- 1,450 is the max available in TC2000 (1,500 doesn't work)
- Sugar Baby is a STOCK SELECTION strategy, not a setup
- Once identified, trade SOS/ANT/REVERSAL/EP on these stocks
- Source: Sugar Babies Guide Part 6 (transcript line 109): "five days, ten days, twenty days, fifty days, one twenty six days, two fifty two, five zero four"
- Min-3 rule from Part 6 (line 119): "all of these for five, ten, and twenty days, minimum reading should be three"

---

## 5. Anticipation (3T/2T Tight Days)

**What it finds:** Stocks in momentum context with narrow-range days (consolidation before breakout)

**TC2000 Formula:**
```
TI65 > 1.05  (or M20 = true)
AND ABS(C / C1 - 1) < 0.01  (daily change < 1%)
AND price >= 10
```

**Notes:**
- `TI65` = Tortoise Indicator 65-day (momentum measure)
- `M20` = Monthly Momentum 20 (binary: above/below monthly average)
- Our implementation: Requires 4%+ move in last 10 days OR close > AVG C20 as momentum proxy
- 3T = 3 consecutive tight days (highest priority)
- 2T = 2 consecutive tight days
- Entry: BSLO or active monitoring at 3:30 PM, enter 3:58-3:59 PM
- Works ONLY in confirmed bull markets

---

## 6. WSS (Weak Structure Short)

**What it finds:** Waterfall decline + weak bounce — short setup

**TC2000 Formula:**
```
3+ consecutive down days (close < open)
Total decline >= 10% OR >= $10
Then 1-3 days of weak bounce (each day up < 2.5%)
Then down resumes
```

**Notes:**
- "Niagara 3×10, Weak 3×2.5" — Pradeep's mnemonic
- Entry: Next negative day near end of session
- Works in all market conditions (bull, bear, choppy)
- Our implementation now includes decline magnitude check

---

## 7. Reversal Bullish

**What it finds:** Exhaustion candle after selling — buying opportunity

**TC2000 Formula:**
```
3-5 consecutive down days
AND (Hammer candle OR Doji candle)
AND volume > average volume
AND price >= 5 (or 10 preferred)
AND institutional quality (1000+ funds)
```

**Candle definitions:**
- **Hammer:** Lower wick >= 2× body, upper wick <= 0.5× body
- **Doji:** Body < $0.50, both wicks > 2× body

**Notes:**
- Entry: 3:50-3:58 PM (last 5-10 minutes only)
- Stop: 2.5% or less
- If gaps up next day = let it run ("free money")
- If gaps down = close immediately at open
- Requires market or sector oversold context

---

## Cross-Validation Instructions

### Step 1: Set up TC2000
1. Open TC2000
2. Go to **Scan** → **EasyScan**
3. Create new scan for each setup above

### Step 2: Compare Results
Run both our scanner and TC2000 on the same date, compare:

| Metric | Our Scanner | TC2000 | Tolerance |
|--------|-------------|--------|-----------|
| Candidate count | | | ±5 |
| Top 5 tickers | | | 3+ overlap |
| Volume ranking | | | Order roughly same |

### Step 3: Document Differences
If counts differ significantly (>10%), check:
1. **Data source:** FMP vs TC2000 (RealTick/FactSet)
2. **Universe:** Are we including same exchanges?
3. **Adjustments:** Split-adjusted vs raw prices
4. **Timing:** End-of-day vs intraday snapshots

### Step 4: Iterate
- If TC2000 finds stocks we miss → investigate why (data gap? filter difference?)
- If we find stocks TC2000 misses → likely data source difference, document it

---

## Data Source Differences

| Aspect | Our System (FMP) | TC2000 (RealTick) |
|--------|-------------------|-------------------|
| Universe | ~4,956 tickers | ~6,462 tickers |
| Coverage | 75% of TC2000 | Full Worden Common |
| Missing | Delisted, sub-$3, some OTC | All active US stocks |
| Adjustments | Split-adjusted | Split-adjusted |
| EOD timing | Market close | Market close |

**Conclusion:** Our scans will find ~70-80% of TC2000's candidates. The remaining 20-30% are likely smaller/OTC stocks not in FMP's universe.

---

## Quick Reference: Our vs TC2000

| Scan | Our Implementation | TC2000 Equivalent | Gap |
|------|-------------------|-------------------|-----|
| EP 9M | FMP biggest-gainers + volume filter | EasyScan: change% ≥ 4%, V ≥ 9M | Small |
| SOS | SQL: C/C1 ≥ 1.04, V ≥ 9M | EasyScan: same formula | None |
| DEP | SQL: 25d lookback, max volume | EasyScan: 25d lookback, V > V1 | Small |
| Sugar Baby | SQL: count breakouts over 5/10/20/50/126/252/504/756/1450 days | CountThrough per TF | Moderate* |
| ANT | Momentum proxy + tight days | TI65 + tight days | Moderate |
| WSS | Waterfall + weak bounce + magnitude | Same | Small |
| Reversal | Hammer/doji + 3+ down days | Same + institutional filter | Small |

*Sugar Baby gap due to our shorter lookback (~400d vs 1450d) for performance. Can be extended if needed. Timeframes: 5, 10, 20, 50, 126, 252, 504, 756, 1450 (source: SB Guide Part 6). Min 3 hits for 5d/10d/20d.*

---

*Last updated: 2026-06-10*
