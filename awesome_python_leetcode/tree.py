from typing import List, Optional


class QuadTreeNode:
    """Quad tree node."""

    def __init__(
        self,
        val: int = 0,
        isLeaf: int | bool = False,
        topLeft: Optional["QuadTreeNode"] = None,
        topRight: Optional["QuadTreeNode"] = None,
        bottomLeft: Optional["QuadTreeNode"] = None,
        bottomRight: Optional["QuadTreeNode"] = None,
    ):
        self.val = val
        self.isLeaf = bool(isLeaf)
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, QuadTreeNode):
            return False
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
            return None  # type: ignore

        node_data = levelorder.pop(0)
        if node_data is None:
            return None  # type: ignore

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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TreeNode):
            return False
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
    def build(levelorder: List[Optional[int]]) -> Optional["TreeNode"]:
        """Build a binary tree from levelorder traversal."""
        if not levelorder:
            return None
        val_0 = levelorder[0]
        if val_0 is None:
            return None
        root = TreeNode(val_0)
        queue = [root]

        i = 1
        while i < len(levelorder):
            node = queue.pop(0)

            # Left child
            if i < len(levelorder):
                val_l = levelorder[i]
                if val_l is not None:
                    node.left = TreeNode(val_l)
                    queue.append(node.left)
            i += 1

            # Right child
            if i < len(levelorder):
                val_r = levelorder[i]
                if val_r is not None:
                    node.right = TreeNode(val_r)
                    queue.append(node.right)
            i += 1
        return root
