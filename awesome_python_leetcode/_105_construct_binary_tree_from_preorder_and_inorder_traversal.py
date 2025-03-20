from typing import List, Optional


from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Given two integer arrays preorder and inorder where preorder is the preorder
        traversal of a binary tree and inorder is the inorder traversal of the same
        tree, construct and return the binary tree.
        """
        if not preorder or not inorder:
            return None
        root = preorder[0]
        mid = inorder.index(root)
        return TreeNode(
            val=root,
            left=self.buildTree(preorder[1 : mid + 1], inorder[:mid]),
            right=self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :]),
        )
