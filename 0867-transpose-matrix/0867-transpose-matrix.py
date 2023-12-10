class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(n):
            x=[]
            for j in range(m):
                x.append(matrix[j][i])
            l.append(x)
        return l