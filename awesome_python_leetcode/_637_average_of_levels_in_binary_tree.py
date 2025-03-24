from typing import List, Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Given the root of a binary tree, return the average value of the nodes on each
        level in the form of an array. Answers within 10-5 of the actual answer will be
        accepted.
        """
        parents = [root]
        result = []
        while parents:
            # Build average value
            total_sum = 0
            for p in parents:
                total_sum += p.val
            result.append(total_sum / len(parents))

            # Build childs
            childs = []
            for p in parents:
                if p.left:
                    childs.append(p.left)
                if p.right:
                    childs.append(p.right)
            parents = childs
        return result
