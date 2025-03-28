from typing import List, Tuple


class Solution:
    """Base class for all LeetCode Problems."""

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and
        0's (water), return the number of islands.

        An island is surrounded by water and is formed by connecting adjacent lands
        horizontally or vertically. You may assume all four edges of the grid are all
        surrounded by water.
        """
        y, x = len(grid), len(grid[0])
        num_islands = 0
        visited = set()

        def neighbors(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
            next_pos = [
                (pos[0] - 1, pos[1]),
                (pos[0], pos[1] - 1),
                (pos[0] + 1, pos[1]),
                (pos[0], pos[1] + 1),
            ]
            neighbors = [
                p
                for p in next_pos
                if p[0] >= 0
                and p[1] >= 0
                and p[0] < x
                and p[1] < y
                and grid[p[1]][p[0]] == "1"
                and p not in visited
            ]
            return neighbors

        for x_ in range(x):
            for y_ in range(y):
                if grid[y_][x_] != "1" or (x_, y_) in visited:
                    continue
                # BFS
                queue = [(x_, y_)]
                visited.add((x_, y_))
                while queue:
                    pos = queue.pop(0)
                    next_pos = neighbors(pos)
                    for p in next_pos:
                        visited.add(p)
                        queue.append(p)
                num_islands += 1
        return num_islands
