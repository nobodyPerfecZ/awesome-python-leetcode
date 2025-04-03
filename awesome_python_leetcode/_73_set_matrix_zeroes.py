from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Given an m x n integer matrix matrix, if an element is 0, set its entire row
        and column to 0's.

        You must do it in place.
        """
        rowZero = False
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        rowZero = True

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for row in range(len(matrix)):
                matrix[row][0] = 0

        if rowZero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
