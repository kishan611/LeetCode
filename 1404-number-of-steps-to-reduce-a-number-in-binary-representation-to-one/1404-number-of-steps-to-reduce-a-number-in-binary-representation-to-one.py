class Solution:
    def numSteps(self, s: str) -> int:
        def call(s,n):
            c=-1
            z=0
            for i in range(n-1,-1,-1):
                if s[i]=='1':
                    s[i]='0'
                    z+=1
                else:
                    c=i
                    break
            if c>=0:
                s[c]='1'
                return s,n-z,z
            return ['1']+s,n+1-z,z
            
        s=list(s)
        n=len(s)
        count=0
        z=0
        while n>1:
            if s[n-1]=='0':
                n=n-1
            elif s[n-1]=='1':
                s,n,z=call(s,n)
            count+=1+z
            z=0
        return count
                
        