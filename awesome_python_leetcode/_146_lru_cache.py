from typing import Optional


class Node:
    """A node in a doubly linked list used for LRU cache.

    Attributes:
        key (int): The key of the cached item.
        val (int): The value of the cached item.
        prev (Optional[Node]): Pointer to the previous node.
        next (Optional[Node]): Pointer to the next node.
    """

    def __init__(
        self,
        key: int,
        val: int,
        prev: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ) -> None:
        """Initializes a new Node.

        Args:
            key: The key of the cached item.
            val: The value of the cached item.
            prev: Pointer to the previous node.
            next: Pointer to the next node.
        """
        self.key: int = key
        self.val: int = val
        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next


class LRUCache:
    """Design a data structure that follows the constraints of a Least Recently
    Used (LRU) cache.

    Implement the LRUCache class:
    - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    - int get(int key) Return the value of the key if the key exists,
      otherwise return -1.
    - void put(int key, int value) Update the value of the key if the key exists.
      Otherwise, add the key-value pair to the cache. If the number of keys exceeds the
      capacity from this operation, evict the least recently used key.

    The functions get and put must each run in O(1) average time complexity.
    """

    def __init__(self, capacity: int) -> None:
        """Initializes the LRU cache with capacity.

        Args:
            capacity: Positive size capacity of the cache.
        """
        self.cap: int = capacity
        self.cache: dict[int, Node] = {}

        # left=LRU, right=MRU
        self.left: Node = Node(0, 0)
        self.right: Node = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node) -> None:
        """Removes a node from the doubly linked list.

        Args:
            node: The node to remove.
        """
        prev, nxt = node.prev, node.next
        if prev is not None and nxt is not None:
            prev.next, nxt.prev = nxt, prev

    def insert(self, node: Node) -> None:
        """Inserts a node at the right (MRU) of the doubly linked list.

        Args:
            node: The node to insert.
        """
        prev = self.right.prev
        nxt = self.right
        if prev is not None:
            prev.next = node
            node.prev = prev
            node.next = nxt
            nxt.prev = node

    def get(self, key: int) -> int:
        """Gets the value of the key if the key exists, otherwise returns -1.

        Args:
            key: The key to search.

        Returns:
            The value of the key, or -1.
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """Puts a key-value pair into the cache, evicting the LRU item
        if capacity exceeded.

        Args:
            key: The key.
            value: The value.
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            if lru is not None:
                self.remove(lru)
                del self.cache[lru.key]
