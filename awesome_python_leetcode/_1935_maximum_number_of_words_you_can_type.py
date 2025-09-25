class Solution:
    """Base class for all LeetCode Problems."""

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        There is a malfunctioning keyboard where some letter keys do not work. All other
        keys on the keyboard work properly.

        Given a string text of words separated by a single space (no leading or trailing
        spaces) and a string brokenLetters of all distinct letter keys that are broken,
        return the number of words in text you can fully type using this keyboard.

        """
        words = text.split(" ")
        broken = set(brokenLetters)
        res = len(words)
        for word in words:
            for c in word:
                if c in broken:
                    res -= 1
                    break
        return res
