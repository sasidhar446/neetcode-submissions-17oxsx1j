class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = defaultdict(int), defaultdict(int)
        if len(s) != len(t):
            return False
        for c in s:
            s_map[c] += 1
        for c in t:
            t_map[c] += 1
        for k, v in s_map.items():
            if t_map[k] != v:
                return False
        return True
        
        