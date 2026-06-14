from typing import List

import pytest

from awesome_python_leetcode._2130_maximum_twin_sum_of_a_linked_list import Solution
from awesome_python_leetcode.list import ListNode


@pytest.mark.parametrize(
    argnames=["head", "expected"],
    argvalues=[
        ([5, 4, 2, 1], 6),
        ([4, 2, 2, 3], 7),
        ([1, 100000], 100001),
    ],
)
def test_func(head: List[int], expected: int):
    """Tests the solution of a LeetCode problem."""
    head_node = ListNode.build(head)
    actual = Solution().pairSum(head_node)
    assert actual == expected
