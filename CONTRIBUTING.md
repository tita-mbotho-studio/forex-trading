# Development and review workflow

1. Select the next roadmap item; branch from current main using `implementation/NN-short-name`.
2. Make focused changes; include related notebooks or tests in the same implementation.
3. Check accuracy, examples, links and relevant tests; disclose anything not verified.
4. Open a pull request targeting main and provide local PowerShell review commands.
5. Apply feedback on the same branch.
6. Merge only after explicit user approval. Confirm merge status, update progress and clean up completed branches where permissions allow.

Never merge an unapproved implementation or enable auto-merge. Avoid force pushes. Do not commit real account numbers, broker credentials or personal trade logs.

## Content standards

Keep theory short. Use everyday examples and South African time (SAST) where relevant. Explain instrument-specific assumptions, units, and costs. Verify external links and distinguish illustrative strategies from proven results. Prefer simple code and standard libraries; use VS Code with a Python kernel for notebooks. The only direct notebook runtime dependency is ipykernel; uv is available for creating the project environment.

For notebooks, execute examples and test calculations, including invalid inputs. For MT5, compile with MetaEditor and record demo test evidence across compatible instruments and account modes before claiming support. Never claim exact loss limits or guaranteed execution.

## Review commands

For the first local clone:
```powershell
git clone https://github.com/tita-mbotho-studio/forex-trading.git
cd forex-trading
git switch --track origin/implementation/00-project-setup
git diff --stat origin/main...HEAD
python -m unittest discover -s tests -v
```

For a later branch, fetch first, switch to the named branch, and pull with `--ff-only`. Review before approval.
