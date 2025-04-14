from typing import List

import pytest

from awesome_python_leetcode._1143_longest_common_subsequence import Solution


@pytest.mark.parametrize(
    argnames=["text1", "text2", "expected"],
    argvalues=[
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
    ],
)
def test_func(text1: str, text2: str, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    two_sum = Solution().longestCommonSubsequence(text1, text2)
    assert two_sum == expected
