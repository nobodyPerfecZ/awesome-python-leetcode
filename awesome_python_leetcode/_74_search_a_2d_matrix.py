from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        You are given an m x n integer matrix matrix with the following two properties:
        - Each row is sorted in non-decreasing order.
        - The first integer of each row is greater than the last integer of the previous
        row.

        Given an integer target, return true if target is in matrix or false otherwise.

        You must write a solution in O(log(m * n)) time complexity.
        """
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols) - 1
        while left <= right:
            mid = (right + left) // 2
            row = mid // cols
            col = mid % cols
            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                return True
        return False
