import pytest

from awesome_python_leetcode._8_string_to_integer import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("42", 42),
        ("   -042", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("words and 987", 0),
    ],
)
def test_func(s: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    num = Solution().myAtoi(s)
    assert num == expected
