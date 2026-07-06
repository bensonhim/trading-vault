---
title: "Pradeep Ultratrader — Bottom-Up Market Analysis Framework"
date: 2026-07-03
tags: [design, pradeep-ultratrader, market-analysis, bottom-up, sector-rs, validation, x-api]
---

# Pradeep Ultratrader — Bottom-Up Market Analysis Framework

> Post-Wave 10 improvement plan. Addresses the discrepancy found on 2026-07-02 where our pipeline said "bullish, 63 actionable" while Pradeep said "choppy, no actionable longs, don't bet."
>
> **Root cause:** Our pipeline is top-down (one breadth indicator → regime → allow all longs). Pradeep's analysis is bottom-up (individual stocks → sector → market → conclusion).

## The Problem

On 2026-07-02, Pradeep's session said:
- "The rally was three days old already"
- "20% study greater than 100 — caution territory"
- "Semiconductors showing top-forming signature"
- "Rotation into beaten-down names is a trap"
- "I don't see anything which is actionable"

Our pipeline said:
- Regime: bullish (net_primary = +590)
- 63 actionable candidates (2 A+, 42 B+, 19 B)
- All long setups allowed

**Three missing pieces:**
1. 20% study signal was `info` level (not gating)
2. No rally maturity tracking (3 days old = mature)
3. No sector top detection (semis rolling over)

