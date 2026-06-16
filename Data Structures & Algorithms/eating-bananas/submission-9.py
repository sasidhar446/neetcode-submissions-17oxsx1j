import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right, result = 1, max(piles), 0

        while left <= right:
            mid = (left + right) // 2
            time_ = 0
            for pile in piles:
                time_ += math.ceil(pile/mid)
            if time_ <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result