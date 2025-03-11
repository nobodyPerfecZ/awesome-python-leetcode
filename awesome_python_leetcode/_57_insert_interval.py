from typing import List


class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int],
    ) -> List[List[int]]:
        """
        You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
        represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
        You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

        Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and
        intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

        Return intervals after the insertion.

        Note that you don't need to modify intervals in-place. You can make a new array and return it.
        """
        output = []
        i = 0

        # Add all intervals that come before newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        output.append(newInterval)

        # Add remaining intervals
        while i < len(intervals):
            output.append(intervals[i])
            i += 1

        return output
