import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right, result = 1, max(piles), 0

        while left <= right:
            mid = (left + right) // 2
            eating_hours = 0
            for pile in piles:
                eating_hours += math.ceil(pile / mid)
            print(mid, eating_hours)
            if eating_hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
        