class Solution:
    def numSteps(self, s: str) -> int:
        n=len(s)-1
        count=0
        c=0
        while n>0:
            if int(s[n])+c==0:
                count+=1
            elif int(s[n])+c==2:
                count+=1
            else:
                c=1
                count+=2
            n-=1
        if c==1:
            count+=1
        return count
                
        