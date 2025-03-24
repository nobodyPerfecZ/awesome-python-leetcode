from typing import List, Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given the root of a binary tree, return the level order traversal of its nodes'
        values. (i.e., from left to right, level by level).
        """
        if root is None:
            return []
        parents = [root]
        result = []
        while parents:
            # Build childs and level
            childs = []
            level = []
            for p in parents:
                if p.left:
                    childs.append(p.left)
                if p.right:
                    childs.append(p.right)
                level.append(p.val)
            parents = childs
            result.append(level)
        return result
