class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_map = Counter(s1)

        left, right = 0, len(s1)

        while right <= len(s2):
            temp_map = Counter(s2[left: right])
            
            if temp_map == s1_map:
                return True
            
            left += 1
            right += 1

        return False