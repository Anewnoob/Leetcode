#面试题 08.01. 三步问题
#三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，
#计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。


class Solution:
    def waysToStep(self, n: int) -> int:
        if n < 3:
            return max(n,0)

        dp = [0 for _ in range(n)]
        dp[0],dp[1],dp[2] = 1,2,4
        for i in range(3,n):
            dp[i] = (dp[i-3]+dp[i-2]+dp[i-1])%1000000007
        return dp[-1]
