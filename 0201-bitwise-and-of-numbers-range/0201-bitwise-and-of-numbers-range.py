from math import log
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==0:
            return 0
        if left==right:
            return left
        x=log(left,2)
        y=int(log(right,2))
        if int(x)!=y:
            return 0
        if x-int(x)==0:
            return 2**int(x)
        y=2**int(x)
        x=left
        i=left+1
        while i<right+1 and x!=y:
            x=x&i
            i+=1
        return x
        