class Solution:
    def pivotInteger(self, n: int) -> int:
        i=1
        j=n
        curre=n
        while i<=j:
            if curre>=i:
                curre-=i
                i+=1
            else:
                j-=1
                curre+=j
        if curre==0:
            return j
        return -1
        