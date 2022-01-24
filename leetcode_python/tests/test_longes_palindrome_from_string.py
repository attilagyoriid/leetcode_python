from leetcode_python.src.algorithms.string.longes_palindrome_from_string import LongestPalindromeFromString


def test_calculate():
    text = "acekrtacthjk"
    longestPalindromeFromString = LongestPalindromeFromString()
    result = longestPalindromeFromString.calculate(text)
    print(result)
    assert result == 9
