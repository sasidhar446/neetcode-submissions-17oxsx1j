class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {')': '(', '}': '{', ']':'['}
        stack = []
        if len(s) <= 1: return False
        for char in s:
            if char not in lookup:
                stack.append(char)
            else:
                if stack and stack[-1] == lookup[char]:
                    stack.pop()
                else:
                    return False
        return not stack

        