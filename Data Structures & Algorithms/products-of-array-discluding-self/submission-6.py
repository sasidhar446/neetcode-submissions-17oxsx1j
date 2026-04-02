class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       prefix, suffix = 1, 1
       result = [0] * len(nums)
       for i in range(len(nums)):
            result[i] = prefix
            prefix = nums[i] * prefix
       for i in range(len(nums) - 1, -1, -1):            
            result[i] *= suffix
            suffix = suffix * nums[i]
       return result





                    
        