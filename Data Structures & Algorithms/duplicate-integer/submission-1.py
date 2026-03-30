class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains_in_set = set()
        for num in nums:
            if num in contains_in_set:
                return True
            else:
                contains_in_set.add(num)
        return False
        