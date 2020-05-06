#714. 买卖股票的最佳时机含手续费
#给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
#你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
#返回获得利润的最大值。
#注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0] - fee

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][0]-prices[i]-fee,dp[i-1][1])
        return dp[-1][0]
        
 #better 
     def maxProfit(self, prices: List[int], fee: int) -> int:
        pre_0,pre_1 = 0,-prices[0] - fee
        cur_0,cur_1 = pre_0,pre_1
        for i in range(1,len(prices)):
            cur_0 = max(pre_0,pre_1+prices[i])
            cur_1 = max(pre_0-prices[i]-fee,pre_1)
            pre_0,pre_1 = cur_0,cur_1
        return cur_0
