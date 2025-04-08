from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Given two sorted arrays nums1 and nums2 of size m and n respectively, return
        the median of the two sorted arrays.

        The overall run time complexity should be O(log (m+n)).
        """
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums2) < len(nums1):
            big, small = nums1, nums2
        else:
            big, small = nums2, nums1

        left, right = 0, len(small) - 1
        while True:
            i = (left + right) // 2
            j = half - i - 2

            leftSmall = small[i] if i >= 0 else -float("inf")
            rightSmall = small[i + 1] if (i + 1) < len(small) else float("inf")
            leftBig = big[j] if j >= 0 else -float("inf")
            rightBig = big[j + 1] if (j + 1) < len(big) else float("inf")

            if leftSmall <= rightBig and leftBig <= rightSmall:
                if total % 2:
                    return min(rightSmall, rightBig)
                else:
                    return (max(leftSmall, leftBig) + min(rightSmall, rightBig)) / 2
            elif leftSmall > rightBig:
                right = i - 1
            else:
                left = i + 1
