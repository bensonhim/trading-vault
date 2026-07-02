---
title: "Pradeep Ultratrader — Implementation Plan"
date: 2026-06-30
tags: [design, pradeep-ultratrader, stockbee, implementation, plan]
---

# Pradeep Ultratrader — Implementation Plan

> Step-by-step implementation plan for the Pradeep Ultratrader agent and Python backend.
> Each wave is independently testable and deployable.

## Progress Summary

| Wave | Description | Status | Commit |
|------|-------------|--------|--------|
| 1 | Foundation | ✅ COMPLETE | `a5e9743` |
| 2 | Sugar Baby Rebuild | ✅ COMPLETE | `567946e` |
| 3 | SOS Rebuild | ✅ COMPLETE | `0582dc8` |
| 4 | EP 9M Rebuild | ✅ COMPLETE | `0bafc6c` |
| 5 | DEP Rebuild | ✅ COMPLETE | `246ac35` |
| 6 | Intraday Daemon | ✅ COMPLETE | `7489004` |
| 7 | Nightly Pipeline Integration | ⏳ PENDING | — |
| 8 | OpenCode Agent Definition | ⏳ PENDING | — |
| 9 | Trade Management | ⏳ PENDING | — |
| 10 | Testing & Deployment | ⏳ PENDING | — |

---

## Wave 1: Foundation ✅ COMPLETE

### 1.1 Trading Calendar ✅
**File:** `src/market/trading_calendar.py` (new) ✅

- Use `pandas_market_calendars` for NYSE holidays + DST-aware market hours
- `is_trading_day(date) -> bool`
- `market_open(date) -> datetime` (9:30 AM ET)
- `market_close(date) -> datetime` (4:00 PM ET)
- `is_market_open_now() -> bool`
- `next_trading_day(date) -> date`

**Test:** Verify NYSE 2026 holidays return `is_trading_day=False`; verify market open/close times handle DST.

### 1.2 DB Schema Migration ✅
**File:** `src/data/db.py` (modify)

New tables and columns:

```sql
-- Sugar Baby multi-timeframe
ALTER TABLE sugar_babies ADD COLUMN count_504d INTEGER DEFAULT 0;
ALTER TABLE sugar_babies ADD COLUMN count_252d INTEGER DEFAULT 0;
ALTER TABLE sugar_babies ADD COLUMN count_126d INTEGER DEFAULT 0;
ALTER TABLE sugar_babies ADD COLUMN count_63d INTEGER DEFAULT 0;
ALTER TABLE sugar_babies ADD COLUMN count_21d INTEGER DEFAULT 0;
ALTER TABLE sugar_babies ADD COLUMN count_10d INTEGER DEFAULT 0;
ALTER TABLE sugar_babies ADD COLUMN count_5d INTEGER DEFAULT 0;
ALTER TABLE sugar_babies ADD COLUMN sb_tier TEXT;  -- 'core' | 'expanded' | NULL

-- Leg detection
ALTER TABLE scan_results ADD COLUMN leg_count INTEGER;
ALTER TABLE scan_results ADD COLUMN leg_number INTEGER;  -- 1, 2, 3+
ALTER TABLE scan_results ADD COLUMN is_first_leg BOOLEAN;

-- Magna 53
CREATE TABLE IF NOT EXISTS magna53_scores (
    ticker TEXT,
    target_date TEXT,
    m_score BOOLEAN,      -- massive earnings/sales
    a_score BOOLEAN,      -- 39%+ sales growth 2Q
    g_score BOOLEAN,      -- gap up 4%+
    n_score BOOLEAN,      -- neglect
    five_score BOOLEAN,   -- short interest 5+
    three_score BOOLEAN,  -- 3+ analyst raises
    cap10 BOOLEAN,        -- market cap < $10B
    ipo_under_10yr BOOLEAN,
    total_essential INTEGER,  -- count of M/A/G/N
    total_optional INTEGER,   -- count of 5/3
    score_text TEXT,      -- e.g. "MAGN + 5 + 3 + Cap10x10"
    PRIMARY KEY (ticker, target_date)
);

-- Trade tracking
CREATE TABLE IF NOT EXISTS trades (
    ticker TEXT,
    setup_type TEXT,
    entry_date TEXT,
    entry_price REAL,
    stop_price REAL,
    target_price REAL,
    shares INTEGER,
    position_usd REAL,
    status TEXT,          -- 'open' | 'closed' | 'stopped'
    exit_date TEXT,
    exit_price REAL,
    pnl_usd REAL,
    pnl_pct REAL,
    notes TEXT,
    PRIMARY KEY (ticker, entry_date)
);

-- Catalyst enrichment (refined)
ALTER TABLE catalyst_results ADD COLUMN magna53_essential INTEGER DEFAULT 0;
ALTER TABLE catalyst_results ADD COLUMN magna53_optional INTEGER DEFAULT 0;
ALTER TABLE catalyst_results ADD COLUMN cap10x10 BOOLEAN DEFAULT FALSE;
```

