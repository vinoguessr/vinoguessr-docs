"""Relative links in the README and ADRs must point at files that exist in this repository."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def broken_links(page):
    broken = []
    for target in re.findall(r'\]\(([^)]+)\)', page.read_text()):
        path = target.split('#', 1)[0]
        if not path or '://' in path or path.startswith('mailto:'):
            continue
        if not (page.parent / path).exists():
            broken.append(target)
    return broken


class MarkdownLinkTests(unittest.TestCase):
    def test_readme_and_adr_relative_links_resolve(self):
        pages = [ROOT / 'README.md', *sorted((ROOT / 'docs/adr').glob('*.md'))]
        for page in pages:
            with self.subTest(page=page.relative_to(ROOT)):
                self.assertEqual(broken_links(page), [])

    def test_detects_a_missing_target(self):
        page = ROOT / 'scripts' / '_fixture.md'
        page.write_text('[gone](missing.md) [ok](test_markdown_links.py) [web](https://example.com)')
        try:
            self.assertEqual(broken_links(page), ['missing.md'])
        finally:
            page.unlink()


if __name__ == '__main__':
    unittest.main()
