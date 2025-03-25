from typing import List

import pytest

from awesome_python_leetcode._21_merge_two_sorted_lists import ListNode, Solution


@pytest.mark.parametrize(
    argnames=["list1", "list2", "expected"],
    argvalues=[
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ],
)
def test_func(list1: List[int], list2: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    list1 = ListNode.build(list1)
    list2 = ListNode.build(list2)
    expected = ListNode.build(expected)
    actual = Solution().mergeTwoLists(list1, list2)
    assert actual == expected
