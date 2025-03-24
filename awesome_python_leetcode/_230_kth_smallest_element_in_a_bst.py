from typing import Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Given the root of a binary search tree, and an integer k, return the kth
        smallest value (1-indexed) of all the values of the nodes in the tree.
        """
        res = 0

        def dfs(root: Optional[TreeNode]):
            nonlocal res, k
            if root is None:
                return
            else:
                dfs(root.left)
                if k > 0:
                    res = root.val
                    k -= 1
                dfs(root.right)

        dfs(root)
        return res
