#给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

#不占用额外内存空间能否做到？

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix)
        for i in range(m):
            for j in range(0,i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(m):
            matrix[i].reverse()
        return matrix
