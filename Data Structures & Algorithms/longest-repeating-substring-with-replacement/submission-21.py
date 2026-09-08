class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, result, hashmap = 0, 0, 0, defaultdict(int)

        while right < len(s):
            hashmap[s[right]] += 1
            max_key = max(hashmap, key=hashmap.get)
            window_length = right - left + 1
            if window_length - hashmap[max_key] > k:
                hashmap[s[left]] -= 1
                left += 1
            else:
                result = max(result, window_length)
            
            right += 1
        
        return result
        
    