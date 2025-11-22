from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def minimumOperations(self, nums: List[int]) -> int:
        """
        You are given an integer array nums. In one operation, you can add or subtract
        1 from any element of nums.

        Return the minimum number of operations to make all elements of nums divisible
        by 3.
        """
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        num_ops = 0
        k = 3
        for num in nums:
            if num % k:
                remain = num % k
                num_ops += min(remain, k - remain)
        return num_ops
