from typing import List

import pytest

from awesome_python_leetcode._1304_find_n_unique_integers_sum_up_to_zero import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (5, [0, -1, 1, -2, 2]),
        (3, [0, -1, 1]),
        (1, [0]),
    ],
)
def test_func(n: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    sum_zero = Solution().sumZero(n)
    assert sum_zero == expected
