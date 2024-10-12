class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        res,endp=0,0
        start=sorted(i[0] for i in intervals)
        end=sorted(i[1] for i in intervals)
        for i in start:
            if i>end[endp]:
                endp+=1
            else:
                res+=1
        return res
        