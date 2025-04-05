from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Given two integers n and k, return all possible combinations of k numbers
        chosen from the range [1, n].

        You may return the answer in any order.
        """
        res = []

        def dfs(i: int, left: int, right: int, pair: List[int]):
            if i == k:
                res.append(pair)
                return

            for j in range(left, right + 1):
                new_i = i + 1
                new_left = j + 1
                new_right = right
                new_pair = pair + [j]
                dfs(new_i, new_left, new_right, new_pair)

        dfs(0, 1, n, [])
        return res
