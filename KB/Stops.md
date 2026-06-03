---
title: Stops
date: 2026-06-03
tags: [kb, stops, risk-management, stop-placement, trade-management]
---

# Stops

> **Index note** — brief summaries with [[wikilinks]] to guides and transcripts.
> For full detail, follow the links. The transcripts are the most comprehensive source.

## Stop Placement Rules by Setup

| Setup | Stop Placement | Width | When to Move | Source |
|-------|---------------|-------|-------------|--------|
| **DEP** | Below tight consolidation (NOT low of day) | 0.5–2.5% (40¢–$1) | Breakeven + $1 quickly; tighten at 50% profit | [[16. DEP Guide\|DEP Part 5, 8]] |
| **EP Day 1** | Low of the day (if known) or structural level | 8–20% (up to 40% for nano-caps) | Tighten after 20% gain; sell 80% at 100% | [[13. Episodic Pivots Guide\|EP 9M]] |
| **SOS** | Low of the day (preferred) or half of the day | <2% on high-priced; wider on low-priced | Move to breakeven next day if opens positive | [[15. Start of a Swing Guide\|SOS Part 4, 11]] |
| **Anticipation** | Below tight consolidation | <1% (40¢–$1 fixed) | Next morning breakeven if breakout; 4–5% in 30 min → breakeven now | [[08. Anticipation (ANTS) Guide\|ANTS Part 3, 4]] |
| **Momentum Burst** | Low of the day (early) or half of day (later) | 2.5–8% average; 20% for sub-$1 | To breakeven if opens positive; trailing 2–3% by day 3–4 | [[03. Bullish Momentum Burst Guide\|Bullish MB Section 4]] |
| **Reversal Bullish** | At or just below open price / prior day close | 0.5–2.5% | Set next morning; move to breakeven on positive open | [[22. Reversals Guide\|Reversals]] |
| **Sugar Babies** | Low of the day | Standard | Within 1 hour to breakeven | [[14. Sugar Babies Guide\|Sugar Babies Part 6]] |
| **FHP / Dollar Breakout** | Low of the day (NOT half of day) | <2% ($1–$3 on $100+ stocks) | Breakeven + $1 | [[15. Start of a Swing Guide\|SOS Part 9]] |
| **Weak Structure Short** | Half of entry day's range above entry | Tight | Move daily to protect profit; gap-down = take profit | [[10. Weak Structure Short Guide\|WSS Part 3]] |

## Stop Width by Price Point

| Stock Price | Typical Stop Width | Setup |
|------------|-------------------|-------|
| **>$100 (FHP)** | $1–$3 (<2%) | SOS, Dollar Breakout |
| **$10–$100** | 2.5–5% | DEP, SOS, Momentum Burst |
| **$3–$10** | 5–8% | EP 9M, Momentum Burst |
| **<$3** | 8–20% | EP 9M (not recommended for DEP) |
| **Sub-$1** | 20%+ | Momentum Burst only |

## Stop Management Progression

| Stage | Action | Trigger | Source |
|-------|--------|---------|--------|
| **Entry** | Place stop at defined level | Before entering trade | Universal |
| **First move** | Move to breakeven or breakeven+ | Stock opens positive or moves 4–5% in 30 min | [[22. Reversals Guide\|Reversals 3]], [[08. Anticipation (ANTS) Guide\|ANTS Part 4]] |
| **Profit building** | Tighten stop aggressively | Stock makes 40–50% | [[16. DEP Guide\|DEP Part 5]] |
| **Home run** | Sell 80%, keep 20% with trailing stop | Stock makes 100%+ | [[16. DEP Guide\|DEP Part 5]], [[21. Process Guide\|Process]] |
| **Time-based exit** | Kill trade regardless of P/L | Day 3 midday for momentum burst; day 4–5 for MB | [[03. Bullish Momentum Burst Guide\|Bullish MB Section 4]] |

## "Invalidated" Definition

> *"We can put a stop at the low of this particular day as a start of a swing because if this low of the day is invalidated, that means this setup is not going to work."* — [[15. Start of a Swing Guide\|SOS Part 4]]

When the low of the entry day is taken out, the setup's underlying logic is proven false. The trade thesis is dead. **Do NOT re-enter immediately** unless a brand-new setup forms.

## Pre-Market Considerations

| Rule | Source |
|------|--------|
| Stops are **active during market hours only** (9:30 AM – 4:00 PM) | [[03. Bullish Momentum Burst Guide\|Bullish MB Section 4]] |
| Do NOT put stops in pre-market or after-hours — low liquidity will blow you out | [[03. Bullish Momentum Burst Guide\|Bullish MB Section 4]] |
| "Low of the day" = lowest price from 9:30 AM to 4:00 PM, NOT pre-market | [[15. Start of a Swing Guide\|SOS Part 2]] |

## Gap-Down Handling

| Scenario | Action | Source |
|----------|--------|--------|
| Stock gaps down below stop at open | Exit immediately, no questions | [[22. Reversals Guide\|Reversals 3]] |
| Stock gaps up too much pre-market | Skip the trade — widened stop kills edge | [[16. DEP Guide\|DEP Part 8]] |
| Overnight gap on short | Take profit and run | [[10. Weak Structure Short Guide\|WSS Part 3]] |

## Retry Rules

| Setup | Retries | Source |
|-------|---------|--------|
| **DEP** | Up to 3 attempts on genuine catalyst | [[16. DEP Guide\|DEP Part 5]] |
| **Sugar Babies / General** | Do NOT re-enter after stop-out | [[14. Sugar Babies Guide\|Sugar Babies Part 6]] |
| **Short side (broken business)** | Multiple attempts okay — "keep hammering" | [[16. DEP Guide\|DEP Part 5]] |
| **Catalyst-based** | Re-entry allowed if new catalyst forms | [[17. Catalyst Guide\|Catalyst Part 1]] |

## What NOT to Do

| Mistake | Why Wrong | Correct Way | Source |
|---------|-----------|-------------|--------|
| Mental stops | Easy to skip losses, not move stops | Hard stops in system, market hours only | [[03. Bullish Momentum Burst Guide\|Bullish MB Section 4]] |
| High-of-day stop on shorts | Terrible risk/reward, guaranteed loss | Low of day or half of day | [[21. Process Guide\|Process EP9M]] |
| Low-of-day stop on DEP | Defeats purpose — stop becomes 4–8% | 40¢–$1 below entry | [[16. DEP Guide\|DEP Part 8]] |
| Not moving to breakeven | Lets winners turn into losers | Move to breakeven+ as soon as stock opens positive | [[22. Reversals Guide\|Reversals 3]] |
| GTC stops | Carry over to next day, can gap against you | Day-only stops or manual management | [[22. Reversals Guide\|Reversals 3]] |

## See Also

- [[Entries]] — which entry types use which stops
- [[Position Sizing]] — how stop width determines position size
- [[Trade Management]] — what to do after stop is placed
- [[Short Side]] — short-specific stop rules
- [[Common Mistakes]] — stop mistakes across all setups
