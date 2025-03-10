from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
        """

        def rev(left: int, right: int):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        k = k % len(nums)
        rev(0, len(nums) - 1)
        rev(0, k - 1)
        rev(k, len(nums) - 1)
