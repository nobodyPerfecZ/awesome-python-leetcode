from typing import List, Optional, Tuple

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
def test_func(
    head: List[Tuple[int, Optional[int]]], expected: List[Tuple[int, Optional[int]]]
):
    """Tests the solution of a LeetCode problem."""
    head_node = Node.build(head)
    expected_node = Node.build(expected)
    actual_node = Solution().copyRandomList(head_node)
    assert actual_node == expected_node
