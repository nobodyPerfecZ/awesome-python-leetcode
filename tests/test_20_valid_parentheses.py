import pytest

from awesome_python_leetcode._20_valid_parentheses import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
    ],
)
def test_func(s: str, expected: bool):
    """Tests the solution of a LeetCode problem."""
    is_valid = Solution().isValid(s)
    assert is_valid is expected
