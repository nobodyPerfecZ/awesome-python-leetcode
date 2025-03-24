from typing import List
import pytest

from awesome_python_leetcode._128_longest_consecutive_sequence import Solution


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
    ],
)
def test_func(nums: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    longest_consecutive = Solution().longestConsecutive(nums)
    assert longest_consecutive == expected
