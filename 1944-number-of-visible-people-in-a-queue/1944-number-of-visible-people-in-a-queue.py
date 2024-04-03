class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        s=[]
        n=len(heights)
        res=[1]*n
        for i in range(n-1,-1,-1):
            count=0
            while s and heights[s[-1]]<heights[i]:
                s.pop()
                count+=1
            if s:
                res[i]+=count
            else:
                res[i]=count
            s.append(i)
        return res