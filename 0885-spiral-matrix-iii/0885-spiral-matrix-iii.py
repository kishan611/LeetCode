class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        direct=[(0,1),(1,0),(0,-1),(-1,0)]
        res=[[rStart,cStart]]
        wc=1
        n=rows*cols
        s=d=0
        while wc<n:
            if d%2==0:
                s+=1
            for i in range(s):
                rStart+=direct[d][0]
                cStart+=direct[d][1]
                if 0<=rStart<rows and 0<=cStart<cols:
                    res.append([rStart,cStart])
                    wc+=1
                if wc==n:
                    return res
            d=(d+1)%4
        return res