from typing import Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        """
        You are given the heads of two sorted linked lists list1 and list2.

        Merge the two lists into one sorted list. The list should be made by splicing
        together the nodes of the first two lists.

        Return the head of the merged linked list.
        """
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return ListNode(list2.val, self.mergeTwoLists(None, list2.next))
        elif list2 is None:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, None))
        elif list1.val <= list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
