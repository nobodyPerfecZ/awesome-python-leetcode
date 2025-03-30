from typing import List

import pytest

from awesome_python_leetcode._167_two_sum_II_input_array_is_sorted import Solution


@pytest.mark.parametrize(
    argnames=["numbers", "target", "expected"],
    argvalues=[
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
    ],
)
def test_func(numbers: List[int], target: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    two_sum = Solution().twoSum(numbers, target)
    assert two_sum == expected
