import pytest

from awesome_python_leetcode._392_is_subsequence import Solution


@pytest.mark.parametrize(
    argnames=["s", "t", "expected"],
    argvalues=[
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
    ],
)
def test_func(s: str, t: str, expected: bool):
    """Tests the solution of a LeetCode problem."""
    is_subsequence = Solution().isSubsequence(s, t)
    assert is_subsequence == expected
