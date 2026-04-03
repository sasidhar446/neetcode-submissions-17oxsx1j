class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signature = defaultdict(list)
        result = []
        for str_ in strs:
            key = [0] * 26
            for c in str_:
                key[ord(c) - ord('a')] += 1
            signature[tuple(key)].append(str_)
        for value in signature.values():
            result.append(value)
        return result
        

        