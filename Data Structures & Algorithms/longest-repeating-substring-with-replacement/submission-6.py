class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, length, result, lookup = 0, 0, 0, 0, defaultdict(int)
        while right < len(s):
            lookup[s[right]] += 1
            length = right - left + 1
            max_ = max(lookup, key=lookup.get)
            if length - lookup[max_] <= k:
                result = max(result, length)
            else:
                lookup[s[left]] -= 1
                left += 1
            right += 1
        return result
        