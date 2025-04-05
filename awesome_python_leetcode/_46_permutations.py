from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of distinct integers, return all the possible permutations.
        You can return the answer in any order.
        """
        res = []

        def dfs(pair: List[int], rest: List[int]):
            if not rest:
                res.append(pair)
                return

            for i, n in enumerate(rest):
                new_pair = pair + [n]
                new_rest = rest[:i] + rest[i + 1 :]
                dfs(new_pair, new_rest)

        dfs([], nums)
        return res
