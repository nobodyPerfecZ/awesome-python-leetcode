from typing import List, Optional

from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Given an integer array nums where the elements are sorted in ascending order,
        convert it to a height-balanced binary search tree.
        """
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(val=nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1 :])
        return node
