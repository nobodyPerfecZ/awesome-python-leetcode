from typing import List

import pytest

from awesome_python_leetcode._148_sort_list import Solution, ListNode


@pytest.mark.parametrize(
    argnames=["head", "expected"],
    argvalues=[
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
        ([], []),
    ],
)
def test_func(head: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    head = ListNode.build(head)
    expected = ListNode.build(expected)
    actual = Solution().sortList(head)
    assert actual == expected
