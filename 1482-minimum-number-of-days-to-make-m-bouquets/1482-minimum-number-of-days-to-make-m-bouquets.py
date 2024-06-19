class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def helper(days):
            b=f=0
            for day in bloomDay:
                if day<=days:
                    f+=1
                    if f==k:
                        f=0
                        b+=1
                else:
                    f=0
            return b>=m
        n=len(bloomDay)
        if m*k>n:
            return -1
        if m*k==n:
            return max(bloomDay)
        l=1
        r=10**9
        ans=-1
        while l<=r:
            mid=l+(r-l)//2
            if helper(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
        