**Test:** Run migration on existing DB; verify columns exist; verify no data loss.

### 1.3 Common Consolidation/Tight-Day Module ✅
**File:** `src/pricing/consolidation.py` (new)

Extract tight day and consolidation detection as a shared module used by ANTS, DEP, SOS, and leg detector.

```python
def is_tight_day(change_pct: float, threshold: float = 1.0) -> bool
def count_consecutive_tight_days(bars: list[dict], threshold: float = 1.0) -> int
def detect_consolidation(bars, breakout_bar, max_days=10, min_days=2,
                         tight_threshold=1.5, no_breakdown_pct=4.0) -> ConsolidationResult
def is_rising_wedge(bars) -> bool
```

`ConsolidationResult` dataclass:
- `is_valid: bool`
- `num_days: int`
- `high: float` (consolidation high)
- `low: float` (consolidation low)
- `avg_volume: float`
- `has_breakdown: bool` (4%+ down day during consolidation)
- `volume_vs_breakout: float` (ratio)
- `direction: str` ("flat" | "down" | "rising")
- `holds_gain: bool` (close ≥ 85% of breakout close)

**Test:** Unit tests with synthetic OHLCV data — valid consolidation, breakdown, rising wedge, stalemate.

### 1.4 Leg Detector ✅
**File:** `src/pricing/leg_detector.py` (new)

```python
def count_legs(ticker, target_date, lookback_days=25) -> LegResult
```

`LegResult`:
- `leg_count: int` (1, 2, 3+)
- `current_leg_number: int`
- `is_first_leg: bool`
- `is_third_or_later: bool`
- `breakout_days: list[date]` (dates of 4%+ breakouts)
- `legs: list[Leg]` (each with start_date, end_date, breakout_date, consolidation_days)

Algorithm:
1. Find all 4%+ breakout days in lookback (close >= prev_close × 1.04, V > V1)
2. Group consecutive breakouts (within 2 days) as same leg
3. New leg = ≥3 tight/consolidation days between breakouts
4. Return count and current leg number

**Test:** Synthetic data: 5 consecutive 4% days = 1 leg; breakout→3 tight→breakout = 2 legs.

### 1.5 Telegram Smoke Test ✅ (blocked by corp proxy; works at home)
**File:** `src/cli/test_telegram.py` (new)

- Read `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` from env
- Send test message: "Pradeep Ultratrader — Telegram smoke test ✅"
- Print success/failure

**Test:** Run at home workstation (no proxy); verify message received on phone.

### 1.6 Remove VWAP Gating ✅
**Files:** `src/pricing/vwap.py` (modify), `src/pricing/entry_exit.py` (modify), `src/scans/cross_reference.py` (modify)

- Remove VWAP as entry-blocking filter in `is_entry_allowed()`
- Keep VWAP as optional informational field in deep_dive notes only
- `is_entry_allowed()` now returns `(True, None)` for all setups (no VWAP blocking)
- Entry filters are: 4%+ breakout, volume expansion, Two Lynch, MM regime, leg count, catalyst

**Test:** Run existing pipeline; verify no VWAP blocks; verify notes still show VWAP as info.

---

## Wave 2: Sugar Baby Rebuild ✅ COMPLETE

### 2.1 Multi-Timeframe Sugar Baby Computation
**File:** `src/scans/compute_sugar_babies.py` (rewrite)

