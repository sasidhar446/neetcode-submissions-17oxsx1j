class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, current = [], []

        def backtrack(index, remaining_target):
            if remaining_target == 0:
                result.append(current[:])
                return
            
            if remaining_target < 0 or index >= len(nums):
                return

            current.append(nums[index])
            backtrack(index, remaining_target - nums[index])
            current.pop()
            backtrack(index + 1, remaining_target)
        
        backtrack(0, target)

        return result
        


        
        