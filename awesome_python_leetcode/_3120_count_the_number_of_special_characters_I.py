import string


class Solution:
    """Base class for all LeetCode Problems."""

    def numberOfSpecialChars(self, word: str) -> int:
        """
        You are given a string word. A letter is called special if it appears both
        in lowercase and uppercase in word.

        Return the number of special letters in word.
        """
        s = set(word)
        return sum(c in s and c.upper() in s for c in string.ascii_lowercase)
