---
title: "20% Study — TC2000 Setup and Daily Entry Guide"
date: 2026-07-23
tags: [guide, tc2000, 20-study, setup, daily-process, stockbee, pradeep-bonde]
---

# 20% Study — TC2000 Setup and Daily Entry Guide

## What the 20% Study Measures

Stocks up/down **≥20% over the last 5 trading days**. Pradeep's #1 situational awareness signal.

> "First thing, when I open my computer, when I come to the office, the first thing which I do is to do a 20% study because this is bread and butter for me."  
> — Pradeep, "Learn from 20% Study" video (Jan 3, 2026)

---

## Setting Up the Scan in TC2000

### Step 1: Create the Bullish 20% Study Scan

1. Click **Scan** → **EasyScan** → **New**
2. Name: `20% Study Up`
3. Universe: US Common Stocks + ETFs + ADRs
4. Add Condition (PCF):
   ```
   C >= C5 * 1.20
   ```
   This means: today's close ≥ 20% above the close 5 days ago.
5. Add Condition: `C >= 5` (price ≥ $5)
6. Add Condition: `V >= 100000` (volume ≥ 100K today)
7. Sort by: **Max Volume 25** (descending)
8. Save

### Step 2: Create the Bearish 20% Study Scan

1. Click **Scan** → **EasyScan** → **New**
2. Name: `20% Study Down`
3. Universe: US Common Stocks + ETFs + ADRs
4. Add Condition (PCF):
   ```
   C <= C5 * 0.80
   ```
   This means: today's close ≤ 20% below the close 5 days ago.
5. Add Condition: `C >= 5` (price ≥ $5)
6. Add Condition: `V >= 100000` (volume ≥ 100K today)
7. Sort by: **Max Volume 25** (descending)
8. Save

### Step 3: Daily Routine

After market close (4:00 PM+):

1. Run `20% Study Up` scan → note the **total count** (bottom of the watchlist)
2. Run `20% Study Down` scan → note the **total count**
3. Enter into the system:
   ```
   py src/cli/enter_20pct_study.py --date YYYY-MM-DD --up <up_count> --down <down_count>
   ```
   Example:
   ```
   py src/cli/enter_20pct_study.py --date 2026-07-22 --up 25 --down 42
   ```

Or run without args for interactive prompt:
   ```
   py src/cli/enter_20pct_study.py
   ```

### Step 4: Verify in Radar

The radar generator automatically uses manual TC2000 entries when available, falling back to calculated values. The callout box will show:
- **(manual TC2000)** label when using your entry
- **(calculated)** label when using the SQLite approximation

---

## Reading the 20% Study

| Reading (bullish) | Meaning | Action |
|---|---|---|
| **< 15** | Very low — funds not buying | NO_TRADE — SIPs/day trade only |
| **15-30** | Low — funds not aggressively buying | RANGE_BOUND — no swing longs |
| **30-50** | Marginal — selective setups only | CAUTIOUS_BULL — DEP with catalyst only |
| **50-100** | Healthy — full playbook | FULL_BULL — size into confluences |
| **100-200** | Elevated — caution | CAUTIOUS_BULL — tighten stops |
| **> 200** | Euphoria — top forming | NO_TRADE — London Calling |

| Reading (bearish) | Meaning | Action |
|---|---|---|
| **< 20** | Low selling pressure | Normal |
| **20-50** | Normal | Normal |
| **50-100** | Elevated selling | Watch for bounce |
| **> 100** | Extreme bearishness | Bounce likely (3-5 days) |

> "Excessive bearishness is bullish. Bottoms formed at this stage tend to last for many years."  
> — Pradeep, on T2108 < 10% + bearish 20% study > 100

---

## Why Manual Entry Is Better Than Calculated

| Aspect | Calculated (SQLite) | Manual (TC2000) |
|---|---|---|
| **Universe** | TC2000 universe table (may be stale) | Live TC2000 scan (always current) |
| **Price filter** | $5 (after fix) | $5 (exact match) |
| **Volume filter** | 100K on end date only | 100K (TC2000 handles natively) |
| **Corporate actions** | May miss recent splits/delistings | Always current |
| **New IPOs** | May not be in universe table | Automatically included |
| **Accuracy** | ±5 stocks of Pradeep's count | Exact match with Pradeep |

**Recommendation**: Use manual entry when possible. The calculated version is a fallback for when you can't run TC2000 (e.g., traveling, automated runs).

---

## Source

- [[../../04-Transcripts/stockbee/videos/2026-01-03_2025-study.md|Learn from 20% Study Video]]
- `src/cli/enter_20pct_study.py` — manual entry script
- `src/pricing/range_detector.py` — calculated fallback (min_price=$5, min_volume=100K)