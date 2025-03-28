import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        """
        You are given an array of variable pairs equations and an array of real numbers
        values, where equations[i] = [Ai, Bi] and values[i] represent the equation
        Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single
        variable.

        You are also given some queries, where queries[j] = [Cj, Dj] represents the
        jth query where you must find the answer for Cj / Dj = ?.

        Return the answers to all queries. If a single answer cannot be determined,
        return -1.0.

        Note: The input is always valid. You may assume that evaluating the queries
        will not result in division by zero and that there is no contradiction.

        Note: The variables that do not occur in the list of equations are undefined,
        so the answer cannot be determined for them.
        """
        adj = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            queue = [(src, 1)]
            visited = {src}
            while queue:
                cur, res = queue.pop(0)
                if cur == target:
                    return res
                for nxt, weight in adj[cur]:
                    if nxt not in visited:
                        queue.append((nxt, res * weight))
                        visited.add(nxt)
            return -1

        return [bfs(q[0], q[1]) for q in queries]
