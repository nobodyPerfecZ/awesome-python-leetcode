import pytest

from awesome_python_leetcode._10_regular_expression_matching import Solution


@pytest.mark.parametrize(
    argnames=["s", "p", "expected"],
    argvalues=[
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("ab", ".*c", False),
        ("a", "ab*", True),
    ],
)
def test_func(s: str, p: str, expected: bool):
    """Tests the solution of a LeetCode problem."""
    is_match = Solution().isMatch(s, p)
    assert is_match is expected
