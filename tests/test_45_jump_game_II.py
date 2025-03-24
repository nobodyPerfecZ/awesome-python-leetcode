from typing import List

import pytest

from awesome_python_leetcode._45_jump_game_II import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    num_jumps = Solution().jump(nums)
    assert num_jumps == expected
