class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, current = [], []

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
            
            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()
            
        backtrack([])

        return result
        