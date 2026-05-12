import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        
        maxHeap = nums
        heapq.heapify(maxHeap)
        result = 0

        while k > 0:
            result = heapq.heappop(maxHeap)
            k -= 1
        
        return result * -1


        