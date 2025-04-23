from typing import Optional, Tuple

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def rob(self, root: Optional[TreeNode]) -> int:
        """
        The thief has found himself a new place for his thievery again. There is only
        one entrance to this area, called root.

        Besides the root, each house has one and only one parent house. After a tour,
        the smart thief realized that all houses in this place form a binary tree. It
        will automatically contact the police if two directly-linked houses were broken
        into on the same night.

        Given the root of the binary tree, return the maximum amount of money the thief
        can rob without alerting the police.
        """

        def dfs(root: Optional[TreeNode]) -> Tuple[int, int]:
            if root is None:
                return 0, 0
            left_first, left_second = dfs(root.left)
            right_first, right_second = dfs(root.right)
            tmp = max(root.val + left_second + right_second, left_first + right_first)
            second = left_first + right_first
            first = tmp
            return first, second

        return dfs(root)[0]
