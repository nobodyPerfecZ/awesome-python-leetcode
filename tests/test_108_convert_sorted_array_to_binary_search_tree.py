from typing import List

import pytest

from awesome_python_leetcode._108_convert_sorted_array_to_binary_search_tree import (
    Solution,
    TreeNode,
)


@pytest.mark.parametrize(
    argnames=["nums", "expected"],
    argvalues=[
        ([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5]),
        ([1, 3], [3, 1]),
    ],
)
def test_func(nums: List[int], expected: List[int]):
    """Tests the solution of a LeetCode problem."""
    expected = TreeNode.build(expected)
    actual = Solution().sortedArrayToBST(nums)
    assert actual == expected
