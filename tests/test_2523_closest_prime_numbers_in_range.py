from typing import List

import pytest

from awesome_python_leetcode._2523_closest_prime_numbers_in_range import Solution


@pytest.mark.parametrize(
    argnames=["left", "right", "expected"],
    argvalues=[
        (10, 19, [11, 13]),
        (4, 6, [-1, -1]),
        (19, 31, [29, 31]),
    ],
)
def test_func(left: int, right: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    closest_primes = Solution().closestPrimes(left, right)
    assert closest_primes == expected
