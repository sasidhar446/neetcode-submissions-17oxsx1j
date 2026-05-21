class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        need = Counter(s1)
        left, right = 0, len(s1)
        while right <= len(s2):
            have = Counter(s2[left:right])
            if need == have:
                return True
            left += 1
            right += 1
        return False


            
    
        