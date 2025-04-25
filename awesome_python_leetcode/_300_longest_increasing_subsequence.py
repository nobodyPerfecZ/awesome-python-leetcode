import bisect
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def lengthOfLISBS(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the length of the longest strictly
        increasing subsequence.

        A subsequence is an array that can be derived from another array by deleting
        some or no elements without changing the order of the remaining elements.
        """
        # Binary Search Solution: O(n log n)
        seq = [nums[0]]
        for k in range(1, len(nums)):
            if nums[k] > seq[-1]:
                seq.append(nums[k])
            else:
                i = bisect.bisect_left(seq, nums[k])
                seq[i] = nums[k]
        return len(seq)

    def lengthOfLISDP(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the length of the longest strictly
        increasing subsequence.

        A subsequence is an array that can be derived from another array by deleting
        some or no elements without changing the order of the remaining elements.
        """
        # DP (LIS) Solution: O(n²)
        dp = [1] * (len(nums))
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
