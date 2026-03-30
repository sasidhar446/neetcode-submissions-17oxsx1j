class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        lookup = set(nums)
        for num in nums:
            count = 0
            if num -1 not in lookup:
                num += 1
                count += 1
                while num in lookup:
                    count += 1
                    num += 1
            longest_sequence = max(count, longest_sequence)
        return longest_sequence


        