import random
class RandomizedSet:

    def __init__(self):
        self.d={}

    def insert(self, val: int) -> bool:
        if self.d.get(val,0):
            return False
        self.d[val]=1
        return True

    def remove(self, val: int) -> bool:
        if self.d.get(val,0):
            del self.d[val]
            return True
        return False

    def getRandom(self) -> int:
        l=[i for i,j in self.d.items()]
        return random.choice(l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()