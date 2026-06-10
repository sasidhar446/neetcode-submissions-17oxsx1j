class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([ str(len(str_))+"#"+str_ for str_ in strs])

    def decode(self, s: str) -> List[str]:
        left, right, result = 0, 0, []
        while right < len(s):
            while s[right] != '#':
                right += 1
            word_length = int(s[left: right])
            right += 1
            result.append(s[right: word_length + right])
            left =  word_length + right
            right = left
        
        return result


