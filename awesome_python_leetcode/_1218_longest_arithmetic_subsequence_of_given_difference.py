from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        Given an integer array arr and an integer difference, return the length of the
        longest subsequence in arr which is an arithmetic sequence such that the
        difference between adjacent elements in the subsequence equals difference.

        A subsequence is a sequence that can be derived from arr by deleting some or no
        elements without changing the order of the remaining elements.
        """
        dp = {}
        result = 0
        for i in range(len(arr)):
            if arr[i] - difference in dp:
                dp[arr[i]] = dp[arr[i] - difference] + 1
            else:
                dp[arr[i]] = 1
            result = max(result, dp[arr[i]])
        return result
