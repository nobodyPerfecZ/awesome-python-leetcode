from typing import List

import pytest

from awesome_python_leetcode._92_reverse_linked_list_II import ListNode, Solution


@pytest.mark.parametrize(
    argnames=["head", "left", "right", "expected"],
    argvalues=[
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
    ],
)
def test_func(head: List[int], left: int, right: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    head = ListNode.build(head)
    expected = ListNode.build(expected)
    head = Solution().reverseBetween(head, left, right)
    assert head == expected
