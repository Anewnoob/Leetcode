#给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

#相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if not triangle: return 
        tri_len = len(triangle)

        # #从底向上
        # for i in range(tri_len-1,0,-1):
        #     for j in range(i):
        #         triangle[i-1][j] += min(triangle[i][j],triangle[i][j+1])
        # return triangle[0][0]

        #从上向下 DP
        dp = [[float('inf')]*tri_len for _ in range(tri_len)]
        # for i in range(tri_len):
        #     for j in range(i+1):
        #         dp[i][j] = 0
        dp[0][0] = triangle[0][0]
        for i in range(1,tri_len):
            for j in range(i+1):
                dp[i][j] = min(dp[i-1][j-1] + triangle[i][j],dp[i-1][j]+triangle[i][j])
        return min(dp[-1])

