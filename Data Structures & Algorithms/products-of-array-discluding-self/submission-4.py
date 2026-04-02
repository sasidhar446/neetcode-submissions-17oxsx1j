class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       prefix, suffix = 1, 1
       prefix_prod = [0] * len(nums)
       suffix_prod = [0] * len(nums)
       result = [0] * len(nums)
       for i in range(len(nums)):
            prefix_prod[i] = prefix
            prefix = nums[i] * prefix
       for i in range(len(nums) - 1, -1, -1):
            suffix_prod[i] = suffix
            suffix = suffix * nums[i]
       for i in range(len(nums)):
            result[i] = suffix_prod[i] * prefix_prod[i]
       return result





                    
        