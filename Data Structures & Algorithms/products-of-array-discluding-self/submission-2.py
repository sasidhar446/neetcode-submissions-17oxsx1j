class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       prefix = 1
       suffix = 1
       prefix_res = [0] * len(nums)
       suffix_res = [0] * len(nums)
       for i in range(len(nums)):
           prefix_res[i] = prefix
           prefix *= nums[i]
       for i in range(len(nums) -1, -1, -1):
           suffix_res[i] = suffix
           suffix *= nums[i]
       for i in range(len(prefix_res)):
           prefix_res[i] *= suffix_res[i]
       return prefix_res





                    
        