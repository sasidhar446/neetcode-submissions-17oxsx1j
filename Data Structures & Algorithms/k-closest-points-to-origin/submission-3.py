import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap, result = [], []

        for point in points:
            minHeap.append((point[0]**2 + point[1]**2, point))
        heapq.heapify(minHeap)

        while k > 0:
            result.append(heapq.heappop(minHeap)[1])
            k -= 1
        
        return result

        
        