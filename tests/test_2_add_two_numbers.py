from typing import List

import pytest

from awesome_python_leetcode._2_add_two_numbers import ListNode, Solution


@pytest.mark.parametrize(
    argnames=["l1", "l2", "expected"],
    argvalues=[
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_func(l1: List[int], l2: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    l1 = ListNode.build(l1)
    l2 = ListNode.build(l2)
    expected = ListNode.build(expected)
    actual = Solution().addTwoNumbers(l1, l2)
    assert actual == expected
