from typing import Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a complete binary tree, return the number of the nodes in the
        tree.

        According to Wikipedia, every level, except possibly the last, is completely
        filled in a complete binary tree, and all nodes in the last level are as far
        left as possible. It can have between 1 and 2h nodes inclusive at the last
        level h.

        Design an algorithm that runs in less than O(n) time complexity.
        """
        if root is None:
            return 0
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
