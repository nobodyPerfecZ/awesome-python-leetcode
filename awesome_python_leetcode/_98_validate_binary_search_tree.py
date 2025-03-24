from typing import Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Given the root of a binary tree, determine if it is a valid binary search
        tree (BST).

        A valid BST is defined as follows:
        - The left subtree of a node contains only nodes with keys less than the node's
        key.
        - The right subtree of a node contains only nodes with keys greater than the
        node's key.
        - Both the left and right subtrees must also be binary search trees.
        """

        def dfs(root: Optional[TreeNode], left: int, right: int):
            if root is None:
                return True
            else:
                return (
                    dfs(root.left, left, root.val)
                    and dfs(root.right, root.val, right)
                    and left < root.val
                    and root.val < right
                )

        return dfs(root, -float("inf"), +float("inf"))
