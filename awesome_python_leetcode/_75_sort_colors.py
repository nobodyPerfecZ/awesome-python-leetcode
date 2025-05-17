from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def sortColorsBS(self, nums: List[int]) -> None:
        """
        Given an array nums with n objects colored red, white, or blue, sort them
        in-place so that objects of the same color are adjacent, with the colors in the
        order red, white, and blue.

        We will use the integers 0, 1, and 2 to represent the color red, white, and
        blue, respectively.

        You must solve this problem without using the library's sort function.

        Do not return anything, modify nums in-place instead.
        """
        # Bucket Sort Solution
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # Count the number of occurrences of each color
        count = [0, 0, 0]
        for i in range(len(nums)):
            count[nums[i]] += 1

        # Fill the array with the sorted colors
        j = 0
        for i in range(len(nums)):
            while j < len(count) and count[j] == 0:
                j += 1
            nums[i] = j
            count[j] -= 1

    def sortColorsQS(self, nums: List[int]) -> None:
        """
        Given an array nums with n objects colored red, white, or blue, sort them
        in-place so that objects of the same color are adjacent, with the colors in the
        order red, white, and blue.

        We will use the integers 0, 1, and 2 to represent the color red, white, and
        blue, respectively.

        You must solve this problem without using the library's sort function.

        Do not return anything, modify nums in-place instead.
        """
        # (Simple) Quick Sort Solution
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        left, right = 0, len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                i -= 1
            i += 1
