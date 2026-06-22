class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result, current = [], []

        def backtrack(index, remaining_target):
            if remaining_target == 0:
                result.append(current[:])
                return

            if remaining_target < 0:
                return
            
            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(i, remaining_target - nums[i])
                current.pop()
        
        backtrack(0, target)

        return result




        
        