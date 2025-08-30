from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        A matrix diagonal is a diagonal line of cells starting from some cell in either
        the topmost row or leftmost column and going in the bottom-right direction until
        reaching the matrix's end. For example, the matrix diagonal starting from
        mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1],
        and mat[4][2].

        Given an m x n matrix mat of integers, sort each matrix diagonal in ascending
        order and return the resulting matrix.
        """
        # Collect diagonals
        diag = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                key = i - j
                if key not in diag:
                    diag[key] = []
                diag[key].append(mat[i][j])

        # Sort in decreasing / increasing order for each diagonal
        diag = dict(
            zip(
                diag.keys(),
                map(lambda key: sorted(diag[key]), diag.keys()),
                strict=False,
            )
        )

        # Apply the results to the result matrix
        result = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                key = i - j
                result[i][j] = diag[key].pop(0)

        return result
