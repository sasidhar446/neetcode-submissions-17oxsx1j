class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        result = float("inf"), None, None
        need = Counter(t)
        have = {}
        left, right, formed, required = 0, 0, 0, len(need)
        while right < len(s):
            char = s[right]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]
                
                if result[0] > right - left + 1:
                    result = (right - left + 1, left, right)
                
                have[char] -= 1
                if char in need and have[char] < need[char]:
                    formed -= 1
                
                left += 1

            right += 1

        return "" if result[0] == float("inf") else s[result[1]: result[2] + 1]