- Count 4%+ breakouts with 9M+ volume and V > V1 over 7 timeframes
- Remove the `LIMIT 400` bug (look back full available data)
- Store per-ticker: `count_504d`, `count_252d`, `count_126d`, `count_63d`, `count_21d`, `count_10d`, `count_5d`
- Compute `sb_tier`: "core" (top 30 by any timeframe), "expanded" (top 150), NULL
- `sb_master_flag`: True if in top-30 of ANY timeframe

**Test:** Run on existing DB; verify counts are >0 for active tickers; verify SB list has ~60-150 stocks.

### 2.2 Nightly Runner — Backfill + SB Step
**File:** `src/cli/nightly_runner.py` (modify)

Add steps:
```
Step 0:   Fetch StockBee MM
Step 0.5: Backfill missing OHLCV (check last date in DB vs yesterday, fetch gap)
Step 0.7: Compute Sugar Babies (multi-timeframe)
Step 1:   Fetch today's FMP daily quotes → insert
Step 2:   Run all scans (using refreshed SB list)
...
```

**Test:** Run nightly pipeline; verify backfill fills gaps; verify SB table has multi-timeframe counts.

---

## Wave 3: SOS Rebuild ✅ COMPLETE

### 3.1 SOS Scan — Two Lynch + Leg Detection
**File:** `src/scans/sos.py` (rewrite)

- Add `V > V1` (volume expansion) check
- Add dollar breakout path for stocks ≥ $60
- Run leg detector on each candidate; flag `is_third_or_later`
- Add Two Lynch heuristic scoring:
  - T: check if stock was up 2 days in a row before breakout (minor ≤0.5% tolerated)
  - L: linearity check (max range / min range < 2.5 over 5 days)
  - Y: leg_count ≤ 2
  - N: day before breakout = narrow (abs(change) < 1%) or negative
  - C: consolidation quality (call `detect_consolidation()`)
  - H: close near high (≥70% of range — needs intraday data for real-time; use daily as proxy for EOD scan)
- Store Two Lynch scores in scan results

**Test:** Run on historical data; verify Two Lynch filters reduce results by 80-90%; verify leg detection.

### 3.2 SOS Entry/Stop with Intraday Data
**File:** `src/pricing/entry_exit.py` (modify)

- SOS entry = current price when 4% breakout triggers (intraday)
- SOS stop:
  - If price ≥ $100: `low_of_day` from 5-min bars
  - If price < $100: `half_of_day = (open + low_of_day) / 2`
  - Preliminary (pre-market): `prior_day_low` (updated intraday)
- Add `is_gap_up` flag: if `open / prev_close ≥ 1.04`

**Test:** Unit tests with synthetic 5-min bars; verify low_of_day and half_of_day calculation.

---

## Wave 4: EP 9M Rebuild ✅ COMPLETE

### 4.1 EP 9M Scan — Gap Detection + Magna 53
**File:** `src/scans/ep_9m.py` (rewrite)

- Add gap-up detection: `open / prev_close ≥ 1.04` = "gap-up EP" (stronger)
- Add intraday breakout: `open / prev_close < 1.02` but `close / prev_close ≥ 1.04` = "intraday EP"
- Fetch earnings calendar (already in CatalystHunter)
- For each EP candidate, compute Magna 53 score:
  - M: FMP income statement → EPS growth YoY ≥ 100% or sales growth QoQ ≥ 100%
  - A: FMP income statement → sales growth ≥ 39% for last 2 quarters
  - G: already detected by gap-up check
  - N: FMP profile → check if stock was flat/down 3 months pre-earnings (proxy: avg volume 3m < avg volume 1y × 0.8)
  - 5: FMP short interest if available
  - 3: FMP analyst estimates → count target raises after earnings
- Compute Cap 10×10: market cap < $10B, IPO < 10 years (from FMP profile)
- Store Magna 53 score in `magna53_scores` table

**Test:** Run on stocks with known earnings; verify Magna 53 scoring; verify gap-up vs intraday classification.

### 4.2 EP Entry/Stop
**File:** `src/pricing/entry_exit.py` (modify)

