class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, sufix, result = 1, 1, [1] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= sufix
            sufix *= nums[i]
        return result