from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        Given an array of integers arr, and three integers a, b and c. You need to
        find the number of good triplets.

        A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
        - 0 <= i < j < k < arr.length
        - |arr[i] - arr[j]| <= a
        - |arr[j] - arr[k]| <= b
        - |arr[i] - arr[k]| <= c

        Where |x| denotes the absolute value of x.

        Return the number of good triplets.
        """
        count = 0
        prefix = [0 for i in range(1001)]
        for j in range(len(arr)):
            for k in range(j + 1, len(arr)):
                if abs(arr[j] - arr[k]) <= b:
                    right = min(arr[j] + a, arr[k] + c)
                    right = min(right, 1000)
                    left = max(arr[j] - a, arr[k] - c)
                    left = max(left, 0)
                    if left <= right:
                        count += prefix[right] - (0 if left == 0 else prefix[left - 1])

            for idx in range(arr[j], 1001):
                prefix[idx] += 1

        return count
