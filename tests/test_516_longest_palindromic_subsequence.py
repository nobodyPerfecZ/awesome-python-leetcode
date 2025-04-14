import pytest

from awesome_python_leetcode._516_longest_palindromic_subsequence import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("bbbab", 4),
        ("cbbd", 2),
    ],
)
def test_func(s: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    lcs = Solution().longestPalindromeSubseq(s)
    assert lcs == expected
