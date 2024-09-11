class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res=0
        while start>0 or goal>0:
            if start%2!=goal%2:
                res+=1
            start//=2
            goal//=2
        return res
        