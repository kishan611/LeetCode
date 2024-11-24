class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        neg=0
        res=0
        d=float("inf")
        for i in range(n):
            for j in range(n):
                x=matrix[i][j]
                if x<0:
                    neg+=1
                x=abs(x)
                res+=x
                d=min(d,x)
        return res if neg%2==0 else res-2*d
                
        