class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, sufix, result = height[0], height[-1], 0
        prefix_max, sufix_max = [0] * len(height), [0] * len(height)

        for i in range(len(height)):
            prefix_max[i] = prefix
            prefix = max(prefix, height[i])
        
        for i in range(len(height) - 1, -1, -1):
            sufix_max[i] = sufix
            sufix = max(sufix, height[i])
        
        for i in range(len(height)):
            water = min(prefix_max[i], sufix_max[i]) - height[i]
            if water > 0:
                result += water
        
        return result


        