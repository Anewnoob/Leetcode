#70. 爬楼梯
#假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#注意：给定 n 是一个正整数。

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0 for _ in range(n+1)]
        dp[0],dp[1],dp[2] = 0,1,2 

        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]
        
 #better
 class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp1,dp2 = 1,2
        for _ in range(3,n+1):
            dp3 = dp1+dp2
            dp1= dp2
            dp2 = dp3
        return dp3
