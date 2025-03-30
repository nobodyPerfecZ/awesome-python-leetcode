import pytest

from awesome_python_leetcode._69_sqrt_x import Solution


@pytest.mark.parametrize(
    argnames=["x", "expected"],
    argvalues=[
        (4, 2),
        (8, 2),
    ],
)
def test_func(x: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    sqrt = Solution().mySqrt(x)
    assert sqrt == expected
