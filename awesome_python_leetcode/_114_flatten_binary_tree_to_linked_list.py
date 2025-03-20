from typing import Optional


from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def flatten(self, root: Optional[TreeNode]):
        """
        Given the root of a binary tree, flatten the tree into a "linked list":
        - The "linked list" should use the same TreeNode class where the right child
        pointer points to the next node in the list and the left child pointer is always
        null.
        - The "linked list" should be in the same order as a pre-order traversal of the
        binary tree.
        - Do not return anything, modify root in-place instead.
        """

        def dfs(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return None

            left = dfs(root.left)
            right = dfs(root.right)

            if root.left:
                left.right = root.right
                root.right = root.left
                root.left = None

            last = right or left or root
            return last

        dfs(root)
