class MyCalendar:

    def __init__(self):
        self.calender=[]
    def book(self, start: int, end: int) -> bool:
        for i,j in self.calender:
            if i<=start<j or i<end<=j or start<j<end:
                return False
        self.calender.append((start,end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)