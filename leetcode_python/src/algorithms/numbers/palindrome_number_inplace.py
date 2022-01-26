class PalindromeNumberInPlace:

    def isPalindrome(self, num: int) -> bool:

        if num < 0:
            return False
        if num < 10:
            return True

        divider = 1
        while num >= divider * 10:
            divider *= 10

        while num != 0:
            left = num // divider
            right = num % 10
            if left != right:
                return False
            num = (num % divider) // 10
            divider //= 100

        return True

