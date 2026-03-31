class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, length, result, counts = 0, 0, 0, 0, defaultdict(int)
        while right < len(s):
            counts[s[right]] += 1
            length = right - left + 1
            max_key = max(counts, key=counts.get)
            if length - counts[max_key] <= k:
                result = max(result, length)
            else:
                counts[s[left]] -= 1
                left += 1
            right += 1
        return result
        


        