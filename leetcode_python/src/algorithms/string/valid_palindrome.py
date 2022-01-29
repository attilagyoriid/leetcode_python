class ValidPalindrome:

    def valid(self, text: str) -> bool:
        left = 0
        right = len(text) - 1

        while left < right:

            while left < right and not self.number_or_digit(text[left]):
                left += 1

            while left < right and not self.number_or_digit(text[right]):
                right -= 1

            if left < right and text[left].lower() != text[right].lower():
                print(f'{text[left]} and {text[right]}')
                return False

            right -= 1
            left += 1

        return True

    def number_or_digit(self, char):
        return ord("a") <= ord(char) <= ord("z") or \
               ord("A") <= ord(char) <= ord("Z") or \
               ord("0") <= ord(char) <= ord("9")
