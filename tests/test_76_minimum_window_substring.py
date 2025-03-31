import pytest

from awesome_python_leetcode._76_minimum_window_substring import Solution


@pytest.mark.parametrize(
    argnames=["s", "t", "expected"],
    argvalues=[
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
    ],
)
def test_func(s: str, t: str, expected: str):
    """Tests the solution of a LeetCode problem."""
    minWindow = Solution().minWindow(s, t)
    assert minWindow == expected
