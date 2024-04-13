class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        r,c=len(matrix),len(matrix[0])
        h=[0]*(c+1)
        ma=0
        for i,row in enumerate(matrix):
            st=[-1]
            row.append('0')
            for j,x in enumerate(row):
                h[j]=h[j]+1 if x=='1' else 0
                while len(st)>1 and (j==c or h[j]<h[st[-1]]):
                    m=st[-1]
                    st.pop()
                    w=j-st[-1]-1
                    area=h[m]*w
                    ma=max(ma, area)
                st.append(j)
        return ma
            
        
            