from typing import Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, remove the nth node from the end of the list
        and return its head.
        """
        dummy = ListNode(0, head)
        left, right = dummy, head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
