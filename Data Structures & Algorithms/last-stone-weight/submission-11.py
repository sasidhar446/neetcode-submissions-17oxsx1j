import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heavy_stones = [-1 * stone for stone in stones]
        heapq.heapify(heavy_stones)
        while len(heavy_stones) > 1:
            x = heapq.heappop(heavy_stones)
            y = heapq.heappop(heavy_stones)
            heapq.heappush(heavy_stones, x - y)
        
        return 0 if not heavy_stones else -1 * heavy_stones[0]

            





        
            



        