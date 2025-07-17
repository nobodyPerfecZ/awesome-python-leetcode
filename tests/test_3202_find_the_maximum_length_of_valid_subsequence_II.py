from typing import List

import pytest

from awesome_python_leetcode._3202_find_the_maximum_length_of_valid_subsequence_II import (  # noqa: E501
    Solution,
)


@pytest.mark.parametrize(
    argnames=["nums", "k", "expected"],
    argvalues=[
        ([1, 2, 3, 4, 5], 2, 5),
        ([1, 4, 2, 3, 1, 4], 3, 4),
    ],
)
def test_func(nums: List[int], k: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    two_sum = Solution().maximumLength(nums, k)
    assert two_sum == expected
