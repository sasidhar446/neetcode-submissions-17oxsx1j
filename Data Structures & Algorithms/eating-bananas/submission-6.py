import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            rate = 0
            for pile in piles:
                rate += math.ceil(pile / mid)
            
            if rate > h:
                left = mid + 1
            elif rate <= h:
                result = mid
                right = mid - 1

        return result 

        