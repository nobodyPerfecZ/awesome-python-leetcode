from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Given an array of intervals where intervals[i] = [starti, endi], merge all
        overlapping intervals, and return an array of the non-overlapping intervals that
        cover all the intervals in the input.
        """
        intervals = sorted(intervals, key=lambda i: i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = output[-1][1]
            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        return output
