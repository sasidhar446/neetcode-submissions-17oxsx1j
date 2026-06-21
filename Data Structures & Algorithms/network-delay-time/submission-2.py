import heapq
from collections import deque, defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        min_heap, visited, adj_list, max_time = [[0, k]], set(), defaultdict(list), 0

        # heapq.heapify(min_heap)

        for u, v, w in times:
            adj_list[u].append([v, w])
        

        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            
            visited.add(node)

            max_time = max(current_time, max_time)

            for neighbour, time_ in adj_list[node]:
                arrival_time = current_time + time_
                heapq.heappush(min_heap, (arrival_time, neighbour))
        
        return max_time if len(visited) == n else -1


        