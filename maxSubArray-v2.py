#53. 最大子序和
#给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1,len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
            max_sum = max(max_sum,dp[i])
        return max_sum
        
#better version
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp0 = nums[0]
        max_sum = dp0
        for i in range(1,len(nums)):
            if dp0 > 0:
                dp1 = dp0 + nums[i]
            else:
                dp1 = nums[i]
            dp0 = dp1
            max_sum = max(max_sum,dp1)
        return max_sum
    
#best
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum, sum_add = nums[0],nums[0]
        for value in nums[1:]:
            sum_add = sum_add + value if sum_add > 0 else value
            max_sum = max_sum if max_sum > sum_add else sum_add
        return max_sum
