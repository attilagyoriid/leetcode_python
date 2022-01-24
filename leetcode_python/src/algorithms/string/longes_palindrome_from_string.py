class LongestPalindromeFromString:

    def calculate(self, text: str) -> int:
        chars = [0] * 128
        for i in text:
            chars[ord(i)] += 1
        length = 0
        for c in chars:

            length += c if c % 2 == 0 else c-1

        if length < len(text):
            length += 1

        return length
