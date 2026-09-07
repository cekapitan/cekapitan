import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


def local_markdown_targets(markdown: Path):
    for match in re.finditer(r"!?\[[^]]*\]\(([^)]+)\)", markdown.read_text()):
        target = match.group(1).strip().strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith(("#", "/")):
            continue
        yield unquote(parsed.path)


class ProfileRepositoryTests(unittest.TestCase):
    def test_readme_identifies_the_profile(self):
        content = README.read_text()
        self.assertIn("# Cody Stamey", content)
        self.assertIn("Infrastructure Engineer", content)

    def test_local_markdown_links_resolve(self):
        missing = [target for target in local_markdown_targets(README) if not (README.parent / target).exists()]
        self.assertEqual([], missing)

    def test_readme_has_no_merge_conflict_markers(self):
        content = README.read_text()
        for marker in ("<<<<<<<", "=======", ">>>>>>>"):
            self.assertNotIn(marker, content)


if __name__ == "__main__":
    unittest.main()
