from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Write a function to find the longest common prefix string amongst an array of
        strings.

        If there is no common prefix, return an empty string "".
        """
        prefix = ""
        for i, c in enumerate(strs[0]):
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return prefix
            prefix += c
        return prefix
