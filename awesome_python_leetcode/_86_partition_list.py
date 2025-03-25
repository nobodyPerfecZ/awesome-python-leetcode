from typing import Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Given the head of a linked list and a value x, partition it such that all nodes
        less than x come before nodes greater than or equal to x.

        You should preserve the original relative order of the nodes in each of the two
        partitions.
        """
        left, right = ListNode(0, None), ListNode(0, None)
        ltail, rtail = left, right

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next

        ltail.next = right.next
        rtail.next = None
        return left.next
