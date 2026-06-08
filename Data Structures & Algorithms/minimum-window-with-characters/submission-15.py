class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right, result = 0, 0, s * 2
        need, have = Counter(t), defaultdict(int)
        required, formed = len(need), 0

        while right < len(s):
            if s[right] in need:
                have[s[right]] += 1
                if have[s[right]] == need[s[right]]:
                    formed += 1
            
            while formed == required and left <= right:
                result = s[left: right + 1] if len(s[left: right + 1]) < len(result) else result
                if s[left] in need:
                    have[s[left]] -= 1              
                if have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1

            right += 1
        
        return "" if result == s * 2 else result

       

            
            
