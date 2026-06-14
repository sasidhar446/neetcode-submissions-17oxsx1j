class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, current = [], []

        def backtrack(index):
            if sum(current) == target:
                result.append(current[:])
                return
            
            if sum(current) > target or index >= len(nums):
                return

            current.append(nums[index])
            backtrack(index)
            current.pop()
            backtrack(index + 1)

        backtrack(0)

        return result



        
        