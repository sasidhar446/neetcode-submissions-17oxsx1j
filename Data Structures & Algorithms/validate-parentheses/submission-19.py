class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {'}':'{', ']':'[', ')':'('}
        stack = []
        for c in s:
            if c not in lookup:
                stack.append(c)
            else:
                if stack and stack[-1] == lookup[c]:
                    stack.pop()
                else:
                    return False
        return not stack