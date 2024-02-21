class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res=0
        f=0
        for i in range(31,-1,-1):
            x=1<<i
            if(x&right and x&left):
                res|=x
                f=1
            elif x&right or x&left:
                break
        return res