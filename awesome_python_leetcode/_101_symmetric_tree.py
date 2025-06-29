from typing import Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Given the root of a binary tree, check whether it is a mirror of itself
        (i.e., symmetric around its center).
        """

        def _is_symmetric(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None and right is None:
                return True
            elif left is None:
                return False
            elif right is None:
                return False
            else:
                return (
                    left.val == right.val
                    and _is_symmetric(left.left, right.right)
                    and _is_symmetric(left.right, right.left)
                )

        if root is None:
            return True
        return _is_symmetric(root.left, root.right)
