class Solution:
    def numSteps(self, s: str) -> int:
        def call(s,n):
            c=-1
            for i in range(n-1,-1,-1):
                if s[i]=='1':
                    s[i]='0'
                else:
                    c=i
                    break
            if c>=0:
                s[c]='1'
                return s,n
            return ['1']+s,n+1
            
        s=list(s)
        n=len(s)
        count=0
        while n>1:
            if s[-1]=='0':
                s.pop()
                n-=1
            elif s[-1]=='1':
                s,n=call(s,n)
            count+=1
        return count
                
        