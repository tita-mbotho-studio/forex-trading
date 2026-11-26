# Universal Risk Manager EA

Status: planned; no MQL5 source or compiled EA is included yet.

A standalone MetaTrader 5 risk manager, not a signal generator. Default intended settings: 1% of account equity as planned risk, 2% equity as gross target, configurable; preserve existing SL/TP by default. No autonomous strategy entries.

- Mode A: detect manual positions and attempt to attach missing SL/TP after execution.
- Mode B: user clicks BUY/SELL; calculate protection before sending the order with SL/TP.
- Design for buy/sell, multiple symbols and timeframes, and broker-specific tick sizes, volume steps, account currencies, stop/freeze levels and order rules.
- Validate the chosen volume and stop distance; report impossible or rejected protection instead of silently increasing risk. Account for existing protection, costs, and multiple positions. Netting and hedging semantics must be tested separately.
- One-click mode should support sizing from a user-selected valid stop distance; automatic mode must not pretend that a fixed lot size implies a suitable technical stop.
- MT5 terminal or compatible VPS must remain running for automated detection; mobile orders may be managed through that terminal. Broker execution restrictions apply.

SL/TP attachment may fail or be delayed; slippage, gaps and costs can exceed intended risk. No guarantee of exact maximum loss or universal broker compatibility. Demo-test first.

See [testing plan](TESTING.md).
