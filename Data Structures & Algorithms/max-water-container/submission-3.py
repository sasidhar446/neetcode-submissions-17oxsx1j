class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result, left, right = 0, 0, len(heights) - 1
        while left < right:
            result = max(min(heights[left], heights[right]) * (right - left), result)
            if left < right and heights[left] < heights[right]:
                left += 1
            elif left < right and heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return result
        