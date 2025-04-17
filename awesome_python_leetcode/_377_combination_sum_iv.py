from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Given an array of distinct integers nums and a target integer target, return
        the number of possible combinations that add up to target.

        The test cases are generated so that the answer can fit in a 32-bit integer.
        """
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            res = 0
            for j in range(len(nums)):
                if i - nums[j] >= 0:
                    res += dp[i - nums[j]]
            dp[i] = res
        return dp[-1]
