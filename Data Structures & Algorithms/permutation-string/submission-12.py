class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_map, hashmap = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            s1_map[s1[i]] += 1
            hashmap[s2[i]] += 1
        for i in range(len(s1), len(s2)):
            if hashmap == s1_map:
                return True
            hashmap[s2[i]] += 1
            hashmap[s2[i - len(s1)]] -= 1
            if hashmap[s2[i - len(s1)]] == 0:
                del hashmap[s2[i - len(s1)]]
        return hashmap == s1_map


            
    
        