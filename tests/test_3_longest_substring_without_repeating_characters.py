import pytest

from awesome_python_leetcode._3_longest_substring_without_repeating_characters import (
    Solution,
)


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ],
)
def test_func(s: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    max_length = Solution().lengthOfLongestSubstring(s)
    assert max_length == expected
