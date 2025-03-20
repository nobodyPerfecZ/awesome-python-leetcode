from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def lowestCommonAncestor(
        self,
        root: "TreeNode",
        p: "TreeNode",
        q: "TreeNode",
    ) -> "TreeNode":
        """
        Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
        in the tree.

        According to the definition of LCA on Wikipedia: “The lowest common ancestor is
        defined between two nodes p and q as the lowest node in T that has both p and q
        as descendants (where we allow a node to be a descendant of itself).”
        """
        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right
