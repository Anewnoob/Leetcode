class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        if not costs: return
        num_people = len(costs)
        costs.sort(key = lambda x: x[0]-x[1])
        res = 0
        res += sum([costs[i][0] for i in range(num_people//2)])
        res += sum([costs[i][1] for i in range(num_people//2,num_people)])
        return res
