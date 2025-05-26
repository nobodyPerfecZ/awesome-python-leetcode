import pytest

from awesome_python_leetcode._70_climbing_stairs import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (2, 2),
        (3, 3),
    ],
)
def test_funcTD(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    combinations = Solution().climbStairsTD(n)
    assert combinations == expected


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (2, 2),
        (3, 3),
    ],
)
def test_funcBU(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    combinations = Solution().climbStairsBU(n)
    assert combinations == expected


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (2, 2),
        (3, 3),
    ],
)
def test_funcBUOptimized(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    combinations = Solution().climbStairsBUOptimized(n)
    assert combinations == expected
