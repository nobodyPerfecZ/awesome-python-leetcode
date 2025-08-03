class Solution:
    """Base class for all LeetCode Problems."""

    def maxVowels(self, s: str, k: int) -> int:
        """
        Given a string s and an integer k, return the maximum number of vowel letters in
        any substring of s with length k.

        Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
        """
        # Count initial sliding window
        curr = 0
        for i in range(k):
            if s[i] in ["a", "e", "i", "o", "u"]:
                curr += 1
        result = curr

        # Move sliding window
        i = 1
        j = k
        while j < len(s):
            if s[i - 1] in ["a", "e", "i", "o", "u"]:
                curr -= 1
                result = max(result, curr)
            if s[j] in ["a", "e", "i", "o", "u"]:
                curr += 1
                result = max(result, curr)
            i += 1
            j += 1
        return result
