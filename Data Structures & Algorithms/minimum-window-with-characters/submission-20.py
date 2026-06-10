class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right, formed = 0, 0, 0
        need, have = Counter(t), defaultdict(int)
        required = len(need)
        min_window, left_best, right_best = float("inf"), 0, 0

        while right < len(s):
            if s[right] in need:
                have[s[right]] += 1
                if have[s[right]] == need[s[right]]:
                    formed += 1

            while left <= right and formed == required:
                window = right - left + 1
                if window < min_window:
                    min_window = window
                    left_best = left
                    right_best = right
                if s[left] in need:
                    have[s[left]] -= 1
                    if have[s[left]] < need[s[left]]:
                        formed -= 1
                left += 1

            right += 1
        
        return "" if min_window == float("inf") else s[left_best: right_best + 1]
