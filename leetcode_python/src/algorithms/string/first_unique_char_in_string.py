class FirstUniqueCharInString:

    @staticmethod
    def first_unique_char(s: str) -> int:
        """
        Find first unique character in string
        :param s: string to find unique character in
        :type s: string
        :return: the index of the first unique character
        :rtype: integer
        """
        dictionary = {}
        for char in s:
            if char in dictionary:
                dictionary[char] = dictionary[char] + 1
            else:
                dictionary[char] = 1

        for i in range(0, len(s)):
            if dictionary[s[i]] == 1:
                return i

        return -1
