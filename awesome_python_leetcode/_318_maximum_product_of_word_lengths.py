from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxProduct(self, words: List[str]) -> int:
        """
        Given a string array words, return the maximum value of
        length(word[i]) * length(word[j]) where the two words do not share common
        letters. If no such two words exist, return 0.
        """
        n = len(words)
        masks = [0] * n

        # Create bitmask for each word
        for i, word in enumerate(words):
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord("a"))
            masks[i] = mask

        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                # If no common letters, bitwise AND will be 0
                if masks[i] & masks[j] == 0:
                    result = max(result, len(words[i]) * len(words[j]))
        return result
