class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left, right, result, length, lookup = 0, 0, 0, 0, set()
        while right < len(s):
            if s[right] in lookup:
                while s[right] in lookup:
                    lookup.remove(s[left])
                    left += 1
            length = right - left + 1
            result = max(result, length)
            lookup.add(s[right])
            right += 1
        return result

        