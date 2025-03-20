from awesome_python_leetcode.tree import TreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def connect(self, root: TreeNode) -> TreeNode:
        """
        Populate each next pointer to point to its next right node. If there is no next
        right node, the next pointer should be set to NULL.

        Initially, all next pointers are set to NULL.
        """
        if root is None:
            return None

        parents = [root]
        while parents:
            # Connect nodes together
            for i in range(len(parents) - 1):
                parents[i].next = parents[i + 1]

            # Build next layer
            children = []
            for parent in parents:
                if parent.left is not None and parent.right is not None:
                    children.append(parent.left)
                    children.append(parent.right)
                elif parent.left is not None:
                    children.append(parent.left)
                elif parent.right is not None:
                    children.append(parent.right)

            # Update layer
            parents = children
        return root
