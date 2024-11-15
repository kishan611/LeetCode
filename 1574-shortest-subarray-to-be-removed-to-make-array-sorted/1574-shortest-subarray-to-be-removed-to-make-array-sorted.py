class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n,l=len(arr),0
        while l<n-1 and arr[l+1]>=arr[l]:
            l+=1
        if l==n-1:
            return 0
        r=n-1
        while r>l and arr[r]>=arr[r-1]:
            r-=1
        res=min(n-l-1,r)
        for i in range(l+1):
            while r<n and arr[i]>arr[r]:
                r+=1
            if r<n:
                res=min(res,r-i-1)
            else:
                break
        return res