from typing import List

import pytest

from awesome_python_leetcode._23_merge_k_sorted_lists import Solution, ListNode


@pytest.mark.parametrize(
    argnames=["lists", "expected"],
    argvalues=[
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ],
)
def test_func(lists: List[List[int]], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    lists = [ListNode.build(sublist) for sublist in lists]
    expected = ListNode.build(expected)
    actual = Solution().mergeKLists(lists)
    assert actual == expected
