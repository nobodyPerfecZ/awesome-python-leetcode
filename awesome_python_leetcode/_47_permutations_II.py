from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Given a collection of numbers, nums, that might contain duplicates, return all
        possible unique permutations in any order.
        """
        res = []
        cache = set()

        def dfs(pair: List[int], rest: List[int]):
            if tuple(pair) in cache:
                return
            if not rest:
                res.append(pair)
                cache.add(tuple(pair))
                return
            for i, n in enumerate(rest):
                new_pair = pair + [n]
                new_rest = rest[:i] + rest[i + 1 :]
                dfs(new_pair, new_rest)

        dfs([], nums)
        return res
