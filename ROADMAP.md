# Implementation roadmap

Each implementation is reviewed on its own branch and merged only after explicit user approval. Planned deliverables are not yet implemented.

| ID | Deliverable | Scope |
| --- | --- | --- |
| 00 | Project setup | Structure, navigation, workflow and validation |
| 01 | Introduction to Forex Trading | Currency pairs, bid/ask, long/short, brokers and other markets. |
| 02 | Essential Trading Terminology | Pips, ticks, lots, costs, leverage, margin, equity and stop-outs. |
| 03 | Trading Sessions and Timeframes | SAST, daylight saving, liquidity, volatility and M1 considerations. |
| 04 | MetaTrader 5 | Demo setup, charts, orders, SL/TP, trailing stops, hedging and netting. |
| 05 | Technical Analysis | Candlesticks, trend, support/resistance, breakouts and multiple timeframes. |
| 06 | Technical Indicators | MA, EMA, RSI, MACD, ATR, Bollinger Bands and Fibonacci retracement. |
| 07 | Fundamental Analysis | Rates, CPI, GDP, NFP, central banks and economic calendars. |
| 08 | Risk Management | Sizing, SL/TP, R:R, break-even, drawdown, exposure, execution costs and daily limits. |
| 09 | Trading Psychology | How predefined risk and rules reduce emotional pressure; discipline and loss acceptance. |
| 10 | Simple Demo Trading Strategy | One rule-based trend-following pullback strategy; test without claims of profitability. |
| 11 | Trading Journal and Performance | Track trades, outcomes, costs, rule adherence and basic performance. |
| 12 | Universal Risk Manager EA | Strategy-independent MT5/MQL5 automatic SL/TP and protected order entry; demo validation. |
| 13 | Final course audit | Check links, calculations, lesson consistency and EA test evidence |

## Notebook delivery

- 02: pip/tick values, profit/loss, leverage/margin.
- 08: position sizing, SL/TP, risk-to-reward, drawdown/recovery.
- 11: trading performance.

Deliver each notebook alongside its relevant lesson. Include concise theory, formula, worked example, reusable Python function, validation examples, verified online calculator links where available, and limitations.

## Review gate

Implementation 00 is scaffolding only. No trading strategy, calculation notebook or EA code is considered complete until its own implementation passes review.
