from typing import List, Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Given the root of a binary tree, imagine yourself standing on the right side of
        it, return the values of the nodes you can see ordered from top to bottom.
        """
        if root is None:
            return []

        parents = [root]
        result = []
        while parents:
            # Get right side of cur level
            result.append(parents[0].val)

            # Build childs
            childs = []
            for p in parents:
                if p.right:
                    childs.append(p.right)
                if p.left:
                    childs.append(p.left)
            parents = childs
        return result
