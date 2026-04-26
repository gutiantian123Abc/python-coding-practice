"""
860 · 不同岛屿的个数

描述：
    给定一个由 0 和 1 组成的非空二维网格，一个岛屿是指四个方向（横向和纵向）
    都相连的一组 1（1 表示陆地）。你可以假设网格的四个边缘都被水包围。
    找出所有不同的岛屿的个数。如果一个岛屿与另一个岛屿形状相同（不考虑旋转和翻折），
    我们认为这两个岛屿是相同的。

注意：
    11      1
    1   和  11
    是不同的岛屿，因为我们不考虑旋转和翻折。

样例 1：
    输入：
        [[1,1,0,0,1],
         [1,0,0,0,0],
         [1,1,0,0,1],
         [0,1,0,1,1]]
    输出：3
    解释：共有 3 种不同形状的岛屿：
        11    1    1
        1         11
        11
         1

样例 2：
    输入：
        [[1,1,0,0,0],
         [1,1,0,0,0],
         [0,0,0,1,1],
         [0,0,0,1,1]]
    输出：1
    解释：左上和右下的两个 2×2 方块形状相同，只算 1 种
"""

from typing import (
    List,
)
from collections import deque

class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberof_distinct_islands(self, grid: List[List[int]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]
        shapes = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    shape = self.bfs(grid, visited, r, c, directions)
                    shapes.add(shape)

        return len(shapes)

    def bfs(self, grid, visited, start_r, start_c, directions):
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        queue.append((start_r, start_c))
        visited[start_r][start_c] = True

        shape = []

        while queue:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()
                shape.append((r - start_r, c - start_c))

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if (
                            0 <= new_r < rows and
                            0 <= new_c < cols and
                            grid[new_r][new_c] == 1 and
                            not visited[new_r][new_c]
                    ):
                        queue.append((new_r, new_c))
                        visited[new_r][new_c] = True

        return tuple(shape)