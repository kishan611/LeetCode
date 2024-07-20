class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n=len(rowSum)
        m=len(colSum)
        currr=currc=0
        res=[[0 for _ in range(m)]for i in range(n)]
        while currr<n or currc<m:
            if currr>=n:
                res[currr-1][currc]=colSum[currc]
                currc+=1
                continue
            if currc>=m:
                res[currr][currc-1]=rowSum[currr]
                currr+=1
                continue
            value=min(rowSum[currr],colSum[currc])
            rowSum[currr]-=value
            colSum[currc]-=value
            res[currr][currc]=value
            if rowSum[currr]==0:
                currr+=1
            if colSum[currc]==0:
                currc+=1
        return res
        