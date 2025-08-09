from typing import List

import pytest

from awesome_python_leetcode._338_counting_bits import Solution


@pytest.mark.parametrize(
    argnames=["n", "expected"],
    argvalues=[
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
    ],
)
def test_func(n: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    bits = Solution().countBits(n)
    assert bits == expected
