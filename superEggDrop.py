class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = {}
        def dfs(k,n):
            if (k,n) not in dp:
                if n == 0: ans =  0
                elif k == 1: ans = n
                else:
                    i,j = 1,n
                    while i + 1 < j:
                        x = (i+j) // 2
                        res1 = dfs(k-1,x-1)
                        res2 = dfs(k,n-x)
                        if res1 < res2:
                            i = x + 1
                        elif res1 > res2:
                            j = x - 1
                        else:
                            i = j = x
                    ans = 1 + min(max(dfs(k-1,x-1),dfs(k,n-x)) for x in (i,j))
                dp[k,n] = ans
            return dp[k,n]
        return dfs(K,N)
