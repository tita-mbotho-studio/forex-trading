# EA acceptance test plan

Planned checks, not completed tests:

- Compile MQL5 with MetaEditor; record errors and warnings.
- Test buy and sell with valid SL/TP and both operating modes.
- Check manual entries, pre-existing SL/TP, multiple symbols, and duplicate event handling.
- Validate account equity calculations, tick rounding, volume steps and broker stop/freeze levels.
- Test invalid parameters, rejected orders/modifications, disconnection and recovery; verify alerts.
- Test hedging and netting separately, including added/reduced positions.
- Test representative Forex, metal, index and synthetic/crypto instruments when available on the demo broker.
- Record execution costs, spread and slippage; assess actual versus planned loss and profit.
- Confirm no unsolicited orders are opened.

Document broker, symbol, terminal version, account mode, expected result, actual result and pass/fail. Do not use live funds for acceptance tests.
