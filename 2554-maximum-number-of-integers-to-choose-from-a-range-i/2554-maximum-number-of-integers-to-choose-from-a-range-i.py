class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s=set()
        for i in banned:
            if i<=n:
                s.add(i)
        curr=0
        count=0
        for i in range(1,n+1):
            if i not in s:
                if curr+i>maxSum:
                    return count
                curr+=i
                count+=1
        return count
        