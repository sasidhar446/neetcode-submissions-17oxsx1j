import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [[(point[0]*point[0]) + (point[1] * point[1]), point[0], point[1]] for point in points]
        heapq.heapify(minHeap)
        result = []

        while k > 0:
            element = heapq.heappop(minHeap)
            result.append([element[1], element[2]])
            k -= 1
        
        return result

        
        