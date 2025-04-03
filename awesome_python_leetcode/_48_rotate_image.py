from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        You are given an n x n 2D matrix representing an image, rotate the image by 90
        degrees (clockwise).

        You have to rotate the image in-place, which means you have to modify the input
        2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
        """
        i, n = 0, len(matrix) - 1
        while i < n - i:
            j = i
            while j < n - i:
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j][i]
                matrix[n - j][i] = matrix[n - i][n - j]
                matrix[n - i][n - j] = matrix[j][n - i]
                matrix[j][n - i] = tmp
                j += 1
            i += 1
