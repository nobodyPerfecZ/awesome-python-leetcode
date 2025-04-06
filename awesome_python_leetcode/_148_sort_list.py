from typing import Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]):
        dummy = ListNode(0)
        head = dummy
        while left and right:
            if left.val < right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        if left:
            head.next = left
        if right:
            head.next = right
        return dummy.next

    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a linked list, return the list after sorting it in
        ascending order.
        """
        if not head or not head.next:
            return head

        # Split list into two halfs
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        # Recursion
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
