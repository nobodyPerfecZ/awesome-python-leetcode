from typing import List
from heapq import heapify, heappop


class Solution:
    """Base class for all LeetCode Problems."""

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Given an integer array nums and an integer k, return the kth largest element in
        the array.

        Note that it is the kth largest element in the sorted order, not the kth
        distinct element.

        Can you solve it without sorting?
        """
        nums = [-n for n in nums]
        heapify(nums)
        for t in range(k):
            val = heappop(nums)
        return -val
