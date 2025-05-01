import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        """
        You are given an array nums consisting of positive integers.

        We call a subarray of an array complete if the following condition is satisfied:
        - The number of distinct elements in the subarray is equal to the number of
        distinct elements in the whole array.

        Return the number of complete subarrays.

        A subarray is a contiguous non-empty part of an array.
        """
        count = 0
        freq = collections.defaultdict(int)
        i, j = 0, 0
        while i < len(nums):
            while j < len(nums) and len(freq) < len(set(nums)):
                freq[nums[j]] += 1
                j += 1

            if len(freq) < len(set(nums)):
                break

            count += len(nums) - j + 1
            freq[nums[i]] -= 1
            if freq[nums[i]] == 0:
                del freq[nums[i]]
            i += 1
        return count
