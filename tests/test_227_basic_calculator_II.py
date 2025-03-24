import pytest

from awesome_python_leetcode._227_basic_calculator_II import Solution


@pytest.mark.parametrize(
    argnames=["s", "expected"],
    argvalues=[
        ("3+2*2", 7),
        (" 3/2 ", 1),
        (" 3+5 / 2 ", 5),
    ],
)
def test_func(s: str, expected: int):
    """Tests the solution of a LeetCode problem."""
    result = Solution().calculate(s)
    assert result == expected
