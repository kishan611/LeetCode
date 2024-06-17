class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d=2
        while d*d<=c:
            if c%d==0:
                e=0
                while c%d==0:
                    e+=1
                    c/=d
                if d%4==3 and e%2!=0:
                    return False
            d+=1
        return c%4!=3
        