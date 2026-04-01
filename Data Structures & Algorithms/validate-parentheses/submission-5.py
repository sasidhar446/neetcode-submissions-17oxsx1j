class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {']': '[', ')': '(', '}': '{'}
        if len(s) == 0 or len(s) % 2 != 0 or s[0] in lookup.keys():
            return False
        stack = []
        for i in range(len(s)):
            if len(stack) > 0 and s[i] in lookup.keys() and lookup.get(s[i], '') == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
            print(stack)
        if len(stack) == 0:
            return True
        return False

        