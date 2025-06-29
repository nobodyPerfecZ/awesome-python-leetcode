import collections
from typing import Dict, List, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __hash__(self) -> int:
        return self.val

    def __eq__(self, other: Optional["Node"]) -> bool:
        if self is None and other is None:
            return True
        elif self is None:
            return False
        elif other is None:
            return False
        adj1 = self.adj_list()
        adj2 = other.adj_list()
        return adj1 == adj2

    def adj_list(self) -> Dict[int, List[int]]:
        """Return the adjacency list of the graph."""
        adj = collections.defaultdict(list)
        queue = [self]
        visited = {self.val}
        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    adj[node.val].append(neighbor.val)
                    queue.append(neighbor)
                    visited.add(neighbor.val)
        return adj

    @staticmethod
    def build(edges: List[List[int]]) -> Optional["Node"]:
        """Build a graph from an adjacency list."""
        if not edges:
            return None

        nodes = {}
        for i in range(len(edges)):
            if i not in nodes:
                nodes[i + 1] = Node(i + 1)
            for j in edges[i]:
                if j not in nodes:
                    nodes[j] = Node(j)
                nodes[i + 1].neighbors.append(nodes[j])
        return nodes[1]


class Solution:
    """Base class for all LeetCode Problems."""

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        Given a reference of a node in a connected undirected graph.

        Return a deep copy (clone) of the graph.

        Each node in the graph contains a value (int) and a list (List[Node]) of its
        neighbors.

        class Node {
            public int val;
            public List<Node> neighbors;
        }


        Test case format:

        For simplicity, each node's value is the same as the node's index (1-indexed).
        For example, the first node with val == 1, the second node with val == 2, and so
        on. The graph is represented in the test case using an adjacency list.

        An adjacency list is a collection of unordered lists used to represent a finite
        graph. Each list describes the set of neighbors of a node in the graph.

        The given node will always be the first node with val = 1. You must return the
        copy of the given node as a reference to the cloned graph.
        """

        if node is None:
            return None

        # Create all new nodes (without neighbors)
        old_to_copy = {None: None}
        queue = [node]
        visited = {node}
        while queue:
            cur = queue.pop(0)
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            for nxt in cur.neighbors:
                if nxt not in visited:
                    queue.append(nxt)
                    visited.add(nxt)

        # Add all neighbors to new nodes
        queue = [node]
        visited = {node}
        while queue:
            cur = queue.pop(0)
            copy = old_to_copy[cur]
            copy.neighbors = [old_to_copy[nxt] for nxt in cur.neighbors]
            for nxt in cur.neighbors:
                if nxt not in visited:
                    queue.append(nxt)
                    visited.add(nxt)

        return old_to_copy[node]
