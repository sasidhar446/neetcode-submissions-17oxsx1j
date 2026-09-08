class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, result = 0, 0, 0
        lookup = set()

        while right < len(s):
            while s[right] in lookup:
                lookup.remove(s[left])
                left += 1
            result = max(result, right - left + 1)
            lookup.add(s[right])
            right += 1
        
        return result
        