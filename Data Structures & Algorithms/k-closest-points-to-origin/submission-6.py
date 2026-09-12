import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_with_dist = [[x*x + y*y, x, y] for x, y in points]
        heapq.heapify(points_with_dist)
        result = []
        while k > 0:
            result.append([points_with_dist[0][1], points_with_dist[0][2]])
            heapq.heappop(points_with_dist)
            k -= 1
        return result
        