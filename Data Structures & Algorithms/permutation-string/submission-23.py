class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        left, s1_map, s2_map = 0, Counter(s1), Counter(s2[:len(s1)])
        
        if s1_map == s2_map:
            return True

        for i in range(len(s1), len(s2)):
            s2_map[s2[i]] += 1
            s2_map[s2[left]] -= 1
            left += 1
            if s2_map[s2[left]] == 0:
                del s2_map[s2[left]]
            if s2_map == s1_map:
                return True
            
        return False