class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack:
            min_ = min(val, self.stack[-1][1])
        else:
            min_ = min(val, float("inf"))
        self.stack.append((val, min_))
        return
        

    def pop(self) -> None:
        del self.stack[-1]
        return
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]

        
