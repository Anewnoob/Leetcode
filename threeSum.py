#给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
#注意：答案中不可以包含重复的三元组。
class Solution:
    def threeSum(self, nums):
        length = len(nums)
        #if length < 3: return []
        # if length == 3:
        #     if nums[0] + nums[1] == -nums[2]:
        #         nums.sort()
        #         return [nums] 

        # #暴力法
        # #>3
        # new_list = list()
        # for idx_i,i in enumerate(nums[:-1]):
        #     idx_j = idx_i + 1
        #     for j in (nums[idx_j:]):
        #         res = -(i + j)
        #         print(idx_i,idx_j)
        #         for idx_res,val in enumerate(nums):
        #             if res == val and idx_i != idx_res and idx_j != idx_res:
        #                 tmp = [i,j,res]
        #                 #print(idx_i,idx_j,idx_res,tmp)
        #                 tmp.sort()
        #                 # print(tmp)
        #                 if tmp not in new_list:
        #                     new_list.append(tmp) 
        #         idx_j += 1
        # return new_list


        #先排序 + 双指针
        res,k = [],0
        nums.sort()
        for k in range(length - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k-1]:continue
            i,j = k+1,length-1
            while i < j:
                three_sum = nums[k] + nums[j] + nums[i]
                if three_sum < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]: i+=1
                elif three_sum > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j-=1
                else:
                    res.append([nums[k],nums[i],nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]: i+=1
                    while i < j and nums[j] == nums[j+1]: j-=1
        return res



