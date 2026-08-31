from typing import List

import pytest

from awesome_python_leetcode._2058_find_the_minimum_and_maximum_number_of_nodes_between_critical_points import (  # noqa: E501
    Solution,
)
from awesome_python_leetcode.list import ListNode


@pytest.mark.parametrize(
    argnames=["head", "expected"],
    argvalues=[
        ([3, 1], [-1, -1]),
        ([5, 3, 1, 2, 5, 1, 2], [1, 3]),
        ([1, 3, 2, 2, 3, 2, 2, 2, 7], [3, 3]),
    ],
)
def test_func(head: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    nodes = ListNode.build(head)
    nodes_between_critical_points = Solution().nodesBetweenCriticalPoints(nodes)
    assert nodes_between_critical_points == expected
