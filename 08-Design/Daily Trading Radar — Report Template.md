---
title: "Daily Trading Radar — {{date}}"
date: {{date}}
tags: [daily, trading-radar, stockbee, pradeep-ultratrader]
---

# Daily Trading Radar — {{date}}

## 1. Market Regime — LLM Judge Verdict

> [!{{callout_type}}] **{{regime}}** — Action: **{{action}}** (confidence: {{confidence}}%)
> {{reasoning}}

**Key Warnings:**
{{warnings_list}}

---

## 2. Market Monitor (Primary Breadth)

| Indicator | Today | Yesterday | 2 Days Ago | 3 Days Ago | Trend |
|-----------|-------|-----------|------------|------------|-------|
| Net Primary | {{net_today}} | {{net_yesterday}} | {{net_2d}} | {{net_3d}} | {{net_trend}} |
| T2108 | {{t2108_today}}% | {{t2108_yesterday}}% | {{t2108_2d}}% | {{t2108_3d}}% | {{t2108_trend}} |
| Breakouts (4%+) | {{bo_today}} | {{bo_yesterday}} | {{bo_2d}} | {{bo_3d}} | — |
| Breakdowns (4%+) | {{bd_today}} | {{bd_yesterday}} | {{bd_2d}} | {{bd_3d}} | — |
| BO:BD Ratio | {{ratio_today}} | {{ratio_yesterday}} | {{ratio_2d}} | {{ratio_3d}} | — |

**Primary Trend Assessment:** {{primary_trend_assessment}}

> [!note] Pradeep's Rule
> "If you just trade breakouts when the primary indicator is green, you will find most of the time, most of the breakouts work." — Primary is the MOST important indicator.

### 20% Study

| Metric | Value | Signal |
|--------|-------|--------|
| Stocks up 20%+ (5-day) | {{up_20}} | {{up_20_signal}} |
| Stocks down 20%+ (5-day) | {{down_20}} | {{down_20_signal}} |
| Ratio | {{ratio_20}} | {{ratio_20_signal}} |

### Breakout Follow-Through (Last 3 Days)

| Date | Breakouts | Followed Through | Failed | Rate | Signal |
|------|-----------|-----------------|--------|------|--------|
| {{ft_date_1}} | {{ft_bo_1}} | {{ft_followed_1}} | {{ft_failed_1}} | {{ft_rate_1}} | {{ft_signal_1}} |
| {{ft_date_2}} | {{ft_bo_2}} | {{ft_followed_2}} | {{ft_failed_2}} | {{ft_rate_2}} | {{ft_signal_2}} |
| {{ft_date_3}} | {{ft_bo_3}} | {{ft_followed_3}} | {{ft_failed_3}} | {{ft_rate_3}} | {{ft_signal_3}} |

> [!tip] Follow-Through Rate Guide
> >70% = healthy | 50-70% = caution | <50% = reduce size | ~0% = no new longs

---

## 3. Sector Relative Strength

**Leading Sector:** {{leading_sector}} ({{leading_theme}}) — RS_20d: {{leading_rs_20d}} | RS_65d: {{leading_rs_65d}}

