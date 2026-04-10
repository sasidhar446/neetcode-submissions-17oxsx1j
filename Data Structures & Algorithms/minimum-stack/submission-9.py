class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif val <= self.minstack[-1]:
            self.minstack.append(val)
        return
        

    def pop(self) -> None:
        ele = self.stack.pop()
        if ele == self.minstack[-1]:
            self.minstack.pop()
        return


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minstack[-1]
        

        
