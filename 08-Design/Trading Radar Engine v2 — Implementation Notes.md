---
title: Trading Radar Engine v2 — Implementation Notes
date: 2026-06-15
tags: [trading, v2, implementation, pricing, interpretation, mm-interpreter]
---

# Trading Radar Engine v2 — Implementation Notes

> **Status:** Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Phase 4 🔄 | Phase 5 ✅
> **Design docs:** `D:\opencodeworkspace\.trading\docs\v2-design\`
> **Source code:** `D:\opencodeworkspace\.trading\src\`

---

## Phase 1 — Range Detection, Entry/Exit & Position Sizing ✅

**Completed:** 2026-06-15
**Design doc:** [PHASE-1-Range-Detection.md](file:///D:/opencodeworkspace/.trading/docs/v2-design/PHASE-1-Range-Detection.md)

### What Was Built

#### `src/config.py` — Centralized Configuration (115 lines)

- `TradingConfig` dataclass with all trading parameters: `usd_hkd_rate`, `account_hkd`, `risk_per_trade_hkd`, `soft_cap_pct`, `hard_cap_pct`, `fmp_rate_limit_delay`
- `FMPConfig` for API keys and rate limits
- `DeepgramConfig` for transcription settings
- `get_config()` singleton accessor with JSON loading from `config.json`
- `get_trading_config()` convenience accessor
- `get_obsidian_vault_path()` with `{USERPROFILE}` brace expansion (Windows fix)
- `reload()` for runtime config refresh

**Key decision:** Config values come from `config.json` at project root, not hardcoded. User can update `account_hkd` weekly without code changes.

#### `src/pricing/range_detector.py` — Range Detection (445 lines)

| Function | Returns | Data Source |
|----------|---------|-------------|
| `calc_atr(ticker, end_date, n=14)` | `float` — ATR value | SQLite OHLCV |
| `calc_n_day_high(ticker, end_date, n=252)` | `float` — N-day high | SQLite OHLCV |
| `calc_n_day_low(ticker, end_date, n=252)` | `float` — N-day low | SQLite OHLCV |
| `calc_pivot_points(ticker, end_date)` | `PivotPoints` — P, S1-S3, R1-R3 | SQLite OHLCV |
| `calc_fibonacci(swing_high, swing_low)` | `FibonacciLevels` — 23.6%, 38.2%, 50%, 61.8% | Calculated from swing H/L |
| `calc_consolidation_range(ticker, end_date, n=5)` | `ConsolidationRange` — low, high, width%, days | SQLite OHLCV |
| `calc_relative_volume(ticker, end_date, n=20)` | `float` — relative volume ratio | SQLite OHLCV |
| `calc_volume_profile(ticker, end_date, n=20)` | `VolumeProfile` — POC, VA high, VA low | SQLite OHLCV |
| `calc_20pct_study(date, conn, lookback=5)` | `TwentyPctStudy` — up/down 20% counts + tickers | SQLite OHLCV (TC2000 universe) |
| `calc_opening_range(ticker, end_date)` | `dict` — OR high, low, mid (first 3 bars) | FMP 5-min bars |
| `calc_low_of_day(ticker, end_date)` | `float` — intraday low | FMP 5-min bars |
| `calc_half_of_day(ticker, end_date)` | `float` — (open + low) / 2 | FMP 5-min bars |

All functions accept an optional `conn` parameter for database access; if omitted, a new connection is created and closed automatically.

**Data classes:** `ConsolidationRange`, `VolumeProfile`, `PivotPoints`, `FibonacciLevels`, `TwentyPctStudy`

#### `src/pricing/vwap.py` — VWAP Calculator (157 lines)

| Function | Returns | Purpose |
|----------|---------|---------|
| `get_daily_vwap(ticker, target_date)` | `float \| None` | Fetch VWAP from FMP EOD full endpoint |
| `calc_intraday_vwap(ticker, target_date)` | `dict` with `vwap`, `current_price`, `signal`, `bars` | Calculate running VWAP from 5-min bars |
| `_vwap_signal(price, vwap, tolerance=0.002)` | `str` — "above" / "below" / "neutral" | Internal signal classification |
| `calc_vwap_signal(price, vwap, tolerance=0.002)` | `str` | Public signal function |
| `is_entry_allowed(setup_type, vwap_signal)` | `(bool, str \| None)` | VWAP entry filter per setup rules |
| `get_effective_vwap(ticker, target_date)` | `float \| None` | Try daily VWAP first, fall back to intraday |

**VWAP entry filter rules (implemented):**
- **EP 9M:** VWAP warns but doesn't block (catalyst overrides)
- **DEP:** Blocks long entry below VWAP ("shows life" = above VWAP)
- **SOS:** Blocks long entry below VWAP (institutional buying confirmation)
- **ANT:** No VWAP check at BSLO time (pre-market); checked at open
- **Reversal:** VWAP not relevant (entered at 3:58 PM)
- **WSS (short):** Below VWAP = confirmed short signal, not blocked

#### `src/pricing/entry_exit.py` — Setup-Specific Entry/Stop/Target (326 lines)

- `EntryExitResult` dataclass with 18 fields: `ticker`, `setup_type`, `direction`, `entry_method`, `entry_price`, `stop_price`, `target`, `stop_width_pct`, `stop_rationale`, `vwap_signal`, `vwap_price`, `blocked`, `blocked_reason`, `entry_rationale`, `risk_reward_note`, `volume_ok`, `volume_note`, `risk_reward_ratio`
- `calc_setup_entry_exit()` — main function accepting ticker, setup type, date, quote, vwap result, and ranges
- `_compute_levels()` — calculates entry/stop/target for each setup type
- `_check_volume()` — validates volume thresholds by setup type

**Setup-specific entry logic (implemented):**

| Setup | Entry Method | Stop Logic | Target |
|-------|-------------|------------|--------|
| EP 9M | OPG (market-on-open) | ATR-based by price tier | Sell 80% at 100%+ gain |
| DEP | Direct (shows life: open + $0.10-0.30) | Below consolidation range | 40-300%+ over weeks |
| SOS | Breakout (prev_close × 1.04) | Low of day (>$100) or half of day | 3-5 day swing |
| ANT | BSLO (prev_close × 1.01) | Below consolidation range | Next day breakout |
| Reversal | 3:58 PM entry | Open × (1 - 0.5-2.5%) | Next day breakeven |
| WSS | Short bounce | Tight above entry (3-5%) | Gap down = take profit |

#### `src/pricing/position_sizing.py` — Fixed HKD Risk (195 lines)

- `PositionResult` dataclass with 16 fields: shares, position_usd, position_hkd, position_pct, risk_usd, risk_hkd, stop_width_pct, stop_price, entry_price, vwap_signal, warning, blocked, blocked_reason, confluence_bonus, setup_type, account_hkd
- `calculate_position()` — fixed HKD 3,000 risk with 25%/50% caps
- `suggest_stop_width()` — lookup table for setup × volatility
- `position_with_suggested_stop()` — convenience combining suggest + calculate
- `format_position_note()` — human-readable summary for Obsidian

**Key rules implemented:**
- Risk = HKD 3,000 per trade (fixed, not % of account)
- USD/HKD = 7.8 (configurable in `config.json`)
- Soft cap warning at 25% of account
- Hard cap at 50% for DEP + Sugar Baby confluence
- Hard cap at 25% for all other setups
- Below VWAP = blocked (position not calculated, returns shares=0)

#### `src/data/fmp_adapter.py` — Extended (added 2 methods)

- `get_intraday_5min(ticker, from_date, to_date)` — fetches 5-minute bars from `/stable/historical-chart/5min`
- `get_eod_full(ticker, from_date, to_date)` — fetches full EOD data including VWAP field from `/stable/historical-price-eod/full`

### Deviations from Design

| Design | Implemented | Reason |
|--------|-------------|--------|
| `calc_volume_profile()` returns POC/VA | Same as designed | ✅ No deviation |
| Volume thresholds: SOS 2x avg + 300K | Implemented as designed | ✅ |
| ATR calculation uses simple moving average | Same | ✅ |
| 20% study uses TC2000 universe filter | Same | ✅ |

### How to Use

```python
from src.pricing.range_detector import calc_atr, calc_consolidation_range, calc_20pct_study
from src.pricing.vwap import calc_intraday_vwap, is_entry_allowed
from src.pricing.entry_exit import calc_setup_entry_exit
from src.pricing.position_sizing import calculate_position, format_position_note
from src.config import get_trading_config

