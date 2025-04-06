from typing import List

from awesome_python_leetcode.tree import QuadTreeNode


class Solution:
    """Base class for all LeetCode Problems."""

    def construct(self, grid: List[List[int]]) -> "QuadTreeNode":
        """
        Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a
        Quad-Tree.

        Return the root of the Quad-Tree representing grid.

        A Quad-Tree is a tree data structure in which each internal node has exactly
        four children. Besides, each node has two attributes:
        - val: True if the node represents a grid of 1's or False if the node represents
        a grid of 0's. Notice that you can assign the val to True or False when isLeaf
        is False, and both are accepted in the answer.
        - isLeaf: True if the node is a leaf node on the tree or False if the node has
        four children.
        class Node {
            public boolean val;
            public boolean isLeaf;
            public Node topLeft;
            public Node topRight;
            public Node bottomLeft;
            public Node bottomRight;
        }

        We can construct a Quad-Tree from a two-dimensional area using the following
        steps:
        1. If the current grid has the same value (i.e all 1's or all 0's) set isLeaf
        True and set val to the value of the grid and set the four children to Null
        and stop.
        2. If the current grid has different values, set isLeaf to False and set val to
        any value and divide the current grid into four sub-grids as shown in the photo.
        3. Recurse for each of the children with the proper sub-grid.
        """

        def dfs(n: int, row: int, col: int):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[row][col] != grid[row + i][col + j]:
                        allSame = False
                        break
            if allSame:
                return QuadTreeNode(grid[row][col], 1)

            n = n // 2
            topLeft = dfs(n, row, col)
            topRight = dfs(n, row, col + n)
            bottomLeft = dfs(n, row + n, col)
            bottomRight = dfs(n, row + n, col + n)
            return QuadTreeNode(0, 0, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)
