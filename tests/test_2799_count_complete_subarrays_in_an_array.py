from typing import List

import pytest

from awesome_python_leetcode._2799_count_complete_subarrays_in_an_array import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 3, 1, 2, 2], 4),
        ([5, 5, 5, 5], 10),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    count = Solution().countCompleteSubarrays(nums)
    assert count == expected
