import pathlib
import unittest

import regex
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
with (ROOT / "AttoLang.sublime-syntax").open(encoding="utf-8") as stream:
    text = stream.read()
grammar = yaml.safe_load(text.replace("%YAML 1.2\n", "", 1))


class SyntaxTests(unittest.TestCase):
    def test_registration_and_literal_precedence(self):
        self.assertEqual(grammar["name"], "AttoLang")
        self.assertEqual(grammar["file_extensions"], ["atto", "ores"])
        self.assertEqual(grammar["scope"], "source.atto")
        self.assertEqual([p["include"] for p in grammar["contexts"]["main"][:3]],
                         ["comments", "symbols", "strings"])

    def test_modern_callable_keyword_boundaries(self):
        rules = {r["scope"]: r["match"] for r in grammar["contexts"]["main"]
                 if "scope" in r and "match" in r}
        entity = regex.compile(rules["keyword.entity.atto"])
        effect = regex.compile(rules["keyword.effect.atto"])
        for word in ["mtd", "fnc", "routine"]:
            self.assertIsNotNone(entity.fullmatch(word))
        for word in ["pure", "defer", "recover", "panic", "raise", "throw"]:
            self.assertIsNotNone(effect.fullmatch(word))
        for identifier in ["mtd_extra", "_mtd", "method", "pure2", "pure_value"]:
            self.assertIsNone(entity.search(identifier))
            self.assertIsNone(effect.search(identifier))

    def test_compound_keyword_and_nested_comment_contract(self):
        patterns = [r for r in grammar["contexts"]["main"]
                    if r.get("scope") == "keyword.concurrency.atto"]
        compound = regex.compile(patterns[0]["match"])
        self.assertTrue(compound.fullmatch("nb-select"))
        for source in ["nb-select_more", "xnb-select", "nb-select-unsafe"]:
            self.assertFalse(compound.search(source))
        self.assertTrue(any(r.get("push") == "block-comment"
                            for r in grammar["contexts"]["block-comment"]))
        self.assertTrue(any(r.get("pop") is True
                            for r in grammar["contexts"]["block-comment"]))


if __name__ == "__main__":
    unittest.main()
