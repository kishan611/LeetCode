class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0 for _ in range(n)] for i in range(n)]
        t,b,l,r=0,n-1,0,n-1
        x=1
        while t<=b and l<=r:
            for i in range(l,r+1):
                res[t][i]=x
                x+=1
            t+=1
            for i in range(t,b+1):
                res[i][r]=x
                x+=1
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    res[b][i]=x
                    x+=1
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    res[i][l]=x
                    x+=1
                l+=1
        return res