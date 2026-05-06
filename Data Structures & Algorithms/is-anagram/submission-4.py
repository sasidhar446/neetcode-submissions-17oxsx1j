class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map, t_map = defaultdict(int), defaultdict(int)
        for ele in s:
            s_map[ele] += 1
        for ele in t:
            t_map[ele] += 1
        for k, v in s_map.items():
            if t_map[k] != v:
                return False
        return True
        