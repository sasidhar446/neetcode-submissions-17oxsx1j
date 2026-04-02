class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, area = 0, len(heights) - 1, 0
        while left < right:
            area = max(area, (right - left) * min(heights[right], heights[left]))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return area

        