from typing import List

import pytest

from awesome_python_leetcode._643_maximum_average_subarray_I import Solution


@pytest.mark.parametrize(
    argnames=["nums", "k", "expected"],
    argvalues=[
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
    ],
)
def test_func(nums: List[int], k: int, expected: float):
    """Tests the solution of a LeetCode problem."""
    max_average = Solution().findMaxAverage(nums, k)
    assert max_average == expected
