from typing import List

import pytest

from awesome_python_leetcode._3446_sort_matrix_by_diagonals import Solution


@pytest.mark.parametrize(
    argnames=["grid", "expected"],
    argvalues=[
        ([[1, 7, 3], [9, 8, 2], [4, 5, 6]], [[8, 2, 3], [9, 6, 7], [4, 5, 1]]),
        ([[0, 1], [1, 2]], [[2, 1], [1, 0]]),
        ([[1]], [[1]]),
    ],
)
def test_func(grid: List[List[int]], expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    sorted_grid = Solution().sortMatrix(grid)
    assert sorted_grid == expected