- EP entry = OPG (market open price)
- EP stop = `low_of_day` from 5-min bars (8-20% width)
- Preliminary (pre-market): `prior_day_low`
- Price-tiered stop floor:
  - ≥ $100: 5% max stop
  - ≥ $10: 8% max stop
  - ≥ $3: 12% max stop
  - < $3: 20% max stop

**Test:** Verify stop width stays within tiered bounds.

---

## Wave 5: DEP Rebuild ✅ COMPLETE

### 5.1 DEP Scan — Require Valid Pullback
**File:** `src/scans/dep.py` (rewrite)

- Only return candidates where `detect_consolidation()` returns `is_valid=True`
- Add leg detection: flag first pullback (valid DEP) vs second/third (not DEP proper)
- Add gap-and-go detection: if stock gapped ≥8% on breakout day AND no pullback → exclude (not DEP)
- Current price ≥ $3 filter (already done, keep)

**Test:** Run on historical data; verify only valid pullbacks returned; verify gap-and-go excluded.

### 5.2 DEP Entry/Stop — Percentage-Based
**File:** `src/pricing/entry_exit.py` (modify)

- DEP entry = `consolidation_high + buffer` where buffer scales with price:
  - Calculate buffer to keep total stop width within 0.5%-2.5%
  - `buffer = max(consolidation_high × 0.001, $0.10)` (minimum $0.10)
- DEP stop = `consolidation_low - buffer` where buffer scales with price:
  - `buffer = max(consolidation_low × 0.002, $0.10)`
  - Total stop width must be 0.5%-2.5%
- If consolidation width > 25% → block (bad data, no orderly pullback)

**Test:** Verify stop width is 0.5%-2.5% for $10, $50, $100, $300 stocks.

---

## Wave 6: Intraday Daemon ✅ COMPLETE

### 6.1 Intraday Runner
**File:** `src/cli/intraday_runner.py` (new)

Main daemon loop:
```python
1. Check is_trading_day(today)
2. If not trading day: sleep until tomorrow
3. At 9:25 AM ET: pre-market scan
   - Fetch FMP batch quotes for watchlist tickers
   - If any up 4%+ → Telegram alert: "PRE-MARKET BREAKOUT"
4. At 9:30 AM ET: start polling loop
   - Every 60 seconds: fetch quotes for watchlist tickers
   - If current_price >= trigger_price (yesterday_close × 1.04) → Telegram alert: "SOS BREAKOUT TRIGGER"
   - Fetch 5-min bars for triggered tickers → calculate low_of_day, half_of_day
   - Alert includes: ticker, setup, entry price, stop price, shares, position USD
5. At 2:58 PM ET: ANTS scan
   - Find 3T/2T tight day stocks from watchlist
   - Calculate BSLO trigger = close + 1%, stop = tight consolidation low
   - Telegram alert: "ANTS SETUP"
6. At 3:58 PM ET: Reversal scan
   - Find exhaustion patterns from 5-min bars
   - Telegram alert: "REVERSAL SETUP"
7. At 4:00 PM ET: stop polling, run EOD summary
   - Send Telegram summary of the day's alerts
8. Sleep until next trading day
```

### 6.2 Real-Time Alert Format
**File:** `src/alerts/telegram_alerts.py` (modify)

Telegram message templates:
```
🚀 SOS BREAKOUT: NVDA
Price: $135.20 (up 4.2% from $129.80)
Entry: $135.20 (market)
Stop: $132.10 (low of day, 2.3% risk)
Shares: 85 @ $135 = $11,475
Position: 11.5% of account
Two Lynch: T✅ L✅ Y✅ N✅ C✅ H✅
Leg: 1st | Sugar Baby: ✅ | Catalyst: earnings
```

```
⏰ ANTS SETUP: AMD
Trigger: $162.30 (close + 1%)
Limit: $163.00
Stop: $159.80 (tight consolidation low, 1.5% risk)
Shares: 243 @ $162 = $39,366
Position: 39.4% of account
3T: ✅ (3 tight days) | TI65: 1.82
Place BSLO before 9:30 AM tomorrow
```

