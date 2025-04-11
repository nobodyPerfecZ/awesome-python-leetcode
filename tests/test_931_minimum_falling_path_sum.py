from typing import List

import pytest

from awesome_python_leetcode._931_minimum_falling_path_sum import Solution


@pytest.mark.parametrize(
    argnames=["matrix", "expected"],
    argvalues=[
        ([[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13),
        ([[-19, 57], [-40, -5]], -59),
    ],
)
def test_func(matrix: List[List[int]], expected: int):
    """Tests the solution of a LeetCode problem."""
    falling_sum = Solution().minFallingPathSum(matrix)
    assert falling_sum == expected
