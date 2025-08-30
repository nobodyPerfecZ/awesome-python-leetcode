from typing import List

import pytest

from awesome_python_leetcode._1329_sort_the_matrix_diagonally import Solution


@pytest.mark.parametrize(
    argnames=["mat", "expected"],
    argvalues=[
        (
            [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]],
            [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]],
        ),
        (
            [
                [11, 25, 66, 1, 69, 7],
                [23, 55, 17, 45, 15, 52],
                [75, 31, 36, 44, 58, 8],
                [22, 27, 33, 25, 68, 4],
                [84, 28, 14, 11, 5, 50],
            ],
            [
                [5, 17, 4, 1, 52, 7],
                [11, 11, 25, 45, 8, 69],
                [14, 23, 25, 44, 58, 15],
                [22, 27, 31, 36, 50, 66],
                [84, 28, 75, 33, 55, 68],
            ],
        ),
    ],
)
def test_func(mat: List[List[int]], expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    sorted_mat = Solution().diagonalSort(mat)
    assert sorted_mat == expected
