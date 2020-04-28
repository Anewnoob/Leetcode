'''
求解字串最大和---DP算法
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None
        #initial
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1,len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1]+nums[i]
            else:
                dp[i] = nums[i]
            max_sum = max(max_sum,dp[i])
        return max_sum
