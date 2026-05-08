class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        left, right, need, have = 0, 0, Counter(t), defaultdict(int)
        required, formed = len(need), 0
        result = float("inf"), None, None
        while right < len(s):
            char = s[right]
            have[char] += 1
            if char in need and need[char] == have[char]:
                formed += 1
            while left <= right and formed == required:
                length = right - left + 1
                if length < result[0]:
                    result = (length, left, right)
                char = s[left]
                have[char] -= 1
                if char in need and have[char] < need[char]:
                    formed -= 1
                left += 1
            right += 1
        return "" if result[0] == float("inf") else s[result[1]: result[2] + 1]
            
            
