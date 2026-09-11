import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = float("inf")
        left, right = 1, max(piles)

        while left <= right:
            rate = (left + right) // 2
            time_ = 0
            for pile in piles:
                time_ += math.ceil(pile/rate)
            if time_ <= h:
                result = rate
                right = rate - 1
            else:
                left = rate + 1
        
        return result


