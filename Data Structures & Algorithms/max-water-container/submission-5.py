class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, result = 0, len(heights) - 1, float("-inf")

        while left < right:
            length = right - left
            result = max(min(heights[left], heights[right]) * length, result)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return result