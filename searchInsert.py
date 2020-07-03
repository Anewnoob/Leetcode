#给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

#你可以假设数组中无重复元素。

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # #simple
        # if not nums:
        #     return 0
        # len_nums = len(nums)
        # for i in range(len_nums):
        #     if nums[i] < target:
        #         continue
        #     else:
        #         return i
        # return len_nums

        #二分法
        if not nums:
            return 0

        len_nums = len(nums)
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len_nums
        i,j = 0,len_nums-1
        while i < j :
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid
            else:
                j = mid
            if j-i <= 1:
                return j
        return j
            

