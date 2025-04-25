# flake8: noqa
from typing import List

import pytest

from awesome_python_leetcode._1218_longest_arithmetic_subsequence_of_given_difference import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["arr", "difference", "expected"],
    argvalues=[
        ([1, 2, 3, 4], 1, 4),
        ([1, 3, 5, 7], 1, 1),
        ([1, 5, 7, 8, 5, 3, 4, 2, 1], -2, 4),
    ],
)
def test_func(arr: List[int], difference: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    longest_subsequence = Solution().longestSubsequence(arr, difference)
    assert longest_subsequence == expected
