class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        have = Counter(s2[:len(s1)])
        left, right = 0, len(s1)
        while right < len(s2):
            if need == have:
                return True
            else:
                have[s2[right]] += 1
                have[s2[left]] -= 1
                if have[s2[left]] == 0:
                    del have[s2[left]] 
                left += 1
            right += 1
        return need == have


            
    
        