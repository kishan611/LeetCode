class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        curr=0
        arr=[i for i in range(1,n+1)]
        while n>1:
            curr=(curr+k-1)%(n)
            arr.pop(curr)
            n-=1
            if curr>=n:
                curr=0
        return arr[0]
            
            
        