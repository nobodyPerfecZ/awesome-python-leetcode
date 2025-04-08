from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def rob(self, nums: List[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street. Each house
        has a certain amount of money stashed, the only constraint stopping you from
        robbing each of them is that adjacent houses have security systems connected
        and it will automatically contact the police if two adjacent houses were broken
        into on the same night.

        Given an integer array nums representing the amount of money of each house,
        return the maximum amount of money you can rob tonight without alerting the
        police.
        """
        second, first = 0, 0
        for i in range(len(nums)):
            tmp = max(nums[i] + second, first)
            second = first
            first = tmp
        return first
