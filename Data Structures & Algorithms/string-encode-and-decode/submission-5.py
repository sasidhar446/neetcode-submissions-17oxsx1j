class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(ele)) + '#' + ele for ele in strs])

    def decode(self, s: str) -> List[str]:
        left, right = 0, 0
        result = []
        while right < len(s):
            while s[right] != '#':
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = left + length
            result.append(s[left: right])
            left = right
        return result

