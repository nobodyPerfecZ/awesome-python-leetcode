from typing import List

import pytest

from awesome_python_leetcode._129_sum_root_to_leaf_numbers import Solution, TreeNode


@pytest.mark.parametrize(
    argnames=["root", "expected"],
    argvalues=[
        ([1, 2, 3], 25),
        ([4, 9, 0, 5, 1], 1026),
    ],
)
def test_func(root: List[int], expected: int):
    root = TreeNode.build(root)
    sum_root_to_leaf_numbers = Solution().sumNumbers(root)
    assert sum_root_to_leaf_numbers == expected
