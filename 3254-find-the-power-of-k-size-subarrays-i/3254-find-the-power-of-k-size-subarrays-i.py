class Solution:
    def resultsArray(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        if k==1:
            return arr
        res=[-1]*(n-k+1)
        c=0
        for i in range(1,n):
            if arr[i-1]+1==arr[i]:
                c+=1
                if c==k-1:
                    res[i-k+1]=arr[i]
                    c-=1
            else:
                c=0
        return res
