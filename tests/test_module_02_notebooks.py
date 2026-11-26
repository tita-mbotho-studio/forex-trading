"""Execute the educational notebook cells without a Jupyter dependency."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_02 = (
    "01_pips_and_tick_values.ipynb",
    "02_profit_and_loss.ipynb",
    "03_leverage_and_margin.ipynb",
)


class TestModule02Notebooks(unittest.TestCase):
    def test_notebook_code_cells(self):
        for filename in MODULE_02:
            with self.subTest(notebook=filename):
                path = ROOT / "notebooks" / filename
                notebook = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(notebook["nbformat"], 4)
                self.assertTrue(any(cell["cell_type"] == "code" for cell in notebook["cells"]))
                self.assertTrue(any("https://" in "".join(cell["source"])
                                    for cell in notebook["cells"] if cell["cell_type"] == "markdown"))
                namespace = {"__name__": "__notebook__"}
                for number, cell in enumerate(notebook["cells"], start=1):
                    if cell["cell_type"] == "code":
                        source = "".join(cell["source"])
                        exec(compile(source, f"{filename}:cell{number}", "exec"), namespace)


if __name__ == "__main__":
    unittest.main()
