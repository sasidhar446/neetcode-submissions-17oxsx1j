class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, result, hashmap = 0, 0, 0, defaultdict(int)

        while right < len(s):
            hashmap[s[right]] += 1
            max_key = max(hashmap, key=hashmap.get)
            max_val = hashmap[max_key]
            window_length = right - left + 1

            if window_length - max_val <= k:
                result = max(result, window_length)
            else:
                hashmap[s[left]] -= 1
                left += 1

            right += 1
        
        return result
    