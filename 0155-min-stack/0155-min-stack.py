import sys
class MinStack:

    def __init__(self):
        self.s=[]
        self.min=sys.maxsize
        

    def push(self, val: int) -> None:
        self.min=min(val,self.min)
        self.s.append([val,self.min])
        

    def pop(self) -> None:
        self.s.pop()
        if self.s:
            self.min=self.s[-1][1]
        else:
            self.min=sys.maxsize

    def top(self) -> int:
        return self.s[-1][0]
        

    def getMin(self) -> int:
        return self.s[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()