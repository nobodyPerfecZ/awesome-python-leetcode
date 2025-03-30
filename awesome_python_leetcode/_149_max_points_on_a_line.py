import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Given an array of points where points[i] = [xi, yi] represents a point on the
        X-Y plane, return the maximum number of points that lie on the same straight
        line.
        """
        max_points = 1
        for i in range(len(points)):
            p1 = points[i]
            count = collections.defaultdict(int)
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p2[0] == p1[0]:
                    slope = float("inf")
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                count[slope] += 1
                max_points = max(max_points, count[slope] + 1)
        return max_points
