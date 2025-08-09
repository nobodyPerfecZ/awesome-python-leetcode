import pytest

from awesome_python_leetcode._389_find_the_difference import Solution


@pytest.mark.parametrize(
    argnames=["s", "t", "expected"],
    argvalues=[
        ("abcd", "abcde", "e"),
        ("", "y", "y"),
    ],
)
def test_func(s: str, t: str, expected: str):
    """Tests the solution of a LeetCode problem."""
    difference = Solution().findTheDifference(s, t)
    assert difference == expected
