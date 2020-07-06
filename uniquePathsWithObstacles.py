#一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

#机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

#现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1

        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]

        for j in range(1,n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
       
        #better
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1

        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]

        for j in range(1,n):
            if obstacleGrid[0][j] == 1:
                obstacleGrid[0][j] = 0
            else:
                obstacleGrid[0][j] = obstacleGrid[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
