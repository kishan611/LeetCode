class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        x=arr[::]
        i=0
        n=len(arr)
        while i<n-1:
            if x[i]==0:
                x.insert(i,0)
                i+=1
            i+=1
        for i in range(n):
            arr[i]=x[i]
        