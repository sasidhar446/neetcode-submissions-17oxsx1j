class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, hashmap, result = 0, 0, defaultdict(int), 0

        while right < len(s):
            hashmap[s[right]] += 1
            window_length = right - left + 1
            max_key = max(hashmap, key=hashmap.get)
            max_count = hashmap[max_key]

            if window_length - max_count <= k:
                result = max(result, window_length)
            else:
                hashmap[s[left]] -= 1
                left += 1
            
            right += 1
        
        return result



    