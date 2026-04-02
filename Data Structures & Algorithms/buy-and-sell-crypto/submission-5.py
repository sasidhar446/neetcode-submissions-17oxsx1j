class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, result = 0, 0, 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            result = max(result, profit)
            if prices[right] < prices[left]:
                left = right
            right += 1
        return result






        