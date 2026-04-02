class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        lookup = {']': '[', '}': '{', ')': '('}
        stack = []
        for c in s:
            if c not in lookup:
                stack.append(c)
            elif stack and stack[-1] == lookup[c]:
                stack.pop()
            else:
                return False
        return not stack
        