from typing import List

import pytest

from awesome_python_leetcode._24_swap_nodes_in_pairs import Solution
from awesome_python_leetcode.list import ListNode


@pytest.mark.parametrize(
    argnames=["head", "expected"],
    argvalues=[
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [2, 1, 3]),
    ],
)
def test_func(head: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    head_node = ListNode.build(head)
    expected_node = ListNode.build(expected)
    swapped_node = Solution().swapPairs(head_node)
    assert swapped_node == expected_node
