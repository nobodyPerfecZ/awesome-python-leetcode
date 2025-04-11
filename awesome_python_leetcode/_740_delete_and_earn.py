import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        You are given an integer array nums. You want to maximize the number of points
        you get by performing the following operation any number of times:
        - Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must
        delete every element equal to nums[i] - 1 and every element equal to
        nums[i] + 1.

        Return the maximum number of points you can earn by applying the above
        operation some number of times.
        """
        if len(nums) == 1:
            return nums[0]

        count = collections.defaultdict(int)
        minVal, maxVal = float("inf"), -float("inf")
        for n in nums:
            count[n] += n
            minVal = min(minVal, n)
            maxVal = max(maxVal, n)

        dp = [0 for i in range(maxVal + 1)]
        for i in range(minVal, maxVal + 1):
            dp[i] = max(dp[i - 2] + count[i], dp[i - 1])

        return max(dp[-1], dp[-2])
