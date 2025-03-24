from typing import Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a Binary Search Tree (BST), return the minimum absolute
        difference between the values of any two different nodes in the tree.
        """
        prev, res = None, float("inf")

        def dfs(root: Optional[TreeNode]):
            nonlocal prev, res
            if root is None:
                return
            dfs(root.left)
            if prev:
                res = min(res, abs(root.val - prev.val))
            prev = root
            dfs(root.right)

        dfs(root)
        return res
