# flake8: noqa
from typing import List

import pytest

from awesome_python_leetcode._3392_count_subarrays_of_length_three_with_a_condition import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 2, 1, 4, 1], 1),
        ([1, 1, 1], 0),
        ([8, -10, -4], 0),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    num_sub_arrays = Solution().countSubarrays(nums)
    assert num_sub_arrays == expected
