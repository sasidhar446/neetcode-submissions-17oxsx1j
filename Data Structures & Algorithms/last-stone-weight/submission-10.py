import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        minHeap = [-stone for stone in stones]
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)
            if x - y != 0:
                heapq.heappush(minHeap, x - y)
        
        return 0 if not minHeap else -minHeap[0]
            





        
            



        