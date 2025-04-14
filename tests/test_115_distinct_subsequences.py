import pytest

from awesome_python_leetcode._115_distinct_subsequences import Solution


@pytest.mark.parametrize(
    argnames=["s", "t", "expected"],
    argvalues=[
        ("rabbbit", "rabbit", 3),
        ("babgbag", "bag", 5),
    ],
)
def test_func(s: str, t: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    distinct = Solution().numDistinct(s, t)
    assert distinct == expected
