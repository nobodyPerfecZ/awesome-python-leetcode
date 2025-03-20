from typing import Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
        in the sequence has an edge connecting them. A node can only appear in the
        sequence at most once. Note that the path does not need to pass through the
        root.

        The path sum of a path is the sum of the node's values in the path.

        Given the root of a binary tree, return the maximum path sum of any non-empty
        path.
        """
        res = [root.val]

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            else:
                left = max(dfs(root.left), 0)
                right = max(dfs(root.right), 0)
                res[0] = max(res[0], root.val + left + right)
                return root.val + max(left, right)

        dfs(root)
        return res[0]
