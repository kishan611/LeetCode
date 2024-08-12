class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.num=nums
        self.num.sort(reverse=True)
    def add(self, val: int) -> int:
        i=0
        while i<len(self.num):
            if self.num[i]<=val:
                break
            i+=1
        self.num.insert(i,val)
        return self.num[self.k-1]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)