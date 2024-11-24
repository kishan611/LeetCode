class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg=0
        res=0
        d=float("inf")
        for i in matrix:
            for j in i:
                if j<0:
                    neg+=1
                    j=-j
                res+=j
                d=min(d,j)
        return res if neg%2==0 else res-2*d
                
        