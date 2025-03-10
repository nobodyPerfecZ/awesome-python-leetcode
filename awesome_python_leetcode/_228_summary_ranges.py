from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        You are given a sorted unique integer array nums.

        A range [a,b] is the set of all integers from a to b (inclusive).

        Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
        That is, each element of nums is covered by exactly one of the ranges, and there is no
        integer x such that x is in one of the ranges but not in nums.

        Each range [a,b] in the list should be output as:
        - "a->b" if a != b
        - "a" if a == b
        """
        ranges = []
        for left, n in enumerate(nums):
            if n - 1 not in nums:
                length = 0
                right = left
                while (n + length) in nums:
                    length += 1
                    right += 1
                if left == right - 1:
                    ranges.append(f"{nums[left]}")
                else:
                    ranges.append(f"{nums[left]}->{nums[right-1]}")
        return ranges
