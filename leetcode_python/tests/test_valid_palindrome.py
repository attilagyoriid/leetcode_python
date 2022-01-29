from leetcode_python.src.algorithms.string.valid_palindrome import ValidPalindrome
import unittest

class TestSum(unittest.TestCase):

    def test_valid(self):
        palindrome = ValidPalindrome()
        self.assertTrue(palindrome.valid("this is a plaindrome   emordnialpa sis iht "))

    def test_inValid(self):
        palindrome = ValidPalindrome()
        self.assertFalse(palindrome.valid("this is a plaindrome  emordnialpa sis iht A"))

