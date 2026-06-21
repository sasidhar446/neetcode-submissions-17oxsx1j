import heapq
from collections import deque, defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        min_heap, visited, max_time = [(0, k)], set(), 0
        adjlist = defaultdict(list)

        for u, v, w in times:
            adjlist[u].append([v, w])
        
        while min_heap:
            current_time, student = heapq.heappop(min_heap)

            if student in visited:
                continue
            
            visited.add(student)

            max_time = max(max_time, current_time)

            for friend, travel_time in adjlist[student]:
                arrival_time = current_time + travel_time
                heapq.heappush(min_heap, (arrival_time, friend))
            
        return max_time if len(visited) == n else -1


        