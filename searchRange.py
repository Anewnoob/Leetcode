#给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#你的算法时间复杂度必须是 O(log n) 级别。
#如果数组中不存在目标值，返回 [-1, -1]。


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        nums_len = len(nums)
        i,j = 0,nums_len-1
        center = -1
        while i <= j:
            mid = (i+j) // 2
            if nums[mid] == target:
                center = mid
                break
            elif nums[mid] > target:
                j = mid -1 
            else:
                i = mid + 1
        if center == -1:
            return [-1,-1]
        start, end = center,center
        while start - 1 >= 0 and nums[start-1] == target:
            start -= 1
        while end + 1 < nums_len and nums[end+1] == target:
            end  += 1
        return [start, end]

