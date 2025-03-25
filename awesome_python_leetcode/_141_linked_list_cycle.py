from typing import List, Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __eq__(self, other: "ListNode") -> bool:
        if self is None and other is None:
            return True
        elif self is None:
            return False
        elif other is None:
            return False
        else:
            return self.val == other.val and self.next == other.next

    @staticmethod
    def build(values: List[int], pos: Optional[int] = None) -> "ListNode":
        """Build a singly-linked list with cycle."""
        if not values:
            return None

        i = 0
        prev, head, cycle = None, None, None
        for i, val in enumerate(values):
            if i == 0:
                head = ListNode(val=val)
                prev = head
            else:
                node = ListNode(val=val)
                prev.next = node
                prev = node

            if pos is not None and i == pos:
                cycle = prev
            elif pos is not None and i == len(values) - 1:
                prev.next = cycle
        return head


class Solution:
    """Base class for all LeetCode Problems."""

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Given head, the head of a linked list, determine if the linked list has a cycle
        in it.

        There is a cycle in a linked list if there is some node in the list that can be
        reached again by continuously following the next pointer. Internally, pos is
        used to denote the index of the node that tail's next pointer is connected to.
        Note that pos is not passed as a parameter.

        Return true if there is a cycle in the linked list. Otherwise, return false.
        """
        i, j = head, head
        while j and j.next:
            i = i.next
            j = j.next.next
            if i is j:
                return True
        return False
