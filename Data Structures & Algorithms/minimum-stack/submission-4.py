class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        current_min = self.minStack[-1] if self.stack else float("inf")
        self.minStack.append(min(current_min, val)) 
        self.stack.append(val)
        return
        

    def pop(self) -> None:
        del self.minStack[-1]
        del self.stack[-1]
        return
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

        
