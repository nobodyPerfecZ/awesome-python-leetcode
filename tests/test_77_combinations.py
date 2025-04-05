from typing import List

import pytest

from awesome_python_leetcode._77_combinations import Solution


@pytest.mark.parametrize(
    argnames=["n", "k", "expected"],
    argvalues=[
        (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
        (1, 1, [[1]]),
    ],
)
def test_func(n: int, k: int, expected: List[List[int]]):
    """Tests the solution of a LeetCode problem."""
    combinations = Solution().combine(n, k)
    assert combinations == expected
