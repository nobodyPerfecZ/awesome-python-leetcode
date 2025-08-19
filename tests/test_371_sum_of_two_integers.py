import pytest

from awesome_python_leetcode._371_sum_of_two_integers import Solution


@pytest.mark.parametrize(
    argnames=["a", "b", "expected"],
    argvalues=[
        (1, 2, 3),
        (2, 3, 5),
    ],
)
def test_func(a: int, b: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    sum = Solution().getSum(a, b)
    assert sum == expected
