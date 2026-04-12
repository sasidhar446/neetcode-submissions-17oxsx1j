class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate = max(piles)
        left, right, result = 1, rate, 0
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            if total > h:
                left = mid + 1
            elif total <= h:
                result = mid
                right = mid - 1
        return result

