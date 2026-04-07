class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        result = []
        for str_ in strs:
            if len(str_) == 0:
                lookup[tuple([0])].append(str_)
            else:
                key = [0] * 26
                for c in str_:
                    key[ord(c) - ord("a")] += 1
                lookup[tuple(key)].append(str_)
        for value in lookup.values():
            result.append(value)
        return result
        

        