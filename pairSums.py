设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。
输入: nums = [5,6,5], target = 11
输出: [[5,6]]

class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums: return []
        nums_len = len(nums)
        nums.sort()
        i,j = 0,nums_len-1
        res = []
        while i < j :
            two_sum = nums[i] + nums[j]
            if two_sum == target:
                res.append([nums[i],nums[j]])
                i += 1
                j -= 1
            elif two_sum > target:
                j -= 1
            else:
                i += 1
        return res
