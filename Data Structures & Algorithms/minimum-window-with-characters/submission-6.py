class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t): return ""
        left, min_length, result, result_indexes = 0, float("inf"), "", [-1, -1]
        t_map, w_map = Counter(t), defaultdict(int)
        have, need = 0, len(t_map)
        for right in range(len(s)):
            w_map[s[right]] += 1
            if s[right] in t_map and w_map[s[right]] == t_map[s[right]]:
                have += 1
            while have == need:
                window_length = right - left + 1
                if window_length < min_length:
                    min_length = window_length
                    result_indexes = [left, right]
                w_map[s[left]] -= 1
                if s[left] in t_map and w_map[s[left]] < t_map[s[left]]:
                    have -= 1
                left += 1
        return s[result_indexes[0]: result_indexes[1] + 1] if min_length != float("inf") else ""
