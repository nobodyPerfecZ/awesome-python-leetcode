from typing import Optional


from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        You are given the root of a binary tree containing digits from 0 to 9 only.

        Each root-to-leaf path in the tree represents a number.
        - For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
        Return the total sum of all root-to-leaf numbers. Test cases are generated so
        that the answer will fit in a 32-bit integer.

        A leaf node is a node with no children.
        """

        def dfs(root: Optional[TreeNode], curSum: int):
            if root is None:
                return 0
            elif root.left is None and root.right is None:
                return curSum * 10 + root.val
            else:
                return dfs(root.left, curSum * 10 + root.val) + dfs(
                    root.right, curSum * 10 + root.val
                )

        return dfs(root, 0)
