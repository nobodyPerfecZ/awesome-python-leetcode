import pytest

from awesome_python_leetcode._7_reverse_integer import Solution


@pytest.mark.parametrize(
    argnames=["x", "expected"],
    argvalues=[
        (123, 321),
        (-123, -321),
        (120, 21),
    ],
)
def test_func(x: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    reversed_x = Solution().reverse(x)
    assert reversed_x == expected
