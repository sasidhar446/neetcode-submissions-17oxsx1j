class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for item in strs:
            result += str(len(item)) + "#" + item
        return result


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + length
            res.append(s[word_start: word_end])
            i = word_end
        return res
            
