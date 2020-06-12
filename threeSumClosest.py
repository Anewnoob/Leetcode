#给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
#返回这三个数的和。假定每组输入只存在唯一答案。

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or target is None: return
        len_nums = len(nums)
        if len_nums < 3: return
        nums.sort()
        close_sum = nums[0]+nums[1]+nums[2]
        if close_sum > target: return close_sum
        for i in range(len_nums-2):
            if i > 0 and nums[i-1] == nums[i]: continue
            j,k = i+1,len_nums-1  
            while j < k:
                if j-1 > i and nums[j-1] == nums[j]: 
                    j += 1 
                    continue
                if k+1 < len_nums and nums[k] == nums[k+1] : 
                    k -= 1 
                    continue
                three_sum = nums[i]+nums[j]+nums[k]
                if three_sum == target: return three_sum
                if abs(three_sum - target) < abs(close_sum-target):
                    close_sum = three_sum
                if three_sum -target < 0:
                    j += 1
                else:
                    k -= 1
        return close_sum
