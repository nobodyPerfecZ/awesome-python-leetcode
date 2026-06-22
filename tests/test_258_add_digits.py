import pytest

from awesome_python_leetcode._258_add_digits import Solution


@pytest.mark.parametrize(
    argnames=["num", "expected"],
    argvalues=[
        (38, 2),
        (0, 0),
    ],
)
def test_func(num: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    digits = Solution().addDigits(num)
    assert digits == expected
