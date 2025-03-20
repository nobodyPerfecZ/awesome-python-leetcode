from typing import List, Optional


from awesome_python_leetcode.tree import TreeNode


class BSTIterator:
    """
    Implement the BSTIterator class that represents an iterator over the in-order
    traversal of a binary search tree (BST):
    - BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The
    root of the BST is given as part of the constructor. The pointer should be
    initialized to a non-existent number smaller than any element in the BST.
    - boolean hasNext() Returns true if there exists a number in the traversal to the
    right of the pointer, otherwise returns false.
    - int next() Moves the pointer to the right, then returns the number at the pointer.

    Notice that by initializing the pointer to a non-existent smallest number, the first
    call to next() will return the smallest element in the BST.

    You may assume that next() calls will always be valid. That is, there will be at
    least a next number in the in-order traversal when next() is called.
    """

    def __init__(self, root: Optional[TreeNode]):
        self.values = self._inorder_traversal(root)
        self.i = 0

    def _inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """Returns the inorder traversal of a binary tree."""
        if root is None:
            return []
        else:
            return (
                self._inorder_traversal(root.left)
                + [root.val]
                + self._inorder_traversal(root.right)
            )

    def next(self) -> int:
        """Returns the next element in the BST."""
        value = self.values[self.i]
        self.i += 1
        return value

    def hasNext(self) -> bool:
        """Returns True if the iterator has a next element."""
        return self.i < len(self.values)
