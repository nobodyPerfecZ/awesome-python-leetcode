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
    def build(values: List[int]) -> "ListNode":
        """Build a singly-linked list."""
        if not values:
            return None

        head = ListNode(val=values[0], next=None)
        prev = head
        for val in values[1:]:
            cur = ListNode(val=val, next=None)
            prev.next = cur
            prev = cur
        return head
