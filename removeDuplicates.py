#给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_len = len(nums)
        pre_v = nums[0]
        j = 1
        for i in range(1,nums_len):
            if nums[j] == pre_v:
                del nums[j]
                j -= 1
            pre_v = nums[j] 
            j += 1
        return len(nums)
