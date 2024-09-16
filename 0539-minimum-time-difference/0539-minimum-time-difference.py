class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n=len(timePoints)
        arr=[0]*n
        for i in range(n):
            h,m=map(int,timePoints[i].split(":"))
            arr[i]=h*60+m
        arr.sort()
        min_diff=24*60-arr[-1]+arr[0]
        for i in range(1,n):
            min_diff=min(min_diff,arr[i]-arr[i-1])
        return min_diff
    
        