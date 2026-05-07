class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        need = Counter(t)
        have = defaultdict(int)
        required = len(need)
        formed = 0
        left, right = 0, 0
        result = float("inf"), None, None
        while right < len(s):
            char = s[right]
            have[char] += 1
            if char in need and have[char] == need[char]:
                formed += 1
            while left <= right and formed == required:
                char = s[left]
                length = right - left + 1
                if result[0] > length:
                    result = (length, left, right)
                have[char] -= 1
                if char in need and have[char] < need[char]:
                    formed -= 1
                left += 1
            right += 1
        return "" if result[0] == float("inf") else s[result[1]: result[2] + 1]
            
