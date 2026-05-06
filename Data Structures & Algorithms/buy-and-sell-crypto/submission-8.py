class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, result = 0, 0, 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                result = max(result, prices[sell] - prices[buy])
            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1
        return result
        