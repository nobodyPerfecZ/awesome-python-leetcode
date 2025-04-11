from typing import List

import pytest

from awesome_python_leetcode._118_pascals_triangle import Solution


@pytest.mark.parametrize(
    argnames=["numRows", "expected"],
    argvalues=[
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
    ],
)
def test_func(numRows: int, expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    pascals = Solution().generate(numRows)
    assert pascals == expected
