from typing import List

import pytest

from awesome_python_leetcode._120_triangle import Solution


@pytest.mark.parametrize(
    argnames=["triangle", "expected"],
    argvalues=[
        ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
        ([[-10]], -10),
        ([[-1], [2, 3], [1, -1, -3]], -1),
    ],
)
def test_func(triangle: List[List[int]], expected: int):
    """Tests the solution of a LeetCode problem."""
    mts = Solution().minimumTotal(triangle)
    assert mts == expected
