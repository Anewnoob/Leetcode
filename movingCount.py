#MY CODE ---> Wrong
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k == 0:
            return 1
        cnt = 0
        for i in range(m):
            for j in range(n):
                print("xy:",i,j)
                i_list = []
                value = i
                while value:
                    i_list.append(value%10)
                    value = value//10
                j_list = []
                value = j
                while value:
                    j_list.append(value%10)
                    value = value//10
                sum_all = 0
                while i_list:
                    sum_all+=i_list.pop()
                while j_list:
                    sum_all+=j_list.pop()
                
                if sum_all <= k:
                    cnt+=1
                    print("sum:",sum_all,k,cnt)
                    
        return cnt

test = Solution()
test.movingCount(16,8,4)

#correct answer
#DFS
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if not 0 <= i < m or not 0 <= j < n or k < si + sj or (i, j) in visited: return 0
            visited.add((i,j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)

#BFS
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        queue, visited,  = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if i >= m or j >= n or k < si + sj or (i, j) in visited: continue
            visited.add((i,j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)
