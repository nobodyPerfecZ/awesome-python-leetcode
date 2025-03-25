from typing import Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a sorted linked list, delete all nodes that have duplicate
        numbers, leaving only distinct numbers from the original list. Return the linked
        list sorted as well.
        """
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next
