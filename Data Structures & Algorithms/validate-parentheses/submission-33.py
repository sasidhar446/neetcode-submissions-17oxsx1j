class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {')': '(', ']': '[', '}': '{'}
        stack = []
        for bracket in s:
            if bracket not in lookup:
                stack.append(bracket)
            else:
                if stack and stack[-1] == lookup[bracket]:
                    stack.pop()
                else:
                    return False
        return not stack



        