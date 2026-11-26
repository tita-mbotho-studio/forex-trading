# Module 02 — Essential Trading Terminology

**Study time:** approximately 45 minutes for the lesson and initial notebook examples.  
**Goal:** understand the numbers on your trading platform and what they mean for your money.

[Back to course outline](README.md) · [Previous: Module 01](01-introduction.md)

All prices and account amounts are hypothetical, not live quotes.

## 1. Pips, points and ticks

| Term | Meaning | Example: five-decimal EUR/USD |
| --- | --- | --- |
| Pip | Conventional Forex price-movement unit | 0.0001 |
| Point | MT5 display unit | 0.00001 |
| Tick size | Smallest permitted price increment | Often 0.00001; verify the symbol |

Most non-JPY FX pairs use a pip size of 0.0001; JPY-quoted pairs usually use 0.01. Tick can also mean a quote update. Ten points equal one pip on a typical five-decimal EUR/USD or three-decimal USD/JPY quote. Do not apply that rule to every symbol.

Example: EUR/USD moves from 1.10000 to 1.10250. The move is 25 pips (250 points for a five-decimal quote). The pip value depends on position volume and currency conversion.

## 2. Lots and contract size

A lot is the broker's unit of trading volume; the contract size determines the number of underlying units in one lot.

| Forex volume | Common name | Units for a 100,000-unit contract |
| --- | --- | ---: |
| 1.00 | Standard | 100,000 |
| 0.10 | Mini | 10,000 |
| 0.01 | Micro | 1,000 |

These are common FX conventions, not universal. On a USD account, EUR/USD with a standard 100,000-unit contract typically has a $10 pip value at 1 lot, $1 at 0.10 lots and $0.10 at 0.01 lots. On other pairs or in other account currencies, conversion may be necessary.

On MT5 desktop, right-click a symbol in Market Watch and select Specification to inspect contract size, tick size/value, and minimum/maximum volume and volume step. Never assume gold, indices or synthetic symbols share Forex specifications.

**Calculator:** [Notebook 01 — Pips and tick values](../notebooks/01_pips_and_tick_values.ipynb).

## 3. Trading costs and profit/loss

- **Spread:** difference between ask and bid. With bid 1.10000 and ask 1.10020, the spread is 2 conventional EUR/USD pips.
- **Commission:** fee charged by the broker; may be charged per side or round trip.
- **Swap:** overnight financing adjustment, which can be a charge or credit; rules vary by product and account.
- **Slippage:** difference between requested or expected execution price and actual fill. It is not necessarily a fee and can be favourable or unfavourable.

Gross P/L is the trade result before separate fees; net P/L includes applicable charges and credits. For a Forex buy, a higher executed exit price is favourable; for a sell, a lower executed exit price is favourable.

Example: buy 0.10 lots EUR/USD at 1.1002 and close at 1.1050 on a USD account, with a 100,000-unit contract. Gross profit is $48. With $1.20 commission and $0.30 swap charge, net profit is $46.50. Since the prices are executed prices, the spread must not be subtracted again.

**Realised P/L** relates to closed positions; **unrealised (floating) P/L** relates to positions that remain open.

**Calculator:** [Notebook 02 — Profit and loss](../notebooks/02_profit_and_loss.ipynb).

## 4. Leverage and margin

Leverage allows exposure larger than the collateral required to open a position. 1:100 leverage means a ratio of 100; a simple $10,000 notional position at that ratio requires $100 margin, assuming no other margin multipliers.

| Leverage | Illustrative margin for $10,000 exposure |
| --- | ---: |
| 1:20 | $500 |
| 1:50 | $200 |
| 1:100 | $100 |

Margin is collateral, not a trading fee, and not the maximum possible loss. Higher leverage reduces the margin required for the same position but does not reduce the monetary loss from a given price movement. It can make excessive exposure easier.

## 5. Balance, equity and free margin

Imagine the following simplified USD demo account with no credits, blocked funds or unbooked fees:

| Account measure | Meaning | Example |
| --- | --- | ---: |
| Balance | Funds after settled transactions | $1,000 |
| Floating P/L | Current result of open positions | −$100 |
| Equity | Current account value including floating P/L | $900 |
| Used margin | Collateral currently required | $110 |
| Free margin | Equity less used margin | $790 |
| Margin level | Equity divided by used margin, expressed as a percentage | 818.18% |

Equity changes while positions are open. In this simplified example, if you close the losing position with no further price changes or fees, balance becomes $900. Actual MT5 calculations may also include credit, commissions or blocked funds. When used margin is zero, the margin-level ratio is undefined.

**Calculator:** [Notebook 03 — Leverage and margin](../notebooks/03_leverage_and_margin.ipynb).

## 6. Margin call and stop-out

A margin call is a broker-defined warning or restriction associated with inadequate account margin. A stop-out is forced liquidation of positions when the applicable threshold is breached. Thresholds and mechanics depend on account and broker rules; you might not receive a warning in fast markets.

Neither is a substitute for a planned stop loss. A stop loss is a protective instruction and can execute beyond its requested price during gaps or slippage. We will cover position sizing and planned equity risk in Module 08.

## 7. Practice and knowledge check

Open the three notebooks in the order shown above. Run all cells, then change the sample inputs. If MT5 is installed, observe a symbol's contract size, point/tick size, volume step and account currency on a demo account; no order is required.

Answer before opening the solutions:

1. EUR/USD changes from 1.10100 to 1.10300. How many conventional pips and five-decimal points?
2. How many base-currency units does 0.10 lots represent for a 100,000-unit Forex contract?
3. A gross $40 profit incurs $2 commission and a $1 swap charge. What is the net result?
4. A $5,000 notional position uses 1:50 leverage under the simplified margin model. How much margin is required?
5. Balance is $1,000, floating loss is $150 and used margin is $200. What are equity, free margin and margin level?
6. Does doubling leverage while keeping trade volume fixed halve the loss from the same price movement?

<details>
<summary>Solutions</summary>

1. 20 pips; 200 points.
2. 10,000 units.
3. $37.
4. $100.
5. Equity $850; free margin $650; margin level 425%.
6. No. It reduces the estimated margin requirement, not the P/L for the same exposure and price movement.

</details>

## Key takeaways

- Price movement and monetary value are different: volume, contract size and conversion matter.
- Know your costs, particularly when trading M1.
- Margin is not risk. Leverage can increase possible exposure.
- Use actual broker specifications, not universal pip/lot assumptions.
- Keep demo trades small enough to follow your rules without unnecessary emotional pressure.

**Next:** Module 03 — Trading Sessions and Timeframes.

## References (optional)

- [MT5 Market Watch and symbol specifications](https://www.metatrader5.com/en/terminal/help/trading/market_watch)
- [MT5 trading and account measures](https://www.metatrader5.com/en/terminal/help/trading/performing_deals)
- [MQL5 profit estimation](https://www.mql5.com/en/docs/trading/ordercalcprofit)
- [MQL5 margin estimation](https://www.mql5.com/en/docs/trading/ordercalcmargin)
