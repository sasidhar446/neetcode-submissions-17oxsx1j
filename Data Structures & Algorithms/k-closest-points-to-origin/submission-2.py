import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap, result, count = [], [], 0

        for point in points:
            minHeap.append((point[0]**2 + point[1]**2, point))
        heapq.heapify(minHeap)

        while count < k:
            result.append(heapq.heappop(minHeap)[1])
            count += 1
        
        return result

        
        