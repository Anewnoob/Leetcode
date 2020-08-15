class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if not nums: return 
        nums_len = len(nums)
        t = set()
        for i in range(nums_len):
            if nums[i] not in t:
                t.add(nums[i])
            else:
                return nums[i]
        return 
