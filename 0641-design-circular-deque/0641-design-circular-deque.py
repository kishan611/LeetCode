class MyCircularDeque:

    def __init__(self, k: int):
        self.f=-1
        self.r=-1
        self.n=k
        self.dq=[0]*k
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.f+=1
            self.r+=1
        else:
            if self.f==0:
                self.f=self.n-1
            else:
                self.f-=1
        self.dq[self.f]=value
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.f+=1
            self.r+=1
        else:
            self.r=(self.r+1)%self.n
        self.dq[self.r]=value
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.f==self.r:
            self.dq[self.f]=0
            self.f=self.r=-1
            return True
        self.dq[self.f]=0
        self.f=(self.f+1)%self.n
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.f==self.r:
            self.dq[self.f]=0
            self.f=self.r=-1
            return True
        self.dq[self.r]=0
        if self.r==0:
            self.r=self.n-1
        else:
            self.r-=1
        return True
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.dq[self.f]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.dq[self.r]

    def isEmpty(self) -> bool:
        return self.f==-1

    def isFull(self) -> bool:
        return (self.r+1)%self.n==self.f

        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()