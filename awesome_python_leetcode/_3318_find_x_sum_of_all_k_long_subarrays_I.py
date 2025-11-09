import collections
import heapq
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        You are given an array nums of n integers and two integers k and x.

        The x-sum of an array is calculated by the following procedure:
        - Count the occurrences of all elements in the array.
        - Keep only the occurrences of the top x most frequent elements. If two elements
        have the same number of occurrences, the element with the bigger value is
        considered more frequent.
        - Calculate the sum of the resulting array.

        Note that if an array has less than x distinct elements, its x-sum is the sum of
        the array.

        Return an integer array answer of length n - k + 1 where answer[i] is the x-sum
        of the subarray nums[i..i + k - 1].
        """
        count = collections.defaultdict(int)
        prev = None
        res = []
        for i in range(len(nums) - k + 1):
            # Get the sliding window
            window = nums[i : i + k]

            # Update count table
            if i == 0:
                # Compute count table for first time
                for val in window[:-1]:
                    count[val] += 1

            # Remove prev from count table
            if prev:
                count[prev] -= 1
            prev = window[0]

            # Add newest into count table
            count[window[-1]] += 1

            # Get the top-x values with their occurences
            top_x = heapq.nlargest(x, count.items(), key=lambda x: (x[1], x[0]))

            # Compute the x-sum
            sum_x = sum(map(lambda x: x[0] * x[1], top_x))
            res.append(sum_x)

        return res
