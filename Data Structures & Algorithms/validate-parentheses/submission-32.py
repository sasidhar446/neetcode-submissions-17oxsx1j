class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {')': '(', ']': '[', '}': '{'}
        stack = []
        for bracket in s:
            if bracket not in lookup:
                stack.append(bracket)
            else:
                if stack and stack[-1] != lookup[bracket]:
                    return False
                elif stack and stack[-1] == lookup[bracket]:
                    stack.pop()
                else:
                    stack.append(bracket)
        return not stack



        