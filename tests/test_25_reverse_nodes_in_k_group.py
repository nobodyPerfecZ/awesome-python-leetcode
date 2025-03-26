from typing import List

import pytest

from awesome_python_leetcode._25_reverse_nodes_in_k_group import ListNode, Solution


@pytest.mark.parametrize(
    argnames=["head", "k", "expected"],
    argvalues=[
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ],
)
def test_func(head: List[int], k: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    head = ListNode.build(head)
    expected = ListNode.build(expected)
    head = Solution().reverseKGroup(head, k)
    assert head == expected
