from typing import List

import pytest

from awesome_python_leetcode._474_ones_and_zeroes import Solution


@pytest.mark.parametrize(
    argnames=["strs", "m", "n", "expected"],
    argvalues=[
        (["10", "0001", "111001", "1", "0"], 5, 3, 4),
        (["10", "0", "1"], 1, 1, 2),
    ],
)
def test_func(strs: List[str], m: int, n: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    max_subset = Solution().findMaxForm(strs, m, n)
    assert max_subset == expected
