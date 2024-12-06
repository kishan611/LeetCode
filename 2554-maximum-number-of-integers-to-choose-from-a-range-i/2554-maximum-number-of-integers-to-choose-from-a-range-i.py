class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned=set(banned)
        curr=0
        count=0
        for i in range(1,n+1):
            if i not in banned:
                if curr+i>maxSum:
                    return count
                curr+=i
                count+=1
        return count
        