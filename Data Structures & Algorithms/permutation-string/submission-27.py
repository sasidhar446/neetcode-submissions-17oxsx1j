class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_map = Counter(s1)

        left, right = 0, len(s1)

        temp_map = Counter(s2[left: right])

        if s1_map == temp_map:
            return True

        while right < len(s2):
            temp_map[s2[left]] -= 1
            if temp_map[s2[left]] == 0:
                del temp_map[s2[left]]
            temp_map[s2[right]] += 1
            if s1_map == temp_map:
                return True
            left += 1
            right += 1

        return False