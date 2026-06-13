from typing import List, Optional

import pytest

from awesome_python_leetcode._129_sum_root_to_leaf_numbers import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"], argvalues=[([1, 2, 3], 25), ([4, 9, 0, 5, 1], 1026)]
)
def test_func(root: List[Optional[int]], expected: int):
    """Tests the solution of a LeetCode problem."""
    root_node = TreeNode.build(root)
    sum_root_to_leaf_numbers = Solution().sumNumbers(root_node)
    assert sum_root_to_leaf_numbers == expected
