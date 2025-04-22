from typing import List, Optional, Tuple

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        Given an integer n, return all the structurally unique BST's
        (binary search trees), which has exactly n nodes of unique values from 1 to n.
        Return the answer in any order.
        """
        dp = {}

        def dfs(remain: Tuple[int]):
            if not remain:
                return [None]
            if remain in dp:
                return dp[remain]
            trees = []
            for i in range(len(remain)):
                left = dfs(remain[:i])
                right = dfs(remain[i + 1 :])
                for left_ in left:
                    for right_ in right:
                        node = TreeNode(val=remain[i])
                        node.left = left_
                        node.right = right_
                        trees.append(node)
            dp[remain] = trees
            return trees

        return dfs(tuple([i for i in range(1, n + 1)]))
