class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, current, visited = [], [], set()

        def backtrack():
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    current.append(nums[i])
                    visited.add(nums[i])
                    backtrack()
                    current.pop()
                    visited.remove(nums[i])
                
        backtrack()

        return result
