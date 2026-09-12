import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [-num for num in nums]
        heapq.heapify(minheap)
        result = 0
        while k > 0:
            result = heapq.heappop(minheap)
            k -= 1
        return -result




        