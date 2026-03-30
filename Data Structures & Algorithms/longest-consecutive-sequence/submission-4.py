class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        lookup = set(nums)
        for num in lookup:
            if num - 1 not in lookup:
                current_num = num
                current_streak = 1
                while current_num + 1 in lookup:
                    current_streak += 1
                    current_num += 1
                longest_sequence = max(current_streak, longest_sequence)
        return longest_sequence


        