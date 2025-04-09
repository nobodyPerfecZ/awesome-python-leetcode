from typing import List
from heapq import heappop, heappush


class Solution:
    """Base class for all LeetCode Problems."""

    def kSmallestPairs(
        self,
        nums1: List[int],
        nums2: List[int],
        k: int,
    ) -> List[List[int]]:
        """
        You are given two integer arrays nums1 and nums2 sorted in non-decreasing order
        and an integer k.

        Define a pair (u, v) which consists of one element from the first array and one
        element from the second array.

        Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
        """
        res = []
        visited = {(0, 0)}
        heap = []
        heappush(heap, (nums1[0] + nums2[0], 0, 0))

        while k and heap:
            _, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            k -= 1
        return res
