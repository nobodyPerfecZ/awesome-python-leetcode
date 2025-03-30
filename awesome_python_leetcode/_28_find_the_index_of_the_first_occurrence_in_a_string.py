class Solution:
    """Base class for all LeetCode Problems."""

    def strStr(self, haystack: str, needle: str) -> int:
        """
        Given two strings needle and haystack, return the index of the first occurrence
        of needle in haystack, or -1 if needle is not part of haystack.
        """
        return haystack.find(needle)
