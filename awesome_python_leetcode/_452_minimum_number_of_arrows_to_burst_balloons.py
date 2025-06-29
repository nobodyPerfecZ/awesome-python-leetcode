from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        There are some spherical balloons taped onto a flat wall that represents the
        XY-plane. The balloons are represented as a 2D integer array points where
        points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches
        between xstart and xend. You do not know the exact y-coordinates of the
        balloons.

        Arrows can be shot up directly vertically (in the positive y-direction) from
        different points along the x-axis. A balloon with xstart and xend is burst by an
        arrow shot at x if xstart <= x <= xend. There is no limit to the number of
        arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting
        any balloons in its path.

        Given the array points, return the minimum number of arrows that must be shot to
        burst all balloons.
        """
        points = sorted(points, key=lambda p: p[0])
        left, right = points[0][0], points[0][1]
        i, output = 1, 1
        while i < len(points):
            c_left, c_right = points[i][0], points[i][1]
            new_left, new_right = max(left, c_left), min(right, c_right)
            if new_left <= new_right:
                left, right = new_left, new_right
            else:
                left, right = c_left, c_right
                output += 1
            i += 1
        return output
