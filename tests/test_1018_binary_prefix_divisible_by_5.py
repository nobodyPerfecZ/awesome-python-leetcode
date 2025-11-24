from typing import List

import pytest

from awesome_python_leetcode._1018_binary_prefix_divisible_by_5 import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([0, 1, 1], [True, False, False]),
        ([1, 1, 1], [False, False, False]),
    ],
)
def test_func(nums: List[int], expected: List[bool]):
    """Tests the solution of a LeetCode problem."""
    prefixes = Solution().prefixesDivBy5(nums)
    assert prefixes == expected
