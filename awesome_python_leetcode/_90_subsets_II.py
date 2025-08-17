from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums that may contain duplicates, return all possible
        subsets (the power set).

        A subset of an array is a selection of elements (possibly none) of the array.

        The solution set must not contain duplicate subsets. Return the solution in any
        order.
        """
        nums = sorted(nums)
        results = [[]]
        visited = set()
        for value in nums:
            for i in range(0, len(results)):
                new_subset = results[i] + [value]
                if tuple(new_subset) not in visited:
                    visited.add(tuple(new_subset))
                    results.append(new_subset)
        return results
