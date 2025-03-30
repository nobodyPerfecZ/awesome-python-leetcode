import pytest

from awesome_python_leetcode._13_roman_to_integer import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ],
)
def test_func(s: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    integer = Solution().romanToInt(s)
    assert integer == expected
