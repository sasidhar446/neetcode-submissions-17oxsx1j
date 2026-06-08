import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        count = 0
        heapq.heapify(maxHeap)
        while count < k - 1:
            heapq.heappop(maxHeap)
            count += 1
        
        return -heapq.heappop(maxHeap)





        