class Solution:
    def minSwaps(self, s: str) -> int:
        res=0
        for i in s:
            if i=="[":
                res+=1
            elif res>0:
                res-=1
        return (res+1)//2