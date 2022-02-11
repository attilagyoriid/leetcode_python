import unittest

from leetcode_python.src.algorithms.string.vallid_parentheses import ValidParentheses


class TestValidParentheses(unittest.TestCase):

    def test_is_valid(self):
        parentheses = ValidParentheses()
        self.assertTrue(parentheses.is_valid("[({})]"))

    def test_is_valid2(self):
        parentheses = ValidParentheses()
        self.assertTrue(parentheses.is_valid("[]({})"))

    def test_is_valid_failure(self):
        parentheses = ValidParentheses()
        self.assertFalse(parentheses.is_valid("[]({)}()"))

    def test_is_valid_failure2(self):
        parentheses = ValidParentheses()
        self.assertFalse(parentheses.is_valid("[]({}))"))
