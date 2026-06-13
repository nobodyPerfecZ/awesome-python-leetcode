from typing import List

import pytest

from awesome_python_leetcode._86_partition_list import (
    ListNode,
    Solution,
)


@pytest.mark.parametrize(
    argnames=["head", "x", "expected"],
    argvalues=[
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
        ([2, 1], 2, [1, 2]),
    ],
)
def test_func(head: List[int], x: int, expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    head_node = ListNode.build(head)
    expected_node = ListNode.build(expected)
    result_node = Solution().partition(head_node, x)
    assert result_node == expected_node
