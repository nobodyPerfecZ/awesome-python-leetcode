from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        Given an array of points on the X-Y plane points where points[i] = [xi, yi],
        return the area of the largest triangle that can be formed by any three
        different points. Answers within 10-5 of the actual answer will be accepted.
        """
        # [x1, y1] [x2, y2] [x3, y3]
        # Area = 0.5 * |x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)|
        max_area = 0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    new_area = 0.5 * abs(
                        x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
                    )
                    max_area = max(max_area, new_area)
        return max_area
