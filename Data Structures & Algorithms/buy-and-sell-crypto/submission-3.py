class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy, result = 0, 0
        for sell in range(1, len(prices)):
            profit = prices[sell] - prices[buy]
            if profit > 0:
                result = max(profit, result)
            if prices[buy] > prices[sell]:
                buy = sell
        return result





        