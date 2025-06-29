from typing import List

import pytest

from awesome_python_leetcode._141_linked_list_cycle import ListNode, Solution


@pytest.mark.parametrize(
    argnames=["head", "pos", "expected"],
    argvalues=[
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
    ],
)
def test_func(head: List[int], pos: int, expected: bool):
    """Tests the solution of a LeetCode problem."""
    head = ListNode.build(head, pos)
    has_cycle = Solution().hasCycle(head)
    assert has_cycle is expected
