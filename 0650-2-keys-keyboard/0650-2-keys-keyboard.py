class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        min_step=0
        f=2
        while n>1:
            while n%f==0:
                n//=f
                min_step+=f
            f+=1
        return min_step
        