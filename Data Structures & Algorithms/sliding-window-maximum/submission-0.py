class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        if len(nums) < k:
            return result
        for i in range(k, len(nums) + 1):
            print (i -k, i)
            result.append(max(nums[i - k:i]))
        return result