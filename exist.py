class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        if not word: return True

        m,n = len(board),len(board[0])
        visited = [[1]*(n) for _ in range(m)]

        def dfs(i,j,k,visited):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k] or visited[i][j] == 0: return False
            if k == len(word) - 1: return True
            visited[i][j] = 0
            res = dfs(i+1,j,k+1,visited) or dfs(i,j+1,k+1,visited) or dfs(i-1,j,k+1,visited) or dfs(i,j-1,k+1,visited)
            visited[i][j] = 1
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0,visited): return True
        return False

        # def dfs(i, j, k):
        #     if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
        #     if k == len(word) - 1: return True
        #     tmp, board[i][j] = board[i][j], '/'
        #     res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        #     board[i][j] = tmp
        #     return res

        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if dfs(i, j, 0): return True
        # return False
