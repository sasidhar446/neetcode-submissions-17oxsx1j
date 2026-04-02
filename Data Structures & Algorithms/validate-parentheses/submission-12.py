class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        open_ = {']': '[', '}': '{', ')': '('}
        stack = []
        for c in s:
            if c in open_:
                if stack and stack[-1] == open_[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

        