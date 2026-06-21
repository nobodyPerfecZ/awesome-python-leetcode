from typing import Optional

from awesome_python_leetcode.list import ListNode


class Solution:
    """Base class for all LeetCode Problems."""

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        You are given the head of a linked list, and an integer k.
        Return the head of the linked list after swapping the values of the kth node
        from the beginning and the kth node from the end (the list is 1-indexed).
        """
        # Build array of values
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        # Swap kth element
        first_idx, second_idx = k - 1, len(arr) - k
        tmp = arr[first_idx].val
        arr[first_idx].val = arr[second_idx].val
        arr[second_idx].val = tmp

        return head
