from typing import List

import pytest

from awesome_python_leetcode._149_max_points_on_a_line import Solution


@pytest.mark.parametrize(
    argnames=["points", "expected"],
    argvalues=[
        ([[1, 1], [2, 2], [3, 3]], 3),
        ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
    ],
)
def test_func(points: List[List[int]], expected: int):
    """Tests the solution of a LeetCode problem."""
    max_points = Solution().maxPoints(points)
    assert max_points == expected
