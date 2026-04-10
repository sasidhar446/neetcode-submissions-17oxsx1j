class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda a, b : a + b,
            '-': lambda a, b : a - b,
            '*': lambda a, b : a * b,
            '/': lambda a, b : int(a / b)
        }
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                result = operations[token](a, b)
                stack.append(result)
        return stack[0]


        