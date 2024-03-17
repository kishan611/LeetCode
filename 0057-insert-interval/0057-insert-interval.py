class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        if n==0:
            return [newInterval]
        i=0
        if intervals[0][0]>newInterval[0]:
            intervals.insert(0,newInterval)
        else:
            for i in range(n-1):
                if intervals[i][0]<=newInterval[0]<=intervals[i+1][0]:
                    intervals.insert(i+1,newInterval)
                    break
            else:
                intervals.append(newInterval)
        n+=1
        while i<n-1:
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i]=[intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
                del intervals[i+1]
                n-=1
            else:
                i+=1
        return intervals
        
        