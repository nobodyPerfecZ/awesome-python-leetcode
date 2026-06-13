from typing import List, Optional

import pytest

from awesome_python_leetcode._637_average_of_levels_in_binary_tree import Solution
from awesome_python_leetcode.tree import TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([3, 9, 20, None, None, 15, 7], [3.0, 14.5, 11.0]),
        ([3, 9, 20, 15, 7], [3.0, 14.5, 11.0]),
    ],
)
def test_func(root: List[Optional[int]], expected: List[float]):
    """Tests the solution of a LeetCode problem."""
    root_node = TreeNode.build(root)
    average_of_levels = Solution().averageOfLevels(root_node)
    assert average_of_levels == expected
