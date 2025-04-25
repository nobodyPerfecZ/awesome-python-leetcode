import bisect
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def maxEnvelopesBS(self, envelopes: List[List[int]]) -> int:
        """
        You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
        represents the width and the height of an envelope.

        One envelope can fit into another if and only if both the width and height of
        one envelope are greater than the other envelope's width and height.

        Return the maximum number of envelopes you can Russian doll (i.e., put one
        inside the other).

        Note: You cannot rotate an envelope.
        """
        # BS Solution: O(n log n)
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        seq = [envelopes[0]]
        for k in range(1, len(envelopes)):
            if envelopes[k][1] > seq[-1][1]:
                seq.append(envelopes[k])
            else:
                i = bisect.bisect_left(seq, envelopes[k][1], key=lambda x: x[1])
                seq[i] = envelopes[k]
        return len(seq)

    def maxEnvelopesDP(self, envelopes: List[List[int]]) -> int:
        """
        You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
        represents the width and the height of an envelope.

        One envelope can fit into another if and only if both the width and height of
        one envelope are greater than the other envelope's width and height.

        Return the maximum number of envelopes you can Russian doll (i.e., put one
        inside the other).

        Note: You cannot rotate an envelope.
        """
        # DP (LIS) Solution: O(n^2)
        # Invalid: TLE
        envelopes = sorted(envelopes)
        dp = [1 for _ in range(len(envelopes))]
        for i in range(len(envelopes) - 2, -1, -1):
            for j in range(i + 1, len(envelopes)):
                if (
                    envelopes[i][0] < envelopes[j][0]
                    and envelopes[i][1] < envelopes[j][1]
                ):
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
