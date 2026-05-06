class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, hashset, left, right = 0, set(), 0, 0
        while right < len(s):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            result = max(result, right - left + 1)
            hashset.add(s[right])
            right += 1
        return result


        