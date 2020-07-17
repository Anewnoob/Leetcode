给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return []
        matrix_len = len(matrix)
        for i in range(1,matrix_len):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(matrix_len):
            matrix[i].reverse()
        return matrix
