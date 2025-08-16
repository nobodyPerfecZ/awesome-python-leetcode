from typing import List

import pytest

from awesome_python_leetcode._89_gray_code import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (2, [0, 1, 3, 2]),
        (1, [0, 1]),
    ],
)
def test_func(n: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    gray_code = Solution().grayCode(n)
    assert gray_code == expected
