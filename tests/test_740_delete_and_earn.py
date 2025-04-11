from typing import List

import pytest

from awesome_python_leetcode._740_delete_and_earn import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([3, 4, 2], 6),
        ([2, 2, 3, 3, 3, 4], 9),
        ([1], 1),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    earned = Solution().deleteAndEarn(nums)
    assert earned == expected
