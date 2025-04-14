from typing import List

import pytest

from awesome_python_leetcode._673_number_of_longest_increasing_subsequence import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 3, 5, 4, 7], 2),
        ([2, 2, 2, 2, 2], 5),
        ([1, 3, 2], 2),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    num_LIS = Solution().findNumberOfLIS(nums)
    assert num_LIS == expected
