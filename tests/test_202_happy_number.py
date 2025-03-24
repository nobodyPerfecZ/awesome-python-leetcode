import pytest

from awesome_python_leetcode._202_happy_number import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (19, True),
        (2, False),
    ],
)
def test_func(n: int, expected: bool):
    """Tests the solution of a LeetCode problem."""
    is_happy = Solution().isHappy(n)
    assert is_happy == expected
