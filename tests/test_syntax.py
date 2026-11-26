"""Host-only structural and lexical smoke tests for the Sublime preview grammar.

These tests do not invoke Sublime's syntax engine or an Atto compiler.
"""
import pathlib
import re
import unittest

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
GRAMMAR = yaml.safe_load((ROOT / "AttoLang.sublime-syntax").read_text(encoding="utf-8"))
CONTEXTS = GRAMMAR["contexts"]


def scoped_regex(scope):
    patterns = [entry["match"] for entry in CONTEXTS["main"]
                if entry.get("scope") == scope]
    assert patterns, f"missing main scope: {scope}"
    return re.compile("|".join(f"(?:{pattern})" for pattern in patterns))


class GrammarSmokeTests(unittest.TestCase):
    def test_registration(self):
        self.assertEqual(GRAMMAR["scope"], "source.atto")
        self.assertEqual(GRAMMAR["file_extensions"], ["atto", "ores"])
        self.assertEqual(CONTEXTS["main"][:3],
                         [{"include": "comments"}, {"include": "symbols"}, {"include": "strings"}])

    def test_references_resolve_and_regexes_compile(self):
        for name, context in CONTEXTS.items():
            for entry in context:
                if "include" in entry:
                    self.assertIn(entry["include"], CONTEXTS, (name, entry))
                if "push" in entry:
                    self.assertIn(entry["push"], CONTEXTS, (name, entry))
                if "match" in entry:
                    re.compile(entry["match"])

    def test_keyword_boundaries(self):
        decl = scoped_regex("keyword.declaration.atto")
        self.assertIsNotNone(decl.search("define actor Counter"))
        self.assertIsNone(decl.search("reactor_count"))
        self.assertIsNone(decl.search("defined"))
        ctrl = scoped_regex("keyword.control.atto")
        self.assertIsNotNone(ctrl.search("critical-read"))
        self.assertIsNotNone(ctrl.search("nb-select"))
        self.assertIsNone(ctrl.search("my-critical-read-extra"))

    def test_contextual_mtd_only(self):
        decl = scoped_regex("keyword.declaration.atto")
        for source in ("mtd answer()", "mtd method()", "mtd mtd()", "mtd id<T>()",
                       "mtd (C self) answer()", "mtd [Symbol.iterator]()"):
            with self.subTest(source=source):
                self.assertEqual(decl.search(source).group(), "mtd")
        for source in ("method answer()", "method()", "mtd()", "mtd (value)",
                       "x.mtd()", "mtd value;", "mtd List<int> value;", "some_mtd foo()"):
            with self.subTest(source=source):
                self.assertIsNone(decl.search(source))

    def test_literals_and_ownership(self):
        self.assertIsNotNone(scoped_regex("storage.modifier.atto").search("rt borrow mut value"))
        self.assertIsNotNone(scoped_regex("constant.numeric.atto").search("3.14"))
        symbol_patterns = [e["match"] for e in CONTEXTS["symbols"] if e.get("scope") == "constant.other.symbol.atto"]
        self.assertTrue(any(re.search(p, "#ready") for p in symbol_patterns))
        self.assertFalse(any(re.search(p, ":ready") for p in symbol_patterns))

    def test_quote_and_nested_comment_contexts(self):
        self.assertEqual(CONTEXTS["block_comment"][0]["meta_scope"], "comment.block.atto")
        self.assertTrue(any(x.get("push") == "block_comment" for x in CONTEXTS["block_comment"]))
        self.assertTrue(any(x.get("pop") is True for x in CONTEXTS["block_comment"]))
        for name in ("double_symbol", "single_symbol", "double_quoted", "single_quoted", "template"):
            self.assertTrue(any(x.get("pop") is True for x in CONTEXTS[name]))


if __name__ == "__main__":
    unittest.main()
