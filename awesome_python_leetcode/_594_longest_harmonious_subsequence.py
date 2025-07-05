import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def findLHS(self, nums: List[int]) -> int:
        """
        We define a harmonious array as an array where the difference between its
        maximum value and its minimum value is exactly 1.

        Given an integer array nums, return the length of its longest harmonious
        subsequence among all its possible subsequences.
        """
        lhs = 0
        count = collections.Counter(nums)
        for val, freq in count.items():
            hs = 0 if val - 1 not in count else freq + count[val - 1]
            lhs = max(lhs, hs)
        return lhs
