from typing import List

import pytest

from awesome_python_leetcode._19_remove_nth_node_from_end_of_list import (
    ListNode,
    Solution,
)


@pytest.mark.parametrize(
    argnames=["head", "n", "expected"],
    argvalues=[
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ],
)
def test_func(head: List[int], n: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    head = ListNode.build(head)
    expected = ListNode.build(expected)
    head = Solution().removeNthFromEnd(head, n)
    assert head == expected