## The Solution: Bottom-Up Framework

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 1: Individual Stock Behavior                          │
│  • 4%+ breakout scan (done)                                  │
│  • Breakout follow-through tracking (new)                    │
│  • Failed breakout detection (new)                           │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: Sector Behavior                                     │
│  • Sub-sector ETF RS vs SPY (new)                            │
│  • Leading sector identification (new, dynamic)              │
│  • Leading sector top-forming detection (new)                │
│  • Breakout density by sector (new)                          │
├─────────────────────────────────────────────────────────────┤
│  Layer 3: Overall Market                                     │
│  • StockBee MM (done)                                        │
│  • 20% study upgraded to gating (fix 1)                     │
│  • Rally maturity tracking (fix 2)                          │
│  • Breadth quality check (new)                               │
│  • Composite regime: bullish / distributing / bearish        │
├─────────────────────────────────────────────────────────────┤
│  Output: Decision Gating                                     │
│  • FULL LONG: all three layers confirm bullish                │
│  • REDUCE SIZE: rally mature + overbought                    │
│  • NO NEW LONGS: leading sector rolling over + distributing  │
│  • SHORTS ONLY: all three layers bearish                     │
└─────────────────────────────────────────────────────────────┘
```

### Gating Decision Matrix

| Layer 1 (Stocks) | Layer 2 (Sector) | Layer 3 (Market) | Action |
|---|---|---|---|
| Breakouts following through | Leading sector up | Bullish, not overbought | FULL LONG |
| Breakouts but weak | Leading sector flat | Rally mature + overbought | REDUCE SIZE, tighten stops |
| Breakouts failing | Leading sector down SOS | Breadth from beaten-down, not leaders | NO NEW LONGS |
| No breakouts | Leading sector down | Bearish | SHORTS ONLY or cash |

### What 2026-07-02 would have looked like

| Layer | Finding | Conclusion |
|-------|---------|------------|
| Layer 1 | Semis failing breakouts (NVDA, LRCX, MU, AMD all down) | Failed breakouts in leaders |
| Layer 2 | Leading sector (semis) printed range-expansion down day → SOS to downside | Leading sector rolling over |
| Layer 3 | 20% study at 93 (overbought), rally 3 days old (mature), breadth +590 but from beaten-down rotation | Distributing |
| **Composite** | | **NO NEW LONGS — matches Pradeep** |

## Sub-Sector ETF Universe

~30 sub-sector ETFs for granular sector analysis. RS vs SPY computed nightly.

| Theme | ETF Tickers | What It Tracks |
|-------|-------------|----------------|
| Semiconductors | SOXX, SMH | NVDA, AMD, MRVL, MU |
| AI/Tech | AIQ | AI infrastructure |
| Cybersecurity | BUG | CRWD, PANW, S |
| Cloud Computing | SKYY | NET, DDOG, SNOW |
| Biotech | IBB, XBI | Small & large biotech |
| Clean Energy | ICLN | ENPH, SEDG, FSLR |
| Quantum | QTUM | Quantum theme |
| Fintech | FINX | HOOD, SQ, PYPL |
| Space Economy | UFO | RKLB, ASTS, SPCE |
| Aerospace/Defense | PPA | LMT, RTX, NOC |
| Digital Payments | DPOP | V, MA, PYPL |
| Genomics | GNOM | DNA sequencing |
| EV | DRIV | TSLA, RIVN, LI |
| Blockchain | BLOK | COIN, MSTR |
| Home Construction | ITB | PHM, DHI, LEN |
| Energy | XLE, XOP | XOM, CVX |
| Financials | XLF | JPM, BAC, GS |
| Healthcare | XLV | UNH, JNJ |
| Consumer Discretionary | XLY | AMZN, TSLA |
| Gold Miners | GDX | NEM, GOLD |
| Silver Miners | SIL | Silver miners |
| Technology (broad) | XLK | AAPL, MSFT, NVDA |
| Communications | XLC | META, GOOG, NFLX |
| Industrials | XLI | BA, CAT, GE |
| Utilities | XLU | Defensive rotation |
| Real Estate | XLRE | Defensive |
| Materials | XLB | Materials |
| Infrastructure | PAVE | Infrastructure |
| SPY (benchmark) | SPY | S&P 500 |

**Leading sector identification:**
- RS_20d = ETF_20d_return / SPY_20d_return
- RS_65d = ETF_65d_return / SPY_65d_return
- Leading sector = highest RS_20d with RS_65d > 1.0 (sustained outperformance)
- If leading sector's ETF prints range-expansion down day → top-forming warning

## X/Twitter API Integration

### Accounts to Monitor

| Account | Handle | Role | What We Extract |
|---------|--------|------|-----------------|
| Pradeep Bonde | @PradeepBonde | Ground truth | Real-time market calls, regime warnings, stock mentions |
| Kelileo | @KelileoCUP | Community signal | StockBee community sentiment, ticker ideas |
| All-In Podcast | @theallinpod | Thematic context | Macro/tech narrative, sector themes |
| Charlie Bilello | @charliebilello | Quant cross-check | Independent breadth stats, market data, historical comparisons |

### What We Extract From Each Post

For each post from these accounts:
- **Text content** — for keyword extraction (ticker mentions, market direction calls)
- **Date/time** — to align with market sessions
- **Engagement** — likes/retweets as sentiment proxy
- **Ticker mentions** — $TICKER cashtag extraction
- **Sentiment** — bullish/bearish/neutral classification (keyword-based)

### Integration Points

1. **Layer 2 (Sector):** If @PradeepBonde posts about semis failing → weight sector top-forming detection higher
2. **Layer 3 (Market):** If @charliebilello posts breadth stats → cross-check against our 20% study
3. **Thematic context:** @theallinpod posts about AI/crypto/clean energy → tag as sector narrative momentum
4. **Community signal:** @KelileoCUP posts about specific tickers → check if they appear in our scan results
5. **Ground truth comparison:** @PradeepBonde's market calls → store in `pradeep_daily_conclusions` for validation

### X API Details

- API: https://docs.x.com/x-api/introduction
- Fetch recent posts from 4 accounts daily (post-market)
- Store in `x_posts` table: (author, date, text, tickers_mentioned, sentiment, engagement)
- Include in nightly pipeline as Step 0.8 (after Sugar Babies, before scans)
- Cross-reference ticker mentions with scan results in confluence

## Validation Against Pradeep's Sessions

### Available Data

42 session notes in `06-Daily/stockbee/Sessions/` spanning 2026-05-01 to 2026-07-02.

### Validation Process

**Phase C-1: Extract conclusions**
From each session note, extract:
- Date
- Regime call (bullish / bearish / choppy / no-action / cautious)
- Active sectors mentioned
- Active tickers with setup types
- Key warnings ("rally mature", "top forming", "distributing", "don't chase")
- Actionable advice ("EP 9M only", "no new longs", "shorts only")

Store in `pradeep_daily_conclusions` SQLite table.

**Phase C-2: Run pipeline for same dates**
Run our pipeline for all 42 dates and capture:
- Our regime
- Our actionable count
- Our 20% study signal
- Our sector signals (after Phase A+B)

**Phase C-3: Compare**
| Date | Pradeep's Conclusion | Our Pipeline's Conclusion | Match? | Gap |
|------|---------------------|--------------------------|--------|-----|
| 2026-07-02 | Cautious, no new longs | Bullish, 63 actionable | ❌ | 20% study gating, rally maturity, sector top |
| ... | ... | ... | ... | ... |

**Phase C-4: Iterate**
- If <70% match → identify systemic gaps and fix
- If "no actionable" days produce "actionable" results → tighten gating
- Track improvement over iterations

## Knowledge Integration (Phase D)

After validation converges:
1. Store Pradeep's historical conclusions as context
2. When pipeline runs, check: "similar market conditions on date X → Pradeep said Y"
3. Include historical context in daily briefing: "Similar conditions: 2026-06-15, Pradeep said: 'don't chase'"
4. This bridges quantitative pipeline with qualitative session knowledge

## Database Schema Additions

```sql
-- Sub-sector ETF RS
CREATE TABLE IF NOT EXISTS sector_rs (
    date TEXT NOT NULL,
    etf_ticker TEXT NOT NULL,
    theme TEXT,
    rs_20d REAL,        -- ETF 20d return / SPY 20d return
    rs_65d REAL,        -- ETF 65d return / SPY 65d return
    etf_return_20d REAL,
    etf_return_65d REAL,
    spy_return_20d REAL,
    spy_return_65d REAL,
    is_leading BOOLEAN,  -- highest RS_20d with RS_65d > 1.0
    range_expansion_down BOOLEAN, -- ETF printed SOS to downside today
    PRIMARY KEY (date, etf_ticker)
);

