from typing import Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return its maximum depth.

        A binary tree's maximum depth is the number of nodes along the longest path
        from the root node down to the farthest leaf node.
        """
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
