import pytest

from awesome_python_leetcode._224_basic_calculator import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("1 + 1", 2),
        (" 2-1 + 2 ", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
    ],
)
def test_func(s: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    result = Solution().calculate(s)
    assert result == expected
