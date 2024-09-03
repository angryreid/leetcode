class MyQueue:

    def __init__(self):
        self.stackIn = []
        self.stackPop = []
        

    def push(self, x: int) -> None:
        self.stackIn.append(x)
        

    def pop(self) -> int:
        if not self.stackPop:
            while self.stackIn:
                self.stackPop.append(self.stackIn.pop())
        return self.stackPop.pop()
        

    def peek(self) -> int:
        if not self.stackPop:
            while self.stackIn:
                self.stackPop.append(self.stackIn.pop())
        return self.stackPop[-1]
        

    def empty(self) -> bool:
        return not self.stackIn and not self.stackPop
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()