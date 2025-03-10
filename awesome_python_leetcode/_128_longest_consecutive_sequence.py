from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of the
        longest consecutive elements sequence.

        You must write an algorithm that runs in O(n) time.
        """
        nums = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in nums:
                length = 0
                while (n + length) in nums:
                    length += 1
                longest = max(longest, length)
        return longest
