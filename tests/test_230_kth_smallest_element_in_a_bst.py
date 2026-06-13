from typing import List, Optional

import pytest

from awesome_python_leetcode._230_kth_smallest_element_in_a_bst import Solution
from awesome_python_leetcode.tree import TreeNode


@pytest.mark.parametrize(
    argnames=["root", "k", "expected"],
    argvalues=[([3, 1, 4, None, 2], 1, 1), ([5, 3, 6, 2, 4, None, None, 1], 3, 3)],
)
def test_func(root: List[Optional[int]], k: int, expected: int):
    """Tests the solution of a LeetCode problem."""
    root_node = TreeNode.build(root)
    kth_smallest = Solution().kthSmallest(root_node, k)
    assert kth_smallest == expected
