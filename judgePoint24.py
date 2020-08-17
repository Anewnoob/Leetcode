class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums: return False
        def dfs(nums):
            if len(nums) == 1 and abs(nums[0]-24) < 1e-6 : return True
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        new_nums = [nums[k] for k in range(len(nums)) if i != k != j]
                        if dfs(new_nums + [nums[i]+nums[j]]): return True
                        if dfs(new_nums + [nums[i]-nums[j]]): return True
                        if dfs(new_nums + [nums[i]*nums[j]]): return True
                        if nums[j] != 0 and dfs(new_nums + [nums[i]/nums[j]]): return True
            return False
        return dfs(nums)
