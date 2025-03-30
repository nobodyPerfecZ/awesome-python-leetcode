from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is
        equal to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
        integer.

        You must write an algorithm that runs in O(n) time and without using the
        division operation.
        """
        result = []
        prefix = 1
        for i in range(len(nums)):
            result.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
