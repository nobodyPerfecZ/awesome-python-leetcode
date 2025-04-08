import pytest

from awesome_python_leetcode._70_climbing_stairs import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (2, 2),
        (3, 3),
    ],
)
def test_func(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    combinations = Solution().climbStairs(n)
    assert combinations == expected
