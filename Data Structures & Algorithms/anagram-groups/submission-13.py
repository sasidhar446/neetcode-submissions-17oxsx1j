class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str_ in strs:
            signature = [0] * 26
            for c in str_:
                signature[ord('a') - ord(c)] += 1
            result[tuple(signature)].append(str_)
        
        return list(result.values())
        