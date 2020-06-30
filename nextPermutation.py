##实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

#如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

#必须原地修改，只允许使用额外常数空间。

#以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
#1,2,3 → 1,3,2
#3,2,1 → 1,2,3
#1,1,5 → 1,5,1

class Solution(object):


    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums: return 
        len_nums = len(nums)
        min_idx = len_nums-1
        for i in range(len_nums-2,-1,-1):
            j = i+1
            if nums[i] >= nums[j]:
                if i == 0:
                    nums.reverse()
                    return nums
                continue
            else:
                nums[i+1:] = sorted(nums[i+1:],reverse = True)
                idx = i + 1
                while idx < len_nums-1 and nums[idx] > nums[i]:
                    idx += 1
                if nums[idx] <= nums[i]: idx -= 1
                tmp = nums[i]
                nums[i] = nums[idx]
                nums[idx] = tmp
                nums[i+1:] = sorted(nums[i+1:])
                return nums
            
