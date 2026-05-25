class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, current = [], []

        def backtrack(index):
            if sum(current) == target:
                result.append(current[:])
                return
            
            if sum(current) > target or index == len(nums):
                return
            
            current.append(nums[index]) # Make choice
            backtrack(index) # Explore
            current.pop() # Undo choice
            backtrack(index + 1) # Explore
        
        backtrack(0)

        return result


        
        