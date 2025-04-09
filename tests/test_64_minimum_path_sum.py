from typing import List

import pytest

from awesome_python_leetcode._64_minimum_path_sum import Solution


@pytest.mark.parametrize(
    argnames=["grid", "expected"],
    argvalues=[
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 2, 3], [4, 5, 6]], 12),
    ],
)
def test_func(grid: List[List[int]], expected: int):
    """Tests the solution of a LeetCode problem."""
    mps = Solution().minPathSum(grid)
    assert mps == expected
