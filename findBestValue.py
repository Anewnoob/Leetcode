#给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。
#如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
#请注意，答案不一定是 arr 中的数字。
#输入：arr = [4,9,3], target = 10
#输出：3
#解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if not arr or not target: return
        arr_len = len(arr)
        average = target//arr_len  #3

        arr.sort()
        k,sum_left = 0, 0
        while arr[k] < average: 
            sum_left += arr[k]          #2
            k+=1
        #k >= average
        sum_all_pre= sum_left+(arr_len-k)*average  #8,8  k 1
        if sum_all_pre == target: return average
        for i in range(k,arr_len):
            while average < arr[i]:
                sum_all_cur = sum_left + (arr_len-i)*average      #2 + 6 
                res_cur = target - sum_all_cur              #2
                res_pre = target - sum_all_pre              #2
                if res_cur == 0: 
                    return average
                elif res_cur*res_pre < 0:
                    if abs(res_cur) < abs(res_pre):
                        return average
                    else:
                        return average - 1
                else:
                    average += 1                #4
                    sum_all_pre = sum_all_cur   #8
            sum_left += arr[i]
        return average




