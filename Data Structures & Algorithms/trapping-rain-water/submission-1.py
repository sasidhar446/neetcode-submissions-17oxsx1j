class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max, sufix_max = [0] * len(height), [0] * len(height)
        result = 0
        for i in range(1, len(height)):
            prefix_max[i] = max(prefix_max[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            sufix_max[i] = max(sufix_max[i + 1], height[i + 1])
        for i in range(len(height)):
            trapped = min(prefix_max[i], sufix_max[i]) - height[i]
            if trapped > 0:
                result += trapped
        return result

        