```
📊 EOD SUMMARY (2026-06-30)
Alerts sent: 3
- 09:31 NVDA SOS breakout → entered $135.20
- 10:15 AVGO SOS breakout → entered $185.40
- 14:58 AMD ANTS setup → BSLO for tomorrow
Market Monitor: GREEN (450)
Tomorrow's watchlist: 5 DEP candidates, 3 ANTS candidates
```

### 6.3 Windows Task Scheduler Setup
**File:** `scripts/setup_scheduler.ps1` (new)

- Create scheduled task: "PradeepUltratrader" that runs `intraday_runner.py` at boot
- Create scheduled task: "PradeepNightlyPipeline" that runs `nightly_runner.py` at 5:00 PM ET daily

**Test:** Run `intraday_runner.py` manually; verify it detects non-trading day and sleeps.

---

## Wave 7: Nightly Pipeline Integration ⏳ PENDING

### 7.1 Nightly Runner — Full Sequence
**File:** `src/cli/nightly_runner.py` (rewrite)

```
Step 0:   Fetch StockBee MM → store
Step 0.5: Backfill missing OHLCV (gap detection + FMP fetch)
Step 0.7: Compute Sugar Babies (multi-timeframe)
Step 1:   Fetch today's FMP daily quotes → insert
Step 2:   Run scans: SOS, EP 9M, DEP, ANTS, Reversal, Sector ETF
          (each scan: leg detection, Two Lynch, consolidation check)
Step 3:   Catalyst enrichment (CatalystHunter, fast_only=True)
Step 3.5: Magna 53 scoring for EP candidates
Step 4:   Cross-reference with SB + catalyst + MM regime
Step 5:   Entry/stop/position sizing for each candidate
Step 6:   Sector diversification (max 2 per sector in A/A+)
Step 7:   Generate Obsidian notes (MM note, Trade Ideas, Daily Briefing)
Step 8:   Send EOD Telegram summary
Step 9:   Prepare tomorrow's pre-market watchlist
```

### 7.2 Obsidian Note Templates
**File:** `src/interpretation/briefing_generator.py` (modify)

Update templates to include:
- Two Lynch scores (T/L/Y/N/C/H with ✅/❌)
- Leg count (1st/2nd/3rd+)
- Magna 53 score for EP candidates
- Sugar Baby tier (core/expanded)
- Pre-market order sheet (DEP + ANTS with exact prices)
- Intraday watchlist (SOS + EP with trigger prices)

**Test:** Run nightly pipeline; verify Obsidian notes have all new fields.

---

## Wave 8: OpenCode Agent Definition ⏳ PENDING

### 8.1 Agent Definition
**File:** `.opencode/agents/pradeep-ultratrader.md` (new)

```yaml
---
name: Pradeep Ultratrader
description: >
  StockBee methodology trading assistant. Runs daily market monitoring,
  4% breakout screening, Two Lynch qualification, entry/stop/position
  calculation, and Obsidian documentation for US stock market.
  Triggered by: "pradeep", "stockbee", "market monitor", "trade ideas",
  "scan", "breakout", "sugar baby", "EP 9M", "DEP", "SOS", "ANTS"
model: ollama-cloud/glm-5.2
tools:
  - bash
  - read
  - write
  - edit
  - glob
  - grep
---
```

Agent prompt includes:
- StockBee methodology summary (from curriculum notes)
- Technical definitions (from Technical Definitions doc)
- Daily process workflow
- Tool usage instructions (Python CLI commands)
- Obsidian vault structure
- Telegram alert format

### 8.2 Custom Tools (Optional)
**Files:** `.opencode/tools/trading_*.ts` (new)

Optional TypeScript tools for the agent:
- `trading_scan` — run a specific scan (SOS, EP, DEP, ANTS)
- `trading_deep_dive` — run deep dive on a ticker
- `trading_market_monitor` — fetch current MM status
- `trading_send_alert` — send Telegram alert

**Test:** Invoke agent in OpenCode; verify it can run scans and generate notes.

---

## Wave 9: Trade Management ⏳ PENDING

### 9.1 Trade Tracker
**File:** `src/alerts/trade_recorder.py` (modify)

