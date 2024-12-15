import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h=[]
        n=len(classes)
        for i in range(n):
            a=classes[i][0]
            b=classes[i][1]
            heapq.heappush(h,(-((a+1)/(b+1)-a/b),i))
        while extraStudents:
            x=heapq.heappop(h)
            i=x[1]
            classes[i][0]+=1
            classes[i][1]+=1
            a=classes[i][0]
            b=classes[i][1]
            heapq.heappush(h,(-((a+1)/(b+1)-a/b),i))
            extraStudents-=1
        res=0
        for i in classes:
            res+=(i[0]/i[1])
        return res/n