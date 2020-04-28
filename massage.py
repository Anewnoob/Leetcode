#面试题 17.16. 按摩师---
#一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。
#在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。


class Solution:
    def massage(self, nums: List[int]) -> int:

        if not nums:
            return 0
        dp = [[0,0] for _ in range(len(nums))]
        #init
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1,len(nums)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]

        return max(dp[-1][0],dp[-1][1])
    
#better
class Solution:
    def massage(self, nums: List[int]) -> int:

        if not nums:
            return 0
        #init
        dp0 = 0
        dp1 = nums[0]

        for i in range(1,len(nums)):
            tdp0 = max(dp0,dp1)
            tdp1 = dp0 + nums[i]
            dp0 = tdp0
            dp1 = tdp1

        return max(dp0,dp1)