{{#if former_leader_rolling_over}}
> [!warning] Former Leader Rolling Over
> {{former_leader}} — 65-day leader with negative 20-day RS. Institutional distribution in the former leading sector.
{{/if}}

### Sector RS Heatmap (Top 10 by RS_20d)

| Rank | Ticker | Theme | RS_20d | RS_65d | ETF_20d Return | Status |
|------|--------|-------|--------|--------|----------------|--------|
| 1 | {{etf_1}} | {{theme_1}} | {{rs20_1}} | {{rs65_1}} | {{ret20_1}} | {{status_1}} |
| 2 | {{etf_2}} | {{theme_2}} | {{rs20_2}} | {{rs65_2}} | {{ret20_2}} | {{status_2}} |
| 3 | {{etf_3}} | {{theme_3}} | {{rs20_3}} | {{rs65_3}} | {{ret20_3}} | {{status_3}} |
| ... | ... | ... | ... | ... | ... | ... |

**Status Legend:** LEADING | TOP FORMING | ROLLING OVER | HEALTHY

---

## 4. Rally Maturity

| Metric | Value |
|--------|-------|
| Days since last market low | {{rally_days}} |
| Low date | {{low_date}} |
| Low T2108 | {{low_t2108}}% |
| Current T2108 | {{current_t2108}}% |
| Mature (3+ days) | {{is_mature}} |
| Overbought (20% > 50) | {{is_overbought}} |
| Extended (mature + overbought) | {{is_extended}} |

---

## 5. SPY & QQQ Intraday Narrative

### SPY
| Session | Open | Close | Change | Pattern |
|---------|------|-------|--------|---------|
| First hour (9:30-10:30) | {{spy_open}} | {{spy_first_hr_close}} | {{spy_first_hr_chg}}% | — |
| Midday (10:30-14:00) | — | {{spy_midday_close}} | — | {{spy_midday_direction}} |
| Afternoon (14:00-16:00) | {{spy_afternoon_open}} | {{spy_afternoon_close}} | {{spy_afternoon_chg}}% | — |
| **Close position** | — | {{spy_close}} | — | {{spy_close_position}}% of range |

**SPY Pattern:** {{spy_pattern}} — {{spy_narrative}}

### QQQ
**QQQ Pattern:** {{qqq_pattern}} — {{qqq_narrative}}

### SPY Last 5 Days

| Date | Close | Change% | Range | Close Position |
|------|-------|---------|-------|----------------|
| {{spy_day_1}} | {{spy_close_1}} | {{spy_chg_1}}% | {{spy_range_1}}% | {{spy_pos_1}} |
| {{spy_day_2}} | {{spy_close_2}} | {{spy_chg_2}}% | {{spy_range_2}}% | {{spy_pos_2}} |
| {{spy_day_3}} | {{spy_close_3}} | {{spy_chg_3}}% | {{spy_range_3}}% | {{spy_pos_3}} |

---

## 6. Sugar Baby Watchlist

**Core List:** {{sb_core_count}} tickers | **Expanded List:** {{sb_expanded_count}} tickers

### Top 10 Sugar Babies (by count_504d)

| Rank | Ticker | 504d | 252d | 63d | 21d | 5d | Tier | Implication |
|------|--------|------|------|-----|-----|-----|------|-------------|
| 1 | {{sb_1}} | {{sb_504_1}} | {{sb_252_1}} | {{sb_63_1}} | {{sb_21_1}} | {{sb_5_1}} | {{sb_tier_1}} | {{sb_impl_1}} |
| 2 | {{sb_2}} | {{sb_504_2}} | {{sb_252_2}} | {{sb_63_2}} | {{sb_21_2}} | {{sb_5_2}} | {{sb_tier_2}} | {{sb_impl_2}} |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

---

## 7. Trade Ideas — Confluence Tiers

### A+ Confluences (Setup + Sugar Baby + Catalyst → Maximum Size)

| # | Ticker | Setup | SB Rank | Entry | Stop | Width | Shares | Pos USD | Risk HKD | Two Lynch | Leg | Catalyst | Magna 53 |
|---|--------|-------|---------|-------|------|-------|--------|---------|----------|-----------|-----|----------|----------|
{{a_plus_rows}}

### A Confluences (Setup + Sugar Baby → Standard Size)

| # | Ticker | Setup | SB Rank | Entry | Stop | Width | Shares | Pos USD | Risk HKD | Two Lynch | Leg | Status |
|---|--------|-------|---------|-------|------|-------|--------|---------|----------|-----------|-----|--------|
{{a_rows}}

### B+ Confluences (Setup + Catalyst → Standard Size)

| # | Ticker | Setup | Entry | Stop | Width | Shares | Pos USD | Risk HKD | Catalyst | Status |
|---|--------|-------|-------|------|-------|--------|---------|----------|----------|--------|
{{b_plus_rows}}

### B Setups (Setup Only → Smaller Size)

| # | Ticker | Setup | Entry | Stop | Width | Shares | Pos USD | Risk HKD | Status |
|---|--------|-------|-------|------|-------|--------|---------|----------|--------|
{{b_rows}}

### C Watchlist (Sugar Baby Only — No Position)

| Ticker | SB Rank | Notes |
|--------|---------|-------|
{{c_rows}}

---

## 8. Pre-Market Order Sheet

> [!important] Place these orders BEFORE 9:30 AM ET
> DEP and ANTS entry/stop are known from prior-day data — place limit + stop orders before market open.

### DEP Limit Orders (Buy at consolidation high + buffer)

| Ticker | Tier | Entry (Limit) | Stop | Width | Shares | Pos USD | Risk HKD | Consolidation | Breakout Date |
|--------|------|---------------|------|-------|--------|---------|----------|---------------|---------------|
{{dep_orders}}

### ANTS BSLO Orders (Buy Stop Limit at close + 1%)

| Ticker | Tier | Trigger (BSLO) | Stop | Width | Shares | Pos USD | Risk HKD | Tight Days |
|--------|------|----------------|------|-------|--------|---------|----------|------------|
{{ants_orders}}

---

## 9. Intraday Watchlist (SOS + EP 9M)

> [!tip] Monitor during market hours
> Enter when 4% breakout triggers. Stop = low of day (intraday 5-min data). Place stop immediately after entry fills.

### SOS Breakout Candidates

| Ticker | Trigger Price | Two Lynch | Leg | Sugar Baby | 9M Volume | Notes |
|--------|---------------|-----------|-----|------------|-----------|-------|
{{sos_watchlist}}

### EP 9M Candidates

| Ticker | Gap % | Breakout Type | Magna 53 | Cap 10×10 | Catalyst | Notes |
|--------|-------|---------------|----------|-----------|----------|-------|
{{ep_watchlist}}

---

## 10. Sector ETF Momentum Proxies (Watch, Not Trade)

| Ticker | Theme | RS_20d | RS_65d | Status |
|--------|-------|--------|--------|--------|
{{sector_etf_rows}}

---

## 11. Similar Historical Conditions

> Past days with similar market conditions and what Pradeep concluded:

{{#each similar_days}}
**{{this.date}}** (similarity: {{this.similarity}}%)
- Pradeep: {{this.regime}} / {{this.action}}
{{#if this.warnings}}- Warnings: {{this.warnings}}{{/if}}
- T2108: {{this.t2108}}%, Net: {{this.net_primary}}, Rally: {{this.rally_days}}d
- Outcome: {{this.outcome}}
{{/each}}

---

## 12. Account Parameters

| Parameter | Value |
|-----------|-------|
| Account | 1,000,000 HKD |
| Risk per trade | 3,000 HKD (~$385 USD) |
| USD/HKD | 7.8 |
| Soft cap | 25% of account |
| Hard cap | 50% (DEP + Sugar Baby confluence) |
| Universe | ~6,080 TC2000 common stocks |
| ETFs | Sector proxies only (not for individual positions) |

---

## 13. Action Summary

{{#if action_full_long}}
- [ ] Full playbook — size into A+ confluences
- [ ] Place DEP limit orders before open
- [ ] Place ANTS BSLO orders before open
- [ ] Monitor SOS breakout triggers intraday
- [ ] Watch EP 9M candidates for catalyst confirmation
{{/if}}

{{#if action_reduce_size}}
- [ ] Reduce size — tighten stops, selective setups only
- [ ] Place DEP limit orders (reduced shares)
- [ ] Only A+ and A confluences — skip B tier
- [ ] Sell into strength on existing positions
- [ ] Monitor for regime change signals
{{/if}}

{{#if action_no_new_longs}}
- [ ] No new longs — process over chasing
- [ ] Manage existing positions (move stops to breakeven)
- [ ] Watch for capitulation signal (T2108 < 10%)
- [ ] Focus on research and watchlist building
- [ ] Do NOT force trades
{{/if}}

{{#if action_shorts_only}}
- [ ] Shorts only — or cash
- [ ] Look for WSS (Weak Structure Short) setups
- [ ] No new longs under any circumstance
- [ ] Watch for capitulation bounce (T2108 < 10% = generational buy)
{{/if}}

---

## 14. Telegram Alerts Sent Today

| Time | Ticker | Alert Type | Entry | Stop | Status |
|------|--------|------------|-------|------|--------|
{{telegram_alerts}}

---

*Generated by Pradeep Ultratrader Trading Radar Engine*
*LLM Judge: GLM-5.2 | Market Context: 5-day lookback | Validation: 97% match+close (260 dates)*