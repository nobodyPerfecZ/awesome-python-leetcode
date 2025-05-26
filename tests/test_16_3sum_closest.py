from typing import List

import pytest

from awesome_python_leetcode._16_3sum_closest import Solution


@pytest.mark.parametrize(
    argnames=["nums", "target", "expected"],
    argvalues=[
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
    ],
)
def test_func(nums: List[int], target: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    closest = Solution().threeSumClosest(nums, target)
    assert closest == expected
