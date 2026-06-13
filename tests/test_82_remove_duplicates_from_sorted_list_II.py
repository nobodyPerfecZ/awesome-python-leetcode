from typing import List

import pytest

from awesome_python_leetcode._82_remove_duplicates_from_sorted_list_II import (
    ListNode,
    Solution,
)


@pytest.mark.parametrize(
    argnames=["head", "expected"],
    argvalues=[
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 2, 3], [2, 3]),
    ],
)
def test_func(head: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    head_node = ListNode.build(head)
    expected_node = ListNode.build(expected)
    result_node = Solution().deleteDuplicates(head_node)
    assert result_node == expected_node
