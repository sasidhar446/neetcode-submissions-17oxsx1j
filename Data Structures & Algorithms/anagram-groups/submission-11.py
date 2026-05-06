class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies = defaultdict(list)
        for ele in strs:
            signature = [0]*26
            for c in ele:
                signature[ord(c) - ord('a')] += 1
            frequencies[tuple(signature)].append(ele)
        return list(frequencies.values())
        