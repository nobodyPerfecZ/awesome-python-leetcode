from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def triangleNumber(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the number of triplets chosen from the
        array that can make triangles if we take them as side lengths of a triangle.
        """
        nums.sort()
        num_triangles = 0
        for k in range(2, len(nums)):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    num_triangles += j - i
                    j -= 1
                else:
                    i += 1
        return num_triangles
