from typing import List

import pytest

from awesome_python_leetcode._3190_find_minimum_operations_to_make_all_elements_divisible_by_three import (  # noqa: E501
    Solution,
)


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 2, 3, 4], 3),
        ([3, 6, 9], 0),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    min_ops = Solution().minimumOperations(nums)
    assert min_ops == expected
