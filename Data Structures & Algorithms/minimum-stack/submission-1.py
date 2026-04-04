class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        current_min = self.stack[-1][1] if self.stack else float('inf')
        self.stack.append((val, min(current_min, val)))
        return
        

    def pop(self) -> None:
        del self.stack[-1]
        return
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]

        
