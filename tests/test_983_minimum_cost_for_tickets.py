from typing import List

import pytest

from awesome_python_leetcode._983_minimum_cost_for_tickets import Solution


@pytest.mark.parametrize(
    argnames=["days", "costs", "expected"],
    argvalues=[
        ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
    ],
)
def test_func(days: List[int], costs: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    min_ticket_costs = Solution().mincostTickets(days, costs)
    assert min_ticket_costs == expected
