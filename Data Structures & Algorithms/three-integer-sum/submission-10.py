class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total == 0:
                    result.append([nums[left], nums[right], nums[i]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right -1]:
                        right -=1
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return result

        




        