class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, hashmap, left, right = 0, defaultdict(int), 0, 0
        while right < len(s):
            while s[right] in hashmap:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                left += 1
            result = max(result, right - left + 1)
            hashmap[s[right]] += 1
            right += 1
        return result


        