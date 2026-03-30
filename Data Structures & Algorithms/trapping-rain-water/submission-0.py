class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)
        prefix, suffix, result = 0, 0, 0
        for i in range(len(height)):
            prefix_max[i] = prefix
            prefix = max(prefix, height[i])
        for i in range(len(height) - 1, -1, -1):
            suffix_max[i] = suffix
            suffix = max(suffix, height[i])
        for i in range(len(height)):
            trapped = min(prefix_max[i], suffix_max[i]) - height[i]
            if trapped >= 0:
                result += trapped
        return result


        