from typing import List

import pytest

from awesome_python_leetcode._637_average_of_levels_in_binary_tree import Solution
from awesome_python_leetcode.tree import TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([3, 9, 20, None, None, 15, 7], [3.00000, 14.50000, 11.00000]),
        ([3, 9, 20, 15, 7], [3.00000, 14.50000, 11.00000]),
    ],
)
def test_func(root: List[int], expected: List[float]):
    root = TreeNode.build(root)
    average_of_levels = Solution().averageOfLevels(root)
    assert average_of_levels == expected
