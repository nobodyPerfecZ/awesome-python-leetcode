from typing import List, Optional

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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        You are given an array of k linked-lists lists, each linked-list is sorted in
        ascending order.

        Merge all the linked-lists into one sorted linked-list and return it.
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.merge(lists[0], lists[1])
        else:
            mid = len(lists) // 2
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])
            return self.merge(left, right)
