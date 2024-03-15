class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        res=0
        while True:
            while n>0:
                x=n%10
                res+=x**2
                n//=10
            n=res
            res=0
            if n in s:
                return False
            s.add(n)
            if n==1:
                return True
        
            
        
        