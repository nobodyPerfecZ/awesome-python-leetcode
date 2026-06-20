from typing import Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Given a linked list, swap every two adjacent nodes and return its head.

        You must solve the problem without modifying the values in the list's nodes
        (i.e., only nodes themselves may be changed.)
        """
        if head is None:
            # Case: End of tree reached
            return None
        if head.next is None:
            # Case: Subtree has only one node
            return head

        # Recursion: Go deeper to first solve the subtree and then perform
        # the swap with the already solved subtree
        left = head
        middle = head.next
        right = self.swapPairs(head.next.next)

        # Swap nodes: Left -> Middle -> Right becomes Middle -> Left -> Right
        left.next = right
        middle.next = left
        return middle
