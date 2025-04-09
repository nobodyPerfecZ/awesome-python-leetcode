import pytest

from awesome_python_leetcode._5_longest_palindromic_substring import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("babad", "bab"),
        ("cbbd", "bb"),
    ],
)
def test_func(s: str, expected: str):
    """Tests the solution of a LeetCode problem."""
    palindrome = Solution().longestPalindrome(s)
    assert palindrome == expected
