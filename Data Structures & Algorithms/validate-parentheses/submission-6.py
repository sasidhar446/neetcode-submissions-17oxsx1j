class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        lookup = {']': '[', ')': '(', '}': '{'}
        stack = []
        for c in s:
            if c in lookup:
                if stack and lookup[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

        

        