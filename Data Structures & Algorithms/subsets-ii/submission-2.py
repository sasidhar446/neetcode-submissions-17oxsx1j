class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, current = [], []
        nums.sort()

        def backtrack(index):
            result.append(current[:])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()
            
        backtrack(0)

        return result
        