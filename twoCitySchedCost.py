#公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。

#返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        if not costs: return
        num_people = len(costs)
        costs.sort(key = lambda x: x[0]-x[1])   #按差值排序
        res = 0
        res += sum([costs[i][0] for i in range(num_people//2)])                 #前一半去A 
        res += sum([costs[i][1] for i in range(num_people//2,num_people)])      #后一半去B
        return res
