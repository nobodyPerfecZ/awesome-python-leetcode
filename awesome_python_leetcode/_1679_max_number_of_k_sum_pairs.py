import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        You are given an integer array nums and an integer k.

        In one operation, you can pick two numbers from the array whose sum equals k
        and remove them from the array.

        Return the maximum number of operations you can perform on the array.
        """
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        values = collections.defaultdict(int)
        count = 0
        for n in nums:
            diff = k - n
            if diff in values:
                count += 1
                if values[diff] == 1:
                    del values[diff]
                else:
                    values[diff] -= 1
            else:
                values[n] += 1
        return count
