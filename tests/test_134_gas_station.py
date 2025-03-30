from typing import List

import pytest

from awesome_python_leetcode._134_gas_station import Solution


@pytest.mark.parametrize(
    argnames=["gas", "cost", "expected"],
    argvalues=[
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
        ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4),
    ],
)
def test_func(gas: List[int], cost: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    index = Solution().canCompleteCircuit(gas, cost)
    assert index == expected
