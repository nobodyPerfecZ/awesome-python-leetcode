from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given an integer array nums sorted in non-decreasing order, remove some
        duplicates in-place such that each unique element appears at most twice. The
        relative order of the elements should be kept the same.

        Since it is impossible to change the length of the array in some languages, you
        must instead have the result be placed in the first part of the array nums. More
        formally, if there are k elements after removing the duplicates, then the first
        k elements of nums should hold the final result. It does not matter what you
        leave beyond the first k elements.

        Return k after placing the final result in the first k slots of nums.

        Do not allocate extra space for another array. You must do this by modifying the
        input array in-place with O(1) extra memory.
        """
        left = 1
        right = 1
        length = 1
        second_val = True
        val_before = nums[0]
        while right < len(nums):
            if second_val and val_before == nums[right]:
                nums[left] = nums[right]
                val_before = nums[left]
                second_val = False
                left += 1
                right += 1
                length += 1
            elif val_before == nums[right]:
                right += 1
            else:
                nums[left] = nums[right]
                val_before = nums[left]
                second_val = True
                left += 1
                right += 1
                length += 1
        return length
