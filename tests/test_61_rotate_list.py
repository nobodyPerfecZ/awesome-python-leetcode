from typing import List

import pytest

from awesome_python_leetcode._61_rotate_list import ListNode, Solution


@pytest.mark.parametrize(
    argnames=["head", "k", "expected"],
    argvalues=[([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]), ([0, 1, 2], 4, [2, 0, 1])],
)
def test_func(head: List[int], k: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    head_node = ListNode.build(head)
    expected_node = ListNode.build(expected)
    head_node = Solution().rotateRight(head_node, k)
    assert head_node == expected_node
