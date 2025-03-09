from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Given an array nums of size n, return the majority element.

        The majority element is the element that appears more than ⌊n / 2⌋ times.
        You may assume that the majority element always exists in the array.
        """
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        return max(counts, key=lambda k: counts[k])
