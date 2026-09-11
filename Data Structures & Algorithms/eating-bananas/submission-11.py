import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = float("inf")
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2
            rate = 0
            for pile in piles:
                rate += math.ceil(pile/mid)
            if rate <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result


