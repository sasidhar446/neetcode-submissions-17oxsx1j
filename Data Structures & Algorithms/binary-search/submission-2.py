class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            match = nums[middle]
            if match == target:
                return middle
            elif match > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1