#1277. 统计全为 1 的正方形子矩阵
#给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        H = len(matrix)
        W = len(matrix[0])
        cnt = 0
        dp = [[0]*W for _ in range(H)]
        #init
        for i in range(H):
            dp[i][0] = matrix[i][0]
            cnt += matrix[i][0]
        for j in range(W):
            dp[0][j] = matrix[0][j]
            cnt += matrix[0][j]
        
        if matrix[0][0] == 1:
            cnt -= 1

        for i in range(1,H):
            for j in range(1,W):
                if matrix[i][j] == 1:
                    dp[i][j] = min(min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1])+1
                    cnt += dp[i][j]
        return cnt
