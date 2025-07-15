class Solution:
    """Base class for all LeetCode Problems."""

    def isValid(self, word: str) -> bool:
        """
        A word is considered valid if:
        - It contains a minimum of 3 characters.
        - It contains only digits (0-9), and English letters (uppercase and lowercase).
        - It includes at least one vowel.
        - It includes at least one consonant.
        You are given a string word.

        Return true if word is valid, otherwise, return false.

        Notes:
        - 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
        -  A consonant is an English letter that is not a vowel.
        """
        num_characters, num_vowels, num_consonants = 0, 0, 0
        for c in word.lower():
            is_digit = c >= "0" and c <= "9"
            is_letter = c >= "a" and c <= "z"
            is_vowel = c in ["a", "e", "i", "o", "u"]
            is_consonant = not is_vowel and is_letter
            if not (is_digit or is_letter):
                return False
            num_characters += 1
            if is_vowel:
                num_vowels += 1
            if is_consonant:
                num_consonants += 1
        return num_characters >= 3 and num_vowels >= 1 and num_consonants >= 1
