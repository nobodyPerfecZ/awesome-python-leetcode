from typing import List

import pytest

from awesome_python_leetcode._46_permutations import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ],
)
def test_func(nums: List[int], expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    permutations = Solution().permute(nums)
    assert permutations == expected
