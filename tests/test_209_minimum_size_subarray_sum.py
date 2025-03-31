from typing import List
import pytest

from awesome_python_leetcode._209_minimum_size_subarray_sum import Solution


@pytest.mark.parametrize(
    argnames=["target", "nums", "expected"],
    argvalues=[
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    ],
)
def test_func(target: int, nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    min_size = Solution().minSubArrayLen(target, nums)
    assert min_size == expected
