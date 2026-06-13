import string


class Solution:
    """Base class for all LeetCode Problems."""

    def numberOfSpecialChars(self, word: str) -> int:
        """
        You are given a string word. A letter c is called special if it appears both
        in lowercase and uppercase in word, and every lowercase occurrence of c
        appears before the first uppercase occurrence of c.

        Return the number of special letters in word.
        """
        # Construct Hash table
        s = {}
        for i, c in enumerate(word):
            if c not in s:
                s[c] = i
            else:
                if c in string.ascii_lowercase:
                    s[c] = i
        return sum(
            c in s and c.upper() in s and s[c] < s[c.upper()]
            for c in string.ascii_lowercase
        )
