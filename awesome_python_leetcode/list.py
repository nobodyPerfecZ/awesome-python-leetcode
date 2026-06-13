from typing import List, Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next

    @staticmethod
    def build(values: List[int]) -> Optional["ListNode"]:
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
