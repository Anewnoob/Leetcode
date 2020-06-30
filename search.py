#假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#你可以假设数组中不存在重复的元素。
#你的算法时间复杂度必须是 O(log n) 级别。

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        len_nums = len(nums)
        i,j = 0, len_nums-1
        while i <= j :
            mid = (i + j) // 2
            if nums[mid] == target: 
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[len_nums-1]:
                    i = mid + 1
                else:
                    j = mid - 1
        return  -1
