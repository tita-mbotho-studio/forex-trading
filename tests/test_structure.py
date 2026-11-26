"""Validate the repository scaffold without third-party dependencies."""
import re
import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestProjectStructure(unittest.TestCase):
    def test_required_files(self):
        files = (
            "README.md", "ROADMAP.md", "PROGRESS.md", "CONTRIBUTING.md",
            "course/README.md", "notebooks/README.md",
            "expert-advisor/README.md", "expert-advisor/TESTING.md",
            "templates/README.md", "resources/README.md",
            ".gitignore", "pyproject.toml",
        )
        for file in files:
            with self.subTest(file=file):
                self.assertTrue((ROOT / file).is_file())

    def test_relative_markdown_links(self):
        for file in ROOT.rglob("*.md"):
            if any(part.startswith(".") for part in file.relative_to(ROOT).parts):
                continue
            if "private" in file.relative_to(ROOT).parts or "local" in file.relative_to(ROOT).parts:
                continue
            for target in re.findall(r"\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                with self.subTest(file=file, target=target):
                    self.assertTrue((file.parent / target.split("#", 1)[0]).exists())

    def test_course_module_count(self):
        content = (ROOT / "course/README.md").read_text(encoding="utf-8")
        ids = re.findall(r"^\| (\d{2}) \|", content, re.M)
        self.assertEqual(ids, [f"{n:02d}" for n in range(1, 13)])

    def test_python_config(self):
        with (ROOT / "pyproject.toml").open("rb") as file:
            config = tomllib.load(file)
        self.assertEqual(config["project"]["requires-python"], ">=3.11")
        self.assertFalse(config["tool"]["uv"]["package"])


if __name__ == "__main__":
    unittest.main()