config = get_trading_config()
atr = calc_atr("NVDA", date(2026, 6, 13), n=14)
vwap = calc_intraday_vwap("NVDA", date(2026, 6, 13))
result = calculate_position(
    entry_price=135.20, stop_price=133.50,
    setup_type="DEP", vwap_signal="above",
    is_sugar_baby=True
)
print(format_position_note(result, "NVDA"))
```

---

## Phase 2 — MM Interpreter & Daily Briefing ✅

**Completed:** 2026-06-15
**Design doc:** [PHASE-2-MM-Interpreter.md](file:///D:/opencodeworkspace/.trading/docs/v2-design/PHASE-2-MM-Interpreter.md)

### What Was Built

#### `src/interpretation/mm_interpreter.py` — Regime Detection (377 lines)

**Data classes:**

| Class | Purpose |
|-------|---------|
| `RegimeResult` | Regime string, net primary, T2108, signals, 20% study data |
| `SetupGating` | Allowed longs/shorts, size multipliers per regime |
| `MMWarning` | Level (critical/important/info), message, source |
| `MMInterpretation` | Complete interpretation: regime, gating, warnings, summary, what_to_trade, what_to_avoid |

**Regime determination (implemented):**

| Regime | Condition | Allowed Long | Size |
|--------|-----------|-------------|------|
| Bullish | Net > 400, T2108 ≥ 10% | EP, SOS, DEP, ANT, SB | Full (1.0x) |
| Mildly Bullish | Net > 200 | EP, DEP, ANT | 80% (0.8x) |
| Weak Bull | Net > 0 | EP, DEP only | 50% (0.5x) |
| Bearish | Net > -200 | None (WSS shorts only) | 50% |
| Deep Bear | Net ≤ -200 | Reversal only | 30% |
| Capitulation | T2108 < 10% | Reversal (aggressive) | 30% |

**Breadth signals (8 types):**
- `yesterday_was_the_day` (breakout > 300)
- `selling_pressure` (breakdown > 300)
- `oversold_bounce` (T2108 < 20%)
- `capitulation_zone` (T2108 < 10%)
- `overbought_caution` (T2108 > 85%)
- `second_day_rule` (yesterday breakout > 200)
- `extreme_20pct_up` (> 50 stocks up 20%+)
- `extreme_20pct_down` (> 50 stocks down 20%+)

**Contextual warnings:**
- Always: "Focus list < 5 stocks", "Articulate your reason in one sentence", "Don't enter long below VWAP"
- Per-regime: choppy warnings (mildly bullish), size reduction (weak bull), bear caution, deep bear restrictions, capitulation rules

**Main function:** `interpret_mm(stockbee_data, twenty_pct_study=None)` → `MMInterpretation`

#### `src/interpretation/briefing_generator.py` — Obsidian Daily Briefing (313 lines)

Generates a full Obsidian markdown note with YAML frontmatter and 13 sections:

1. **Regime call** — emoji indicator (🟢/🟡/🟠/🔴/⚫)
2. **Market Monitor** — StockBee official data table
3. **20% Study** — stocks up/down 20%+
4. **What to Trade Today** — setup gating table
5. **What to Avoid** — bullet list with reasons
6. **A+ Confluences** — SB + setup, max 50% position
7. **A Confluences** — SB + DEP, large position
8. **EP 9M Candidates** — entry/stop/VWAP/shares/risk
9. **SOS Breakouts** — entry/stop/VWAP/shares/risk
10. **DEP Watchlist** — entry/stop/VWAP/shares/risk
11. **Anticipation Setups** — BSLO trigger/stop/shares
12. **Sugar Babies Without Setup** — watch list
13. **Key Warnings** — bullet list

**Output path:** `C:\Users\msh897\Documents\Obsidian\trading-vault\Daily Briefing\YYYY-MM-DD.md`

**YAML frontmatter:** title, date, tags, regime, primary_net, t2108

**Main function:** `generate_daily_briefing(interpretation, scan_results, entry_exit_results, position_results, cross_reference_results, stockbee_data, output_dir=None)` → `str` (file path)

**Helper functions:**
- `_fmt_num(value)` — format numbers with commas
- `_safe_get(d, key, default)` — safe dict access
- `_position_cells(pos)` — format position sizing cells for tables
- `_build_setup_table(candidates, scan_type, pos_map, entry_exit_map, vwap_map)` — build setup-specific markdown table

### How to Use

```python
from src.data.stockbee_scraper import fetch_stockbee_mm
from src.interpretation.mm_interpreter import interpret_mm
from src.interpretation.briefing_generator import generate_daily_briefing
from src.pricing.range_detector import calc_20pct_study
from src.data.db import get_db

