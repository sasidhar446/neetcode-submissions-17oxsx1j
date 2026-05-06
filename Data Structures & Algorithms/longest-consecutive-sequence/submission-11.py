class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        lookup = set(nums)
        for num in lookup:
            count = 0
            if not num - 1 in lookup:
                while num in lookup:
                    count += 1
                    num += 1
                result = max(result, count)
        return result


        