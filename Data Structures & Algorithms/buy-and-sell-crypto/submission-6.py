class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, result = 0, 0, 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                result = max(result, profit)
            else:
                buy = sell
            sell += 1
        return result






        