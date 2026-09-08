class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, result = 0, len(heights) - 1, float("-inf")

        while left < right:
            window_length = right - left
            container = window_length * min(heights[left], heights[right])
            result = max(result, container)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return result
