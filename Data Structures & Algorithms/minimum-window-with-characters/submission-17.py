class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right, result = 0, 0, s * 2
        need, have = Counter(t), defaultdict(int)
        required, formed = len(need), 0
        min_length, best_left, best_right = float("inf"), 0, 0

        while right < len(s):
            if s[right] in need:
                have[s[right]] += 1
                if have[s[right]] == need[s[right]]:
                    formed += 1
            
            while formed == required and left <= right:
                current_length = right - left + 1
                if current_length < min_length:
                    min_length = current_length
                    best_left = left
                    best_right = right
                if s[left] in need:
                    have[s[left]] -= 1              
                if have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1

            right += 1
        
        return "" if min_length == float("inf") else s[best_left: best_right + 1]

       

            
            
