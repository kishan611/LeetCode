import heapq
class AllOne:

    def __init__(self):
        self.d={}

    def inc(self, key: str) -> None:
        self.d[key]=self.d.get(key,0)+1

    def dec(self, key: str) -> None:
        self.d[key]-=1
        if self.d[key]==0:
            del self.d[key]

    def getMaxKey(self) -> str:
        if not self.d:
            return ""
        x=max(self.d.values())
        for i,j in self.d.items():
            if j==x:
                return i

    def getMinKey(self) -> str:
        if not self.d:
            return ""
        x=min(self.d.values())
        for i,j in self.d.items():
            if j==x:
                return i

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()