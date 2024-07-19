class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        res=[]
        for i in range(n):
            x=matrix[i][0]
            index=0
            for j in range(1,m):
                if x>matrix[i][j]:
                    x=matrix[i][j]
                    index=j
            for j in range(n):
                if x<matrix[j][index]:
                    break
            else:
                res.append(x)
        return res
        