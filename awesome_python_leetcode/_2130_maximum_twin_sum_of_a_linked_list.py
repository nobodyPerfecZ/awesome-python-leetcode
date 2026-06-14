from typing import Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            assert slow is not None
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first = head
        second = prev
        max_sum = 0

        while second:
            assert first is not None
            max_sum = max(max_sum, first.val + second.val)

            first = first.next
            second = second.next

        return max_sum
