import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        deq = collections.deque()
        time_, freq, minHeap = 0, Counter(tasks), []

        for val in freq.values():
            minHeap.append(-val)

        heapq.heapify(minHeap)

        while minHeap or deq:
            time_ += 1
            if minHeap:
                count = heapq.heappop(minHeap) + 1
                if count:
                    deq.append([count, time_ + n])
            if deq:
                if time_ == deq[0][1]:
                    heapq.heappush(minHeap, deq.popleft()[0])
        
        return time_



        


        
        