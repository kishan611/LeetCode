class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(n):
            cm=matrix[0][i]
            for j in range(1,m):
                if cm<matrix[j][i]:
                    cm=matrix[j][i]
            for j in range(m):
                if matrix[j][i]==-1:
                    matrix[j][i]=cm
        return matrix
        