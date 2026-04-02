class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        result = 0
        for num in lookup:
            count = 0
            if num - 1 not in lookup:
                while num in lookup:
                    count += 1
                    num += 1
            result = max(result, count)
        return result

        