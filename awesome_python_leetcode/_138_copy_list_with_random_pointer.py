from typing import List, Optional, Tuple


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __hash__(self):
        return hash(self.val)

    def __eq__(self, other: "Node") -> bool:
        n1, n2 = self, other
        while n1 and n2:
            if n1.val != n2.val:
                return False
            elif n1.random is None and n2.random:
                return False
            elif n1.random and n2.random is None:
                return False
            elif n1.random and n2.random and n1.random.val != n2.random.val:
                return False
            n1, n2 = n1.next, n2.next
        if n1 is None and n2:
            return False
        if n1 and n2 is None:
            return False
        return True

    @staticmethod
    def build(values: List[Tuple[int, Optional[int]]]) -> "Node":
        """Build a singly-linked list."""
        if not values:
            return None

        # Step 1: Create all nodes without setting random pointers
        nodes = [Node(x) for x, _ in values]

        # Step 2: Set the `next` pointers
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        # Step 3: Set the `random` pointers
        for i, (_, random_index) in enumerate(values):
            if random_index is not None:
                nodes[i].random = nodes[random_index]

        return nodes[0]


class Solution:
    """Base class for all LeetCode Problems."""

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        A linked list of length n is given such that each node contains an additional
        random pointer, which could point to any node in the list, or null.

        Construct a deep copy of the list. The deep copy should consist of exactly n
        brand new nodes, where each new node has its value set to the value of its
        corresponding original node. Both the next and random pointer of the new nodes
        should point to new nodes in the copied list such that the pointers in the
        original list and copied list represent the same list state. None of the
        pointers in the new list should point to nodes in the original list.

        For example, if there are two nodes X and Y in the original list, where
        X.random --> Y, then for the corresponding two nodes x and y in the copied
        list, x.random --> y.

        Return the head of the copied linked list.

        The linked list is represented in the input/output as a list of n nodes. Each
        node is represented as a pair of [val, random_index] where:
        - val: an integer representing Node.val
        - random_index: the index of the node (range from 0 to n-1) that the random
        pointer points to, or null if it does not point to any node.

        Your code will only be given the head of the original linked list.
        """
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]
