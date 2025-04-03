from typing import List

import pytest

from awesome_python_leetcode._73_set_matrix_zeroes import Solution


@pytest.mark.parametrize(
    argnames=["matrix", "expected"],
    argvalues=[
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ),
    ],
)
def test_func(matrix: List[List[int]], expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    Solution().setZeroes(matrix)
    assert matrix == expected
