from typing import List

import pytest

from awesome_python_leetcode._54_spiral_matrix import Solution


@pytest.mark.parametrize(
    argnames=["matrix", "expected"],
    argvalues=[
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
    ],
)
def test_func(matrix: List[List[int]], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    spiral_order = Solution().spiralOrder(matrix)
    assert spiral_order == expected
