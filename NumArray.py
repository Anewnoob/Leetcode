class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        new_nums = self.nums[i:j+1]
        sumall = 0
        for value in new_nums:
            sumall += value
        return sumall



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
