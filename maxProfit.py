#121. 买卖股票的最佳时机

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #init
        if not prices:
            return 0
        minprice = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] < minprice: minprice = prices[i]
            else: max_profit = max(prices[i] - minprice,max_profit)
        return max_profit 
