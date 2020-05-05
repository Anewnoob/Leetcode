#64. 最小路径和
#给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#说明：每次只能向下或者向右移动一步。

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        #init
        m,n = len(grid),len(grid[0])

        for i in range(1,m):
            grid[i][0] += grid[i-1][0]

        for j in range(1,n):
            grid[0][j] += grid[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])

        return grid[-1][-1]
