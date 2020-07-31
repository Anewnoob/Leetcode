给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        row = len(matrix)
        col = len(matrix[0])
        height = [0] * (col + 2)
        res = 0
        for i in range(row):
            stack = []
            for j in range(col + 2):
                if 1<=j<=col: 
                    if matrix[i][j-1] == "1":
                        height[j] += 1
                    else:
                        height[j] = 0
                while stack and height[stack[-1]] > height[j]:
                    cur = stack.pop()
                    res = max(res, (j - stack[-1] - 1)* height[cur])
                stack.append(j)
        return res
