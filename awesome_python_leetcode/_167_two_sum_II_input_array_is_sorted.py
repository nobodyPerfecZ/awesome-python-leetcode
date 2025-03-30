from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given a 1-indexed array of integers numbers that is already sorted in
        non-decreasing order, find two numbers such that they add up to a specific
        target number. Let these two numbers be numbers[index1] and numbers[index2]
        where 1 <= index1 < index2 <= numbers.length.

        Return the indices of the two numbers, index1 and index2, added by one as an
        integer array [index1, index2] of length 2.

        The tests are generated such that there is exactly one solution. You may not
        use the same element twice.

        Your solution must use only constant extra space.
        """
        if len(numbers) == 2:
            return [1, 2]

        left, right = 0, len(numbers) - 1
        while left < right:
            twosum = numbers[left] + numbers[right]
            if twosum < target:
                left += 1
            elif twosum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return [left + 1, right + 1]
