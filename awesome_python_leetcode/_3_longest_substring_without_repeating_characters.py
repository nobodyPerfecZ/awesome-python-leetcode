class Solution:
    """Base class for all LeetCode Problems."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without duplicate
        characters.
        """
        maxLen, curLen, charToPos = 0, 0, {}
        left, right = 0, 0
        while left < len(s) and right < len(s):
            c = s[right]
            if c not in charToPos or charToPos[c] < left:
                charToPos[c] = right
                curLen += 1
                right += 1
            else:
                pos = charToPos[c]
                maxLen = max(maxLen, curLen)
                curLen -= pos + 1 - left
                left = pos + 1
                del charToPos[c]
        return max(maxLen, curLen)
