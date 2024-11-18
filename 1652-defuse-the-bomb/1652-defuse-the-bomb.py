class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        if k==0:
            return [0]*n
        cs=r=a=0
        if k>0:
            cs=sum(code[1:k+1])
            r,a=1,(k+1)%n
        else:
            k=abs(k)
            cs=sum(code[n-k:])
            r=n-k
            a=0
        res=[]
        for i in code:
            res.append(cs)
            cs-=code[r]
            cs+=code[a]
            r=(r+1)%n
            a=(a+1)%n
        return res

        