from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Given two 0-indexed integer arrays nums1 and nums2, return a list answer of
        size 2 where:
        - answer[0] is a list of all distinct integers in nums1 which are not present
        in nums2.
        - answer[1] is a list of all distinct integers in nums2 which are not present
        in nums1.

        Note that the integers in the lists may be returned in any order.
        """
        return [
            list(set(nums1).difference(set(nums2))),
            list(set(nums2).difference(set(nums1))),
        ]
