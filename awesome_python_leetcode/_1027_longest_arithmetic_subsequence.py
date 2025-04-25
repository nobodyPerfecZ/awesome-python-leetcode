import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
        Given an array nums of integers, return the length of the longest arithmetic
        subsequence in nums.

        Note that:
        - A subsequence is an array that can be derived from another array by deleting
        some or no elements without changing the order of the remaining elements.
        - A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value
        (for 0 <= i < seq.length - 1).
        """
        dp = [collections.defaultdict(int) for _ in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                dp[i][diff] = max(dp[i][diff], 1 + dp[j][diff])
        return 1 + max([max(dp_i.values()) for dp_i in dp])
