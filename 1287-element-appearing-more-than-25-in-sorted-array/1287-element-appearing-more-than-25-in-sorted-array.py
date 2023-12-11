class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        curr=arr[0]
        count=1
        maxc=1
        maxe=arr[0]
        for i in range(1,len(arr)):
            if arr[i]==curr:
                count+=1
            else:
                if count>maxc:
                    maxc=count
                    maxe=curr
                curr=arr[i]
                count=1
        if count>maxc:
            maxe=arr[-1]
        return maxe