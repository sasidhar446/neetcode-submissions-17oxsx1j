class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, sufix = 1, 1
        result, sufix_list = [], [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            sufix_list[i] = sufix
            sufix *= nums[i]
        for i in range(len(nums)):
            result.append(prefix * sufix_list[i])
            prefix *= nums[i]
        return result


        
