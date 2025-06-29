from typing import Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def length(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, reverse the nodes of the list k at a time, and
        return the modified list.

        k is a positive integer and is less than or equal to the length of the linked
        list. If the number of nodes is not a multiple of k then left-out nodes, in the
        end, should remain as it is.

        You may not alter the values in the list's nodes, only nodes themselves may be
        changed.
        """
        dummy = ListNode(0, head)
        left, cur = dummy, head
        n = self.length(head)

        for _ in range(n // k):
            prev = None
            for _ in range(k):
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp
            left.next.next = cur
            tmp2 = left.next
            left.next = prev
            left = tmp2

        return dummy.next
