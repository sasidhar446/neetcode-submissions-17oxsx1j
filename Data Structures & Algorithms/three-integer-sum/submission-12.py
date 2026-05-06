class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1
        return list(result)

        