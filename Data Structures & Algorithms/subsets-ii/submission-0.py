class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, current = [], []
        nums.sort()

        def backtrack(index, current):
            result.append(current[:])

            for i in range(index, len(nums)):
                if i > index and nums[i -1] == nums[i]:
                    continue
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
            
        backtrack(0, [])
        
        return result
        