class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        hashset, result = set(), 0

        while right < len(s):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            result = max(result, right - left + 1)
            right += 1

        return result