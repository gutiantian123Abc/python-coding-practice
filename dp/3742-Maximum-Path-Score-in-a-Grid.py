"""
3742. Maximum Path Score in a Grid

You are given an m x n grid where each cell contains one of the values 0, 1, or 2.
You are also given an integer k.

You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

0: adds 0 to your score and costs 0.
1: adds 1 to your score and costs 1.
2: adds 2 to your score and costs 1.

Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.

Note: If you reach the last cell but the total cost exceeds k, the path is invalid.
"""

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        NEG_INF = float("-inf")
        # dp[i][j][c] =
        # maximum score when reaching cell (i, j)
        # using exactly c cost
        dp = [[[NEG_INF] * (k + 1) for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k + 1):
                    if dp[i][j][c] == NEG_INF:
                        continue
                    else:
                        # move down
                        if i + 1 < m:
                            val = grid[i + 1][j]
                            cost = 0 if val == 0 else 1

                            if c + cost <= k:
                                dp[i + 1][j][c + cost] = max(
                                    dp[i + 1][j][c + cost],
                                    dp[i][j][c] + val
                                )

                        # move right
                        if j + 1 < n:
                            val = grid[i][j + 1]
                            cost = 0 if val == 0 else 1

                            if c + cost <= k:
                                dp[i][j + 1][c + cost] = max(
                                    dp[i][j][c] + val,
                                    dp[i][j + 1][c + cost]
                                )
        # max score with all costs
        ans = max(dp[m - 1][n - 1])

        return -1 if ans < 0 else ans