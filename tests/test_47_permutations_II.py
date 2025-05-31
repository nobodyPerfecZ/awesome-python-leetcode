from typing import List

import pytest

from awesome_python_leetcode._47_permutations_II import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ],
)
def test_func(nums: List[int], expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    permutations = Solution().permuteUnique(nums)
    assert permutations == expected
