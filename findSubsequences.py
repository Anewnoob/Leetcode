给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums_len = len(nums)

        res=set()
        def dfs(nums,temp):
            if len(temp)>=2 :
                res.add(tuple(temp[:]))
            if not nums:
                return
            for i in range(len(nums)):
                if not temp or nums[i]>=temp[-1]:
                    dfs(nums[i+1:],temp+[nums[i]])
        dfs(nums,[])
        return list(res)
      
        ##new##
        if not nums or len(nums) < 2:
            return []
        n = len(nums)
        ans = set()
        def dfs(nums, start, path):
            if len(path) >= 2:
                ans.add(tuple(path[:]))
            for i in range(start, n):
                if len(path) > 0 and nums[i] < path[-1]:
                    continue
                path.append(nums[i])
                dfs(nums, i + 1, path)
                path.pop()
        dfs(nums, 0, [])
        return list(ans)
