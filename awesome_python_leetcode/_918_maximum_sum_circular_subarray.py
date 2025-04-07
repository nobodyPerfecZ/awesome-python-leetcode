from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Given a circular integer array nums of length n, return the maximum possible
        sum of a non-empty subarray of nums.

        A circular array means the end of the array connects to the beginning of the
        array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the
        previous element of nums[i] is nums[(i - 1 + n) % n].

        A subarray may only include each element of the fixed buffer nums at most once.
        Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not
        exist i <= k1, k2 <= j with k1 % n == k2 % n.
        """
        maxSum, curMax = -float("inf"), -float("inf")
        minSum, curMin = float("inf"), float("inf")
        totalSum = 0
        for i in range(len(nums)):
            if curMax < 0:
                curMax = nums[i]
            else:
                curMax += nums[i]
            if curMin > 0:
                curMin = nums[i]
            else:
                curMin += nums[i]
            if curMax > maxSum:
                maxSum = curMax
            if curMin < minSum:
                minSum = curMin
            totalSum += nums[i]
        if maxSum < 0:
            return maxSum
        return max(maxSum, totalSum - minSum)
