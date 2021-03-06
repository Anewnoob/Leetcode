
#给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums: return 
        hashmap = { i:0 for i in range(len(nums))}
        for val in nums:
            if val in hashmap:
                hashmap[val] += 1
                if hashmap[val] >= 2:
                    return val
        return
