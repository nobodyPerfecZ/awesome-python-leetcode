import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxFrequencyElements(self, nums: List[int]) -> int:
        """
        You are given an array nums consisting of positive integers.

        Return the total frequencies of elements in nums such that those elements all
        have the maximum frequency.

        The frequency of an element is the number of occurrences of that element in the
        array.
        """
        # (num -> frequency)
        num_to_frequency = collections.defaultdict(int)

        # (frequency -> count)
        frequency_to_count = collections.defaultdict(int)

        # Count the frequency and the number of frequencies for the numbers
        for n in nums:
            if num_to_frequency[n] > 0:
                frequency_to_count[num_to_frequency[n]] -= 1
            num_to_frequency[n] += 1
            frequency_to_count[num_to_frequency[n]] += 1

        # Get the maximum frequency and the count of that frequency
        max_frequency = max(num_to_frequency.values())
        max_count = frequency_to_count[max_frequency]

        return max_frequency * max_count
