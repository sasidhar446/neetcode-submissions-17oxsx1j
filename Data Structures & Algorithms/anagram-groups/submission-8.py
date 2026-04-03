class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str_ in strs:
            key = [0] * 26
            for c in str_:
                key[ord(c) - ord('a')] += 1
            result[tuple(key)].append(str_)
        return list(result.values())
        

        