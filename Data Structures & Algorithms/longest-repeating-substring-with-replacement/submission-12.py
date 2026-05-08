class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, lookup, result = 0, 0, defaultdict(int), 0
        while right < len(s):
            lookup[s[right]] += 1
            length = right - left + 1
            max_key = max(lookup, key=lookup.get)
            if length - lookup[max_key] <= k:
                result = max(result, length)
            else:
                lookup[s[left]] -= 1
                left += 1
            right += 1
        return result


    