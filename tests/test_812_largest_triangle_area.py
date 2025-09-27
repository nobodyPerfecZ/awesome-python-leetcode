from typing import List

import pytest

from awesome_python_leetcode._812_largest_triangle_area import Solution


@pytest.mark.parametrize(
    argnames=["points", "expected"],
    argvalues=[
        ([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]], 2.0),
        ([[1, 0], [0, 0], [0, 1]], 0.5),
    ],
)
def test_func(points: List[List[int]], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    triangle_area = Solution().largestTriangleArea(points)
    assert triangle_area == expected
