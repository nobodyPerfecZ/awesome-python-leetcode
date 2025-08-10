from typing import List

import pytest

from awesome_python_leetcode._260_single_number_III import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 2, 1, 3, 2, 5], [3, 5]),
        ([-1, 0], [-1, 0]),
        ([0, 1], [1, 0]),
    ],
)
def test_func(nums: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    single_numbers = Solution().singleNumber(nums)
    assert single_numbers == expected
