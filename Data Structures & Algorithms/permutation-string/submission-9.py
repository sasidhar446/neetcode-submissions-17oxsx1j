class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left, right, s2_map = 0, len(s1), defaultdict(int)
        s1_map = Counter(s1)
        for i in range(len(s1)):
            s2_map[s2[i]] += 1
        while right < len(s2):
            if s1_map == s2_map:
                return True
            s2_map[s2[right]] += 1
            s2_map[s2[left]] -= 1

            if s2_map[s2[left]] == 0:
                del s2_map[s2[left]]

            left += 1
            right += 1

        return s1_map == s2_map



