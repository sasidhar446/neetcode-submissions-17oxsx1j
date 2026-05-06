class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(ele)) + '#' + ele for ele in strs])

    def decode(self, s: str) -> List[str]:
        left, right = 0, 0
        result = []
        while right < len(s):
            while s[right] != '#':
                right += 1
            word_length = int(s[left:right])
            right += 1
            result.append(s[right: word_length + right])
            right, left = word_length + right, word_length + right
        return result

