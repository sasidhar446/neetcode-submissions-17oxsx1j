import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)
        
        return 0 if len(stones) == 0 else stones[0] * -1
        
            



        