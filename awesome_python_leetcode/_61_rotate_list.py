from typing import Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def length(self, head: Optional[ListNode]) -> int:
        length, cur = 0, head
        while cur:
            length, cur = length + 1, cur.next
        return length

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, rotate the list to the right by k places.
        """
        if head is None:
            return None
        n = self.length(head)
        k = k % n
        if k == 0:
            return head

        dummy = ListNode(0, head)
        left, right = dummy, head
        while k > 1 and right:
            right = right.next
            k -= 1
        while right.next:
            left = left.next
            right = right.next

        right.next = dummy.next
        dummy.next = left.next
        left.next = None
        return dummy.next
