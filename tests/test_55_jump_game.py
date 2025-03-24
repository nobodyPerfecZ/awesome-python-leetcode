from typing import List

import pytest

from awesome_python_leetcode._55_jump_game import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ],
)
def test_func(nums: List[int], expected: bool):
    """Tests the solution of a LeetCode problem."""
    can_jump = Solution().canJump(nums)
    assert can_jump == expected
