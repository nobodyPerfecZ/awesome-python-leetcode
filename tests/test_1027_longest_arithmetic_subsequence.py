from typing import List

import pytest

from awesome_python_leetcode._1027_longest_arithmetic_subsequence import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([3, 6, 9, 12], 4),
        ([9, 4, 7, 2, 10], 3),
        ([20, 1, 15, 3, 10, 5, 8], 4),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    longest_arithmetic_sequence = Solution().longestArithSeqLength(nums)
    assert longest_arithmetic_sequence == expected
