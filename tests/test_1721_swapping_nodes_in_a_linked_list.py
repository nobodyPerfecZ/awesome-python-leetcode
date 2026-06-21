from typing import List

import pytest

from awesome_python_leetcode._1721_swapping_nodes_in_a_linked_list import Solution
from awesome_python_leetcode.list import ListNode


@pytest.mark.parametrize(
    argnames=["head", "k", "expected"],
    argvalues=[
        ([1, 2, 3, 4, 5], 2, [1, 4, 3, 2, 5]),
        ([7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5, [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]),
    ],
)
def test_func(head: List[int], k: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    head_node = ListNode.build(head)
    expected_node = ListNode.build(expected)
    result_node = Solution().swapNodes(head_node, k)
    assert result_node == expected_node
