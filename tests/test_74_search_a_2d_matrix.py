from typing import List

import pytest

from awesome_python_leetcode._74_search_a_2d_matrix import Solution


@pytest.mark.parametrize(
    argnames=["matrix", "target", "expected"],
    argvalues=[
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ],
)
def test_func(matrix: List[List[int]], target: int, expected: bool):
    """Tests the solution of a LeetCode problem."""
    actual = Solution().searchMatrix(matrix, target)
    assert actual is expected
