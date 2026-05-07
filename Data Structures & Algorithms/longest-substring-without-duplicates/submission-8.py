class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, result, hashset = 0, 0, 0, set()
        while right < len(s):
            while left < right and s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            result = max(result, right - left + 1)
            hashset.add(s[right])
            right += 1
        return result


        