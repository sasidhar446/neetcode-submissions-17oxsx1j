class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right, size = 0, len(s1), len(s1)
        s1_freq = defaultdict(int)
        for c in s1:
            s1_freq[c] += 1
        while right <= len(s2):
            window_freq = defaultdict(int)
            for c in s2[left: right]:
                window_freq[c] += 1
            if s1_freq == window_freq:
                return True
            right += 1
            left += 1
        return False        
        