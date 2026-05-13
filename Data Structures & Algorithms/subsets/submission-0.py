class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            # Base case
            if i >= len(nums):
                res.append(subset[:])
                return
            
            # Choices
            subset.append(nums[i])
            backtrack(i + 1)

            # Backtrack
            subset.pop()
            backtrack(i + 1)

        backtrack(0)

        return res