class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(str_)) + '#' + str_ for str_ in strs])


    def decode(self, s: str) -> List[str]:
        left, right, length, result = 0, 0, 0, []
        while right < len(s):
            while s[right] != '#':
                right +=1
            length = int(s[left: right])
            left = right + 1
            right = length + left
            result.append(s[left: right])
            left = right
            right += 1
        return result
        
            
