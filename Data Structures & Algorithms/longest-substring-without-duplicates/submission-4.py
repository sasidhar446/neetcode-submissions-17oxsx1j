class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left, right, result = 0, 0, 0
        lookup = defaultdict(int)
        while right < len(s):
            if s[right] in lookup:
                while lookup[s[right]] != 0:
                    lookup[s[left]] -= 1
                    left += 1
            result = max(result, right - left + 1)
            lookup[s[right]] += 1
            right += 1
        return result