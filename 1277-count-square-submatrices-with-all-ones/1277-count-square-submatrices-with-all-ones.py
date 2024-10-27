class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    continue
                res+=1
                if i-1<0 or j-1<0:
                    continue
                s=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])
                if s>0:
                    res+=s
                    matrix[i][j]+=s
        return res