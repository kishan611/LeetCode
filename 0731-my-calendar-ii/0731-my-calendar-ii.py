class MyCalendarTwo:

    def __init__(self):
        self.c1=[]
        self.c2=[]

    def book(self, start: int, end: int) -> bool:
        for i,j in self.c2:
            if max(i,start)<min(j,end):
                return False
        for i,j in self.c1:
            if max(i,start)<min(j,end):
                self.c2.append((max(start,i),min(end,j)))
        else:
            self.c1.append((start,end))
        return True

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)