# 1. Fetch StockBee data (sole truth)
sb_data = fetch_stockbee_mm()

# 2. Get 20% study from our data
conn = get_db()
twenty_pct = calc_20pct_study(date.today(), conn)

# 3. Interpret MM
interpretation = interpret_mm(sb_data, twenty_pct)

# 4. Generate briefing
briefing_path = generate_daily_briefing(
    interpretation=interpretation,
    scan_results=scan_results,      # from scanner
    entry_exit_results=ee_results,   # from entry_exit
    position_results=pos_results,   # from position_sizing
    cross_reference_results=[],     # from cross_reference (Phase 5)
    stockbee_data=sb_data,
)
```

---

## Phase 5 — SB Cross-Reference + Nightly Pipeline Integration ✅

**Completed:** 2026-06-16
**Design doc:** [PHASE-5-Integration.md](file:///D:/opencodeworkspace/.trading/docs/v2-design/PHASE-5-Integration.md)

### What Was Built

#### `src/scans/cross_reference.py` — SB × Setup Confluence Engine (487 lines)

The missing piece that ties Sugar Babies to active setups with entry/exit and position sizing.

**Confluence tiers:**

| Tier | Criteria | Position Cap | Example |
|------|----------|-------------|---------|
| **A+** | SB + active setup + strong catalyst | 50% | NVDA is a Sugar Baby + DEP + earnings tomorrow |
| **A** | SB + active setup | 50% | NVDA is a Sugar Baby + DEP (no catalyst) |
| **B+** | Active setup + catalyst (no SB) | 25% | AMD has DEP + earnings |
| **B** | Active setup only | 25% | DELL has SOS today |
| **C** | SB only (watch) | N/A | AAPL is a Sugar Baby, no active setup |

**Data class:** `ConfluenceResult` — ticker, tier, setup type, SB flag, catalyst flag, entry/exit, position, warning, details

**Key functions:**

| Function | Returns | Purpose |
|----------|---------|---------|
| `cross_reference(scan_results, target_date, ...)` | `list[ConfluenceResult]` | Main cross-reference engine |
| `summarize_confluences(results)` | `dict` | Counts by tier and setup type |
| `save_cross_reference_results(results, target_date)` | `int` | Persist to `confluence_results` table |
| `load_cross_reference_results(target_date)` | `list[ConfluenceResult]` | Load from DB |
| `run_full_confluence_pipeline(target_date)` | `tuple` | High-level: fetch MM → cross-reference → save → summarize |

**New DB table:** `confluence_results` — stores daily cross-reference results with entry/stop/shares/position fields, unique on (date, ticker).

**Enrichment logic:** For A+/A/B+/B tier candidates, the engine automatically:
1. Fetches VWAP from `get_effective_vwap()` (daily first, intraday fallback)
2. Calculates consolidation range for DEP/ANT setups
3. Calls `calc_setup_entry_exit()` for entry/stop/target
4. Calls `calculate_position()` with SB confluence bonus
5. Records any VWAP blocks or cap warnings

#### `src/cli/nightly_runner.py` — 9-Step Pipeline (487 lines, fully refactored)

Replaced the old 5-step pipeline with the complete v2 9-step pipeline:

| Step | Function | What It Does |
|------|----------|--------------|
| 0 | `step0_fetch_stockbee()` | Fetch StockBee MM data (sole truth) |
| 1 | `step1_fetch_quotes()` | Batch-quote all TC2000 tickers (~6K) |
| 2 | `step2_insert_ohlcv()` | Upsert OHLCV into SQLite |
| 3 | `step3_run_scans()` | Run all 7 setup scans (EP, SOS, DEP, ANT, WSS, Reversal, SB) |
| 4 | `step4_calculate_ranges()` | Calculate 20% study from SQLite |
| 5 | `step5_entry_exit()` | Entry/stop/target + VWAP filter for each candidate |
| 6 | `step6_position_sizing()` | HKD 3,000 risk, 25%/50% caps per candidate |
| 7 | `step7_cross_reference()` | SB × setup confluence with enrichment |
| 8 | `step8_interpret_mm()` | Regime call, setup gating, warnings |
| 9 | `step9_generate_briefing()` | Full Obsidian daily briefing note |

**New CLI flags:** `--no-briefing`, `--no-scans`, `--sample N`

**Catalyst enrichment** runs between Steps 6 and 7 — enriches unique tickers from all scans with earnings + momentum data, feeding into the confluence engine.

#### `src/cli/scanner.py` — Updated with `--briefing` flag (606 lines)

Added `--briefing` flag to `scanner.py all` that:
1. Runs 20% study via `calc_20pct_study()`
2. Fetches fresh StockBee MM interpretation
3. Runs cross-reference engine with current scan results + catalysts
4. Calculates entry/exit + position sizing for all candidates
5. Generates v2 daily briefing via `generate_daily_briefing()`

**Usage:**
```bash
py src/cli/scanner.py all --briefing     # Run all scans + generate v2 briefing
py src/cli/scanner.py all                # Run all scans + v1 note only
```

### Data Backfill — Complete

**DB status after backfill:**

| Metric | Value |
|--------|-------|
| OHLCV rows | 6,847,562 |
| TC2000 universe tickers | 6,479 |
| Tickers with FMP data | 6,080 (93.8%) |
| Tickers marked unavailable | 399 (SPAC units, rights, warrants, delisted) |
| Sugar Babies | 600 |
| Date range | 2022-06-23 to 2026-06-15 |

The 399 unavailable tickers are SPAC units (`.U`), rights (`.RT`), warrants (`.WI`), and delisted shells — not tradeable stocks. Marked `fmp_available=0` in `tc2000_universe` table.

---

## Phase 3 — Telegram Alerts & Trade Recording ✅

**Completed:** 2026-06-16
**Design doc:** [PHASE-3-Telegram-Alerts.md](file:///D:/opencodeworkspace/.trading/docs/v2-design/PHASE-3-Telegram-Alerts.md)

### What Was Built

#### `src/alerts/telegram_alerts.py` — Alert Sender (340 lines)

- `TelegramAlerter` class using `httpx` and Telegram Bot API
- HTML parse mode with proper escaping
- Quiet hours support (configurable via `config.json`)
- Priority-based suppression (`critical`/`high` bypass quiet hours)
- Formatted alert methods: test, pre-market briefing, setup trigger, VWAP block, EOD summary, regime change, trade entry/exit, stop out, status, P&L
- Volume formatting helper (M/K)

#### `src/alerts/trade_recorder.py` — Trade Recording (300 lines)

- `TradeRecorder` class: `record_entry()`, `record_exit()`, `add_note()`, `get_open_trades()`, `get_closed_trades_today()`
- Trade state persisted to `.trading/data/active_trades.json`
- Obsidian journal notes written to `trading-vault/Trade Journal/YYYY/TICKER-YYYY-MM-DD.md`
- Auto-calculates risk, P&L, and R-multiple
- Notes append to both JSON and Obsidian note

#### `src/alerts/bot_handler.py` — Command Router (350 lines)

- Long-polls Telegram `/getUpdates`
- Commands: `/enter`, `/exit`, `/stop`, `/note`, `/status`, `/pnl`, `/help`
- Strips bot username suffix (e.g., `/status@trading_radar_bot`)
- Sends confirmation replies via `TelegramAlerter`
- `handle_text()` for CLI testing

#### `src/alerts/intraday_monitor.py` — Market-Hours Monitor (240 lines)

- Polls FMP quotes for today's candidates
- Trigger logic:
  - Setup entry trigger when price crosses entry level
  - VWAP block warning when price drops below VWAP (long setups)
  - VWAP confirmation when price crosses above VWAP
  - Stop hit alert when price touches stop
- Throttles repeat alerts (10 min cooldown)
- 60s poll during 9:30-10:00 ET, 5 min poll during 10:00-16:00 ET
- Skips outside US market hours

#### `src/cli/bot_runner.py` — Main Bot Loop (180 lines)

- Combines: command polling + scheduled alerts + intraday monitor
- Scheduled jobs:
  - 8:30 AM ET: pre-market briefing (runs nightly pipeline)
  - 4:15 PM ET: EOD summary
  - 9:00 AM ET: reset intraday monitor for new day
- CLI flags: `--test` (single poll), `--send-test`, `--command '/status'`
- Graceful shutdown on Ctrl+C / SIGTERM
- Sends "bot online" / "bot shutting down" messages

### Commands

| Command | Example |
|---------|---------|
| Start bot | `py src/cli/bot_runner.py` |
| Test mode | `py src/cli/bot_runner.py --test` |
| Send test alert | `py src/cli/bot_runner.py --send-test` |
| Simulate command | `py src/cli/bot_runner.py --command "/status"` |

### Bot Commands (Telegram)

```
/enter TICKER SETUP SHARES PRICE STOP [NOTE]
/exit TICKER PRICE REASON
/stop TICKER PRICE
/note TICKER TEXT
/status
/pnl
/help
```

### Status / Known Issues

- ✅ All modules compile and import successfully
- ✅ Trade recorder entry/exit/journal works locally
- ✅ Bot command parsing works
- ✅ Intraday monitor runs correctly outside market hours
- ⚠️ Telegram API returns **403 Forbidden** — the bot token in `config.json` appears invalid or revoked. The user must create a new bot via @BotFather and update the token.

---

## What's Next

### Phase 4 — Transcript Backfill (Parallel)

- ~150 StockBee meetings (Nov 2023 – Apr 2025)
- Deepgram transcription → curated Obsidian notes
- Budget: ~$135 (within $150.03 credit)

---

## File Map (Phase 1, 2, 3 & 5)

```
src/
├── config.py                          # [Phase 1] Config loader
├── pricing/                           # [Phase 1]
├── interpretation/                    # [Phase 2]
├── scans/
│   ├── cross_reference.py            # [Phase 5] SB × setup confluence
│   └── ... (existing 7 scans)
├── alerts/                            # [Phase 3] NEW package
│   ├── __init__.py
│   ├── telegram_alerts.py            # Telegram sender + formatters
│   ├── trade_recorder.py             # Trade entry/exit → JSON + Obsidian
│   ├── bot_handler.py                # Command parser + router
│   └── intraday_monitor.py           # Market-hours quote polling
├── cli/
│   ├── nightly_runner.py             # [Phase 5] 9-step pipeline
│   ├── scanner.py                    # [Phase 5] --briefing flag
│   └── bot_runner.py                 # [Phase 3] Bot main loop
└── data/
    └── fmp_adapter.py                 # [Phase 1] Extended
```

**Total new code (Phase 3):** ~1,210 lines across 5 files
**Total new code (all phases):** ~4,603 lines across 14 files

---

## Key Design Decisions (Added)

| # | Decision | Rationale | Date |
|---|----------|-----------|------|
| 8 | Confluence tiers A+/A/B+/B/C | Matches Pradeep's priority | 2026-06-16 |
| 9 | Enrich only top N candidates (150) | Saves FMP API calls | 2026-06-16 |
| 10 | SPAC units/rights/warrants = not tradeable | 399 unavailable tickers marked | 2026-06-16 |
| 11 | Trade state in JSON, journal in Obsidian | JSON for app state, Obsidian for human record | 2026-06-16 |
| 12 | HTML parse mode for Telegram | Better formatting than Markdown; escape for safety | 2026-06-16 |
| 13 | Intraday monitor throttling (10 min) | Avoid alert spam on noisy quotes | 2026-06-16 |