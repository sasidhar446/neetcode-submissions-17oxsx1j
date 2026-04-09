class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, result = 0, 0
        w_map = defaultdict(int)
        for right in range(len(s)):
            w_map[s[right]] += 1
            w_length = right - left + 1
            max_ele = max(w_map, key=w_map.get)
            if w_length - w_map[max_ele] <= k:
                result = max(result, w_length)
            else:
                w_map[s[left]] -= 1
                left += 1
        return result
            
            



        