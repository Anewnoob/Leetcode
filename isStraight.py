从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        if not nums: return False
        nums_len = len(nums)
        zero = 0
        stack = [-1]
        nums.sort()
        for i in range(nums_len):
            if nums[i] == 0:
                zero += 1
                continue
            if nums[i] <= stack[-1]: return False

            if stack[-1] != -1:
                last_num = stack[-1]
                while nums[i] - last_num != 1:
                    if zero == 0: return False
                    last_num += 1
                    zero -= 1
            stack.append(nums[i])
        return True
