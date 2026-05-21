class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, result, hashmap = 0, 0, 0, defaultdict(int)
        while right < len(s):
            window_length = right - left + 1
            hashmap[s[right]] += 1
            max_key = max(hashmap, key=hashmap.get)
            max_count = hashmap[max_key]
            if window_length - max_count <= k:
                result = max(result, window_length)
            else:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                left += 1
            right += 1
        return result


    