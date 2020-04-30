#746. 使用最小花费爬楼梯
#数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
#每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
#您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        stairs_len = len(cost)
        if stairs_len <=2:
            return cost[0] if cost[0] < cost[1] else cost[1]
        for i in range(2,stairs_len):
            cost[i] = min(cost[i-1],cost[i-2]) + cost[i]
        min_cost = cost[-1] if cost[-1] < cost[-2] else cost[-2]
        return  min_cost
