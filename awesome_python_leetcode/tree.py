from typing import List, Optional


class TreeNode:
    """Binary tree node."""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: "TreeNode") -> bool:
        if self is None and other is None:
            return True
        elif self is None:
            return False
        elif other is None:
            return False
        else:
            return (
                self.val == other.val
                and self.left == other.left
                and self.right == other.right
            )

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
