#给定一个 没有重复 数字的序列，返回其所有可能的全排列。

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(nums, path, used):
            if len(path) == len(nums):
                res.append(path[:]]
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, path, used)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0: return []

        used = [False for _ in range(size)]
        dfs(nums, [], used)
        return res
