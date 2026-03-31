class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit, min_price = 0, prices[0]
        # for i in range(1, len(prices)):
        #     profit = max(profit, prices[i] - min_price)
        #     min_price = min(min_price, prices[i])
        # return profit
        if len(prices) <= 1:
            return 0
        buy, profit = 0, 0
        for sell in range(1, len(prices)):
            if prices[sell] - prices[buy] > 0:
                profit = max(profit, prices[sell] - prices[buy])
            if prices[buy] > prices[sell]:
                buy = sell
        return profit





        