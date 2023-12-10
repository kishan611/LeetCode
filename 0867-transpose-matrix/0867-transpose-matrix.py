class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l=[]
        m=len(matrix)
        n=len(matrix[0])
        if m==n:
            for i in range(n):
                for j in range(i+1,n):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        elif n>m:
            for i in range(m):
                for j in range(i+1,m):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            while n>m:
                x=[]
                for i in range(m):
                    x.append(matrix[i].pop())
                matrix.insert(m,x)
                n-=1
        else:
            for i in range(n):
                for j in range(i+1,n):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            while m>n:
                x=matrix.pop(n)
                for i in range(n):
                    matrix[i].append(x[i])
                m-=1
        return matrix