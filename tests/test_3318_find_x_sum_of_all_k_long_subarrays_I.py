from typing import List

import pytest

from awesome_python_leetcode._3318_find_x_sum_of_all_k_long_subarrays_I import Solution


@pytest.mark.parametrize(
    argnames=["nums", "k", "x", "expected"],
    argvalues=[
        ([1, 1, 2, 2, 3, 4, 2, 3], 6, 2, [6, 10, 12]),
        ([3, 8, 7, 8, 7, 5], 2, 2, [11, 15, 15, 15, 12]),
    ],
)
def test_func(nums: List[int], k: int, x: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    x_sums = Solution().findXSum(nums, k, x)
    assert x_sums == expected
