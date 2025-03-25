from typing import List, Optional


class TreeNode:
    """Binary tree node with next pointers."""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
        next: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __eq__(self, other: List[int]) -> bool:
        """Compare the pointers to the next node."""
        if self is None or other is None:
            return True

        cur = self
        i = 0
        while i < len(other):
            if other[i] is None:
                if cur is not None:
                    return False
                i += 1
                if i < len(other):
                    cur = TreeNode.find(self, other[i])
                continue
            else:
                if cur.val != other[i]:
                    return False
                i += 1
                cur = cur.next
        return True

    @staticmethod
    def find(root: Optional["TreeNode"], val: int) -> Optional["TreeNode"]:
        """Find a node with a given value."""
        if root is None:
            return None
        elif root.val == val:
            return root
        else:
            return TreeNode.find(root.left, val) or TreeNode.find(root.right, val)

    @staticmethod
    def build(levelorder: List[int]) -> "TreeNode":
        """Build a binary tree from levelorder traversal."""
        if not levelorder or levelorder[0] is None:
            return None
        root = TreeNode(levelorder[0])
        queue = [root]

        i = 1
        while i < len(levelorder):
            node = queue.pop(0)

            # Left child
            if i < len(levelorder) and levelorder[i] is not None:
                node.left = TreeNode(levelorder[i])
                queue.append(node.left)
            i += 1

            # Right child
            if i < len(levelorder) and levelorder[i] is not None:
                node.right = TreeNode(levelorder[i])
                queue.append(node.right)
            i += 1
        return root


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
