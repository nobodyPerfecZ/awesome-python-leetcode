from typing import Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees p and q, write a function to check if they
        are the same or not.

        Two binary trees are considered the same if they are structurally identical, and
        the nodes have the same value.
        """
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False
        else:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
