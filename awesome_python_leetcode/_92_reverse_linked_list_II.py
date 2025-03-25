from typing import Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int,
    ) -> Optional[ListNode]:
        """
        Given the head of a singly linked list and two integers left and right where
        left <= right, reverse the nodes of the list from position left to position
        right, and return the reversed list.
        """
        dummy = ListNode(0, head)
        prev_left, cur = dummy, head
        for i in range(left - 1):
            prev_left, cur = cur, cur.next

        prev_right = None
        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = prev_right
            prev_right, cur = cur, tmp

        prev_left.next.next = cur
        prev_left.next = prev_right
        return dummy.next
