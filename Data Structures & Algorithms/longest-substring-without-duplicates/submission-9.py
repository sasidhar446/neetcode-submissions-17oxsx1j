class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, result = 0, 0, 0
        hashset = set()

        while right < len(s):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            result = max(result, right - left + 1)
            right += 1
        
        return result



        