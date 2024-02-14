class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        maxc=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(n):
            cm=matrix[0][i]
            for j in range(1,m):
                if cm<matrix[j][i]:
                    cm=matrix[j][i]
            maxc.append(cm)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==-1:
                    matrix[i][j]=maxc[j]
        return matrix
        