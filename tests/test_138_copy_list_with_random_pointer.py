from typing import List

import pytest

from awesome_python_leetcode._138_copy_list_with_random_pointer import Node, Solution


@pytest.mark.parametrize(
    argnames=["head", "expected"],
    argvalues=[
        (
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        ),
        ([[1, 1], [2, 1]], [[1, 1], [2, 1]]),
        ([[3, None], [3, 0], [3, None]], [[3, None], [3, 0], [3, None]]),
    ],
)
def test_func(head: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    head = Node.build(head)
    expected = Node.build(expected)
    head = Solution().copyRandomList(head)
    assert head == expected
