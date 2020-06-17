#给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
#一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
#返回一对观光景点能取得的最高分

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        if not A : return 
        #暴力法  超出时间限制
        # max_score = 0
        # len_list = len(A)
        # for i in range(len_list-1):
        #     for j in range(i+1,len_list):
        #         cur_score = A[i]+A[j] + i-j
        #         max_score = cur_score if cur_score>max_score else max_score
        # return max_score
        #

        #better
        len_list = len(A)
        if len_list < 2:
            return 
        max_score = A[0]+ 0 + A[1] - 1
        max_i = A[0] + 0
        for j in range(2,len_list):
            max_i = A[j-1] + j-1  if A[j-1] + j - 1 > max_i else max_i
            max_score = max_i + A[j] - j if max_i + A[j] - j >max_score else max_score
        return max_score

