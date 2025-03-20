from typing import Optional


from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Given the root of a binary tree and an integer targetSum, return true if the
        tree has a root-to-leaf path such that adding up all the values along the path
        equals targetSum.

        A leaf is a node with no children.
        """
        if root is None:
            return False
        elif root.left is None and root.right is None:
            return targetSum - root.val == 0
        elif root.left is None:
            return self.hasPathSum(root.right, targetSum - root.val)
        elif root.right is None:
            return self.hasPathSum(root.left, targetSum - root.val)
        else:
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
                root.right, targetSum - root.val
            )
