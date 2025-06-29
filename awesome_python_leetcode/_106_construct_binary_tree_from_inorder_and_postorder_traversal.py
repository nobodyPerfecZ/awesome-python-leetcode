from typing import List, Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Given two integer arrays inorder and postorder where inorder is the inorder
        traversal of a binary tree and postorder is the postorder traversal of the same
        tree, construct and return the binary tree.
        """
        if not inorder or not postorder:
            return None
        else:
            root = postorder.pop(-1)
            mid = inorder.index(root)
            return TreeNode(
                val=root,
                right=self.buildTree(inorder[mid + 1 :], postorder),
                left=self.buildTree(inorder[:mid], postorder),
            )
