class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, length, result, lookup = 0, 0, 0, 0, set()
        while right < len(s):
            if s[right] in lookup:
                while left < right:
                    if s[left] == s[right]:
                        lookup.remove(s[left])
                        left += 1
                        break
                    lookup.remove(s[left])
                    left += 1
            lookup.add(s[right])
            length = right - left + 1
            result = max(result, length)
            right += 1
        return result
                


        