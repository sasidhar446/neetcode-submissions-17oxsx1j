import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        rates = range(1, max_rate + 1)
        left, right = 0, len(rates) - 1
        result = float("inf")
        
        while left <= right:
            current_rate = 0
            mid = (left + right) // 2
            for pile in piles:
                current_rate += math.ceil(pile / rates[mid])
            
            if current_rate > h:
                left = mid + 1
            elif current_rate <= h:
                result = min(result, rates[mid])
                right = mid - 1
        
        return result
        