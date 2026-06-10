class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        hashset = set(nums)
        for num in hashset:
            count = 0
            if num - 1 not in hashset:
                while num in hashset:
                    count += 1
                    num += 1
            result = max(result, count)
        
        return result

        