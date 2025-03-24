from typing import List

import pytest

from awesome_python_leetcode._189_rotate_array import Solution


@pytest.mark.parametrize(
    argnames=["nums", "k", "expected"],
    argvalues=[
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ],
)
def test_func(nums: List[int], k: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    Solution().rotate(nums, k)
    assert nums == expected
