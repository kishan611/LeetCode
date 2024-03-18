class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n=len(points)
        if n==1:
            return 1 
        points.sort()
        i=points[0]
        j=points[1]
        res=0
        for x in range(2,n):
            if i[1]>=j[0]:
                i[0]=max(i[0],j[0])
                i[1]=min(i[1],j[1])
                j=points[x]
            else:
                res+=1
                i=j
            j=points[x]
        else:
            if i[1]<j[0]:
                res+=1
        return res+1
        