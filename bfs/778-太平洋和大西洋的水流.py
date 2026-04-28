"""
778 · 太平洋和大西洋的水流
描述
给定一个m×n的非负矩阵代表一个大洲，矩阵的每个单元格的值代表此处的地形高度，
矩阵的左边缘和上边缘是“太平洋”，下边缘和右边缘是“大西洋”。

水流只能在四个方向（上，下，左或右）从一个单元格流向另一个海拔和自己相等或比自己低的单元格。
找到那些从此处出发的水既可以流到“太平洋”，又可以流向“大西洋”的单元格的坐标。

例1:
输入:
matrix =
[[1,2,2,3,5],
[3,2,3,4,4],
[2,4,5,3,1],
[6,7,1,4,5],
[5,1,1,2,4]]
输出:
[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
解释:
Pacific ~ ~ ~ ~ ~
      ~ 1 2 2 3 5 *
      ~ 3 2 3 4 4 *
      ~ 2 4 5 3 1 *
      ~ 6 7 1 4 5 *
      ~ 5 1 1 2 4 *
        * * * * * Atlantic

例2:
输入:
matrix =
[[1,2],
[4,3]]
输出:
[[0,1],[1,0],[1,1]]
"""

from typing import (
    List,
)
from collections import deque

class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
             we will sort your return value in output
    """
    def pacific_atlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # write your code here
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        pacific = [[False] * cols for row in range(rows)]
        atlantic = [[False] * cols for row in range(rows)]

        pacific_queue = deque()
        atlantic_queue = deque()

        for col in range(cols):
            pacific[0][col] = True
            atlantic[rows - 1][col] = True
            pacific_queue.append((0, col))
            atlantic_queue.append((rows - 1, col))

        for row in range(rows):
            pacific[row][0] = True
            atlantic[row][cols - 1] = True
            pacific_queue.append((row, 0))
            atlantic_queue.append((row, cols - 1))


        self.bfs(matrix, pacific_queue, pacific)
        self.bfs(matrix, atlantic_queue, atlantic)

        res = []

        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] == True and atlantic[r][c] == True:
                    res.append([r, c])

        return res

    def bfs(self, matrix, queue, visited):
        rows = len(matrix)
        cols = len(matrix[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if (
                            0 <= new_r < rows and
                            0 <= new_c < cols and
                            not visited[new_r][new_c] and
                            matrix[new_r][new_c] >= matrix[r][c]
                    ):
                        queue.append((new_r, new_c))
                        visited[new_r][new_c] = True