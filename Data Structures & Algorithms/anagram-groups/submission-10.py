class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        result = []
        for str_ in strs:
            count = [0] * 26
            for c in str_:
                count[ord(c) - ord("a")] += 1
            lookup[tuple(count)].append(str_)
        return list(lookup.values())
        

        