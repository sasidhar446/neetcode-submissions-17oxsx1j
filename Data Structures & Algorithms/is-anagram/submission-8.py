class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = defaultdict(int), defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_map[s[i]] += 1
            t_map[t[i]] += 1
        for k, v in s_map.items():
            if t_map[k] != v:
                return False
        return True
        
        