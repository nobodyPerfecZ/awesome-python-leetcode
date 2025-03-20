from typing import List, Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

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

    @staticmethod
    def compare(t1: "TreeNode", t2: "TreeNode") -> bool:
        """Compare two binary trees."""
        if t1 is None and t2 is None:
            return True
        elif t1 is None:
            return False
        elif t2 is None:
            return False
        else:
            return (
                t1.val == t2.val
                and TreeNode.compare(t1.left, t2.left)
                and TreeNode.compare(t1.right, t2.right)
            )

    @staticmethod
    def compare_next(root: "TreeNode", nexts: List[int]) -> bool:
        """Compare the pointers to the next node."""
        if root is None or nexts is None:
            return True

        cur = root
        i = 0
        while i < len(nexts):
            if nexts[i] is None:
                if cur is not None:
                    return False
                i += 1
                if i < len(nexts):
                    cur = TreeNode.find(root, nexts[i])
                continue
            else:
                if cur.val != nexts[i]:
                    return False
                i += 1
                cur = cur.next
        return True
