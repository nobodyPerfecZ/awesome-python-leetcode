from typing import Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        def dfs(l1: Optional[ListNode], l2: Optional[ListNode], overhead: int):
            """
            You are given two non-empty linked lists representing two non-negative
            integers. The digits are stored in reverse order, and each of their nodes
            contains a single digit. Add the two numbers and return the sum as a linked
            list.

            You may assume the two numbers do not contain any leading zero, except the
            number 0 itself.
            """
            if l1 is None and l2 is None:
                if overhead == 0:
                    return None
                else:
                    return ListNode(val=overhead, next=None)
            else:
                if l1 is None:
                    val1 = 0
                    next1 = None
                else:
                    val1 = l1.val
                    next1 = l1.next
                if l2 is None:
                    val2 = 0
                    next2 = None
                else:
                    val2 = l2.val
                    next2 = l2.next
            new_val = val1 + val2 + overhead
            digit = new_val % 10
            overhead = new_val // 10
            return ListNode(val=digit, next=dfs(next1, next2, overhead))

        return dfs(l1, l2, 0)