-- Pradeep's daily conclusions (extracted from session notes)
CREATE TABLE IF NOT EXISTS pradeep_daily_conclusions (
    date TEXT PRIMARY KEY,
    regime_call TEXT,      -- bullish / bearish / choppy / no_action / cautious
    active_sectors TEXT,   -- comma-separated
    active_tickers TEXT,   -- comma-separated with setup types
    key_warnings TEXT,     -- rally_mature, top_forming, distributing, etc.
    actionable_advice TEXT,-- EP_9M_only, no_new_longs, shorts_only
    session_note_path TEXT
);

-- X/Twitter posts
CREATE TABLE IF NOT EXISTS x_posts (
    id TEXT PRIMARY KEY,
    author TEXT NOT NULL,
    date TEXT NOT NULL,
    text TEXT,
    tickers_mentioned TEXT,   -- comma-separated
    sentiment TEXT,           -- bullish / bearish / neutral
    likes INTEGER,
    retweets INTEGER,
    fetched_at TEXT
);

-- Rally maturity tracking
CREATE TABLE IF NOT EXISTS rally_maturity (
    date TEXT PRIMARY KEY,
    days_since_low INTEGER,
    low_date TEXT,
    low_t2108 REAL,
    low_net_primary INTEGER,
    current_t2108 REAL,
    current_net_primary INTEGER,
    is_mature BOOLEAN,         -- days_since_low >= 3
    is_overbought BOOLEAN      -- 20% study > 50
);
```

## Implementation Phases

### Phase A: Sub-Sector ETF Infrastructure
1. Add ~30 sub-sector ETFs to ETF cache
2. Fetch daily OHLCV for all sub-sector ETFs
3. Compute RS_20d and RS_65d vs SPY
4. Identify leading sector nightly
5. Detect leading sector range-expansion down day (top forming)
6. Include sub-sector heatmap in daily briefing

**Files:** `src/data/etf_tagging.py` (add sub-sector list), `src/scans/sector_rs.py` (new), `src/interpretation/briefing_generator.py` (heatmap)

### Phase B: Bottom-Up Market Analysis
1. Count breakouts/breakdowns by sector from daily 4% scan
2. Detect rotation trap (breadth positive but from beaten-down, not leaders)
3. Track rally maturity (days since last market low)
4. Upgrade 20% study from `info` to `important`/`critical` level
5. Composite regime: combine Layer 1+2+3 into single gating decision

**Files:** `src/interpretation/mm_interpreter.py` (upgrade 20% study, add composite regime), `src/scans/market_monitor.py` (rally maturity), `src/interpretation/bottom_up_analyzer.py` (new)

### Phase C: Validation Against Pradeep's Sessions
1. Build session note parser to extract conclusions
2. Populate `pradeep_daily_conclusions` table for all 42 dates
3. Run pipeline for all 42 dates
4. Compare and identify systemic gaps
5. Iterate fixes until >80% match

**Files:** `src/validation/session_parser.py` (new), `src/validation/pipeline_comparison.py` (new), `src/cli/backtest_runner.py` (new)

### Phase D: Knowledge Integration
1. Embed historical Pradeep conclusions in pipeline context
2. Pattern-match current conditions to historical sessions
3. Include "similar conditions" references in daily briefing
4. Bridge quantitative + qualitative knowledge

**Files:** `src/interpretation/historical_context.py` (new), `src/interpretation/briefing_generator.py` (add historical context section)

### Phase E: X/Twitter Integration
1. Set up X API access (API key in .env)
2. Fetch daily posts from 4 accounts post-market
3. Extract ticker mentions and sentiment
4. Cross-reference with scan results
5. Include in nightly pipeline as Step 0.8

**Files:** `src/data/x_scraper.py` (new or update existing `src/signals/x_catalyst.py`), `src/cli/nightly_runner.py` (add Step 0.8)

## See Also

- [[Pradeep Ultratrader — Design]] — overall architecture
- [[Pradeep Ultratrader — Technical Definitions]] — precise definitions
- [[Pradeep Ultratrader — Implementation Plan]] — 10-wave implementation (all complete)
- [[_Trading Radar Engine v2 — Implementation Notes]] — previous design