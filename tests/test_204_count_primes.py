import pytest

from awesome_python_leetcode._204_count_primes import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (10, 4),
        (0, 0),
        (1, 0),
    ],
)
def test_func(n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    primes = Solution().countPrimes(n)
    assert primes == expected
