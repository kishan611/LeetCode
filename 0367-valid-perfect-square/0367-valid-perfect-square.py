class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        u=num
        while l<=u:
            m=(l+u)//2
            ms=m*m
            if ms==num:
                return True
            if ms>num:
                u=m-1
            else:
                l=m+1
        return False
            
