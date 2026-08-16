from functools import lru_cache
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def stoneGameII(self, piles: List[int]) -> int:
        """
        Alice and Bob continue their games with piles of stones. There are a number of
        piles arranged in a row, and each pile has a positive integer number of stones
        piles[i]. The objective of the game is to end with the most stones.

        Alice and Bob take turns, with Alice starting first.

        On each player's turn, that player can take all the stones in the first X
        remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially,
        M = 1.

        The game continues until all the stones have been taken.

        Assuming Alice and Bob play optimally, return the maximum number of stones
        Alice can get.
        """
        N = len(piles)

        @lru_cache(None)
        def dp(left, M, alice):
            if left == N:
                return 0
            res = 0 if alice else float("inf")
            total = 0
            for X in range(1, 2 * M + 1):
                if left + X > len(piles):
                    break
                total += piles[left + X - 1]
                if alice:  # first player
                    res = max(res, total + dp(left + X, max(M, X), not alice))
                else:  # second player
                    res = min(res, dp(left + X, max(M, X), not alice))
            return res

        return dp(0, 1, True)
