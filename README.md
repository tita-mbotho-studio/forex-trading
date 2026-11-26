# Forex Trading Crash Course

A concise, practical foundation in Forex trading, with MetaTrader 5 (MT5), reusable Jupyter calculations and one simple demo strategy. This is a reference library to complement practical mentorship, not a quantitative finance textbook or a promise of profitable trading.

## Start here

- [Course outline](course/README.md)
- [Implementation roadmap](ROADMAP.md)
- [Progress tracker](PROGRESS.md)
- [Review workflow](CONTRIBUTING.md)
- [Calculation notebooks](notebooks/README.md)
- [MT5 Expert Advisor](expert-advisor/README.md)
- [Trading templates](templates/README.md)
- [Resources](resources/README.md)

## Learning plan

Allow approximately 10–12 study hours for the foundations, excluding extended demo practice and EA development. The initial demo exercise is to record 50 trades using consistent rules; that sample does not establish long-term profitability.

Capital preservation first. Consistency second. Profitability third. Better risk management can reduce emotional pressure, but does not eliminate emotions or trading losses.

## Local setup

Read Markdown in GitHub or VS Code; no Python installation is needed for the lessons. For later notebooks, use Python 3.11 or newer and [uv](https://docs.astral.sh/uv/).

```powershell
uv sync
uv run jupyter lab
```

For setup validation (no third-party packages needed):

```powershell
python -m unittest discover -s tests -v
```

This repository is educational. Use demo accounts for practice. Leveraged trading involves substantial risk; SL/TP execution may differ from intended prices. Never commit account credentials, personal trading records or broker secrets.
