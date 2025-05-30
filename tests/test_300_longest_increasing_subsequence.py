from typing import List

import pytest

from awesome_python_leetcode._300_longest_increasing_subsequence import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ],
)
def test_func_bs(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    length = Solution().lengthOfLISBS(nums)
    assert length == expected


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ],
)
def test_func_dp(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    length = Solution().lengthOfLISDP(nums)
    assert length == expected
