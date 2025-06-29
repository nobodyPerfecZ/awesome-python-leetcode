from typing import Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Given the root of a binary tree, invert the tree, and return its root."""
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return TreeNode(val=root.val, left=None, right=None)
        elif root.left is None:
            return TreeNode(
                val=root.val,
                left=self.invertTree(root.right),
                right=None,
            )
        elif root.right is None:
            return TreeNode(
                val=root.val,
                left=None,
                right=self.invertTree(root.left),
            )
        else:
            return TreeNode(
                val=root.val,
                left=self.invertTree(root.right),
                right=self.invertTree(root.left),
            )
