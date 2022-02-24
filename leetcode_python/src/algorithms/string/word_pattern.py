class WordPattern:

    def valid(self, pattern: str, words: str) -> bool:

        if not pattern or not words:
            return False
        word_list = words.split(' ')
        if len(word_list) != len(pattern):
            return False

        character_to_word = {}
        word_to_character = {}

        for word, character in zip(word_list, pattern):

            if word in word_to_character and word_to_character[word] != character:
                return False
            if character in character_to_word and character_to_word[character] != word:
                return False

            character_to_word[character] = word
            word_to_character[word] = character

        return True
