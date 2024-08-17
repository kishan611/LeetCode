class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        row,col=len(points),len(points[0])
        for i in range(1,row):
            r=[0]*col
            r[-1]=points[i-1][-1]
            for j in range(col-2,-1,-1):
                r[j]=max(r[j+1]-1,points[i-1][j])
            l=points[i-1][0]
            points[i][0]=max(l,r[0])+points[i][0]
            for j in range(1,col):
                l=max(l-1,points[i-1][j])
                points[i][j]=max(l,r[j])+points[i][j]
        return max(points[-1])
            