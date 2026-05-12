import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 0: return 0

        hashMap = Counter(tasks)

        maxHeap, time_, deq = [], 0, collections.deque()

        for val in hashMap.values():
            maxHeap.append(-val)
        
        heapq.heapify(maxHeap)

        while maxHeap or deq:
            time_ += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    deq.append([cnt, time_ + n])
            if deq and deq[0][1] == time_:
                heapq.heappush(maxHeap, deq.popleft()[0])

        return time_



        


        
        