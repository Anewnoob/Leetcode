class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix and not target: return False
        if not matrix or not target: return False

        m,n = len(matrix),len(matrix[0])

        for k in range(m):
            i,j = 0,n-1
            cur_list = matrix[k]
            while i <= j:
                mid = (i+j) // 2
                if cur_list[mid] == target:
                    return True
                elif cur_list[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
        return False            
