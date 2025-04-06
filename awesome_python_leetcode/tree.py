from typing import List, Optional


class QuadTreeNode:
    """Quad tree node."""

    def __init__(
        self,
        val: int = 0,
        isLeaf: bool = False,
        topLeft: Optional["QuadTreeNode"] = None,
        topRight: Optional["QuadTreeNode"] = None,
        bottomLeft: Optional["QuadTreeNode"] = None,
        bottomRight: Optional["QuadTreeNode"] = None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def __eq__(self, other: "QuadTreeNode") -> bool:
        if self is None and other is None:
            return True
        elif self is None:
            return False
        elif other is None:
            return False
        else:
            return (
                self.val == other.val
                and self.isLeaf == other.isLeaf
                and self.topLeft == other.topLeft
                and self.topRight == other.topRight
                and self.bottomLeft == other.bottomLeft
                and self.bottomRight == other.bottomRight
            )

    @staticmethod
    def build(levelorder: List[List[int]]) -> "QuadTreeNode":
        """Build a binary tree from levelorder traversal."""
        if not levelorder:
            return None

        node_data = levelorder.pop(0)
        if node_data is None:
            return None

        isLeaf, val = node_data
        head = QuadTreeNode(val, isLeaf)
        queue = [(head, isLeaf)]

        while queue and levelorder:
            node, isLeaf = queue.pop(0)

            node_data = levelorder.pop(0)
            if node_data:
                isLeaf, val = node_data
                node.topLeft = QuadTreeNode(val, isLeaf)
                queue.append((node.topLeft, isLeaf))

            node_data = levelorder.pop(0)
            if node_data:
                isLeaf, val = node_data
                node.topRight = QuadTreeNode(val, isLeaf)
                queue.append((node.topRight, isLeaf))

            node_data = levelorder.pop(0)
            if node_data:
                isLeaf, val = node_data
                node.bottomLeft = QuadTreeNode(val, isLeaf)
                queue.append((node.bottomLeft, isLeaf))

            node_data = levelorder.pop(0)
            if node_data:
                isLeaf, val = node_data
                node.bottomRight = QuadTreeNode(val, isLeaf)
                queue.append((node.bottomRight, isLeaf))
        return head


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
