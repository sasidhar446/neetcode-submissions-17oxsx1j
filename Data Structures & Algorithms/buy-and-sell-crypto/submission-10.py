class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        left, right, profit = 0, 1, 0
        while right < len(prices):
            profit = max(profit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
            right += 1
        return profit