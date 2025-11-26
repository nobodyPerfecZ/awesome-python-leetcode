from typing import List

import pytest

from awesome_python_leetcode._2435_paths_in_matrix_whose_sum_is_divisible_by_k import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["grid", "k", "expected"],
    argvalues=[
        ([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3, 2),
        ([[0, 0]], 5, 1),
        ([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1, 10),
    ],
)
def test_funcTD(grid: List[List[int]], k: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    paths = Solution().numberOfPathsTD(grid, k)
    assert paths == expected


@pytest.mark.parametrize(
    argnames=["grid", "k", "expected"],
    argvalues=[
        ([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3, 2),
        ([[0, 0]], 5, 1),
        ([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1, 10),
    ],
)
def test_funcBU(grid: List[List[int]], k: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    paths = Solution().numberOfPathsBU(grid, k)
    assert paths == expected
