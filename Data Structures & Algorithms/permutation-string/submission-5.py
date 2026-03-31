class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        s1_freq = Counter(s1)
        w_freq = Counter(s2[:n1])
        if s1_freq == w_freq:
            return True
        for i in range(n1, n2):
            char_in = s2[i]
            char_out = s2[i - n1]
            w_freq[char_in] += 1
            w_freq[char_out] -=1
            if w_freq[char_out] == 0:
                del w_freq[char_out]
            if s1_freq == w_freq:
                return True 
        return False
        