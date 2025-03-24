from typing import List, Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given the root of a binary tree, return the zigzag level order traversal of its
        nodes' values. (i.e., from left to right, then right to left for the next level
        and alternate between).
        """
        if root is None:
            return []
        parents = [root]
        result = []
        even_level = True
        while parents:
            # Build childs and zig-zag levelorder
            childs = []
            levelorder = []
            for p in reversed(parents):
                if even_level:
                    if p.left:
                        childs.append(p.left)
                    if p.right:
                        childs.append(p.right)
                else:
                    if p.right:
                        childs.append(p.right)
                    if p.left:
                        childs.append(p.left)
                levelorder.append(p.val)
            parents = childs
            result.append(levelorder)
            even_level = not even_level
        return result