- Record trade entry: ticker, setup, entry price, stop, shares, position
- Track open positions
- Update stop progression: low_of_day → half_range → breakeven → trailing
- Time stop alerts: momentum burst day 3-5; reversal next day
- 80/20 exit alerts: sell 80% at 40-50% profit; sell remaining at 100%+

### 9.2 Position Monitor
**File:** `src/alerts/intraday_monitor.py` (modify)

- For open positions: fetch 5-min bars every 5 minutes
- Check if stop was hit (low ≤ stop_price)
- Check if profit target reached
- Send Telegram alert on stop hit or target reached

**Test:** Simulate a position; verify stop-hit alert fires correctly.

---

## Wave 10: Testing & Deployment ⏳ PENDING

### 10.1 End-to-End Test
- Run nightly pipeline on a trading day
- Verify Obsidian notes generated
- Verify Telegram alerts sent
- Run intraday daemon during market hours
- Verify SOS breakout alert fires
- Verify ANTS scan at 2:58 PM
- Verify EOD summary at 4:00 PM

### 10.2 Home Workstation Setup
- Install `pandas_market_calendars`: `py -m pip install pandas_market_calendars`
- Set up Windows Task Scheduler tasks
- Verify daemon starts at boot and sleeps on non-trading days
- Verify Telegram alerts received on phone

### 10.3 Documentation
- Update `.trading/STATUS.md` with new architecture
- Update `AGENTS.md` with Pradeep Ultratrader agent entry
- Update this implementation plan with completion status

---

## File Summary

### New Files (14)
| File | Wave | Purpose |
|------|------|---------|
| `src/market/calendar.py` | 1 | NYSE trading calendar |
| `src/pricing/consolidation.py` | 1 | Shared tight day + consolidation detection |
| `src/pricing/leg_detector.py` | 1 | Leg counting (1st/2nd/3rd+) |
| `src/cli/test_telegram.py` | 1 | Telegram smoke test |
| `src/cli/intraday_runner.py` | 6 | Real-time intraday daemon |
| `scripts/setup_scheduler.ps1` | 6 | Windows Task Scheduler setup |
| `.opencode/agents/pradeep-ultratrader.md` | 8 | OpenCode agent definition |
| `.opencode/tools/trading_scan.ts` | 8 | Agent tool: run scan (optional) |
| `.opencode/tools/trading_deep_dive.ts` | 8 | Agent tool: deep dive (optional) |
| `.opencode/tools/trading_market_monitor.ts` | 8 | Agent tool: MM status (optional) |
| `.opencode/tools/trading_send_alert.ts` | 8 | Agent tool: send alert (optional) |

### Modified Files (12)
| File | Wave | Changes |
|------|------|---------|
| `src/data/db.py` | 1 | Schema migration (SB multi-TF, legs, Magna53, trades) |
| `src/pricing/vwap.py` | 1 | Remove VWAP gating; keep as info only |
| `src/pricing/entry_exit.py` | 3,4,5 | SOS/EP/DEP entry/stop with intraday data; % buffers |
| `src/scans/sos.py` | 3 | Two Lynch + leg detection + dollar breakout |
| `src/scans/ep_9m.py` | 4 | Gap detection + Magna 53 scoring |
| `src/scans/dep.py` | 5 | Require valid pullback; leg detection |
| `src/scans/compute_sugar_babies.py` | 2 | Multi-timeframe computation |
| `src/cli/nightly_runner.py` | 2,7 | Backfill + SB + full sequence |
| `src/interpretation/briefing_generator.py` | 7 | Updated note templates |
| `src/alerts/telegram_alerts.py` | 6 | Real-time alert templates |
| `src/alerts/trade_recorder.py` | 9 | Trade tracking |
| `src/alerts/intraday_monitor.py` | 9 | Position monitoring |
| `src/scans/cross_reference.py` | 1,7 | Remove VWAP; add leg/MM/SB weighting |

## Dependency to Install

```
py -m pip install pandas_market_calendars
```

## See Also

- [[Pradeep Ultratrader — Design]] — overall architecture
- [[Pradeep Ultratrader — Technical Definitions]] — precise definitions
- [[_Trading Radar Engine v2 — Implementation Notes]] — previous design (reference)