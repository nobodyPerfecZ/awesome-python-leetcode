from typing import List

import pytest

from awesome_python_leetcode._135_candy import Solution


@pytest.mark.parametrize(
    argnames=["ratings", "expected"],
    argvalues=[
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([29, 51, 87, 87, 72, 12], 12),
    ],
)
def test_func(ratings: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    candies = Solution().candy(ratings)
    assert candies == expected
